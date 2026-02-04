# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3187
标题: Maximum Profitable Triplets With Increasing Prices I
难度: medium
链接: https://leetcode.cn/problems/maximum-profitable-triplets-with-increasing-prices-i/
题目类型: 树状数组、线段树、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2907. 价格递增的最大利润三元组 I - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针和二分查找来找到满足条件的三元组，并计算最大利润。

算法步骤:
1. 将价格数组排序并记录原始索引。
2. 使用双指针遍历价格数组，找到所有满足条件的三元组。
3. 对于每个三元组，使用二分查找找到中间元素，计算利润并更新最大利润。

关键点:
- 排序后使用双指针可以有效地找到满足条件的三元组。
- 使用二分查找可以快速找到中间元素，从而提高效率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(prices: List[int]) -> int:
    """
    函数式接口 - 实现
    """
    n = len(prices)
    if n < 3:
        return 0

    # 记录原始索引
    indexed_prices = sorted(enumerate(prices), key=lambda x: x[1])
    prices = [p for i, p in indexed_prices]
    indices = [i for i, p in indexed_prices]

    max_profit = 0

    # 双指针遍历
    for i in range(n):
        for j in range(i + 1, n):
            left, right = i + 1, j - 1
            while left <= right:
                mid = (left + right) // 2
                if indices[i] < indices[mid] < indices[j]:
                    profit = prices[j] - prices[i] - prices[mid]
                    max_profit = max(max_profit, profit)
                    break
                elif indices[mid] < indices[i]:
                    left = mid + 1
                else:
                    right = mid - 1

    return max_profit


Solution = create_solution(solution_function_name)