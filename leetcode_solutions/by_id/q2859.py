# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2859
标题: Add Two Promises
难度: easy
链接: https://leetcode.cn/problems/add-two-promises/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2723. 两个 Promise 对象相加 - 给定两个 promise 对象 promise1 和 promise2，返回一个新的 promise。promise1 和 promise2 都会被解析为一个数字。返回的 Promise 应该解析为这两个数字的和。 示例 1： 输入： promise1 = new Promise(resolve => setTimeout(() => resolve(2), 20)), promise2 = new Promise(resolve => setTimeout(() => resolve(5), 60)) 输出：7 解释：两个输入的 Promise 分别解析为值 2 和 5。返回的 Promise 应该解析为 2 + 5 = 7。返回的 Promise 解析的时间不作为判断条件。 示例 2： 输入： promise1 = new Promise(resolve => setTimeout(() => resolve(10), 50)), promise2 = new Promise(resolve => setTimeout(() => resolve(-12), 30)) 输出：-2 解释：两个输入的 Promise 分别解析为值 10 和 -12。返回的 Promise 应该解析为 10 + -12 = -2。 提示： * promise1 和 promise2 都是被解析为一个数字的 promise 对象
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 `asyncio` 库来处理异步操作，等待两个 Promise 对象解析完成后，将它们的结果相加并返回一个新的 Promise。

算法步骤:
1. 使用 `asyncio.gather` 同时等待两个 Promise 对象解析。
2. 将解析后的结果相加。
3. 返回一个新的 Promise 对象，解析为两个 Promise 对象的和。

关键点:
- 使用 `asyncio.gather` 可以同时等待多个异步操作完成。
- 返回一个新的 Promise 对象，解析为两个 Promise 对象的和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 因为我们只是在等待两个 Promise 对象解析并进行一次加法操作。
空间复杂度: O(1) - 除了输入和输出的 Promise 对象外，没有使用额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

import asyncio
from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


async def add_two_promises(promise1, promise2):
    """
    函数式接口 - 返回一个新的 Promise，解析为两个输入 Promise 的和。
    """
    # 等待两个 Promise 对象解析
    result1, result2 = await asyncio.gather(promise1, promise2)
    
    # 计算两个结果的和
    total = result1 + result2
    
    # 返回一个新的 Promise，解析为两个结果的和
    return total


Solution = create_solution(add_two_promises)