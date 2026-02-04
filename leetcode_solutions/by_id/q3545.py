# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3545
标题: Minimum Number of Increasing Subsequence to Be Removed
难度: hard
链接: https://leetcode.cn/problems/minimum-number-of-increasing-subsequence-to-be-removed/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3231. 要删除的递增子序列的最小数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和二分查找来找到最长递增子序列 (LIS)，然后计算需要删除的子序列数量。

算法步骤:
1. 计算数组的 LIS 长度。
2. 使用二分查找优化 LIS 的计算过程。
3. 计算需要删除的子序列数量，即 n - LIS 长度。

关键点:
- 使用二分查找优化 LIS 的计算过程，使得时间复杂度从 O(n^2) 降低到 O(n log n)。
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

def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    def length_of_LIS(nums: List[int]) -> int:
        tails = []
        for num in nums:
            idx = bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)

    from bisect import bisect_left

    n = len(nums)
    lis_length = length_of_LIS(nums)
    return n - lis_length

Solution = create_solution(solution_function_name)