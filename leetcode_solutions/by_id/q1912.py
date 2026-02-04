# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1912
标题: Number of Restricted Paths From First to Last Node
难度: medium
链接: https://leetcode.cn/problems/number-of-restricted-paths-from-first-to-last-node/
题目类型: 图、拓扑排序、动态规划、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1786. 从第一个节点出发到最后一个节点的受限路径数 - 现有一个加权无向连通图。给你一个正整数 n ，表示图中有 n 个节点，并按从 1 到 n 给节点编号；另给你一个数组 edges ，其中每个 edges[i] = [ui, vi, weighti] 表示存在一条位于节点 ui 和 vi 之间的边，这条边的权重为 weighti 。 从节点 start 出发到节点 end 的路径是一个形如 [z0, z1, z2, ..., zk] 的节点序列，满足 z0 = start 、zk = end 且在所有符合 0 <= i <= k-1 的节点 zi 和 zi+1 之间存在一条边。 路径的距离定义为这条路径上所有边的权重总和。用 distanceToLastNode(x) 表示节点 n 和 x 之间路径的最短距离。受限路径 为满足 distanceToLastNode(zi) > distanceToLastNode(zi+1) 的一条路径，其中 0 <= i <= k-1 。 返回从节点 1 出发到节点 n 的 受限路径数 。由于数字可能很大，请返回对 109 + 7 取余 的结果。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/03/07/restricted_paths_ex1.png] 输入：n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]] 输出：3 解释：每个圆包含黑色的节点编号和蓝色的 distanceToLastNode 值。三条受限路径分别是： 1) 1 --> 2 --> 5 2) 1 --> 2 --> 3 --> 5 3) 1 --> 3 --> 5 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/03/07/restricted_paths_ex22.png] 输入：n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]] 输出：1 解释：每个圆包含黑色的节点编号和蓝色的 distanceToLastNode 值。唯一一条受限路径是：1 --> 3 --> 7 。 提示： * 1 <= n <= 2 * 104 * n - 1 <= edges.length <= 4 * 104 * edges[i].length == 3 * 1 <= ui, vi <= n * ui != vi * 1 <= weighti <= 105 * 任意两个节点之间至多存在一条边 * 任意两个节点之间至少存在一条路径
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Dijkstra 算法计算从最后一个节点到其他所有节点的最短路径，然后使用动态规划计算从第一个节点到最后一个节点的受限路径数。

算法步骤:
1. 构建图的邻接表表示。
2. 使用 Dijkstra 算法计算从最后一个节点到其他所有节点的最短路径。
3. 使用动态规划计算从第一个节点到最后一个节点的受限路径数，确保路径上的节点满足受限路径的条件。

关键点:
- 使用优先队列优化 Dijkstra 算法的时间复杂度。
- 动态规划时，使用记忆化搜索避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((E + V) log V)，其中 E 是边的数量，V 是节点的数量。Dijkstra 算法的时间复杂度是 O((E + V) log V)，动态规划的时间复杂度是 O(E + V)。
空间复杂度: O(E + V)，存储图的邻接表、最短路径和动态规划的状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from heapq import heappop, heappush

def countRestrictedPaths(n: int, edges: List[List[int]]) -> int:
    MOD = 10**9 + 7
    graph = [[] for _ in range(n + 1)]
    
    # 构建图的邻接表
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # 使用 Dijkstra 算法计算从最后一个节点到其他所有节点的最短路径
    dist = [float('inf')] * (n + 1)
    dist[n] = 0
    pq = [(0, n)]
    
    while pq:
        d, node = heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if dist[neighbor] > d + weight:
                dist[neighbor] = d + weight
                heappush(pq, (dist[neighbor], neighbor))
    
    # 动态规划计算从第一个节点到最后一个节点的受限路径数
    dp = [-1] * (n + 1)
    
    def dfs(node: int) -> int:
        if node == n:
            return 1
        if dp[node] != -1:
            return dp[node]
        
        count = 0
        for neighbor, _ in graph[node]:
            if dist[neighbor] < dist[node]:
                count += dfs(neighbor)
                count %= MOD
        
        dp[node] = count
        return count
    
    return dfs(1)

Solution = create_solution(countRestrictedPaths)