# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2909
标题: Delay the Resolution of Each Promise
难度: medium
链接: https://leetcode.cn/problems/delay-the-resolution-of-each-promise/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2821. 延迟每个 Promise 对象的解析 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 `asyncio` 库来处理异步操作，并使用 `async` 和 `await` 关键字来延迟每个 Promise 的解析。

算法步骤:
1. 定义一个异步函数 `delayed_resolve`，该函数接受一个 Promise 对象和一个延迟时间作为参数。
2. 在 `delayed_resolve` 函数中，使用 `await asyncio.sleep(delay)` 来延迟指定的时间。
3. 在 `delayed_resolve` 函数中，使用 `await promise` 来解析 Promise 对象。
4. 定义主函数 `delay_all_promises`，该函数接受一个 Promise 列表和一个延迟时间列表作为参数。
5. 在 `delay_all_promises` 函数中，使用 `asyncio.gather` 来并行处理所有延迟解析的 Promise 对象。

关键点:
- 使用 `asyncio` 库来处理异步操作。
- 使用 `await asyncio.sleep` 来实现延迟。
- 使用 `asyncio.gather` 来并行处理多个异步任务。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + max(delay))，其中 n 是 Promise 列表的长度，max(delay) 是最大的延迟时间。
空间复杂度: O(n)，存储所有的 Promise 对象和延迟时间。
"""

# ============================================================================
# 代码实现
# ============================================================================

import asyncio
from typing import List

async def delayed_resolve(promise, delay):
    """
    延迟解析单个 Promise 对象
    """
    await asyncio.sleep(delay)
    return await promise

async def delay_all_promises(promises: List[asyncio.Future], delays: List[int]) -> List[asyncio.Future]:
    """
    延迟解析所有 Promise 对象
    """
    tasks = [delayed_resolve(promise, delay) for promise, delay in zip(promises, delays)]
    return await asyncio.gather(*tasks)

# 示例用法
# async def main():
#     promises = [asyncio.Future() for _ in range(3)]
#     delays = [1, 2, 3]
#     results = await delay_all_promises(promises, delays)
#     print(results)

# asyncio.run(main())

Solution = delay_all_promises