# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2343
标题: Count Unguarded Cells in the Grid
难度: medium
链接: https://leetcode.cn/problems/count-unguarded-cells-in-the-grid/
题目类型: 数组、矩阵、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2257. 统计网格图中没有被保卫的格子数 - 给你两个整数 m 和 n 表示一个下标从 0 开始的 m x n 网格图。同时给你两个二维整数数组 guards 和 walls ，其中 guards[i] = [rowi, coli] 且 walls[j] = [rowj, colj] ，分别表示第 i 个警卫和第 j 座墙所在的位置。 一个警卫能看到 4 个坐标轴方向（即东、南、西、北）的 所有 格子，除非他们被一座墙或者另外一个警卫 挡住 了视线。如果一个格子能被 至少 一个警卫看到，那么我们说这个格子被 保卫 了。 请你返回空格子中，有多少个格子是 没被保卫 的。 示例 1： [https://assets.leetcode.com/uploads/2022/03/10/example1drawio2.png] 输入：m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]] 输出：7 解释：上图中，被保卫和没有被保卫的格子分别用红色和绿色表示。 总共有 7 个没有被保卫的格子，所以我们返回 7 。 示例 2： [https://assets.leetcode.com/uploads/2022/03/10/example2drawio.png] 输入：m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]] 输出：4 解释：上图中，没有被保卫的格子用绿色表示。 总共有 4 个没有被保卫的格子，所以我们返回 4 。 提示： * 1 <= m, n <= 105 * 2 <= m * n <= 105 * 1 <= guards.length, walls.length <= 5 * 104 * 2 <= guards.length + walls.length <= m * n * guards[i].length == walls[j].length == 2 * 0 <= rowi, rowj < m * 0 <= coli, colj < n * guards 和 walls 中所有位置 互不相同 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个二维数组来标记每个格子的状态，并通过四个方向遍历每个警卫的视野范围。

算法步骤:
1. 初始化一个 m x n 的二维数组 `grid`，用于标记每个格子的状态（0 表示未访问，1 表示警卫，2 表示墙，3 表示被保卫）。
2. 将所有的警卫和墙的位置标记在 `grid` 中。
3. 对于每个警卫，向四个方向（东、南、西、北）遍历，直到遇到墙或另一个警卫为止，将路径上的格子标记为被保卫。
4. 最后统计 `grid` 中未被保卫的格子数量。

关键点:
- 使用一个二维数组来标记每个格子的状态。
- 通过四个方向遍历每个警卫的视野范围，确保每个格子只被访问一次。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)
空间复杂度: O(m * n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_unguarded_cells(m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    # 初始化网格
    grid = [[0] * n for _ in range(m)]
    
    # 标记警卫和墙
    for r, c in guards:
        grid[r][c] = 1
    for r, c in walls:
        grid[r][c] = 2
    
    # 四个方向
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # 遍历每个警卫
    for r, c in guards:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2 and grid[nr][nc] != 1:
                grid[nr][nc] = 3
                nr += dr
                nc += dc
    
    # 统计未被保卫的格子数量
    unguarded_count = sum(cell == 0 for row in grid for cell in row)
    return unguarded_count


Solution = create_solution(count_unguarded_cells)