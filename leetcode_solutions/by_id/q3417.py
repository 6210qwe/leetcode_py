# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3417
标题: Find the Index of Permutation
难度: medium
链接: https://leetcode.cn/problems/find-the-index-of-permutation/
题目类型: 树状数组、线段树、数组、二分查找、分治、有序集合、归并排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3109. 查找排列的下标 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来找到排列的下标。

算法步骤:
1. 对输入数组进行排序。
2. 使用二分查找在原数组中找到排序后的数组的第一个元素的位置。
3. 检查该位置是否满足排列条件，如果满足则返回该位置，否则继续查找。

关键点:
- 二分查找的时间复杂度为 O(log n)，可以有效减少查找时间。
- 排序的时间复杂度为 O(n log n)，但只需要进行一次。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 排序操作的时间复杂度。
空间复杂度: O(1) - 除了输入和输出外，只使用了常数级的额外空间。
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
    函数式接口 - 查找排列的下标
    """
    # 对输入数组进行排序
    sorted_nums = sorted(nums)
    
    # 使用二分查找在原数组中找到排序后的数组的第一个元素的位置
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    # 找到排序后数组的第一个元素在原数组中的位置
    index = binary_search(nums, sorted_nums[0])
    
    # 检查该位置是否满足排列条件
    for i in range(len(nums)):
        if nums[(index + i) % len(nums)] != sorted_nums[i]:
            return -1
    return index


Solution = create_solution(solution_function_name)