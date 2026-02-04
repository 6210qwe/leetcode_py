# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 948
标题: Sort an Array
难度: medium
链接: https://leetcode.cn/problems/sort-an-array/
题目类型: 数组、分治、桶排序、计数排序、基数排序、排序、堆（优先队列）、归并排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
912. 排序数组 - 给你一个整数数组 nums，请你将该数组升序排列。 你必须在 不使用任何内置函数 的情况下解决问题，时间复杂度为 O(nlog(n))，并且空间复杂度尽可能小。 示例 1： 输入：nums = [5,2,3,1] 输出：[1,2,3,5] 解释：数组排序后，某些数字的位置没有改变（例如，2 和 3），而其他数字的位置发生了改变（例如，1 和 5）。 示例 2： 输入：nums = [5,1,1,2,0,0] 输出：[0,0,1,1,2,5] 解释：请注意，nums 的值不一定唯一。 提示： * 1 <= nums.length <= 5 * 104 * -5 * 104 <= nums[i] <= 5 * 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用归并排序算法来实现数组的升序排列。

算法步骤:
1. 将数组分成两个子数组。
2. 递归地对每个子数组进行排序。
3. 合并两个已排序的子数组。

关键点:
- 归并排序的时间复杂度为 O(n log n)，空间复杂度为 O(n)。
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


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def solution_function_name(nums: List[int]) -> List[int]:
    """
    函数式接口 - 使用归并排序算法对数组进行升序排列
    """
    return merge_sort(nums)


Solution = create_solution(solution_function_name)