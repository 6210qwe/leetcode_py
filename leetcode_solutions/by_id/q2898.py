# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2898
标题: Parallel Execution of Promises for Individual Results Retrieval
难度: medium
链接: https://leetcode.cn/problems/parallel-execution-of-promises-for-individual-results-retrieval/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2795. 并行执行 Promise 以获取独有的结果 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 asyncio 库来并行执行多个异步任务，并使用 gather 来收集所有任务的结果。

算法步骤:
1. 定义一个异步函数 `solution_function_name`，该函数接受一个 promise 列表作为参数。
2. 使用 asyncio.gather 并行执行所有的 promise。
3. 返回所有 promise 的结果列表。

关键点:
- 使用 asyncio.gather 可以并行执行多个异步任务，并在所有任务完成后返回结果列表。
- 确保所有的 promise 是异步函数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 其中 n 是 promise 列表的长度。因为所有 promise 是并行执行的，总的时间复杂度取决于最慢的那个 promise。
空间复杂度: O(n) - 存储所有 promise 的结果需要 O(n) 的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

import asyncio
from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


async def solution_function_name(promises: List[callable]) -> List[Optional]:
    """
    函数式接口 - 并行执行多个异步任务，并返回所有任务的结果列表。
    """
    # 使用 asyncio.gather 并行执行所有的 promise
    results = await asyncio.gather(*promises)
    return results


Solution = create_solution(solution_function_name)