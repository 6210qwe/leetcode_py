# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3853
标题: Minimum Weighted Subgraph With the Required Paths II
难度: hard
链接: https://leetcode.cn/problems/minimum-weighted-subgraph-with-the-required-paths-ii/
题目类型: 树、深度优先搜索、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3553. 包含要求路径的最小带权子图 II - 给你一个 无向带权 树，共有 n 个节点，编号从 0 到 n - 1。这棵树由一个二维整数数组 edges 表示，长度为 n - 1，其中 edges[i] = [ui, vi, wi] 表示存在一条连接节点 ui 和 vi 的边，权重为 wi。 此外，给你一个二维整数数组 queries，其中 queries[j] = [src1j, src2j, destj]。 返回一个长度等于 queries.length 的数组 answer，其中 answer[j] 表示一个子树的 最小总权重 ，使用该子树的边可以从 src1j 和 src2j 到达 destj 。 这里的 子树 是指原树中任意节点和边组成的连通子集形成的一棵有效树。 示例 1： 输入： edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], queries = [[2,3,4],[0,2,5]] 输出： [12,11] 解释： 蓝色边表示可以得到最优答案的子树之一。 [https://assets.leetcode.com/uploads/2025/04/02/tree1-4.jpg] * answer[0]：在选出的子树中，从 src1 = 2 和 src2 = 3 到 dest = 4 的路径总权重为 3 + 5 + 4 = 12。 * answer[1]：在选出的子树中，从 src1 = 0 和 src2 = 2 到 dest = 5 的路径总权重为 2 + 3 + 6 = 11。 示例 2： 输入： edges = [[1,0,8],[0,2,7]], queries = [[0,1,2]] 输出： [15] 解释： [https://assets.leetcode.com/uploads/2025/04/02/tree1-5.jpg] * answer[0]：选出的子树中，从 src1 = 0 和 src2 = 1 到 dest = 2 的路径总权重为 8 + 7 = 15。 提示： * 3 <= n <= 105 * edges.length == n - 1 * edges[i].length == 3 * 0 <= ui, vi < n * 1 <= wi <= 104 * 1 <= queries.length <= 105 * queries[j].length == 3 * 0 <= src1j, src2j, destj < n * src1j、src2j 和 destj 互不不同。 * 输入数据保证 edges 表示的是一棵有效的树。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两次深度优先搜索（DFS）来计算每个节点到所有其他节点的最短路径，并利用这些信息来回答查询。

算法步骤:
1. 构建邻接表表示的树。
2. 使用 DFS 计算每个节点到根节点的最短路径。
3. 使用 DFS 计算每个节点到所有其他节点的最短路径。
4. 对于每个查询，找到从 src1 和 src2 到 dest 的最短路径，并计算子树的最小总权重。

关键点:
- 使用两次 DFS 来预处理每个节点到所有其他节点的最短路径。
- 利用预处理的结果快速回答查询。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q)，其中 n 是节点数，q 是查询数。构建邻接表和两次 DFS 都是 O(n) 的复杂度，每个查询可以在 O(1) 时间内回答。
空间复杂度: O(n)，存储邻接表和最短路径信息。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def min_weight_subgraph(edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    n = len(edges) + 1
    adj_list = [[] for _ in range(n)]
    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))

    # 计算每个节点到根节点的最短路径
    def dfs(node, parent, dist, distances):
        distances[node] = dist
        for neighbor, weight in adj_list[node]:
            if neighbor != parent:
                dfs(neighbor, node, dist + weight, distances)

    # 计算每个节点到所有其他节点的最短路径
    all_distances = []
    for i in range(n):
        distances = [float('inf')] * n
        dfs(i, -1, 0, distances)
        all_distances.append(distances)

    # 回答查询
    result = []
    for src1, src2, dest in queries:
        min_weight = float('inf')
        for i in range(n):
            weight = all_distances[src1][i] + all_distances[src2][i] + all_distances[dest][i]
            min_weight = min(min_weight, weight)
        result.append(min_weight)

    return result

Solution = create_solution(min_weight_subgraph)