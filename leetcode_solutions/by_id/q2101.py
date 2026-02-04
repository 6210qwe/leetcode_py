# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2101
标题: Last Day Where You Can Still Cross
难度: hard
链接: https://leetcode.cn/problems/last-day-where-you-can-still-cross/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、二分查找、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1970. 你能穿过矩阵的最后一天 - 给你一个下标从 1 开始的二进制矩阵，其中 0 表示陆地，1 表示水域。同时给你 row 和 col 分别表示矩阵中行和列的数目。 一开始在第 0 天，整个 矩阵都是 陆地 。但每一天都会有一块新陆地被 水 淹没变成水域。给你一个下标从 1 开始的二维数组 cells ，其中 cells[i] = [ri, ci] 表示在第 i 天，第 ri 行 ci 列（下标都是从 1 开始）的陆地会变成 水域 （也就是 0 变成 1 ）。 你想知道从矩阵最 上面 一行走到最 下面 一行，且只经过陆地格子的 最后一天 是哪一天。你可以从最上面一行的 任意 格子出发，到达最下面一行的 任意 格子。你只能沿着 四个 基本方向移动（也就是上下左右）。 请返回只经过陆地格子能从最 上面 一行走到最 下面 一行的 最后一天 。 示例 1： [https://assets.leetcode.com/uploads/2021/07/27/1.png] 输入：row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]] 输出：2 解释：上图描述了矩阵从第 0 天开始是如何变化的。 可以从最上面一行到最下面一行的最后一天是第 2 天。 示例 2： [https://assets.leetcode.com/uploads/2021/07/27/2.png] 输入：row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]] 输出：1 解释：上图描述了矩阵从第 0 天开始是如何变化的。 可以从最上面一行到最下面一行的最后一天是第 1 天。 示例 3： [https://assets.leetcode.com/uploads/2021/07/27/3.png] 输入：row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]] 输出：3 解释：上图描述了矩阵从第 0 天开始是如何变化的。 可以从最上面一行到最下面一行的最后一天是第 3 天。 提示： * 2 <= row, col <= 2 * 104 * 4 <= row * col <= 2 * 104 * cells.length == row * col * 1 <= ri <= row * 1 <= ci <= col * cells 中的所有格子坐标都是 唯一 的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找和深度优先搜索 (DFS) 来找到最后一天。

算法步骤:
1. 初始化矩阵为全陆地状态。
2. 使用二分查找来确定最后一天。
3. 在每次二分查找的过程中，使用 DFS 检查是否可以从最上面一行到达最下面一行。
4. 如果可以，则更新左边界；否则，更新右边界。

关键点:
- 二分查找的时间复杂度较低，适合处理大规模数据。
- DFS 用于检查连通性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(row * col * log(row * col)) - 二分查找的时间复杂度为 O(log(row * col))，每次检查的时间复杂度为 O(row * col)。
空间复杂度: O(row * col) - 存储矩阵和递归栈的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def can_cross(matrix: List[List[int]], start_row: int, start_col: int, visited: List[List[bool]]) -> bool:
    if start_row < 0 or start_row >= len(matrix) or start_col < 0 or start_col >= len(matrix[0]):
        return False
    if matrix[start_row][start_col] == 1 or visited[start_row][start_col]:
        return False
    if start_row == len(matrix) - 1:
        return True
    visited[start_row][start_col] = True
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in directions:
        if can_cross(matrix, start_row + dr, start_col + dc, visited):
            return True
    return False

def can_cross_from_top_to_bottom(matrix: List[List[int]]) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    for col in range(cols):
        if can_cross(matrix, 0, col, visited):
            return True
    return False

def solution_function_name(row: int, col: int, cells: List[List[int]]) -> int:
    """
    函数式接口 - 找到可以从最上面一行走到最下面一行的最后一天
    """
    left, right = 0, len(cells)
    while left < right:
        mid = (left + right) // 2
        matrix = [[0] * col for _ in range(row)]
        for i in range(mid):
            r, c = cells[i]
            matrix[r - 1][c - 1] = 1
        if can_cross_from_top_to_bottom(matrix):
            left = mid + 1
        else:
            right = mid
    return left - 1

Solution = create_solution(solution_function_name)