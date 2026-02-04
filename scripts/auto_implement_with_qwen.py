#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
使用通义千问 API 自动实现未完成的 LeetCode 题目（并发版，密钥写在代码中）

功能：
1. 扫描 leetcode_solutions/by_id/qXXXX.py 中含有 TODO / [待实现] / pass 的题目
2. 对每个未实现题目，调用通义千问（OpenAI 兼容接口）让模型补全实现
3. 以题 1 的风格为参考，要求输出完整的 Python 文件内容并覆盖原文件
4. 支持多线程并发处理多个题目

依赖：
    pip install langchain-openai

注意：
- 已在代码中直接写入 dashscope 的密钥和 base URL，如需更换账号请自行修改常量。
"""

import os
import re
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple, Optional

from langchain_openai import ChatOpenAI


# ==============================
# 全局路径配置
# ==============================

BASE_DIR = Path(__file__).resolve().parent.parent  # 假设脚本位于项目的 scripts 目录
BY_ID_DIR = BASE_DIR / "leetcode_solutions" / "by_id"


# ==============================
# 通义千问 API 配置（直写在代码中）
# ==============================

# 使用更强的 qwen-max 模型
QWEN_MODEL_NAME = "qwen-max"
QWEN_API_KEY = "sk-3caf28ae9b084173b8f48dce107645d7"  # 如需更换账号，请改这里
QWEN_API_BASE = "https://dashscope.aliyuncs.com/compatible-mode/v1"


# ==============================
# 1. 扫描未实现题目
# ==============================

def check_unimplemented_problems(base_dir: Path = BY_ID_DIR) -> List[Tuple[int, Path]]:
    """
    检查未实现的题目

    规则：
    - 文件中包含 TODO / [待实现] / 待实现
    - 或者包含 pass 且文件中有 TODO 字样
    """
    if not base_dir.exists():
        print(f"目录不存在: {base_dir}")
        return []

    unimplemented: List[Tuple[int, Path]] = []
    todo_patterns = [
        r"TODO.*实现",
        r"\[待实现\]",
        r"# TODO:",
        r"待实现",
    ]

    python_files = sorted(base_dir.glob("q*.py"))

    for file_path in python_files:
        try:
            content = file_path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"读取文件 {file_path} 时出错: {e}")
            continue

        has_todo = any(re.search(pat, content, re.IGNORECASE) for pat in todo_patterns)
        has_pass = "pass" in content and "def " in content

        if has_todo or (has_pass and "TODO" in content.upper()):
            m = re.search(r"q(\d+)\.py", file_path.name)
            if m:
                pid = int(m.group(1))
                unimplemented.append((pid, file_path))

    unimplemented.sort(key=lambda x: x[0])
    return unimplemented


# ==============================
# 2. 构造 LLM 客户端（通义千问）
# ==============================

def build_llm(timeout: int = 60) -> ChatOpenAI:
    """
    构造 ChatOpenAI 客户端，使用通义千问的兼容接口。

    这里直接在代码中写死 API Key 和 Base URL。
    """
    llm = ChatOpenAI(
        model=QWEN_MODEL_NAME,
        openai_api_key=QWEN_API_KEY,
        openai_api_base=QWEN_API_BASE,
        timeout=timeout,
    )
    return llm


# ==============================
# 3. LLM 提示词
# ==============================

SYSTEM_PROMPT = """你是一个资深 Python 算法工程师，正在维护一个巨大的 LeetCode 题解代码库。

总体目标：为每道题写出**时间复杂度和空间复杂度尽可能最优**的算法实现，同时保持代码结构清晰、风格优雅易读。

要求：
1. 你会收到某道题对应的 Python 源码文件的完整内容。
2. 文件里已经包含题目信息、中文思路注释和函数/类的骨架，但实现部分是 TODO 或 pass，或者文档里有 [待实现]。
3. 你的任务是：
   - 在保留现有文件结构、注释风格和导入方式的前提下，补全所有算法实现。
   - 对每个需要实现的函数/类：
     * 选择该题目前业界/题解中**公认的最优或接近最优**的时间复杂度和空间复杂度解法（例如：能用 O(n) 就不要 O(n log n)，能用 O(1) 额外空间就不要 O(n)）。
     * 代码结构要简洁、可读性好：合理拆分小函数（如果有必要）、清晰的变量命名、必要但不过度的注释。
   - 已经写好的代码不要改动（除非明显错误），尽量只在 TODO / [待实现] / pass 部分补充实现。
   - 文档中的「实现思路」「复杂度分析」区，如果存在 [待实现] / TODO，要改成与你具体实现**严格一致**且简洁准确的描述，并明确标出时间复杂度和空间复杂度。
