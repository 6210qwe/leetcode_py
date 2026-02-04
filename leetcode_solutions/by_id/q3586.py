# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3586
标题: Constructing Two Increasing Arrays
难度: hard
链接: https://leetcode.cn/problems/constructing-two-increasing-arrays/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3269. 构建两个递增数组 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来构建两个递增数组。我们需要找到一种方法，使得两个数组的和尽可能小。

算法步骤:
1. 初始化一个二维数组 dp，其中 dp[i][j] 表示前 i 个元素中，第一个数组的最后一个元素为 j 时的最小和。
2. 遍历每个元素，更新 dp 数组。
3. 最后，通过回溯 dp 数组来构建两个递增数组。

关键点:
- 使用动态规划来记录每一步的最优解。
- 通过回溯 dp 数组来构建最终的两个数组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是数组的长度。
空间复杂度: O(n^2)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int]) -> List[List[int]]:
    """
    函数式接口 - 构建两个递增数组
    """
    n = len(nums)
    if n == 0:
        return [[], []]

    # 初始化 dp 数组
    dp = [[float('inf')] * n for _ in range(n)]
    prev = [[None] * n for _ in range(n)]

    # 基本情况
    for i in range(n):
        dp[0][i] = nums[i]
        prev[0][i] = -1

    # 动态规划填充 dp 数组
    for i in range(1, n):
        for j in range(i, n):
            for k in range(j):
                if nums[k] < nums[j] and dp[i-1][k] + nums[j] < dp[i][j]:
                    dp[i][j] = dp[i-1][k] + nums[j]
                    prev[i][j] = k

    # 找到最优解
    min_sum = float('inf')
    last_index = -1
    for j in range(n):
        if dp[n-1][j] < min_sum:
            min_sum = dp[n-1][j]
            last_index = j

    # 回溯构建两个数组
    array1, array2 = [], []
    for i in range(n-1, -1, -1):
        if i % 2 == 0:
            array1.append(nums[last_index])
        else:
            array2.append(nums[last_index])
        last_index = prev[i][last_index]

    return [array1[::-1], array2[::-1]]


Solution = create_solution(solution_function_name)