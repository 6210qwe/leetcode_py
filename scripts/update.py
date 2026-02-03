# -*- coding: utf-8 -*-
"""
@Time   : 2026/2/2
@Author : zhang
@Desc   : 仅description为空时补全（同时补描述+标签），本地数据写保护
"""
import sys
import re
import json
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from lxml import etree

# 项目根路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


# 代理配置
def get_proxy():
    tunnel = "g184.kdltps.com:15818"
    username = "t13632437348639"
    password = "10cc7lx7"
    return {
        "http": f"http://{username}:{password}@{tunnel}",
        "https": f"http://{username}:{password}@{tunnel}",
    }


# 提取题目描述
def extract_description_from_html(html_content):
    try:
        parser = etree.HTMLParser()
        tree = etree.fromstring(html_content.encode("utf-8"), parser)
        nodes = tree.xpath("//meta[@name='description']/@content")
        if not nodes:
            return ""
        desc = (nodes[0] or "").strip()
        return re.sub(r"\s+", " ", desc).strip() or ""
    except Exception as e:
        print(f"提取描述失败: {e}")
        return ""


# 提取标签
def extract_topic_tags_from_html(html_content):
    try:
        pattern = r'"topicTags"\s*:\s*(\[[\s\S]*?\])'
        m = re.search(pattern, html_content, re.DOTALL)
        if m:
            arr = json.loads(m.group(1))
            if isinstance(arr, list):
                return [
                    {
                        "name": item.get("name"),
                        "slug": item.get("slug", "").strip(),
                        "translatedName": item.get("translatedName"),
                    }
                    for item in arr
                    if isinstance(item, dict) and item.get("slug", "").strip()
                ]
    except Exception as e:
        print(f"提取标签失败: {e}")
    return []


# 构建topics字段
def build_topics_from_topic_tags(topic_tags):
    topics = []
    for t in topic_tags:
        name = (t.get("translatedName") or t.get("name") or t.get("slug") or "").strip()
        if name and name not in topics:
            topics.append(name)
    return topics


