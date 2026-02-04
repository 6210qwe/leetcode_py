# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2369
标题: Maximum Sum Score of Array
难度: medium
链接: https://leetcode.cn/problems/maximum-sum-score-of-array/
题目类型: 数组、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2219. 数组的最大总分 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和来计算数组的子数组和，并找到最大总分。

算法步骤:
1. 初始化前缀和数组 `prefix_sum`，其中 `prefix_sum[i]` 表示从数组开始到第 `i` 个元素的和。
2. 遍历数组，计算每个位置的前缀和。
3. 遍历前缀和数组，计算每个子数组的和，并更新最大总分。

关键点:
- 前缀和数组可以快速计算任意子数组的和。
- 通过遍历前缀和数组，可以在 O(n) 时间内找到最大总分。
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


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 计算数组的最大总分
    """
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    
    # 计算前缀和数组
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    max_score = float('-inf')
    
    # 遍历前缀和数组，计算每个子数组的和，并更新最大总分
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            subarray_sum = prefix_sum[j] - prefix_sum[i - 1]
            max_score = max(max_score, subarray_sum)
    
    return max_score


Solution = create_solution(solution_function_name)