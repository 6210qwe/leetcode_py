# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3386
标题: Find Edges in Shortest Paths
难度: hard
链接: https://leetcode.cn/problems/find-edges-in-shortest-paths/
题目类型: 深度优先搜索、广度优先搜索、图、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3123. 最短路径中的边 - 给你一个 n 个节点的无向带权图，节点编号为 0 到 n - 1 。图中总共有 m 条边，用二维数组 edges 表示，其中 edges[i] = [ai, bi, wi] 表示节点 ai 和 bi 之间有一条边权为 wi 的边。 对于节点 0 为出发点，节点 n - 1 为结束点的所有最短路，你需要返回一个长度为 m 的 boolean 数组 answer ，如果 edges[i] 至少 在其中一条最短路上，那么 answer[i] 为 true ，否则 answer[i] 为 false 。 请你返回数组 answer 。 注意，图可能不连通。 示例 1： [https://assets.leetcode.com/uploads/2024/03/05/graph35drawio-1.png] 输入：n = 6, edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]] 输出：[true,true,true,false,true,true,true,false] 解释： 以下为节点 0 出发到达节点 5 的 所有 最短路： * 路径 0 -> 1 -> 5 ：边权和为 4 + 1 = 5 。 * 路径 0 -> 2 -> 3 -> 5 ：边权和为 1 + 1 + 3 = 5 。 * 路径 0 -> 2 -> 3 -> 1 -> 5 ：边权和为 1 + 1 + 2 + 1 = 5 。 示例 2： [https://assets.leetcode.com/uploads/2024/03/05/graphhhh.png] 输入：n = 4, edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]] 输出：[true,false,false,true] 解释： 只有一条从节点 0 出发到达节点 3 的最短路 0 -> 2 -> 3 ，边权和为 1 + 2 = 3 。 提示： * 2 <= n <= 5 * 104 * m == edges.length * 1 <= m <= min(5 * 104, n * (n - 1) / 2) * 0 <= ai, bi < n * ai != bi * 1 <= wi <= 105 * 图中没有重边。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Dijkstra 算法找到从起点到终点的最短路径，并记录所有在最短路径上的边。

算法步骤:
1. 构建图的邻接表表示。
2. 使用 Dijkstra 算法找到从起点到终点的最短路径，并记录路径上的边。
3. 再次使用 Dijkstra 算法找到从终点到起点的最短路径，并记录路径上的边。
4. 合并两次 Dijkstra 算法记录的边，得到最终结果。

关键点:
- 使用 Dijkstra 算法找到最短路径。
- 记录路径上的边。
- 两次 Dijkstra 算法分别从起点到终点和从终点到起点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((m + n) log n)，其中 m 是边的数量，n 是节点的数量。Dijkstra 算法的时间复杂度是 O((m + n) log n)。
空间复杂度: O(m + n)，存储图的邻接表和优先队列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Tuple
import heapq

def find_edges_in_shortest_paths(n: int, edges: List[List[int]]) -> List[bool]:
    def dijkstra(graph: List[List[Tuple[int, int]]], start: int, end: int) -> List[Tuple[int, int]]:
        dist = [float('inf')] * n
        dist[start] = 0
        pq = [(0, start)]
        visited = [False] * n
        shortest_edges = set()

        while pq:
            d, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True

            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
                    shortest_edges.add((u, v))
                    shortest_edges.add((v, u))

        return shortest_edges

    # 构建图的邻接表表示
    graph = [[] for _ in range(n)]
    for a, b, w in edges:
        graph[a].append((b, w))
        graph[b].append((a, w))

    # 从起点到终点的最短路径
    forward_edges = dijkstra(graph, 0, n - 1)

    # 从终点到起点的最短路径
    reverse_edges = dijkstra(graph, n - 1, 0)

    # 合并两次 Dijkstra 算法记录的边
    result = [False] * len(edges)
    for i, (a, b, _) in enumerate(edges):
        if (a, b) in forward_edges and (b, a) in reverse_edges:
            result[i] = True

    return result

Solution = create_solution(find_edges_in_shortest_paths)