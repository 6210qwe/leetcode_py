# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1847
标题: Largest Subarray Length K
难度: easy
链接: https://leetcode.cn/problems/largest-subarray-length-k/
题目类型: 贪心、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1708. 长度为 K 的最大子数组 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口找到长度为 k 的最大子数组。

算法步骤:
1. 初始化一个变量 `max_subarray` 来存储当前找到的最大子数组。
2. 使用滑动窗口遍历数组，每次比较当前窗口的子数组与 `max_subarray`，更新 `max_subarray`。
3. 返回 `max_subarray`。

关键点:
- 使用切片操作来获取当前窗口的子数组。
- 比较子数组时，使用字典序比较。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int], k: int) -> List[int]:
    """
    函数式接口 - 找到长度为 k 的最大子数组
    """
    n = len(nums)
    if n == k:
        return nums
    
    max_subarray = nums[:k]
    
    for i in range(1, n - k + 1):
        current_subarray = nums[i:i + k]
        if current_subarray > max_subarray:
            max_subarray = current_subarray
    
    return max_subarray


Solution = create_solution(solution_function_name)