# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1704
标题: Special Positions in a Binary Matrix
难度: easy
链接: https://leetcode.cn/problems/special-positions-in-a-binary-matrix/
题目类型: 数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1582. 二进制矩阵中的特殊位置 - 给定一个 m x n 的二进制矩阵 mat，返回矩阵 mat 中特殊位置的数量。 如果位置 (i, j) 满足 mat[i][j] == 1 并且行 i 与列 j 中的所有其他元素都是 0（行和列的下标从 0 开始计数），那么它被称为 特殊 位置。 示例 1： [https://assets.leetcode.com/uploads/2021/12/23/special1.jpg] 输入：mat = [[1,0,0],[0,0,1],[1,0,0]] 输出：1 解释：位置 (1, 2) 是一个特殊位置，因为 mat[1][2] == 1 且第 1 行和第 2 列的其他所有元素都是 0。 示例 2： [https://assets.leetcode.com/uploads/2021/12/24/special-grid.jpg] 输入：mat = [[1,0,0],[0,1,0],[0,0,1]] 输出：3 解释：位置 (0, 0)，(1, 1) 和 (2, 2) 都是特殊位置。 提示： * m == mat.length * n == mat[i].length * 1 <= m, n <= 100 * mat[i][j] 是 0 或 1。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个数组分别记录每一行和每一列中 1 的数量，然后遍历矩阵找到满足条件的特殊位置。

算法步骤:
1. 初始化两个数组 `row_count` 和 `col_count`，分别记录每一行和每一列中 1 的数量。
2. 遍历矩阵，更新 `row_count` 和 `col_count`。
3. 再次遍历矩阵，检查每个位置 (i, j) 是否满足 `mat[i][j] == 1` 且 `row_count[i] == 1` 且 `col_count[j] == 1`，如果是，则该位置为特殊位置。

关键点:
- 使用两个数组来记录每一行和每一列中 1 的数量，可以避免多次遍历矩阵。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 是矩阵的行数，n 是矩阵的列数。需要遍历矩阵两次。
空间复杂度: O(m + n)，使用了两个数组 `row_count` 和 `col_count` 来记录每一行和每一列中 1 的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def num_special_positions(mat: List[List[int]]) -> int:
    """
    函数式接口 - 返回矩阵中特殊位置的数量
    """
    m, n = len(mat), len(mat[0])
    row_count = [0] * m
    col_count = [0] * n

    # 记录每一行和每一列中 1 的数量
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                row_count[i] += 1
                col_count[j] += 1

    # 找到满足条件的特殊位置
    special_count = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                special_count += 1

    return special_count


Solution = create_solution(num_special_positions)