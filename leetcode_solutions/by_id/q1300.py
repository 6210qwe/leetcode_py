# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1300
标题: Critical Connections in a Network
难度: hard
链接: https://leetcode.cn/problems/critical-connections-in-a-network/
题目类型: 深度优先搜索、图、双连通分量
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1192. 查找集群内的关键连接 - 力扣数据中心有 n 台服务器，分别按从 0 到 n-1 的方式进行了编号。它们之间以 服务器到服务器 的形式相互连接组成了一个内部集群，连接是无向的。用 connections 表示集群网络，connections[i] = [a, b] 表示服务器 a 和 b 之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器。 关键连接 是在该集群中的重要连接，假如我们将它移除，便会导致某些服务器无法访问其他服务器。 请你以任意顺序返回该集群内的所有 关键连接 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/original_images/critical-connections-in-a-network.png] 输入：n = 4, connections = [[0,1],[1,2],[2,0],[1,3]] 输出：[[1,3]] 解释：[[3,1]] 也是正确的。 示例 2: 输入：n = 2, connections = [[0,1]] 输出：[[0,1]] 提示： * 2 <= n <= 105 * n - 1 <= connections.length <= 105 * 0 <= ai, bi <= n - 1 * ai != bi * 不存在重复的连接
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Tarjan 算法找到图中的桥（即关键连接）。

算法步骤:
1. 构建图的邻接表表示。
2. 使用深度优先搜索 (DFS) 遍历图，记录每个节点的发现时间和最低可达时间。
3. 在 DFS 过程中，如果一条边连接的两个节点的最低可达时间满足特定条件，则这条边是桥。

关键点:
- 使用一个全局计时器来记录每个节点的发现时间和最低可达时间。
- 通过回溯更新节点的最低可达时间。
- 如果当前节点的子节点的最低可达时间大于或等于当前节点的发现时间，则这条边是桥。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(V + E)，其中 V 是节点数，E 是边数。因为我们需要遍历所有节点和边。
空间复杂度: O(V + E)，用于存储图的邻接表和辅助数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
    def dfs(node: int, parent: int):
        nonlocal time
        disc[node] = low[node] = time
        time += 1

        for neighbor in graph[node]:
            if disc[neighbor] == -1:  # 未访问过的节点
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > disc[node]:
                    bridges.append([node, neighbor])
            elif neighbor != parent:  # 回溯更新最低可达时间
                low[node] = min(low[node], disc[neighbor])

    graph = [[] for _ in range(n)]
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    disc = [-1] * n
    low = [-1] * n
    bridges = []
    time = 0

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)

    return bridges

Solution = create_solution(criticalConnections)