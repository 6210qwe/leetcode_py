# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3273
标题: Most Expensive Item That Can Not Be Bought
难度: medium
链接: https://leetcode.cn/problems/most-expensive-item-that-can-not-be-bought/
题目类型: 数学、动态规划、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2979. 最贵的无法购买的商品 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和数论的方法来解决这个问题。具体来说，我们可以使用一个布尔数组来表示每个价格是否可以被购买。

算法步骤:
1. 初始化一个布尔数组 `can_buy`，长度为 `maxPrice + 1`，初始值为 `False`。
2. 遍历每个价格 `price`，将 `can_buy[price]` 设为 `True`。
3. 使用双重循环遍历所有可能的价格组合，更新 `can_buy` 数组。
4. 找到第一个 `False` 的位置，即为最贵的无法购买的商品。

关键点:
- 使用布尔数组来记录每个价格是否可以被购买。
- 通过双重循环更新布尔数组，确保所有可能的价格组合都被考虑。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * maxPrice)，其中 n 是价格列表的长度，maxPrice 是最大价格。
空间复杂度: O(maxPrice)，用于存储布尔数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(prices: List[int], maxPrice: int) -> int:
    """
    函数式接口 - 找到最贵的无法购买的商品
    """
    # 初始化布尔数组
    can_buy = [False] * (maxPrice + 1)
    can_buy[0] = True  # 价格为0时总是可以购买

    # 标记每个价格是否可以被购买
    for price in prices:
        if price <= maxPrice:
            can_buy[price] = True

    # 更新布尔数组
    for i in range(1, maxPrice + 1):
        for price in prices:
            if i - price >= 0 and can_buy[i - price]:
                can_buy[i] = True
                break

    # 找到第一个无法购买的价格
    for i in range(maxPrice, -1, -1):
        if not can_buy[i]:
            return i

    return -1


Solution = create_solution(solution_function_name)