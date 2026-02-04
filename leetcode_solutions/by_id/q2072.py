# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2072
标题: Maximum of Minimum Values in All Subarrays
难度: medium
链接: https://leetcode.cn/problems/maximum-of-minimum-values-in-all-subarrays/
题目类型: 栈、数组、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1950. 所有子数组最小值中的最大值 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用单调栈来找到每个元素作为子数组最小值的范围。

算法步骤:
1. 初始化一个单调递增栈，用于存储元素的索引。
2. 遍历数组，对于每个元素，计算其作为子数组最小值的范围。
3. 使用栈来维护当前元素左侧和右侧第一个小于当前元素的位置。
4. 计算每个元素作为子数组最小值的最大值。

关键点:
- 使用单调栈可以在线性时间内找到每个元素作为子数组最小值的范围。
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


def max_of_min_subarray(nums: List[int]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    n = len(nums)
    left_bound = [0] * n
    right_bound = [n - 1] * n
    stack = []

    # 找到每个元素左侧第一个小于它的位置
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            left_bound[i] = stack[-1] + 1
        stack.append(i)

    stack = []

    # 找到每个元素右侧第一个小于它的位置
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            right_bound[i] = stack[-1] - 1
        stack.append(i)

    # 计算每个元素作为子数组最小值的最大值
    result = 0
    for i in range(n):
        min_val = nums[i]
        subarray_length = right_bound[i] - left_bound[i] + 1
        result = max(result, min_val * subarray_length)

    return result


Solution = create_solution(max_of_min_subarray)