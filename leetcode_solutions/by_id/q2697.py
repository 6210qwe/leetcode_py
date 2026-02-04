# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2697
标题: Minimum Number of Visited Cells in a Grid
难度: hard
链接: https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/
题目类型: 栈、广度优先搜索、并查集、数组、动态规划、矩阵、单调栈、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2617. 网格图中最少访问的格子数 - 给你一个下标从 0 开始的 m x n 整数矩阵 grid 。你一开始的位置在 左上角 格子 (0, 0) 。 当你在格子 (i, j) 的时候，你可以移动到以下格子之一： * 满足 j < k <= grid[i][j] + j 的格子 (i, k) （向右移动），或者 * 满足 i < k <= grid[i][j] + i 的格子 (k, j) （向下移动）。 请你返回到达 右下角 格子 (m - 1, n - 1) 需要经过的最少移动格子数，如果无法到达右下角格子，请你返回 -1 。 示例 1： [https://assets.leetcode.com/uploads/2023/01/25/ex1.png] 输入：grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]] 输出：4 解释：上图展示了到达右下角格子经过的 4 个格子。 示例 2： [https://assets.leetcode.com/uploads/2023/01/25/ex2.png] 输入：grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]] 输出：3 解释：上图展示了到达右下角格子经过的 3 个格子。 示例 3： [https://assets.leetcode.com/uploads/2023/01/26/ex3.png] 输入：grid = [[2,1,0],[1,0,0]] 输出：-1 解释：无法到达右下角格子。 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 105 * 1 <= m * n <= 105 * 0 <= grid[i][j] < m * n * grid[m - 1][n - 1] == 0
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用优先队列（最小堆）来优化广度优先搜索（BFS），确保每次扩展的节点都是当前最优的选择。

算法步骤:
1. 初始化两个优先队列，分别用于存储行和列的可达位置。
2. 将起点 (0, 0) 加入优先队列，并初始化距离为 1。
3. 从优先队列中取出当前最优的节点，检查是否到达终点 (m-1, n-1)。
4. 如果未到达终点，将当前节点可以到达的所有新节点加入优先队列，并更新它们的距离。
5. 重复步骤 3 和 4，直到优先队列为空或找到终点。

关键点:
- 使用优先队列来保证每次扩展的节点都是当前最优的选择。
- 通过维护两个优先队列，分别处理行和列的可达位置，避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * log(m * n))，其中 m 和 n 分别是网格的行数和列数。每个节点最多被处理一次，且每次处理需要 O(log(m * n)) 的时间进行堆操作。
空间复杂度: O(m * n)，最坏情况下所有节点都会被加入优先队列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from heapq import heappush, heappop

def min_visited_cells(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])
    row_queues = [[] for _ in range(m)]
    col_queues = [[] for _ in range(n)]
    distances = [[float('inf')] * n for _ in range(m)]
    distances[0][0] = 1

    def add_to_queue(queue, i, j, distance):
        heappush(queue, (distance, i, j))

    def process_queue(queue):
        while queue and distances[queue[0][1]][queue[0][2]] < queue[0][0]:
            heappop(queue)

    def expand(i, j, distance):
        if i == m - 1 and j == n - 1:
            return distance
        max_row = min(j + grid[i][j], n - 1)
        max_col = min(i + grid[i][j], m - 1)
        for k in range(j + 1, max_row + 1):
            if distances[i][k] > distance + 1:
                distances[i][k] = distance + 1
                add_to_queue(row_queues[i], i, k, distance + 1)
        for k in range(i + 1, max_col + 1):
            if distances[k][j] > distance + 1:
                distances[k][j] = distance + 1
                add_to_queue(col_queues[j], k, j, distance + 1)

    add_to_queue(row_queues[0], 0, 0, 1)
    add_to_queue(col_queues[0], 0, 0, 1)

    while any(row_queues) or any(col_queues):
        for i in range(m):
            process_queue(row_queues[i])
            if row_queues[i]:
                _, i, j = heappop(row_queues[i])
                result = expand(i, j, distances[i][j])
                if result != float('inf'):
                    return result
        for j in range(n):
            process_queue(col_queues[j])
            if col_queues[j]:
                _, i, j = heappop(col_queues[j])
                result = expand(i, j, distances[i][j])
                if result != float('inf'):
                    return result

    return -1

Solution = create_solution(min_visited_cells)