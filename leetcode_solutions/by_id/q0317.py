# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 317
标题: Shortest Distance from All Buildings
难度: hard
链接: https://leetcode.cn/problems/shortest-distance-from-all-buildings/
题目类型: 广度优先搜索、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
317. 离建筑物最近的距离 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 从每个建筑物BFS，累加距离，找最小总距离

算法步骤:
1. 从每个建筑物开始BFS
2. 累加每个空地的距离
3. 找到最小总距离的空地

关键点:
- 多源BFS
- 累加距离
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m*n*k) - k为建筑物数量
空间复杂度: O(m*n) - 距离矩阵
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import deque
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def shortest_distance(grid: List[List[int]]) -> int:
    """
    函数式接口 - 离建筑物最近的距离
    
    实现思路:
    从每个建筑物BFS，累加距离，找最小总距离。
    
    Args:
        grid: 网格矩阵（0为空地，1为建筑物，2为障碍）
        
    Returns:
        最小总距离，如果不存在返回-1
        
    Example:
        >>> shortest_distance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]])
        7
    """
    if not grid or not grid[0]:
        return -1
    
    m, n = len(grid), len(grid[0])
    buildings = []
    
    # 找到所有建筑物
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                buildings.append((i, j))
    
    # 距离矩阵和可达计数
    dist = [[0] * n for _ in range(m)]
    reach = [[0] * n for _ in range(m)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 从每个建筑物BFS
    for bi, bj in buildings:
        queue = deque([(bi, bj, 0)])
        visited = {(bi, bj)}
        
        while queue:
            i, j, d = queue.popleft()
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and \
                   grid[ni][nj] == 0 and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    dist[ni][nj] += d + 1
                    reach[ni][nj] += 1
                    queue.append((ni, nj, d + 1))
    
    # 找到最小总距离
    result = float('inf')
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and reach[i][j] == len(buildings):
                result = min(result, dist[i][j])
    
    return result if result != float('inf') else -1


# 自动生成Solution类（无需手动编写）
Solution = create_solution(shortest_distance)