4. 保持与题号 1（两数之和）的风格一致：
   - 使用明确的函数签名（不要用 params 占位）。
   - 对于设计题，按 LeetCode 要求实现类，并保持文件里已有的工厂函数 + create_solution 形式。
5. 代码风格：
   - 遵循 Python 常规风格：小写下划线命名函数/变量，类用驼峰命名。
   - 控制函数长度，适当拆分逻辑，避免过深嵌套。
   - 仅在关键步骤添加简洁注释，避免注释噪音。
6. 输出格式：
   - 最重要：最终输出时，**只输出该 Python 源文件的完整最终内容**，不要加任何解释、Markdown 或额外文本。
"""

USER_PROMPT_TEMPLATE = """下面是当前题目对应的 Python 源码文件内容，请在其中补全所有 [待实现] / TODO / pass 的实现，并修正文档中的思路和复杂度（如果标为 [待实现]）。

文件路径: {file_path}

当前文件内容如下（从第一行开始）：
----------------------------------------
{file_content}
----------------------------------------

请直接输出修改后的完整 Python 源文件内容。"""


# ==============================
# 4. 针对单个文件调用 LLM 并覆盖
# ==============================

def process_one_file(
    llm: ChatOpenAI,
    problem_id: int,
    file_path: Path,
    retry: int = 3,
) -> bool:
    """
    使用 LLM 处理单个文件：生成新的完整文件内容并覆盖原文件。

    返回 True 表示成功，False 表示失败。
    """
    try:
        original_content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"[{problem_id}] 读取文件失败: {file_path}, error={e}")
        return False

    user_prompt = USER_PROMPT_TEMPLATE.format(
        file_path=str(file_path.relative_to(BASE_DIR)),
        file_content=original_content,
    )

    for attempt in range(1, retry + 1):
        try:
            resp = llm.invoke(
                [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ]
            )
            new_content = resp.content

            # 兼容不同返回格式
            if isinstance(new_content, str):
                text = new_content.strip()
            else:
                # langchain 可能返回 Message 内容列表，这里简单拼接
                try:
                    text = "".join(part["text"] for part in new_content).strip()
                except Exception:
                    text = str(new_content).strip()

            # 如果模型意外用 ```python 包裹，去掉包裹
            if text.startswith("```"):
                lines = text.splitlines()
                if len(lines) >= 2 and lines[0].startswith("```") and lines[-1].startswith("```"):
                    text = "\n".join(lines[1:-1]).strip()

            file_path.write_text(text, encoding="utf-8")
            print(f"[{problem_id}] 已生成并写回: {file_path.name}")
            return True
        except Exception as e:
            print(f"[{problem_id}] 调用 LLM 失败 (attempt {attempt}/{retry}): {e}")
            time.sleep(2 * attempt)

    print(f"[{problem_id}] 最终失败，跳过: {file_path}")
    return False


# ==============================
# 5. 主流程：并发处理
# ==============================

def main(max_workers: int = 4, only_range: Optional[Tuple[int, int]] = None) -> None:
    """
    主入口：并发处理未实现题目。

    Args:
        max_workers: 并发线程数
        only_range: 只处理某个题号区间（可选，如 (350, 399)）
    """
    print("=" * 60)
    print("自动实现未完成的 LeetCode 题目（通义千问 + 并发）")
    print("=" * 60)

    unimplemented = check_unimplemented_problems(BY_ID_DIR)
    if not unimplemented:
        print("✓ 未找到未实现的题目，已全部完成。")
        return

    if only_range is not None:
        lo, hi = only_range
        unimplemented = [(pid, p) for pid, p in unimplemented if lo <= pid <= hi]

    if not unimplemented:
        print("指定区间内没有未实现的题目。")
        return

    print(f"共发现 {len(unimplemented)} 个未实现题目，将使用 {max_workers} 个线程并发处理。\n")

    llm = build_llm()

    success = 0
    fail = 0

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(process_one_file, llm, pid, path): (pid, path)
            for pid, path in unimplemented
        }

        for fut in as_completed(futures):
            pid, path = futures[fut]
            ok = False
            try:
                ok = fut.result()
            except Exception as e:
                print(f"[{pid}] 处理时抛出异常: {e}")

            if ok:
                success += 1
            else:
                fail += 1

    print("\n" + "=" * 60)
    print(f"处理完成：成功 {success} 个，失败 {fail} 个，总计 {len(unimplemented)} 个。")
    print("=" * 60)


if __name__ == "__main__":
    # 示例 1：只处理 350–399 区间的题目
    # main(max_workers=4, only_range=(350, 399))

    # 示例 2：处理所有未实现题目
    main(max_workers=8)


