# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1073
标题: Number of Enclaves
难度: medium
链接: https://leetcode.cn/problems/number-of-enclaves/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1020. 飞地的数量 - 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。 示例 1： [https://assets.leetcode.com/uploads/2021/02/18/enclaves1.jpg] 输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]] 输出：3 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。 示例 2： [https://assets.leetcode.com/uploads/2021/02/18/enclaves2.jpg] 输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]] 输出：0 解释：所有 1 都在边界上或可以到达边界。 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 500 * grid[i][j] 的值为 0 或 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来标记所有可以从边界到达的陆地单元格，然后计算剩余的陆地单元格数量。

算法步骤:
1. 初始化一个与 grid 大小相同的 visited 矩阵，用于记录访问状态。
2. 从边界上的每个陆地单元格开始进行 DFS，将所有可以到达的陆地单元格标记为已访问。
3. 遍历整个 grid，统计未被标记的陆地单元格数量。

关键点:
- 从边界开始进行 DFS，确保所有可以到达边界的陆地单元格都被标记。
- 只统计未被标记的陆地单元格。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是 grid 的行数和列数。每个单元格最多访问一次。
空间复杂度: O(m * n)，最坏情况下递归栈的深度可能达到 m * n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def numEnclaves(grid: List[List[int]]) -> int:
    """
    函数式接口 - 计算飞地的数量
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r: int, c: int):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or visited[r][c]:
            return
        visited[r][c] = True
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    # 从边界开始进行 DFS
    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    # 统计未被标记的陆地单元格数量
    enclaves = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                enclaves += 1

    return enclaves


Solution = create_solution(numEnclaves)