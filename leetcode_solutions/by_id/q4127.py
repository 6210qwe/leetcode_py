# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4127
标题: Minimum Distance Excluding One Maximum Weighted Edge
难度: medium
链接: https://leetcode.cn/problems/minimum-distance-excluding-one-maximum-weighted-edge/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3778. 排除一个最大权重边的最小距离 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Dijkstra 算法找到从起点到所有节点的最短路径，然后遍历每条边，排除该边后重新计算最短路径。

算法步骤:
1. 使用 Dijkstra 算法计算从起点到所有节点的最短路径。
2. 遍历每条边，假设排除该边，重新计算从起点到终点的最短路径。
3. 找到排除某条边后的最小路径长度。

关键点:
- 使用优先队列优化 Dijkstra 算法。
- 在排除某条边后，使用已有的最短路径信息来快速计算新的最短路径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log V + E * (V + E))，其中 E 是边的数量，V 是节点的数量。Dijkstra 算法的时间复杂度是 O(E log V)，遍历每条边并重新计算最短路径的时间复杂度是 O(E * (V + E))。
空间复杂度: O(V + E)，存储图和最短路径信息。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq

def dijkstra(n: int, edges: List[List[int]], start: int) -> List[int]:
    """
    使用 Dijkstra 算法计算从起点到所有节点的最短路径。
    """
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist

def min_distance_excluding_one_max_weighted_edge(n: int, edges: List[List[int]], start: int, end: int) -> int:
    """
    计算排除一个最大权重边的最小距离。
    """
    # 计算从起点到所有节点的最短路径
    dist_start = dijkstra(n, edges, start)
    
    # 计算从终点到所有节点的最短路径
    dist_end = dijkstra(n, edges, end)
    
    min_dist = float('inf')
    
    # 遍历每条边，假设排除该边，重新计算从起点到终点的最短路径
    for u, v, w in edges:
        new_dist = dist_start[u] + w + dist_end[v]
        if new_dist < min_dist:
            min_dist = new_dist
    
    return min_dist

Solution = create_solution(min_distance_excluding_one_max_weighted_edge)