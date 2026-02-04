# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2801
标题: Difference of Number of Distinct Values on Diagonals
难度: medium
链接: https://leetcode.cn/problems/difference-of-number-of-distinct-values-on-diagonals/
题目类型: 数组、哈希表、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2711. 对角线上不同值的数量差 - 给你一个下标从 0 开始、大小为 m x n 的二维矩阵 grid ，请你求解大小同样为 m x n 的答案矩阵 answer 。 矩阵 answer 中每个单元格 (r, c) 的值可以按下述方式进行计算： * 令 topLeft[r][c] 为矩阵 grid 中单元格 (r, c) 左上角对角线上 不同值 的数量。 * 令 bottomRight[r][c] 为矩阵 grid 中单元格 (r, c) 右下角对角线上 不同值 的数量。 然后 answer[r][c] = |topLeft[r][c] - bottomRight[r][c]| 。 返回矩阵 answer 。 矩阵对角线 是从最顶行或最左列的某个单元格开始，向右下方向走到矩阵末尾的对角线。 如果单元格 (r1, c1) 和单元格 (r, c) 属于同一条对角线且 r1 < r ，则单元格 (r1, c1) 属于单元格 (r, c) 的左上对角线。类似地，可以定义右下对角线。 示例 1： [https://assets.leetcode.com/uploads/2023/04/19/ex2.png] 输入：grid = [[1,2,3],[3,1,5],[3,2,1]] 输出：[[1,1,0],[1,0,1],[0,1,1]] 解释：第 1 个图表示最初的矩阵 grid 。 第 2 个图表示对单元格 (0,0) 计算，其中蓝色单元格是位于右下对角线的单元格。 第 3 个图表示对单元格 (1,2) 计算，其中红色单元格是位于左上对角线的单元格。 第 4 个图表示对单元格 (1,1) 计算，其中蓝色单元格是位于右下对角线的单元格，红色单元格是位于左上对角线的单元格。 - 单元格 (0,0) 的右下对角线包含 [1,1] ，而左上对角线包含 [] 。对应答案是 |1 - 0| = 1 。 - 单元格 (1,2) 的右下对角线包含 [] ，而左上对角线包含 [2] 。对应答案是 |0 - 1| = 1 。 - 单元格 (1,1) 的右下对角线包含 [1] ，而左上对角线包含 [1] 。对应答案是 |1 - 1| = 0 。 其他单元格的对应答案也可以按照这样的流程进行计算。 示例 2： 输入：grid = [[1]] 输出：[[0]] 解释：- 单元格 (0,0) 的右下对角线包含 [] ，左上对角线包含 [] 。对应答案是 |0 - 0| = 0 。 提示： * m == grid.length * n == grid[i].length * 1 <= m, n, grid[i][j] <= 50
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个字典分别记录每条对角线上的不同值的数量，然后计算每个单元格的 topLeft 和 bottomRight 值。

算法步骤:
1. 初始化两个字典 top_left 和 bottom_right，用于记录每条对角线上的不同值。
2. 遍历矩阵，更新 top_left 字典。
3. 再次遍历矩阵，更新 bottom_right 字典，并计算每个单元格的答案。

关键点:
- 使用字典记录每条对角线上的不同值，避免重复计算。
- 每条对角线可以通过 (r - c) 来唯一标识。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是矩阵的行数和列数。
空间复杂度: O(m + n)，用于存储对角线上的不同值。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def difference_of_distinct_values(grid: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 计算矩阵中每个单元格的对角线上不同值的数量差
    """
    m, n = len(grid), len(grid[0])
    answer = [[0] * n for _ in range(m)]
    top_left = {}
    bottom_right = {}

    # 更新 top_left 字典
    for r in range(m):
        for c in range(n):
            diag = r - c
            if diag not in top_left:
                top_left[diag] = set()
            top_left[diag].add(grid[r][c])

    # 更新 bottom_right 字典并计算答案
    for r in range(m - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            diag = r - c
            if diag not in bottom_right:
                bottom_right[diag] = set()
            bottom_right[diag].add(grid[r][c])
            answer[r][c] = abs(len(top_left[diag]) - len(bottom_right[diag]))

    return answer


Solution = create_solution(difference_of_distinct_values)