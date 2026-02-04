# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3389
标题: Minimum Time to Visit Disappearing Nodes
难度: medium
链接: https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/
题目类型: 图、数组、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3112. 访问消失节点的最少时间 - 给你一个二维数组 edges 表示一个 n 个点的无向图，其中 edges[i] = [ui, vi, lengthi] 表示节点 ui 和节点 vi 之间有一条需要 lengthi 单位时间通过的无向边。 同时给你一个数组 disappear ，其中 disappear[i] 表示节点 i 从图中消失的时间点，在那一刻及以后，你无法再访问这个节点。 注意，图有可能一开始是不连通的，两个节点之间也可能有多条边。 请你返回数组 answer ，answer[i] 表示从节点 0 到节点 i 需要的 最少 单位时间。如果从节点 0 出发 无法 到达节点 i ，那么 answer[i] 为 -1 。 示例 1： [https://assets.leetcode.com/uploads/2024/03/09/example1.png] 输入：n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5] 输出：[0,-1,4] 解释： 我们从节点 0 出发，目的是用最少的时间在其他节点消失之前到达它们。 * 对于节点 0 ，我们不需要任何时间，因为它就是我们的起点。 * 对于节点 1 ，我们需要至少 2 单位时间，通过 edges[0] 到达。但当我们到达的时候，它已经消失了，所以我们无法到达它。 * 对于节点 2 ，我们需要至少 4 单位时间，通过 edges[2] 到达。 示例 2： [https://assets.leetcode.com/uploads/2024/03/09/example2.png] 输入：n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,3,5] 输出：[0,2,3] 解释： 我们从节点 0 出发，目的是用最少的时间在其他节点消失之前到达它们。 * 对于节点 0 ，我们不需要任何时间，因为它就是我们的起点。 * 对于节点 1 ，我们需要至少 2 单位时间，通过 edges[0] 到达。 * 对于节点 2 ，我们需要至少 3 单位时间，通过 edges[0] 和 edges[1] 到达。 示例 3： 输入：n = 2, edges = [[0,1,1]], disappear = [1,1] 输出：[0,-1] 解释： 当我们到达节点 1 的时候，它恰好消失，所以我们无法到达节点 1 。 提示： * 1 <= n <= 5 * 104 * 0 <= edges.length <= 105 * edges[i] == [ui, vi, lengthi] * 0 <= ui, vi <= n - 1 * 1 <= lengthi <= 105 * disappear.length == n * 1 <= disappear[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Dijkstra 算法来找到从节点 0 到其他节点的最短路径，并且在计算过程中考虑每个节点的消失时间。

算法步骤:
1. 构建图的邻接表表示。
2. 使用 Dijkstra 算法，从节点 0 开始进行最短路径搜索。
3. 在每次更新节点的距离时，检查该节点是否已经消失。
4. 如果节点已经消失，则跳过该节点。
5. 如果可以到达某个节点，则记录其最短路径时间。
6. 返回结果数组。

关键点:
- 使用优先队列（最小堆）来实现 Dijkstra 算法。
- 在更新距离时，检查节点是否已经消失。
- 初始化结果数组为 -1，表示无法到达。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log E)，其中 E 是边的数量。Dijkstra 算法的时间复杂度主要由优先队列的操作决定。
空间复杂度: O(N + E)，其中 N 是节点数量，E 是边的数量。存储图的邻接表和优先队列所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

def minimum_time_to_visit_disappearing_nodes(n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
    # 构建图的邻接表表示
    graph = [[] for _ in range(n)]
    for u, v, length in edges:
        graph[u].append((v, length))
        graph[v].append((u, length))

    # 初始化距离数组和优先队列
    dist = [float('inf')] * n
    dist[0] = 0
    pq = [(0, 0)]  # (distance, node)

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        # 如果当前节点已经消失，跳过
        if current_dist >= disappear[current_node]:
            continue
        
        # 更新邻居节点的距离
        for neighbor, length in graph[current_node]:
            new_dist = current_dist + length
            if new_dist < dist[neighbor] and new_dist < disappear[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    # 构建结果数组
    result = [-1] * n
    for i in range(n):
        if dist[i] != float('inf'):
            result[i] = dist[i]

    return result

Solution = create_solution(minimum_time_to_visit_disappearing_nodes)