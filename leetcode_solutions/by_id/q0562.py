# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 562
标题: Longest Line of Consecutive One in Matrix
难度: medium
链接: https://leetcode.cn/problems/longest-line-of-consecutive-one-in-matrix/
题目类型: 数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
562. 矩阵中最长的连续1线段 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来记录四个方向（水平、垂直、对角线和反对角线）的最长连续1线段。

算法步骤:
1. 初始化一个四维数组 dp，其中 dp[i][j][0] 表示从 (i, j) 开始的水平方向的最长连续1线段长度，
   dp[i][j][1] 表示从 (i, j) 开始的垂直方向的最长连续1线段长度，
   dp[i][j][2] 表示从 (i, j) 开始的对角线方向的最长连续1线段长度，
   dp[i][j][3] 表示从 (i, j) 开始的反对角线方向的最长连续1线段长度。
2. 遍历矩阵，更新 dp 数组，并记录最长的连续1线段长度。

关键点:
- 使用动态规划避免重复计算
- 通过四个方向的状态转移方程来更新 dp 数组
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是矩阵的行数和列数。
空间复杂度: O(m * n)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_line(matrix: List[List[int]]) -> int:
    """
    函数式接口 - 计算矩阵中最长的连续1线段
    """
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(m)]
    max_length = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                # 水平方向
                dp[i][j][0] = dp[i][j-1][0] + 1 if j > 0 else 1
                # 垂直方向
                dp[i][j][1] = dp[i-1][j][1] + 1 if i > 0 else 1
                # 对角线方向
                dp[i][j][2] = dp[i-1][j-1][2] + 1 if i > 0 and j > 0 else 1
                # 反对角线方向
                dp[i][j][3] = dp[i-1][j+1][3] + 1 if i > 0 and j < n-1 else 1
                # 更新最大长度
                max_length = max(max_length, max(dp[i][j]))

    return max_length


Solution = create_solution(longest_line)