# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3158
标题: Maximum Length of Semi-Decreasing Subarrays
难度: medium
链接: https://leetcode.cn/problems/maximum-length-of-semi-decreasing-subarrays/
题目类型: 栈、数组、排序、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2863. 最长半递减子数组的长度 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针法来找到最长的半递减子数组。

算法步骤:
1. 初始化两个指针 left 和 right，都指向数组的第一个元素。
2. 移动右指针 right，直到不满足半递减条件（即 nums[right] > nums[right-1]）。
3. 更新最长半递减子数组的长度。
4. 将左指针 left 移动到 right 的位置，继续寻找下一个半递减子数组。
5. 重复步骤 2-4，直到遍历完整个数组。

关键点:
- 使用双指针法可以在线性时间内找到最长的半递减子数组。
- 每次移动右指针时，检查当前元素是否大于前一个元素，如果不满足条件则更新最长长度并移动左指针。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。每个元素最多被访问两次（一次作为右指针，一次作为左指针）。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_semi_decreasing_subarray_length(nums: List[int]) -> int:
    """
    函数式接口 - 找到最长的半递减子数组的长度
    """
    if not nums:
        return 0

    n = len(nums)
    left = 0
    max_length = 1

    for right in range(1, n):
        if nums[right] > nums[right - 1]:
            # 不满足半递减条件，更新最长长度并移动左指针
            max_length = max(max_length, right - left)
            left = right

    # 最后一段子数组的长度
    max_length = max(max_length, n - left)

    return max_length


Solution = create_solution(max_semi_decreasing_subarray_length)