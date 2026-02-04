# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3101
标题: Maximum Coins Heroes Can Collect
难度: medium
链接: https://leetcode.cn/problems/maximum-coins-heroes-can-collect/
题目类型: 数组、双指针、二分查找、前缀和、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2838. 英雄可以获得的最大金币数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找和前缀和来优化时间复杂度。

算法步骤:
1. 对英雄的能力值进行排序。
2. 计算每个能力值的前缀和。
3. 使用二分查找找到每个英雄可以收集的最大金币数。

关键点:
- 通过前缀和快速计算区间和。
- 通过二分查找快速定位每个英雄可以收集的最大金币数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n + m log n)，其中 n 是英雄的数量，m 是金币堆的数量。
空间复杂度: O(n)，用于存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_coins(heroes: List[int], piles: List[List[int]]) -> int:
    """
    函数式接口 - 计算英雄可以获得的最大金币数
    """
    # 对英雄的能力值进行排序
    heroes.sort()
    
    # 对金币堆按能力值要求排序
    piles.sort(key=lambda x: x[0])
    
    # 计算每个能力值的前缀和
    prefix_sum = [0]
    for pile in piles:
        prefix_sum.append(prefix_sum[-1] + pile[1])
    
    def binary_search(target):
        left, right = 0, len(piles)
        while left < right:
            mid = (left + right) // 2
            if piles[mid][0] > target:
                right = mid
            else:
                left = mid + 1
        return left
    
    total_coins = 0
    for hero in heroes:
        idx = binary_search(hero)
        total_coins += prefix_sum[idx]
    
    return total_coins


Solution = create_solution(max_coins)