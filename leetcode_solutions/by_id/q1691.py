# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1691
标题: Minimum Number of Days to Disconnect Island
难度: hard
链接: https://leetcode.cn/problems/minimum-number-of-days-to-disconnect-island/
题目类型: 深度优先搜索、广度优先搜索、数组、矩阵、强连通分量
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1568. 使陆地分离的最少天数 - 给你一个大小为 m x n ，由若干 0 和 1 组成的二维网格 grid ，其中 1 表示陆地， 0 表示水。岛屿 由水平方向或竖直方向上相邻的 1 （陆地）连接形成。 如果 恰好只有一座岛屿 ，则认为陆地是 连通的 ；否则，陆地就是 分离的 。 一天内，可以将 任何单个 陆地单元（1）更改为水单元（0）。 返回使陆地分离的最少天数。 示例 1： [https://assets.leetcode.com/uploads/2021/12/24/land1.jpg] 输入：grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]] 输出：2 解释：至少需要 2 天才能得到分离的陆地。 将陆地 grid[1][1] 和 grid[0][2] 更改为水，得到两个分离的岛屿。 示例 2： [https://assets.leetcode.com/uploads/2021/12/24/land2.jpg] 输入：grid = [[1,1]] 输出：2 解释：如果网格中都是水，也认为是分离的 ([[1,1]] -> [[0,0]])，0 岛屿。 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 30 * grid[i][j] 为 0 或 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过深度优先搜索 (DFS) 来判断岛屿是否可以被分成两部分。如果岛屿本身就是不连通的，则返回 0。如果岛屿只有一个点，则返回 1。否则，尝试删除每个陆地单元并检查是否可以使岛屿分离。

算法步骤:
1. 定义 DFS 函数来遍历岛屿。
2. 定义一个函数来检查岛屿是否连通。
3. 遍历每个陆地单元，尝试将其变为水，并检查岛屿是否分离。
4. 如果岛屿不能通过删除一个陆地单元分离，则返回 2。

关键点:
- 使用 DFS 来遍历岛屿。
- 通过删除每个陆地单元并检查岛屿是否分离来找到最小天数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * (m + n))，其中 m 和 n 是网格的行数和列数。最坏情况下，我们需要对每个陆地单元进行一次完整的 DFS 检查。
空间复杂度: O(m * n)，用于存储访问状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def dfs(grid, i, j, visited):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or visited[i][j]:
        return
    visited[i][j] = True
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for di, dj in directions:
        dfs(grid, i + di, j + dj, visited)

def is_connected(grid):
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(grid, i, j, visited)
                count += 1
    return count == 1

def min_days_to_disconnect_island(grid: List[List[int]]) -> int:
    if not is_connected(grid):
        return 0
    if sum(cell for row in grid for cell in row) == 1:
        return 1
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                grid[i][j] = 0
                if not is_connected(grid):
                    return 1
                grid[i][j] = 1
    return 2

Solution = create_solution(min_days_to_disconnect_island)