# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1171
标题: Shortest Path in Binary Matrix
难度: medium
链接: https://leetcode.cn/problems/shortest-path-in-binary-matrix/
题目类型: 广度优先搜索、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1091. 二进制矩阵中的最短路径 - 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求： * 路径途经的所有单元格的值都是 0 。 * 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。 畅通路径的长度 是该路径途经的单元格总数。 示例 1： [https://assets.leetcode.com/uploads/2021/02/18/example1_1.png] 输入：grid = [[0,1],[1,0]] 输出：2 示例 2： [https://assets.leetcode.com/uploads/2021/02/18/example2_1.png] 输入：grid = [[0,0,0],[1,1,0],[1,1,0]] 输出：4 示例 3： 输入：grid = [[1,0,0],[1,1,0],[1,1,0]] 输出：-1 提示： * n == grid.length * n == grid[i].length * 1 <= n <= 100 * grid[i][j] 为 0 或 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 来找到从左上角到右下角的最短路径。

算法步骤:
1. 检查起点和终点是否可达，如果不可达直接返回 -1。
2. 初始化队列，将起点 (0, 0) 加入队列，并标记为已访问。
3. 使用 BFS 进行层次遍历，每次从队列中取出一个节点，检查其八个方向的邻居节点。
4. 如果邻居节点是终点，返回当前路径长度。
5. 如果邻居节点未被访问且值为 0，则将其加入队列并标记为已访问。
6. 如果队列为空且未找到终点，返回 -1。

关键点:
- 使用队列进行层次遍历。
- 使用集合记录已访问的节点，避免重复访问。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是矩阵的边长。每个节点最多只会被访问一次。
空间复杂度: O(n^2)，队列和访问集合的最大空间消耗。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    """
    函数式接口 - 使用广度优先搜索 (BFS) 找到从左上角到右下角的最短路径。
    """
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    queue = [(0, 0, 1)]  # (row, col, path_length)
    visited = set([(0, 0)])
    
    while queue:
        row, col, path_length = queue.pop(0)
        if row == n - 1 and col == n - 1:
            return path_length
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, path_length + 1))
                visited.add((new_row, new_col))
    
    return -1


Solution = create_solution(shortest_path_binary_matrix)