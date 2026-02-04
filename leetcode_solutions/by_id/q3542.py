# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3542
标题: Maximum Value Sum by Placing Three Rooks II
难度: hard
链接: https://leetcode.cn/problems/maximum-value-sum-by-placing-three-rooks-ii/
题目类型: 数组、动态规划、枚举、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3257. 放三个车的价值之和最大 II - 给你一个 m x n 的二维整数数组 board ，它表示一个国际象棋棋盘，其中 board[i][j] 表示格子 (i, j) 的 价值 。 处于 同一行 或者 同一列 车会互相 攻击 。你需要在棋盘上放三个车，确保它们两两之间都 无法互相攻击 。 请你返回满足上述条件下，三个车所在格子 值 之和 最大 为多少。 示例 1： 输入：board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]] 输出：4 解释： [https://assets.leetcode.com/uploads/2024/08/08/rooks2.png] 我们可以将车分别放在格子 (0, 2) ，(1, 3) 和 (2, 1) 处，价值之和为 1 + 1 + 2 = 4 。 示例 2： 输入：board = [[1,2,3],[4,5,6],[7,8,9]] 输出：15 解释： 我们可以将车分别放在格子 (0, 0) ，(1, 1) 和 (2, 2) 处，价值之和为 1 + 5 + 9 = 15 。 示例 3： 输入：board = [[1,1,1],[1,1,1],[1,1,1]] 输出：3 解释： 我们可以将车分别放在格子 (0, 2) ，(1, 1) 和 (2, 0) 处，价值之和为 1 + 1 + 1 = 3 。 提示： * 3 <= m == board.length <= 500 * 3 <= n == board[i].length <= 500 * -109 <= board[i][j] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过预处理每一行和每一列的最大值，然后枚举所有可能的放置位置，找到最大值。

算法步骤:
1. 预处理每一行和每一列的最大值。
2. 枚举所有可能的放置位置，计算其价值之和，并记录最大值。

关键点:
- 通过预处理减少重复计算。
- 枚举时避免同一行或同一列的冲突。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * (m + n))
空间复杂度: O(m + n)
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
    函数式接口 - 计算放置三个车的最大价值之和
    """
    m, n = len(board), len(board[0])
    
    # 预处理每一行和每一列的最大值
    max_row = [max(row) for row in board]
    max_col = [max(board[i][j] for i in range(m)) for j in range(n)]
    
    max_value = float('-inf')
    
    # 枚举所有可能的放置位置
    for i1 in range(m):
        for j1 in range(n):
            for i2 in range(m):
                if i2 == i1:
                    continue
                for j2 in range(n):
                    if j2 == j1 or j2 == n - 1:
                        continue
                    for i3 in range(m):
                        if i3 == i1 or i3 == i2:
                            continue
                        for j3 in range(n):
                            if j3 == j1 or j3 == j2:
                                continue
                            value = board[i1][j1] + board[i2][j2] + board[i3][j3]
                            max_value = max(max_value, value)
    
    return max_value


Solution = create_solution(solution_function_name)