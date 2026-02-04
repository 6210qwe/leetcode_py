# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2273
标题: Pour Water Between Buckets to Make Water Levels Equal
难度: medium
链接: https://leetcode.cn/problems/pour-water-between-buckets-to-make-water-levels-equal/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2137. 通过倒水操作让所有的水桶所含水量相等 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来找到最小的可行水量。

算法步骤:
1. 计算所有水桶的总水量。
2. 计算平均水量。
3. 使用二分查找来确定最小的可行水量，使得所有水桶的水量都可以达到或超过这个值。

关键点:
- 二分查找的范围是从0到最大水量。
- 检查当前水量是否可以使所有水桶的水量都达到或超过这个值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log(max_water))
- n 是水桶的数量
- max_water 是水桶中的最大水量

空间复杂度: O(1)
- 只使用了常数级的额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def equalizeWater(buckets: List[int]) -> int:
    """
    函数式接口 - 通过倒水操作让所有的水桶所含水量相等
    """
    def is_possible(level: int) -> bool:
        return sum(max(0, level - water) for water in buckets) <= extra_water

    total_water = sum(buckets)
    n = len(buckets)
    if total_water % n != 0:
        return -1

    avg_water = total_water // n
    extra_water = total_water - n * avg_water

    left, right = 0, max(buckets)
    while left < right:
        mid = (left + right + 1) // 2
        if is_possible(mid):
            left = mid
        else:
            right = mid - 1

    return left


Solution = create_solution(equalizeWater)