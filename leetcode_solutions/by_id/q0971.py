# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 971
标题: Shortest Bridge
难度: medium
链接: https://leetcode.cn/problems/shortest-bridge/
题目类型: 深度优先搜索、广度优先搜索、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
934. 最短的桥 - 给你一个大小为 n x n 的二元矩阵 grid ，其中 1 表示陆地，0 表示水域。 岛 是由四面相连的 1 形成的一个最大组，即不会与非组内的任何其他 1 相连。grid 中 恰好存在两座岛 。 你可以将任意数量的 0 变为 1 ，以使两座岛连接起来，变成 一座岛 。 返回必须翻转的 0 的最小数目。 示例 1： 输入：grid = [[0,1],[1,0]] 输出：1 示例 2： 输入：grid = [[0,1,0],[0,0,0],[0,0,1]] 输出：2 示例 3： 输入：grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]] 输出：1 提示： * n == grid.length == grid[i].length * 2 <= n <= 100 * grid[i][j] 为 0 或 1 * grid 中恰有两个岛
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）找到第一个岛屿，并将其所有陆地标记为已访问。然后使用广度优先搜索（BFS）从这些已访问的陆地开始，逐步扩展到相邻的水域，直到到达第二个岛屿。

算法步骤:
1. 使用 DFS 找到第一个岛屿，并将其所有陆地标记为已访问。
2. 使用 BFS 从第一个岛屿的所有陆地开始，逐步扩展到相邻的水域，直到到达第二个岛屿。

关键点:
- 使用 DFS 标记第一个岛屿的所有陆地。
- 使用 BFS 从第一个岛屿的所有陆地开始扩展，找到最短路径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是网格的边长。每个单元格最多被访问两次（一次在 DFS 中，一次在 BFS 中）。
空间复杂度: O(n^2)，用于存储队列和访问标记。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def dfs(grid, i, j, queue):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
        return
    grid[i][j] = -1  # 标记为已访问
    queue.append((i, j))
    dfs(grid, i + 1, j, queue)
    dfs(grid, i - 1, j, queue)
    dfs(grid, i, j + 1, queue)
    dfs(grid, i, j - 1, queue)

def bfs(grid, queue):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    steps = 0
    while queue:
        for _ in range(len(queue)):
            i, j = queue.pop(0)
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                    if grid[ni][nj] == 1:
                        return steps
                    elif grid[ni][nj] == 0:
                        grid[ni][nj] = -1  # 标记为已访问
                        queue.append((ni, nj))
        steps += 1
    return steps

def solution_function_name(grid: List[List[int]]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    n = len(grid)
    queue = []
    
    # 使用 DFS 找到第一个岛屿，并将其所有陆地标记为已访问
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(grid, i, j, queue)
                break
        if queue:
            break
    
    # 使用 BFS 从第一个岛屿的所有陆地开始扩展，找到最短路径
    return bfs(grid, queue)

Solution = create_solution(solution_function_name)