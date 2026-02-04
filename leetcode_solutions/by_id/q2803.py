# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2803
标题: Modify Graph Edge Weights
难度: hard
链接: https://leetcode.cn/problems/modify-graph-edge-weights/
题目类型: 图、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2699. 修改图中的边权 - 给你一个 n 个节点的 无向带权连通 图，节点编号为 0 到 n - 1 ，再给你一个整数数组 edges ，其中 edges[i] = [ai, bi, wi] 表示节点 ai 和 bi 之间有一条边权为 wi 的边。 部分边的边权为 -1（wi = -1），其他边的边权都为 正 数（wi > 0）。 你需要将所有边权为 -1 的边都修改为范围 [1, 2 * 109] 中的 正整数 ，使得从节点 source 到节点 destination 的 最短距离 为整数 target 。如果有 多种 修改方案可以使 source 和 destination 之间的最短距离等于 target ，你可以返回任意一种方案。 如果存在使 source 到 destination 最短距离为 target 的方案，请你按任意顺序返回包含所有边的数组（包括未修改边权的边）。如果不存在这样的方案，请你返回一个 空数组 。 注意：你不能修改一开始边权为正数的边。 示例 1： [https://assets.leetcode.com/uploads/2023/04/18/graph.png] 输入：n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5 输出：[[4,1,1],[2,0,1],[0,3,3],[4,3,1]] 解释：上图展示了一个满足题意的修改方案，从 0 到 1 的最短距离为 5 。 示例 2： [https://assets.leetcode.com/uploads/2023/04/18/graph-2.png] 输入：n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6 输出：[] 解释：上图是一开始的图。没有办法通过修改边权为 -1 的边，使得 0 到 2 的最短距离等于 6 ，所以返回一个空数组。 示例 3： [https://assets.leetcode.com/uploads/2023/04/19/graph-3.png] 输入：n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6 输出：[[1,0,4],[1,2,3],[2,3,5],[0,3,1]] 解释：上图展示了一个满足题意的修改方案，从 0 到 2 的最短距离为 6 。 提示： * 1 <= n <= 100 * 1 <= edges.length <= n * (n - 1) / 2 * edges[i].length == 3 * 0 <= ai, bi < n * wi = -1 或者 1 <= wi <= 107 * ai != bi * 0 <= source, destination < n * source != destination * 1 <= target <= 109 * 输入的图是连通图，且没有自环和重边。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Dijkstra 算法计算最短路径，并在需要时调整边权。

算法步骤:
1. 构建图的邻接表表示。
2. 使用 Dijkstra 算法计算从 source 到 destination 的最短路径。
3. 如果最短路径小于 target，则无法通过增加边权来达到目标，返回空数组。
4. 如果最短路径等于 target，则返回当前的边列表。
5. 如果最短路径大于 target，则尝试将边权为 -1 的边调整为合适的值，使得最短路径等于 target。

关键点:
- 使用优先队列（最小堆）实现 Dijkstra 算法。
- 在调整边权时，确保调整后的边权仍然在 [1, 2 * 10^9] 范围内。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((E + V) log V)，其中 E 是边的数量，V 是顶点的数量。
空间复杂度: O(E + V)，用于存储图的邻接表和 Dijkstra 算法的辅助数据结构。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq

def modify_graph_edge_weights(n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
    # 构建图的邻接表表示
    graph = [[] for _ in range(n)]
    edge_indices = {}
    for i, (u, v, w) in enumerate(edges):
        graph[u].append((v, w, i))
        graph[v].append((u, w, i))
        if w == -1:
            edge_indices[(u, v)] = i
            edge_indices[(v, u)] = i

    def dijkstra() -> int:
        min_heap = [(0, source)]
        distance = [float('inf')] * n
        distance[source] = 0
        while min_heap:
            dist, node = heapq.heappop(min_heap)
            if dist > distance[node]:
                continue
            for neighbor, weight, idx in graph[node]:
                new_dist = dist + (weight if weight != -1 else 1)
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))
        return distance[destination]

    # 计算初始最短路径
    shortest_path = dijkstra()

    if shortest_path < target:
        return []
    elif shortest_path == target:
        return edges

    # 尝试调整边权
    for u, v, w in edges:
        if w == -1:
            idx = edge_indices[(u, v)]
            edges[idx][2] = 2 * 10**9
            shortest_path = dijkstra()
            if shortest_path <= target:
                edges[idx][2] = target - (shortest_path - 2 * 10**9) + 1
                return edges
            edges[idx][2] = 1

    return []

Solution = create_solution(modify_graph_edge_weights)