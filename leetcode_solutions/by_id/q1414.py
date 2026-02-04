# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1414
标题: Shortest Path in a Grid with Obstacles Elimination
难度: hard
链接: https://leetcode.cn/problems/shortest-path-in-a-grid-with-obstacles-elimination/
题目类型: 广度优先搜索、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1293. 网格中的最短路径 - 给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。 如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1 。 示例 1： [https://pic.leetcode.cn/1700710956-kcxqcC-img_v3_025f_d55a658c-8f40-464b-800f-22ccd27cc9fg.jpg] 输入： grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1 输出：6 解释： 不消除任何障碍的最短路径是 10。 消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2). 示例 2： [https://pic.leetcode.cn/1700710701-uPqkZe-img_v3_025f_0edd50fb-8a70-4a42-add0-f602caaad35g.jpg] 输入：grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1 输出：-1 解释：我们至少需要消除两个障碍才能找到这样的路径。 提示： * grid.length == m * grid[0].length == n * 1 <= m, n <= 40 * 1 <= k <= m*n * grid[i][j] 是 0 或 1 * grid[0][0] == grid[m-1][n-1] == 0
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 来找到从起点到终点的最短路径。使用一个队列来存储当前节点的位置、剩余可消除障碍物的数量和当前步数。同时使用一个集合来记录已经访问过的状态，避免重复访问。

算法步骤:
1. 初始化队列和访问集合。
2. 从起点 (0, 0) 开始进行 BFS。
3. 对于每个节点，检查其四个方向的邻居。
4. 如果邻居是终点且可以到达，则返回当前步数。
5. 如果邻居是障碍物且剩余可消除障碍物数量大于 0，则将其加入队列。
6. 如果邻居是空地，则直接加入队列。
7. 如果遍历完所有可能的路径仍未找到终点，则返回 -1。

关键点:
- 使用元组 (x, y, remaining_k) 来表示状态，确保不会重复访问相同的状态。
- 通过 BFS 保证找到的路径是最短路径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * k)，其中 m 和 n 分别是网格的行数和列数，k 是最多可以消除的障碍物数量。每个状态最多会被访问一次。
空间复杂度: O(m * n * k)，用于存储队列和访问集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def shortest_path_with_obstacles_elimination(grid: List[List[int]], k: int) -> int:
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [(0, 0, k)]
    visited = set([(0, 0, k)])

    steps = 0
    while queue:
        for _ in range(len(queue)):
            x, y, remaining_k = queue.pop(0)
            if x == m - 1 and y == n - 1:
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    next_k = remaining_k - grid[nx][ny]
                    if next_k >= 0 and (nx, ny, next_k) not in visited:
                        visited.add((nx, ny, next_k))
                        queue.append((nx, ny, next_k))

        steps += 1

    return -1


Solution = create_solution(shortest_path_with_obstacles_elimination)