# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3204
标题: Maximum Profitable Triplets With Increasing Prices II
难度: hard
链接: https://leetcode.cn/problems/maximum-profitable-triplets-with-increasing-prices-ii/
题目类型: 树状数组、线段树、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2921. 价格递增的最大利润三元组 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用树状数组（Fenwick Tree）来高效地处理区间查询和更新。

算法步骤:
1. 初始化树状数组，并将所有价格存入一个有序集合中以去重。
2. 遍历每个价格，计算以当前价格为中间价格的三元组的最大利润。
3. 使用树状数组维护前缀最大值，以便快速查询和更新。

关键点:
- 使用树状数组可以在 O(log n) 时间内完成区间查询和更新。
- 通过有序集合去重并映射到索引，可以有效地处理重复价格。
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

from typing import List
import bisect

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] = max(self.tree[i], delta)
            i += i & -i

    def query(self, i):
        result = 0
        while i > 0:
            result = max(result, self.tree[i])
            i -= i & -i
        return result


def solution_function_name(prices: List[int]) -> int:
    """
    函数式接口 - 计算价格递增的最大利润三元组
    """
    unique_prices = sorted(set(prices))
    price_to_index = {price: i for i, price in enumerate(unique_prices)}
    
    n = len(unique_prices)
    fenwick_tree = FenwickTree(n)
    max_profit = 0
    
    for price in prices:
        index = price_to_index[price]
        left_max = fenwick_tree.query(index - 1)
        right_max = 0
        
        # Update the tree with the current price and its profit
        fenwick_tree.update(index, left_max + price)
        
        # Calculate the maximum profit for the current price as the middle element
        max_profit = max(max_profit, left_max + right_max + price)
    
    return max_profit


Solution = create_solution(solution_function_name)