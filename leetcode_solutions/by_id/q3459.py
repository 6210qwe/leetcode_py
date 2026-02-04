# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3459
标题: Find the Minimum Area to Cover All Ones II
难度: hard
链接: https://leetcode.cn/problems/find-the-minimum-area-to-cover-all-ones-ii/
题目类型: 数组、枚举、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3197. 包含所有 1 的最小矩形面积 II - 给你一个二维 二进制 数组 grid。你需要找到 3 个 不重叠、面积 非零 、边在水平方向和竖直方向上的矩形，并且满足 grid 中所有的 1 都在这些矩形的内部。 返回这些矩形面积之和的 最小 可能值。 注意，这些矩形可以相接。 示例 1： 输入： grid = [[1,0,1],[1,1,1]] 输出： 5 解释： [https://assets.leetcode.com/uploads/2024/05/14/example0rect21.png] * 位于 (0, 0) 和 (1, 0) 的 1 被一个面积为 2 的矩形覆盖。 * 位于 (0, 2) 和 (1, 2) 的 1 被一个面积为 2 的矩形覆盖。 * 位于 (1, 1) 的 1 被一个面积为 1 的矩形覆盖。 示例 2： 输入： grid = [[1,0,1,0],[0,1,0,1]] 输出： 5 解释： [https://assets.leetcode.com/uploads/2024/05/14/example1rect2.png] * 位于 (0, 0) 和 (0, 2) 的 1 被一个面积为 3 的矩形覆盖。 * 位于 (1, 1) 的 1 被一个面积为 1 的矩形覆盖。 * 位于 (1, 3) 的 1 被一个面积为 1 的矩形覆盖。 提示： * 1 <= grid.length, grid[i].length <= 30 * grid[i][j] 是 0 或 1。 * 输入保证 grid 中至少有三个 1 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们可以通过预处理来计算每个位置的前缀和，然后使用动态规划来找到最小的矩形面积。

算法步骤:
1. 计算每个位置的前缀和。
2. 使用动态规划来枚举所有可能的矩形组合，并记录最小的面积和。
3. 返回最小的矩形面积和。

关键点:
- 使用前缀和来快速计算矩形内的 1 的数量。
- 动态规划的状态转移方程需要仔细设计，以确保不重叠的矩形组合。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^4 * m^2)，其中 n 和 m 分别是 grid 的行数和列数。我们需要枚举所有可能的矩形组合。
空间复杂度: O(n * m)，用于存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def min_area_rectangles(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    
    # 计算前缀和
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + grid[i - 1][j - 1]
    
    # 动态规划
    dp = [[[float('inf')] * m for _ in range(m)] for _ in range(4)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(j + 1, m + 1):
                count = prefix_sum[i][k] - prefix_sum[i][j - 1] - prefix_sum[i - 1][k] + prefix_sum[i - 1][j - 1]
                if count > 0:
                    dp[1][j][k] = min(dp[1][j][k], (i - 1) * (k - j))
                    for l in range(1, j):
                        dp[2][l][k] = min(dp[2][l][k], dp[1][l][j] + (i - 1) * (k - j))
                        for p in range(1, l):
                            dp[3][p][k] = min(dp[3][p][k], dp[2][p][l] + (i - 1) * (k - j))
    
    return min(min(row) for row in dp[3])

Solution = create_solution(min_area_rectangles)