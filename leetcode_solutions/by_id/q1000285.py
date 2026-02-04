# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000285
标题: 最小路径和
难度: medium
链接: https://leetcode.cn/problems/0i0mDW/
题目类型: 数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 099. 最小路径和 - 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 说明：一个机器人每次只能向下或者向右移动一步。 示例 1： [https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg] 输入：grid = [[1,3,1],[1,5,1],[4,2,1]] 输出：7 解释：因为路径 1→3→1→1→1 的总和最小。 示例 2： 输入：grid = [[1,2,3],[4,5,6]] 输出：12 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 200 * 0 <= grid[i][j] <= 100 注意：本题与主站 64 题相同： https://leetcode.cn/problems/minimum-path-sum/ [https://leetcode.cn/problems/minimum-path-sum/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i][j] 为到达 (i, j) 位置的最小路径和。状态转移方程为 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]。

算法步骤:
1. 初始化 dp 数组，dp[0][0] = grid[0][0]。
2. 填充第一行和第一列，因为它们只能从左边或上边到达。
3. 从 (1, 1) 开始填充 dp 数组，直到 (m-1, n-1)。
4. 返回 dp[m-1][n-1] 作为结果。

关键点:
- 动态规划的状态转移方程
- 初始化 dp 数组的第一行和第一列
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是网格的行数和列数。
空间复杂度: O(m * n)，使用了同样大小的 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(grid: List[List[int]]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # 初始化起点
    dp[0][0] = grid[0][0]

    # 初始化第一行
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # 初始化第一列
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # 填充 dp 数组
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[m - 1][n - 1]


Solution = create_solution(solution_function_name)