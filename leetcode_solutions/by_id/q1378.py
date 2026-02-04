# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1378
标题: Cells with Odd Values in a Matrix
难度: easy
链接: https://leetcode.cn/problems/cells-with-odd-values-in-a-matrix/
题目类型: 数组、数学、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1252. 奇数值单元格的数目 - 给你一个 m x n 的矩阵，最开始的时候，每个单元格中的值都是 0。 另有一个二维索引数组 indices，indices[i] = [ri, ci] 指向矩阵中的某个位置，其中 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。 对 indices[i] 所指向的每个位置，应同时执行下述增量操作： 1. ri 行上的所有单元格，加 1 。 2. ci 列上的所有单元格，加 1 。 给你 m、n 和 indices 。请你在执行完所有 indices 指定的增量操作后，返回矩阵中 奇数值单元格 的数目。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/11/06/e1.png] 输入：m = 2, n = 3, indices = [[0,1],[1,1]] 输出：6 解释：最开始的矩阵是 [[0,0,0],[0,0,0]]。 第一次增量操作后得到 [[1,2,1],[0,1,0]]。 最后的矩阵是 [[1,3,1],[1,3,1]]，里面有 6 个奇数。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/11/06/e2.png] 输入：m = 2, n = 2, indices = [[1,1],[0,0]] 输出：0 解释：最后的矩阵是 [[2,2],[2,2]]，里面没有奇数。 提示： * 1 <= m, n <= 50 * 1 <= indices.length <= 100 * 0 <= ri < m * 0 <= ci < n 进阶：你可以设计一个时间复杂度为 O(n + m + indices.length) 且仅用 O(n + m) 额外空间的算法来解决此问题吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个计数器分别记录每一行和每一列的增量次数，然后计算最终矩阵中奇数值单元格的数量。

算法步骤:
1. 初始化两个计数器 `row_counts` 和 `col_counts`，分别记录每一行和每一列的增量次数。
2. 遍历 `indices`，对于每个索引 `[ri, ci]`，将 `row_counts[ri]` 和 `col_counts[ci]` 增加 1。
3. 遍历整个矩阵，对于每个单元格 `(i, j)`，其值为 `row_counts[i] + col_counts[j]`，如果该值为奇数，则计数器 `odd_count` 增加 1。
4. 返回 `odd_count`。

关键点:
- 使用两个计数器来避免直接构建矩阵，从而节省空间。
- 通过遍历矩阵并计算每个单元格的值来确定奇数值单元格的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m + n + len(indices))
空间复杂度: O(m + n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def oddCells(m: int, n: int, indices: List[List[int]]) -> int:
    """
    计算矩阵中奇数值单元格的数量
    """
    row_counts = [0] * m
    col_counts = [0] * n
    
    for ri, ci in indices:
        row_counts[ri] += 1
        col_counts[ci] += 1
    
    odd_count = 0
    for i in range(m):
        for j in range(n):
            if (row_counts[i] + col_counts[j]) % 2 == 1:
                odd_count += 1
    
    return odd_count


Solution = create_solution(oddCells)