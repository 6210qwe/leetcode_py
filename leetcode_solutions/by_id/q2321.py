# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2321
标题: Minimum Weighted Subgraph With the Required Paths
难度: hard
链接: https://leetcode.cn/problems/minimum-weighted-subgraph-with-the-required-paths/
题目类型: 图、最短路
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2203. 包含要求路径的最小带权子图 - 给你一个整数 n ，它表示一个 带权有向 图的节点数，节点编号为 0 到 n - 1 。 同时给你一个二维整数数组 edges ，其中 edges[i] = [fromi, toi, weighti] ，表示从 fromi 到 toi 有一条边权为 weighti 的 有向 边。 最后，给你三个 互不相同 的整数 src1 ，src2 和 dest ，表示图中三个不同的点。 请你从图中选出一个 边权和最小 的子图，使得从 src1 和 src2 出发，在这个子图中，都 可以 到达 dest 。如果这样的子图不存在，请返回 -1 。 子图 中的点和边都应该属于原图的一部分。子图的边权和定义为它所包含的所有边的权值之和。 示例 1： [https://assets.leetcode.com/uploads/2022/02/17/example1drawio.png] 输入：n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5 输出：9 解释： 上图为输入的图。 蓝色边为最优子图之一。 注意，子图 [[1,0,3],[0,5,6]] 也能得到最优解，但无法在满足所有限制的前提下，得到更优解。 示例 2： [https://assets.leetcode.com/uploads/2022/02/17/example2-1drawio.png] 输入：n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2 输出：-1 解释： 上图为输入的图。 可以看到，不存在从节点 1 到节点 2 的路径，所以不存在任何子图满足所有限制。 提示： * 3 <= n <= 105 * 0 <= edges.length <= 105 * edges[i].length == 3 * 0 <= fromi, toi, src1, src2, dest <= n - 1 * fromi != toi * src1 ，src2 和 dest 两两不同。 * 1 <= weight[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Dijkstra 算法分别从 src1, src2 和 dest 出发计算最短路径，然后枚举所有可能的交点，找到最小的路径和。

算法步骤:
1. 构建图的邻接表表示。
2. 使用 Dijkstra 算法从 src1, src2 和 dest 出发分别计算最短路径。
3. 枚举所有可能的交点，计算从 src1 和 src2 到 dest 的路径和，找到最小的路径和。

关键点:
- 使用优先队列（堆）来实现 Dijkstra 算法。
- 通过枚举所有可能的交点来找到最小的路径和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((E + V) log V)，其中 E 是边的数量，V 是节点的数量。Dijkstra 算法的时间复杂度是 O((E + V) log V)。
空间复杂度: O(E + V)，存储图的邻接表和最短路径的结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq
from collections import defaultdict

def dijkstra(n: int, graph: List[List[int]], start: int) -> List[int]:
    """
    使用 Dijkstra 算法计算从 start 到其他节点的最短路径。
    """
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

def minimum_weighted_subgraph(n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
    # 构建图的邻接表表示
    forward_graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for u, v, w in edges:
        forward_graph[u].append((v, w))
        reverse_graph[v].append((u, w))
    
    # 计算从 src1, src2 和 dest 出发的最短路径
    dist_src1 = dijkstra(n, forward_graph, src1)
    dist_src2 = dijkstra(n, forward_graph, src2)
    dist_dest = dijkstra(n, reverse_graph, dest)
    
    # 找到最小的路径和
    min_cost = float('inf')
    for i in range(n):
        if dist_src1[i] != float('inf') and dist_src2[i] != float('inf') and dist_dest[i] != float('inf'):
            min_cost = min(min_cost, dist_src1[i] + dist_src2[i] + dist_dest[i])
    
    return min_cost if min_cost != float('inf') else -1

Solution = create_solution(minimum_weighted_subgraph)