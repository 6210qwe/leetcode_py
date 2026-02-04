# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1102
标题: Check If a Number Is Majority Element in a Sorted Array
难度: easy
链接: https://leetcode.cn/problems/check-if-a-number-is-majority-element-in-a-sorted-array/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1150. 检查一个数是否在数组中占绝大多数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来确定目标值的左右边界，从而计算出目标值的出现次数。

算法步骤:
1. 使用二分查找找到目标值的左边界。
2. 使用二分查找找到目标值的右边界。
3. 计算目标值的出现次数，并判断是否超过数组长度的一半。

关键点:
- 二分查找的时间复杂度为 O(log n)，通过两次二分查找可以高效地找到目标值的边界。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def find_left(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def find_right(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

def is_majority_element(nums: List[int], target: int) -> bool:
    """
    函数式接口 - 判断目标值是否在数组中占绝大多数
    """
    left_index = find_left(nums, target)
    right_index = find_right(nums, target)
    
    # 如果目标值不存在于数组中
    if left_index == len(nums) or nums[left_index] != target:
        return False
    
    count = right_index - left_index
    return count > len(nums) // 2

Solution = create_solution(is_majority_element)