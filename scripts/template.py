# -*- coding: utf-8 -*-
"""
@Time   :   2026/2/2 下午5:32
@Author :   zhang
@Desc   :   核心功能：从 leetcode.json 增量生成题目模板（仅处理 used=0 的题目，生成后更新 used=1）
@Note   :   生成后会更新 leetcode.json 中的 used 字段，避免重复生成
"""
# -*- coding:utf-8 -*-
"""
从 leetcode.json 一键生成所有题目模板文件（by_id + by_difficulty + by_topic）。

数据源：项目根目录 leetcode.json（由 scripts/build_leetcode_json.py 生成/更新）

生成内容：
1) leetcode_solutions/by_id/qXXXX.py：包含题目信息、description（如果有）、topicTags（translatedName）
2) leetcode_solutions/by_difficulty/<easy|medium|hard>/qXXXX.py：导入 by_id 实现
3) leetcode_solutions/by_topic/<中文标签>/qXXXX.py：导入 by_id 实现（题目类型使用 topicTags[].translatedName）

核心逻辑调整：
- 仅处理 used == 0 的题目（需要新增的题目）
- used == 1 的题目直接跳过
- 成功生成模板后，将 leetcode.json 中对应题目的 used 字段从 0 更新为 1
- 保留 leetcode.json 中其他所有字段不变

使用方法：
python scripts/generate_templates_from_leetcode_json.py
"""

import sys
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def format_problem_id(problem_id: int) -> str:
    return f"q{problem_id:04d}"


def safe_dir_name(name: str) -> str:
    """
    将 topic 中文名转换成安全的目录名（尽量保留中文，但去掉 Windows 不允许字符）。
    """
    bad = '<>:"/\\|?*'
    out = "".join("_" if c in bad else c for c in name.strip())
    out = out.strip().strip(".")
    return out or "other"


def parse_difficulty(level: Optional[int]) -> str:
    # all 接口：1 easy, 2 medium, 3 hard
    return {1: "easy", 2: "medium", 3: "hard"}.get(level or 1, "easy")


def get_topic_names(pair: Dict[str, Any]) -> List[str]:
    """
    题目类型：优先使用 topicTags[].translatedName（你要求的）
    fallback：topics 字段（build_leetcode_json.py 会写），再 fallback slug
    """
    out: List[str] = []
    tags = pair.get("topicTags")
    if isinstance(tags, list):
        for t in tags:
            if not isinstance(t, dict):
                continue
            name = (t.get("translatedName") or t.get("name") or t.get("slug") or "").strip()
            if name and name not in out:
                out.append(name)
    if out:
        return out
    topics = pair.get("topics")
    if isinstance(topics, list):
        for x in topics:
            if isinstance(x, str) and x.strip() and x.strip() not in out:
                out.append(x.strip())
    return out or ["其他"]


def load_leetcode_json(path: Path) -> Dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("leetcode.json 不是 JSON object")
    return data


def save_leetcode_json(path: Path, data: Dict[str, Any]) -> None:
    """保存更新后的 leetcode.json，保留原有格式（缩进2）"""
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def render_by_id_template(problem_id: int, title: str, slug: str, difficulty: str, description: str,
                          topics: List[str]) -> str:
    topics_str = "、".join(topics) if topics else "（无）"
    desc_block = description or "[TODO] 请运行 scripts/build_leetcode_json.py 补齐 description"

    return f'''# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: {problem_id}
标题: {title}
难度: {difficulty}
链接: https://leetcode.cn/problems/{slug}/
题目类型: {topics_str}
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
{desc_block}
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
'''


