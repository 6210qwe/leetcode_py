# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3693
标题: Minimum Time to Break Locks II
难度: hard
链接: https://leetcode.cn/problems/minimum-time-to-break-locks-ii/
题目类型: 深度优先搜索、图、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3385. 破解锁的最少时间 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用Dijkstra算法找到从起点到终点的最短路径。

算法步骤:
1. 初始化一个优先队列（最小堆），将起点加入队列，并设置起点的距离为0。
2. 使用一个字典来记录每个节点的最短距离。
3. 从优先队列中取出当前距离最小的节点，更新其邻居节点的距离。
4. 如果邻居节点的距离被更新，则将其加入优先队列。
5. 重复上述步骤，直到优先队列为空或找到终点。

关键点:
- 使用优先队列来确保每次处理的都是当前距离最小的节点。
- 使用字典来记录每个节点的最短距离，避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log V)，其中E是边的数量，V是节点的数量。因为每次从优先队列中取出元素的时间复杂度是O(log V)，而我们需要处理所有的边。
空间复杂度: O(V + E)，存储节点和边的信息。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import heapq

def solution_function_name(grid: List[List[int]]) -> int:
    """
    函数式接口 - 使用Dijkstra算法找到从起点到终点的最短路径。
    """
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]  # (distance, x, y)

    while pq:
        d, x, y = heapq.heappop(pq)
        if x == m - 1 and y == n - 1:
            return d
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                new_dist = d + grid[nx][ny]
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))

    return -1

Solution = create_solution(solution_function_name)