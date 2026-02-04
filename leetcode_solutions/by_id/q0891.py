# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 891
标题: Score After Flipping Matrix
难度: medium
链接: https://leetcode.cn/problems/score-after-flipping-matrix/
题目类型: 贪心、位运算、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
861. 翻转矩阵后的得分 - 给你一个大小为 m x n 的二元矩阵 grid ，矩阵中每个元素的值为 0 或 1 。 一次 移动 是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。 在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的 得分 就是这些数字的总和。 在执行任意次 移动 后（含 0 次），返回可能的最高分数。 示例 1： [https://assets.leetcode.com/uploads/2021/07/23/lc-toogle1.jpg] 输入：grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]] 输出：39 解释：0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39 示例 2： 输入：grid = [[0]] 输出：1 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 20 * grid[i][j] 为 0 或 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过贪心算法最大化每一行的二进制值。首先确保每一行的第一个元素为1，然后逐列检查，如果某一列的0比1多，则翻转该列。

算法步骤:
1. 确保每一行的第一个元素为1，如果不是则翻转该行。
2. 逐列检查，如果某一列的0比1多，则翻转该列。
3. 计算最终矩阵的得分。

关键点:
- 优先保证每一行的第一个元素为1，因为最高位对二进制数的影响最大。
- 逐列检查并翻转0比1多的列，以最大化每行的二进制值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def flip_row(grid: List[List[int]], row: int) -> None:
    for col in range(len(grid[0])):
        grid[row][col] = 1 - grid[row][col]


def flip_col(grid: List[List[int]], col: int) -> None:
    for row in range(len(grid)):
        grid[row][col] = 1 - grid[row][col]


def matrix_score(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    # 确保每一行的第一个元素为1
    for row in range(m):
        if grid[row][0] == 0:
            flip_row(grid, row)
    
    # 逐列检查，如果某一列的0比1多，则翻转该列
    for col in range(1, n):
        count_ones = sum(grid[row][col] for row in range(m))
        if count_ones < (m + 1) // 2:
            flip_col(grid, col)
    
    # 计算最终矩阵的得分
    score = 0
    for row in range(m):
        binary_value = 0
        for col in range(n):
            binary_value = (binary_value << 1) | grid[row][col]
        score += binary_value
    
    return score


Solution = create_solution(matrix_score)