# GraphQL兜底获取标签
def fetch_topic_tags_from_graphql(session, proxies, slug):
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        topicTags { name slug translatedName }
      }
    }
    """
    try:
        resp = session.post(
            "https://leetcode.cn/graphql/",
            json={"query": query, "variables": {"titleSlug": slug}},
            proxies=proxies,
            timeout=20,
            headers={"Content-Type": "application/json"},
        )
        resp.raise_for_status()
        tags = resp.json().get("data", {}).get("question", {}).get("topicTags", [])
        return [
            {
                "name": t.get("name"),
                "slug": t.get("slug", "").strip(),
                "translatedName": t.get("translatedName"),
            }
            for t in tags
            if isinstance(t, dict) and t.get("slug", "").strip()
        ]
    except Exception as e:
        print(f"GraphQL获取标签失败 {slug}: {e}")
        return []


# 抓取单题：同时拿描述+标签
def fetch_question_detail(session, proxies, slug):
    url = f"https://leetcode.cn/problems/{slug}/"
    for attempt in range(3):
        try:
            r = session.get(url, proxies=proxies, timeout=15)
            r.raise_for_status()
            desc = extract_description_from_html(r.text)
            tags = extract_topic_tags_from_html(r.text)
            # 标签为空时走GraphQL兜底
            tags = tags if tags else fetch_topic_tags_from_graphql(session, proxies, slug)
            return desc, tags
        except Exception as e:
            print(f"抓取详情失败 {slug} 第{attempt+1}次: {e}")
            time.sleep(0.6 * (attempt + 1))
    return "", []


class LeetCodeDataUpdater:
    def __init__(self):
        self.use_proxy = True
        self.max_workers = 10
        self.output_file = project_root / "leetcode.json"
        self.proxies = get_proxy() if self.use_proxy else None

        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9",
        })

        # 写保护字段：本地有值就永不覆盖
        self.protected_fields = ["description", "topicTags", "topics", "used"]

    # 加载本地数据并去重
    def load_and_clean_local_data(self):
        if not self.output_file.exists():
            print("本地文件不存在，初始化空数据")
            return {"stat_status_pairs": []}, {}

        try:
            with open(self.output_file, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
        except Exception as e:
            print(f"读取本地文件失败：{e}")
            return {"stat_status_pairs": []}, {}

        if not isinstance(raw_data, dict) or "stat_status_pairs" not in raw_data:
            print("本地数据结构不合法，初始化空数据")
            return {"stat_status_pairs": []}, {}

        clean_pairs = []
        local_qid_map = {}
        seen_qids = set()

        for item in raw_data["stat_status_pairs"]:
            qid = item.get("stat", {}).get("question_id")
            if qid is None or not isinstance(qid, int):
                continue

            if qid not in seen_qids:
                seen_qids.add(qid)
                clean_pairs.append(item)
                # 缓存本地保护字段
                local_qid_map[qid] = {
                    k: item.get(k, "" if k != "topicTags" else [])
                    for k in self.protected_fields
                }

        print(f"本地数据去重后：{len(clean_pairs)} 条，唯一 qid：{len(local_qid_map)}")
        return {"stat_status_pairs": clean_pairs}, local_qid_map

    # 获取接口最新数据
    def fetch_latest_api_data(self):
        try:
            resp = self.session.get(
                "https://leetcode.cn/api/problems/all/",
                proxies=self.proxies,
                timeout=30
            )
            resp.raise_for_status()
            data = resp.json()
            if not isinstance(data, dict) or "stat_status_pairs" not in data:
                raise ValueError("接口返回缺少 stat_status_pairs")
            print(f"接口数据：{len(data['stat_status_pairs'])} 条")
            return data
        except Exception as e:
            print(f"获取接口数据失败：{e}")
            raise

    # 安全合并：本地保护字段绝不覆盖
    def merge_data_with_protection(self, local_data, local_qid_map, api_data):
        api_qid_map = {}
        for item in api_data["stat_status_pairs"]:
            qid = item.get("stat", {}).get("question_id")
            if qid is not None and isinstance(qid, int) and qid not in api_qid_map:
                api_qid_map[qid] = item

        merged_pairs = []

        # 接口存在的题目：基础数据用接口，保护字段用本地
        for qid, api_item in api_qid_map.items():
            merged = api_item.copy()
            if qid in local_qid_map:
                merged.update(local_qid_map[qid])
            else:
                # 新题初始化
                merged["description"] = ""
                merged["topicTags"] = []
                merged["topics"] = []
                merged["used"] = 0
            merged_pairs.append(merged)

        # 本地独有题目完整保留
        local_only = set(local_qid_map.keys()) - set(api_qid_map.keys())
        for qid in local_only:
            for item in local_data["stat_status_pairs"]:
                if item.get("stat", {}).get("question_id") == qid:
                    merged_pairs.append(item)
                    break

        merged_data = api_data.copy()
        merged_data["stat_status_pairs"] = merged_pairs
        print(f"合并完成：总计 {len(merged_pairs)} 条")
        return merged_data

    # 保存数据
    def save_data(self, data, tip=""):
        try:
            self.output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.output_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            if tip:
                print(f"✅ {tip}")
        except Exception as e:
            print(f"保存失败：{e}")
            raise

    # 核心逻辑：仅description为空时，补全描述+标签
    def enrich_detail_when_desc_empty(self, data):
        pairs = data["stat_status_pairs"]
        jobs = []

        # 筛选规则：仅description为空时才补全
        for idx, item in enumerate(pairs):
            if not isinstance(item, dict):
                continue
            stat = item.get("stat", {})
            qid = stat.get("question_id")
            slug = stat.get("question__title_slug")

            if qid is None or not slug or not isinstance(slug, str):
                continue
            slug = slug.strip()

            # 唯一判断条件：description为空
            if not item.get("description"):
                jobs.append((idx, qid, slug))
                print(f"题目 {qid} ({slug})：description为空，需补全描述+标签")

        print(f"\n需要补全的题目总数：{len(jobs)}")
        if not jobs:
            return data

        ok = 0
        fail = 0

        # 多线程补全（同时补描述+标签）
        with ThreadPoolExecutor(max_workers=self.max_workers) as ex:
            future_map = {
                ex.submit(fetch_question_detail, self.session, self.proxies, slug): (idx, qid, slug)
                for idx, qid, slug in jobs
            }

            for i, fut in enumerate(as_completed(future_map), 1):
                idx, qid, slug = future_map[fut]
                desc, tags = fut.result()
                topics = build_topics_from_topic_tags(tags)

                # 仅当description为空时更新（双重保护）
                if not pairs[idx].get("description"):
                    pairs[idx]["description"] = desc
                    pairs[idx]["topicTags"] = tags
                    pairs[idx]["topics"] = topics

                # 统计结果
                if desc or tags:
                    ok += 1
                    print(f"[{i}/{len(jobs)}] ✅ 补全成功 {qid} ({slug})：描述={len(desc)}字符，标签={len(tags)}个")
                else:
                    fail += 1
                    print(f"[{i}/{len(jobs)}] ❌ 补全失败 {qid} ({slug})：无有效数据")

                # 每50题分批保存
                if i % 50 == 0:
                    self.save_data(data, tip=f"分批保存：已处理 {i}/{len(jobs)} 题")
                    print(f"进度：成功 {ok} | 失败 {fail}")

        # 最终保存
        self.save_data(data, tip=f"补全完成：成功 {ok} 题，失败 {fail} 题")
        return data

    # 主流程
    def run(self):
        try:
            print("===== 加载本地数据 =====")
            local_data, local_qid_map = self.load_and_clean_local_data()
            print("\n===== 获取接口数据 =====")
            api_data = self.fetch_latest_api_data()
            print("\n===== 安全合并（写保护） =====")
            merged_data = self.merge_data_with_protection(local_data, local_qid_map, api_data)
            self.save_data(merged_data, tip="合并完成，本地详情已保护")
            print("\n===== 补全description为空的题目（同时补描述+标签） =====")
            final_data = self.enrich_detail_when_desc_empty(merged_data)
            print("\n🎉 全部完成！规则：仅description为空时补全（描述+标签），本地数据100%保留")
        except Exception as e:
            print(f"\n❌ 执行失败：{e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)


if __name__ == "__main__":
    updater = LeetCodeDataUpdater()
    updater.run()