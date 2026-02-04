# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 918
标题: Reachable Nodes In Subdivided Graph
难度: hard
链接: https://leetcode.cn/problems/reachable-nodes-in-subdivided-graph/
题目类型: 图、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
882. 细分图中的可到达节点 - 给你一个无向图（原始图），图中有 n 个节点，编号从 0 到 n - 1 。你决定将图中的每条边 细分 为一条节点链，每条边之间的新节点数各不相同。 图用由边组成的二维数组 edges 表示，其中 edges[i] = [ui, vi, cnti] 表示原始图中节点 ui 和 vi 之间存在一条边，cnti 是将边 细分 后的新节点总数。注意，cnti == 0 表示边不可细分。 要 细分 边 [ui, vi] ，需要将其替换为 (cnti + 1) 条新边，和 cnti 个新节点。新节点为 x1, x2, ..., xcnti ，新边为 [ui, x1], [x1, x2], [x2, x3], ..., [xcnti-1, xcnti], [xcnti, vi] 。 现在得到一个 新的细分图 ，请你计算从节点 0 出发，可以到达多少个节点？如果节点间距离是 maxMoves 或更少，则视为 可以到达 。 给你原始图和 maxMoves ，返回 新的细分图中从节点 0 出发 可到达的节点数 。 示例 1： [https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/01/origfinal.png] 输入：edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3 输出：13 解释：边的细分情况如上图所示。 可以到达的节点已经用黄色标注出来。 示例 2： 输入：edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4 输出：23 示例 3： 输入：edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5 输出：1 解释：节点 0 与图的其余部分没有连通，所以只有节点 0 可以到达。 提示： * 0 <= edges.length <= min(n * (n - 1) / 2, 104) * edges[i].length == 3 * 0 <= ui < vi < n * 图中 不存在平行边 * 0 <= cnti <= 104 * 0 <= maxMoves <= 109 * 1 <= n <= 3000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Dijkstra 算法找到从节点 0 出发到其他节点的最短路径，并记录每条边上可以到达的新节点数。

算法步骤:
1. 构建图的邻接表表示。
2. 使用 Dijkstra 算法找到从节点 0 出发到其他节点的最短路径。
3. 计算每个节点的可达性。
4. 计算每条边上可以到达的新节点数。

关键点:
- 使用优先队列来实现 Dijkstra 算法。
- 记录每条边上可以到达的新节点数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((E + V) log V)，其中 E 是边的数量，V 是节点的数量。
空间复杂度: O(E + V)，用于存储图的邻接表和最短路径信息。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

def reachableNodes(edges: List[List[int]], maxMoves: int, n: int) -> int:
    # 构建图的邻接表表示
    graph = [[] for _ in range(n)]
    for u, v, cnt in edges:
        graph[u].append((v, cnt))
        graph[v].append((u, cnt))

    # Dijkstra 算法
    dist = [float('inf')] * n
    dist[0] = 0
    pq = [(0, 0)]  # (distance, node)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, cnt in graph[u]:
            if d + cnt + 1 < dist[v]:
                dist[v] = d + cnt + 1
                heapq.heappush(pq, (dist[v], v))

    # 计算每个节点的可达性
    reachable_nodes = sum(1 for d in dist if d <= maxMoves)

    # 计算每条边上可以到达的新节点数
    used_edges = {}
    for u, v, cnt in edges:
        used_edges[(u, v)] = min(cnt, max(maxMoves - dist[u], 0))
        used_edges[(v, u)] = min(cnt, max(maxMoves - dist[v], 0))
        reachable_nodes += min(cnt, used_edges[(u, v)] + used_edges[(v, u)])

    return reachable_nodes

Solution = create_solution(reachableNodes)