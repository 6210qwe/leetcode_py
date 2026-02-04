# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3079
标题: Minimum Edge Weight Equilibrium Queries in a Tree
难度: hard
链接: https://leetcode.cn/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/
题目类型: 树、图、数组、强连通分量
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2846. 边权重均等查询 - 现有一棵由 n 个节点组成的无向树，节点按从 0 到 n - 1 编号。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ui, vi, wi] 表示树中存在一条位于节点 ui 和节点 vi 之间、权重为 wi 的边。 另给你一个长度为 m 的二维整数数组 queries ，其中 queries[i] = [ai, bi] 。对于每条查询，请你找出使从 ai 到 bi 路径上每条边的权重相等所需的 最小操作次数 。在一次操作中，你可以选择树上的任意一条边，并将其权重更改为任意值。 注意： * 查询之间 相互独立 的，这意味着每条新的查询时，树都会回到 初始状态 。 * 从 ai 到 bi的路径是一个由 不同 节点组成的序列，从节点 ai 开始，到节点 bi 结束，且序列中相邻的两个节点在树中共享一条边。 返回一个长度为 m 的数组 answer ，其中 answer[i] 是第 i 条查询的答案。 示例 1： [https://assets.leetcode.com/uploads/2023/08/11/graph-6-1.png] 输入：n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]] 输出：[0,0,1,3] 解释：第 1 条查询，从节点 0 到节点 3 的路径中的所有边的权重都是 1 。因此，答案为 0 。 第 2 条查询，从节点 3 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 0 。 第 3 条查询，将边 [2,3] 的权重变更为 2 。在这次操作之后，从节点 2 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 1 。 第 4 条查询，将边 [0,1]、[1,2]、[2,3] 的权重变更为 2 。在这次操作之后，从节点 0 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 3 。 对于每条查询 queries[i] ，可以证明 answer[i] 是使从 ai 到 bi 的路径中的所有边的权重相等的最小操作次数。 示例 2： [https://assets.leetcode.com/uploads/2023/08/11/graph-9-1.png] 输入：n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries = [[4,6],[0,4],[6,5],[7,4]] 输出：[1,2,2,3] 解释：第 1 条查询，将边 [1,3] 的权重变更为 6 。在这次操作之后，从节点 4 到节点 6 的路径中的所有边的权重都是 6 。因此，答案为 1 。 第 2 条查询，将边 [0,3]、[3,1] 的权重变更为 6 。在这次操作之后，从节点 0 到节点 4 的路径中的所有边的权重都是 6 。因此，答案为 2 。 第 3 条查询，将边 [1,3]、[5,2] 的权重变更为 6 。在这次操作之后，从节点 6 到节点 5 的路径中的所有边的权重都是 6 。因此，答案为 2 。 第 4 条查询，将边 [0,7]、[0,3]、[1,3] 的权重变更为 6 。在这次操作之后，从节点 7 到节点 4 的路径中的所有边的权重都是 6 。因此，答案为 3 。 对于每条查询 queries[i] ，可以证明 answer[i] 是使从 ai 到 bi 的路径中的所有边的权重相等的最小操作次数。 提示： * 1 <= n <= 104 * edges.length == n - 1 * edges[i].length == 3 * 0 <= ui, vi < n * 1 <= wi <= 26 * 生成的输入满足 edges 表示一棵有效的树 * 1 <= queries.length == m <= 2 * 104 * queries[i].length == 2 * 0 <= ai, bi < n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用倍增法（LCA）和前缀和来高效处理每个查询。

算法步骤:
1. 构建树的邻接表表示。
2. 使用DFS计算每个节点的深度和父节点。
3. 使用倍增法预处理每个节点的2^k级祖先及其路径上的边权统计。
4. 对于每个查询，使用LCA找到路径上的边权统计，计算最小操作次数。

关键点:
- 使用倍增法快速找到LCA。
- 使用前缀和统计路径上的边权。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n + m log n)
空间复杂度: O(n log n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def min_operations_queries(n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    # 构建树的邻接表表示
    tree = [[] for _ in range(n)]
    for u, v, w in edges:
        tree[u].append((v, w))
        tree[v].append((u, w))

    # 倍增法预处理
    MAX_LOG = 15
    depth = [0] * n
    parent = [[-1] * MAX_LOG for _ in range(n)]
    edge_count = [[0] * 27 for _ in range(n)]

    def dfs(node: int, prev: int, d: int):
        depth[node] = d
        for next_node, weight in tree[node]:
            if next_node != prev:
                parent[next_node][0] = node
                edge_count[next_node][:] = edge_count[node][:]
                edge_count[next_node][weight] += 1
                dfs(next_node, node, d + 1)

    dfs(0, -1, 0)

    for k in range(1, MAX_LOG):
        for i in range(n):
            if parent[i][k - 1] != -1:
                parent[i][k] = parent[parent[i][k - 1]][k - 1]

    def lca(u: int, v: int) -> int:
        if depth[u] > depth[v]:
            u, v = v, u
        for k in range(MAX_LOG - 1, -1, -1):
            if depth[v] - (1 << k) >= depth[u]:
                v = parent[v][k]
        if u == v:
            return u
        for k in range(MAX_LOG - 1, -1, -1):
            if parent[u][k] != parent[v][k]:
                u = parent[u][k]
                v = parent[v][k]
        return parent[u][0]

    def get_edge_count(u: int, v: int) -> List[int]:
        lca_node = lca(u, v)
        result = [edge_count[u][i] + edge_count[v][i] - 2 * edge_count[lca_node][i] for i in range(27)]
        return result

    def min_operations(edge_count: List[int]) -> int:
        total_edges = sum(edge_count)
        max_edges = max(edge_count)
        return total_edges - max_edges

    results = []
    for u, v in queries:
        edge_count_query = get_edge_count(u, v)
        results.append(min_operations(edge_count_query))

    return results

Solution = create_solution(min_operations_queries)