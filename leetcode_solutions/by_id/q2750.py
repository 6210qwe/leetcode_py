# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2750
标题: Promise Pool
难度: medium
链接: https://leetcode.cn/problems/promise-pool/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2636. Promise 对象池 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用异步编程和并发控制来管理 Promise 对象池。

算法步骤:
1. 定义一个异步函数 `async_function` 来模拟异步操作。
2. 定义一个类 `PromisePool` 来管理 Promise 对象池。
3. 在 `PromisePool` 类中，使用 `asyncio.Semaphore` 来控制并发数量。
4. 使用 `asyncio.gather` 来并行执行所有异步任务。

关键点:
- 使用 `asyncio.Semaphore` 控制并发数量，避免过多并发导致的性能问题。
- 使用 `asyncio.gather` 来并行执行所有异步任务，提高效率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是任务的数量。每个任务都会被处理一次。
空间复杂度: O(m)，其中 m 是并发数量。需要维护一个大小为 m 的信号量。
"""

# ============================================================================
# 代码实现
# ============================================================================

import asyncio
from typing import List, Callable, Any


class PromisePool:
    def __init__(self, max_concurrent: int):
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)

    async def async_function(self, task: Callable[[], Any]) -> Any:
        async with self.semaphore:
            return await task()

    async def run(self, tasks: List[Callable[[], Any]]) -> List[Any]:
        return await asyncio.gather(*[self.async_function(task) for task in tasks])


async def example_task(index: int) -> str:
    await asyncio.sleep(1)
    return f"Task {index} completed"


def solution_function_name(params):
    """
    函数式接口 - 实现 Promise 对象池
    """
    max_concurrent = 3  # 可以根据需要调整并发数量
    pool = PromisePool(max_concurrent)

    tasks = [lambda: example_task(i) for i in range(10)]
    result = asyncio.run(pool.run(tasks))
    return result


Solution = create_solution(solution_function_name)