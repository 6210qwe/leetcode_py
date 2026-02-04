# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3550
标题: Maximum Value Sum by Placing Three Rooks I
难度: hard
链接: https://leetcode.cn/problems/maximum-value-sum-by-placing-three-rooks-i/
题目类型: 数组、动态规划、枚举、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3256. 放三个车的价值之和最大 I - 给你一个 m x n 的二维整数数组 board ，它表示一个国际象棋棋盘，其中 board[i][j] 表示格子 (i, j) 的 价值 。 处于 同一行 或者 同一列 车会互相 攻击 。你需要在棋盘上放三个车，确保它们两两之间都 无法互相攻击 。 请你返回满足上述条件下，三个车所在格子 值 之和 最大 为多少。 示例 1： 输入：board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]] 输出：4 解释： [https://assets.leetcode.com/uploads/2024/08/08/rooks2.png] 我们可以将车分别放在格子 (0, 2) ，(1, 3) 和 (2, 1) 处，价值之和为 1 + 1 + 2 = 4 。 示例 2： 输入：board = [[1,2,3],[4,5,6],[7,8,9]] 输出：15 解释： 我们可以将车分别放在格子 (0, 0) ，(1, 1) 和 (2, 2) 处，价值之和为 1 + 5 + 9 = 15 。 示例 3： 输入：board = [[1,1,1],[1,1,1],[1,1,1]] 输出：3 解释： 我们可以将车分别放在格子 (0, 2) ，(1, 1) 和 (2, 0) 处，价值之和为 1 + 1 + 1 = 3 。 提示： * 3 <= m == board.length <= 100 * 3 <= n == board[i].length <= 100 * -109 <= board[i][j] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用预处理和动态规划来找到三个不冲突的车的最大价值和。

算法步骤:
1. 预处理每一行和每一列的最大值及其索引。
2. 枚举所有可能的三行组合，并计算每种组合下的最大值。
3. 使用动态规划来优化枚举过程，减少重复计算。

关键点:
- 预处理每一行和每一列的最大值及其索引，以便快速查找。
- 使用动态规划来优化枚举过程，减少时间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * log n)
空间复杂度: O(m * n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(board: List[List[int]]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    m, n = len(board), len(board[0])
    
    # 预处理每一行的最大值及其索引
    row_maxes = []
    for i in range(m):
        max_val = max(board[i])
        max_idx = board[i].index(max_val)
        row_maxes.append((max_val, max_idx))
    
    # 预处理每一列的最大值及其索引
    col_maxes = []
    for j in range(n):
        col = [board[i][j] for i in range(m)]
        max_val = max(col)
        max_idx = col.index(max_val)
        col_maxes.append((max_val, max_idx))
    
    # 动态规划表
    dp = [[[float('-inf')] * n for _ in range(n)] for _ in range(m)]
    
    # 初始化dp表
    for i in range(m):
        for j in range(n):
            for k in range(n):
                if j != k:
                    dp[i][j][k] = board[i][j] + board[i][k]
    
    # 填充dp表
    for i in range(1, m):
        for j in range(n):
            for k in range(n):
                if j != k:
                    for l in range(n):
                        if l != j and l != k:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][l][j] + board[i][k])
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][l][k] + board[i][j])
    
    # 找到最大值
    max_sum = float('-inf')
    for i in range(m):
        for j in range(n):
            for k in range(n):
                if j != k:
                    max_sum = max(max_sum, dp[i][j][k])
    
    return max_sum


Solution = create_solution(solution_function_name)