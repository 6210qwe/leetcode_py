# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 576
标题: Out of Boundary Paths
难度: medium
链接: https://leetcode.cn/problems/out-of-boundary-paths/
题目类型: 动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
576. 出界的路径数 - 给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。 给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 109 + 7 取余 后的结果。 示例 1： [https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_1.png] 输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0 输出：6 示例 2： [https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_2.png] 输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1 输出：12 提示： * 1 <= m, n <= 50 * 0 <= maxMove <= 50 * 0 <= startRow < m * 0 <= startColumn < n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。定义 dp[i][j][k] 表示从 (i, j) 出发，经过 k 步后出界的路径数。

算法步骤:
1. 初始化一个三维数组 dp，其中 dp[i][j][k] 表示从 (i, j) 出发，经过 k 步后出界的路径数。
2. 对于每一个位置 (i, j)，如果它在边界上，则 dp[i][j][0] = 1，否则 dp[i][j][0] = 0。
3. 通过状态转移方程更新 dp 数组：
   - 如果当前位置 (i, j) 不在边界上，则 dp[i][j][k] = (dp[i-1][j][k-1] + dp[i+1][j][k-1] + dp[i][j-1][k-1] + dp[i][j+1][k-1]) % (10**9 + 7)
   - 如果当前位置 (i, j) 在边界上，则 dp[i][j][k] = 0
4. 最终结果是 dp[startRow][startColumn][maxMove]

关键点:
- 使用三维数组 dp 来记录每个位置在每一步的状态。
- 状态转移方程考虑了四个方向的移动。
- 结果需要对 10^9 + 7 取余。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * maxMove)
空间复杂度: O(m * n * maxMove)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def out_of_boundary_paths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    """
    函数式接口 - 计算从 (startRow, startColumn) 出发，经过 maxMove 步后出界的路径数
    """
    MOD = 10**9 + 7
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 初始化 dp 数组
    dp = [[[0 for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]
    
    # 边界上的初始值
    for i in range(m):
        dp[i][0][0] = 1
        dp[i][n-1][0] = 1
    for j in range(n):
        dp[0][j][0] = 1
        dp[m-1][j][0] = 1
    
    # 更新 dp 数组
    for k in range(1, maxMove + 1):
        for i in range(m):
            for j in range(n):
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        dp[i][j][k] += dp[ni][nj][k-1]
                        dp[i][j][k] %= MOD
    
    return dp[startRow][startColumn][maxMove]


Solution = create_solution(out_of_boundary_paths)