def write_file(path: Path, content: str) -> bool:
    """写入文件，仅当文件不存在时写入"""
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def main() -> None:
    json_path = project_root / "leetcode.json"
    if not json_path.exists():
        raise FileNotFoundError(f"未找到 {json_path}，请先运行 scripts/build_leetcode_json.py")

    # 加载原始数据
    data = load_leetcode_json(json_path)
    pairs = data.get("stat_status_pairs", [])
    if not isinstance(pairs, list):
        raise ValueError("leetcode.json 缺少 stat_status_pairs 或类型不为 list")

    by_id_dir = project_root / "leetcode_solutions" / "by_id"
    by_diff_dir = project_root / "leetcode_solutions" / "by_difficulty"
    by_topic_dir = project_root / "leetcode_solutions" / "by_topic"

    # 统计变量
    total = 0  # 总遍历题目数
    created = 0  # 新建模板数
    skipped_by_used = 0  # 因 used=1 跳过的题目数
    skipped_no_pid = 0  # 无有效题目ID跳过的数
    updated_json = False  # 是否需要更新 json 文件

    # 遍历所有题目
    for idx, pair in enumerate(pairs):
        if not isinstance(pair, dict):
            total += 1
            continue

        stat = pair.get("stat") or {}
        if not isinstance(stat, dict):
            total += 1
            continue

        # 获取题目ID
        pid = stat.get("question_id")
        if not isinstance(pid, int):
            total += 1
            skipped_no_pid += 1
            continue

        # ===================== 核心逻辑调整：只处理 used == 0 的题目 =====================
        used = pair.get("used", 0)
        if used == 1:  # 已生成过模板，跳过
            skipped_by_used += 1
            total += 1
            continue
        # =========================================================================

        # 获取题目基础信息
        slug = (stat.get("question__title_slug") or "").strip()
        title = (stat.get("question__title") or "").strip() or f"题目{pid}"
        if not slug:
            total += 1
            continue

        difficulty = parse_difficulty(
            (pair.get("difficulty") or {}).get("level") if isinstance(pair.get("difficulty"), dict) else None)
        description = (pair.get("description") or "").strip()
        topics = get_topic_names(pair)

        qname = format_problem_id(pid)

        # 1) 生成 by_id 目录下的核心模板文件
        by_id_path = by_id_dir / f"{qname}.py"
        content = render_by_id_template(pid, title, slug, difficulty, description, topics)
        if write_file(by_id_path, content):
            created += 1

        # 2) 生成 by_difficulty 目录下的导入文件
        diff_path = by_diff_dir / difficulty / f"{qname}.py"
        diff_content = f'''# -*- coding:utf-8 -*-
"""{difficulty}题：{pid}. {title}（复用by_id中的实现）"""

from leetcode_solutions.by_id.{qname} import solution_function_name, Solution

__all__ = ['solution_function_name', 'Solution']
'''
        write_file(diff_path, diff_content)

        # 3) 生成 by_topic 目录下的导入文件（按中文标签分类）
        for t in topics:
            topic_dir = safe_dir_name(t)
            topic_path = by_topic_dir / topic_dir / f"{qname}.py"
            topic_content = f'''# -*- coding:utf-8 -*-
"""{topic_dir}题：{pid}. {title}（复用by_id中的实现）"""

from leetcode_solutions.by_id.{qname} import solution_function_name, Solution

__all__ = ['solution_function_name', 'Solution']
'''
            write_file(topic_path, topic_content)

        # ===================== 关键更新：将 used 从 0 改为 1 =====================
        pairs[idx]["used"] = 1
        updated_json = True
        total += 1

    # 如果有更新，保存修改后的 leetcode.json
    if updated_json:
        data["stat_status_pairs"] = pairs
        save_leetcode_json(json_path, data)
        print(f"✓ 已更新 leetcode.json 中的 used 字段（共修改 {created} 个题目）")

    # 输出统计信息
    print(f"✓ 总遍历题目数: {total}")
    print(f"✓ 因 used == 1 跳过的题目数: {skipped_by_used}")
    print(f"✓ 因无有效ID跳过的题目数: {skipped_no_pid}")
    print(f"✓ 新建 by_id 模板数: {created}")


if __name__ == "__main__":
    main()