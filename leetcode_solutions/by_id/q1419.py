# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1419
标题: Make Array Non-decreasing or Non-increasing
难度: hard
链接: https://leetcode.cn/problems/make-array-non-decreasing-or-non-increasing/
题目类型: 贪心、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2263. 数组变为有序的最小操作次数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来计算将数组变为非递减或非递增所需的最小操作次数。

算法步骤:
1. 初始化两个数组 `dp_inc` 和 `dp_dec`，分别表示将数组变为非递减和非递增所需的最小操作次数。
2. 遍历数组，对于每个元素，更新 `dp_inc` 和 `dp_dec`。
3. 最后返回 `dp_inc` 和 `dp_dec` 的最小值。

关键点:
- 使用动态规划来避免重复计算。
- 通过比较相邻元素来决定是否需要进行操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_operations_to_sort_array(nums: List[int]) -> int:
    """
    函数式接口 - 计算将数组变为非递减或非递增所需的最小操作次数
    """
    n = len(nums)
    if n <= 1:
        return 0

    dp_inc = [0] * n
    dp_dec = [0] * n

    for i in range(1, n):
        if nums[i] >= nums[i - 1]:
            dp_inc[i] = dp_inc[i - 1]
        else:
            dp_inc[i] = dp_inc[i - 1] + 1

        if nums[i] <= nums[i - 1]:
            dp_dec[i] = dp_dec[i - 1]
        else:
            dp_dec[i] = dp_dec[i - 1] + 1

    return min(dp_inc[-1], dp_dec[-1])


Solution = create_solution(min_operations_to_sort_array)