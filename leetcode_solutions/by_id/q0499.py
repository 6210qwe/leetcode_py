# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 499
标题: The Maze III
难度: hard
链接: https://leetcode.cn/problems/the-maze-iii/
题目类型: 深度优先搜索、广度优先搜索、图、数组、字符串、矩阵、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
499. 迷宫 III - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用带权 A* 算法来找到从起点到终点的最短路径

算法步骤:
1. 初始化迷宫的行数和列数，定义四个方向的移动向量
2. 定义一个优先队列，用于存储当前节点的状态 (距离, 步数, 当前位置)
3. 定义一个二维数组 `visited` 来记录每个位置的最小步数
4. 从起点开始进行 A* 搜索
5. 对于每个节点，尝试向四个方向滚动，直到遇到墙壁或边界
6. 更新优先队列和 `visited` 数组
7. 如果到达终点，返回结果

关键点:
- 使用优先队列来保证每次扩展的都是当前最优的节点
- 优化时间和空间复杂度
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * log(m * n)) - 其中 m 和 n 分别是迷宫的行数和列数
空间复杂度: O(m * n) - 用于存储 `visited` 数组和优先队列
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Tuple
import heapq

def the_maze_iii(maze: List[List[int]], start: List[int], destination: List[int]) -> str:
    """
    函数式接口 - 使用带权 A* 算法找到从起点到终点的最短路径
    
    实现思路:
    使用带权 A* 算法来找到从起点到终点的最短路径，并返回路径的字符串表示
    
    Args:
        maze: 二维数组表示的迷宫
        start: 起点坐标 [row, col]
        destination: 终点坐标 [row, col]
        
    Returns:
        返回从起点到终点的最短路径的字符串表示，如果无法到达终点则返回 "impossible"
        
    Example:
        >>> the_maze_iii([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,2], [0,4])
        'lul'
    """
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[float('inf')] * cols for _ in range(rows)]
    pq = [(0, 0, start[0], start[1])]
    visited[start[0]][start[1]] = 0

    while pq:
        dist, steps, r, c = heapq.heappop(pq)

        if [r, c] == destination:
            return build_path(maze, start, destination, visited)

        for dr, dc in directions:
            nr, nc, ndist, nsteps = r, c, dist, steps
            while 0 <= nr + dr < rows and 0 <= nc + dc < cols and maze[nr + dr][nc + dc] == 0:
                nr += dr
                nc += dc
                ndist += 1
                nsteps += 1

            if visited[nr][nc] > nsteps:
                visited[nr][nc] = nsteps
                heapq.heappush(pq, (ndist, nsteps, nr, nc))

    return "impossible"

def build_path(maze: List[List[int]], start: List[int], destination: List[int], visited: List[List[int]]) -> str:
    rows, cols = len(maze), len(maze[0])
    path = []
    r, c = destination
    steps = visited[r][c]

    while steps > 0:
        for dr, dc, dir_char in [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]:
            nr, nc = r - dr, c - dc
            if 0 <= nr < rows and 0 <= nc < cols and visited[nr][nc] == steps - 1:
                path.append(dir_char)
                r, c = nr, nc
                steps -= 1
                break

    return ''.join(reversed(path))

# 自动生成Solution类（无需手动编写）
Solution = create_solution(the_maze_iii)