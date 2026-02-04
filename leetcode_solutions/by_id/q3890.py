# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3890
标题: Smallest Subarray to Sort in Every Sliding Window
难度: medium
链接: https://leetcode.cn/problems/smallest-subarray-to-sort-in-every-sliding-window/
题目类型: 栈、贪心、数组、双指针、排序、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3555. 排序每个滑动窗口中最小的子数组 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用单调栈和双指针来找到每个滑动窗口中需要排序的最小子数组。

算法步骤:
1. 使用单调递增栈从左到右遍历数组，找到每个元素左边第一个大于它的元素的位置。
2. 使用单调递减栈从右到左遍历数组，找到每个元素右边第一个小于它的元素的位置。
3. 对于每个滑动窗口，通过上述两个栈的结果，找到需要排序的最小子数组的起始和结束位置。

关键点:
- 使用单调栈可以在 O(n) 时间内找到每个元素左右边界。
- 双指针用于在每个滑动窗口中快速找到需要排序的子数组。
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

from typing import List

def smallest_subarray_to_sort(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    left_greater = [-1] * n
    right_less = [n] * n
    stack = []
    
    # 单调递增栈，找到每个元素左边第一个大于它的元素的位置
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            top = stack.pop()
            right_less[top] = i
        if stack:
            left_greater[i] = stack[-1]
        stack.append(i)
    
    # 单调递减栈，找到每个元素右边第一个小于它的元素的位置
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] < nums[i]:
            top = stack.pop()
            left_greater[top] = i
        if stack:
            right_less[i] = stack[-1]
        stack.append(i)
    
    result = []
    for i in range(n - k + 1):
        start = i
        end = i + k - 1
        while start <= end and (left_greater[start] >= i or right_less[start] <= i + k - 1):
            start += 1
        while start <= end and (left_greater[end] >= i or right_less[end] <= i + k - 1):
            end -= 1
        result.append(end - start + 1)
    
    return result

Solution = create_solution(smallest_subarray_to_sort)