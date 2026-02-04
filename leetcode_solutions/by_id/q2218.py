# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2218
标题: Paths in Maze That Lead to Same Room
难度: medium
链接: https://leetcode.cn/problems/paths-in-maze-that-lead-to-same-room/
题目类型: 图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给你一个 m x n 的矩阵 maze (下标从 0 开始)，maze[i][j] 不是 0 就是 1。0 表示空地，你可以穿过它；1 表示墙，你不能穿过它。
如果两个空地直接相邻（水平或垂直），那么它们属于同一个房间。你需要找到所有从起点到终点的路径，使得这些路径最终到达同一个房间。
返回所有这样的路径数量。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来遍历所有可能的路径，并使用哈希表来记录每个房间的访问情况。

算法步骤:
1. 初始化一个哈希表 `visited` 来记录每个房间的访问情况。
2. 定义一个递归的 DFS 函数，参数包括当前坐标 (x, y) 和当前路径。
3. 在 DFS 函数中，检查当前坐标是否越界或为墙，如果是则返回。
4. 检查当前坐标是否已经访问过，如果是则返回。
5. 如果当前坐标是终点，则将当前路径加入结果集。
6. 标记当前坐标为已访问。
7. 递归调用 DFS 函数，分别向四个方向移动 (上、下、左、右)。
8. 回溯时，取消标记当前坐标为已访问。

关键点:
- 使用哈希表记录每个房间的访问情况，避免重复访问。
- 使用递归和回溯来遍历所有可能的路径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(4^(m*n)) - 最坏情况下，每个格子都有四种可能的移动方向。
空间复杂度: O(m*n) - 递归栈的深度最多为 m*n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    """
    函数式接口 - 返回从起点到终点的所有路径数量，使得这些路径最终到达同一个房间。
    """
    if not maze or not maze[0]:
        return 0

    m, n = len(maze), len(maze[0])
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n or maze[x][y] == 1:
            return 0
        if (x, y) in visited:
            return 0
        if [x, y] == destination:
            return 1
        
        visited.add((x, y))
        count = sum(dfs(x + dx, y + dy) for dx, dy in directions)
        visited.remove((x, y))
        return count
    
    return dfs(start[0], start[1])

Solution = create_solution(solution_function_name)