# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2807
标题: Execute Asynchronous Functions in Parallel
难度: medium
链接: https://leetcode.cn/problems/execute-asynchronous-functions-in-parallel/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2721. 并行执行异步函数 - 给定一个异步函数数组 functions，返回一个新的 promise 对象 promise。数组中的每个函数都不接受参数并返回一个 promise。所有的 promise 都应该并行执行。 promise resolve 条件： * 当所有从 functions 返回的 promise 都成功的并行解析时。promise 的解析值应该是一个按照它们在 functions 中的顺序排列的 promise 的解析值数组。promise 应该在数组中的所有异步函数并行执行完成时解析。 promise reject 条件： * 当任何从 functions 返回的 promise 被拒绝时。promise 也会被拒绝，并返回第一个拒绝的原因。 请在不使用内置的 Promise.all 函数的情况下解决。 示例 1： 输入：functions = [ () => new Promise(resolve => setTimeout(() => resolve(5), 200)) ] 输出：{"t": 200, "resolved": [5]} 解释： promiseAll(functions).then(console.log); // [5] 单个函数在 200 毫秒后以值 5 成功解析。 示例 2： 输入：functions = [ () => new Promise(resolve => setTimeout(() => resolve(1), 200)), () => new Promise((resolve, reject) => setTimeout(() => reject("Error"), 100)) ] 输出：{"t": 100, "rejected": "Error"} 解释：由于其中一个 promise 被拒绝，返回的 promise 也在同一时间被拒绝并返回相同的错误。 示例 3： 输入：functions = [ () => new Promise(resolve => setTimeout(() => resolve(4), 50)), () => new Promise(resolve => setTimeout(() => resolve(10), 150)), () => new Promise(resolve => setTimeout(() => resolve(16), 100)) ] 输出：{"t": 150, "resolved": [4, 10, 16]} 解释：所有的 promise 都成功执行。当最后一个 promise 被解析时，返回的 promise 也被解析了。 提示： * 函数 functions 是一个返回 promise 的函数数组 * 1 <= functions.length <= 10
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用计数器来跟踪所有异步函数的完成情况，并在所有函数都完成后解析最终的 promise。

算法步骤:
1. 初始化一个计数器 `count` 和一个结果数组 `results`。
2. 遍历 `functions` 数组，对每个函数调用并处理其返回的 promise。
3. 在每个 promise 的回调中，更新结果数组 `results` 并递减计数器 `count`。
4. 如果计数器 `count` 为 0，表示所有 promise 都已完成，解析最终的 promise。
5. 如果任何一个 promise 被拒绝，立即拒绝最终的 promise 并返回拒绝原因。

关键点:
- 使用计数器来跟踪所有异步函数的完成情况。
- 在所有 promise 完成后解析最终的 promise。
- 如果任何一个 promise 被拒绝，立即拒绝最终的 promise。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 functions 的长度。每个函数的 promise 都会被并行执行，但总的等待时间取决于最慢的那个 promise。
空间复杂度: O(n)，需要存储结果数组和计数器。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import asyncio

async def promise_all(functions: List[callable]) -> List:
    """
    并行执行异步函数数组，并返回一个新的 promise 对象。
    """
    results = [None] * len(functions)
    count = len(functions)
    final_promise = asyncio.get_event_loop().create_future()

    def on_resolve(index, value):
        nonlocal count
        results[index] = value
        count -= 1
        if count == 0:
            final_promise.set_result(results)

    def on_reject(reason):
        final_promise.set_exception(Exception(reason))

    for i, func in enumerate(functions):
        promise = func()
        promise.add_done_callback(lambda f, idx=i: (
            on_resolve(idx, f.result()) if f.exception() is None else on_reject(str(f.exception()))
        ))

    return await final_promise

Solution = create_solution(promise_all)