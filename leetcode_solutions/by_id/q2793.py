# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2793
标题: Count the Number of Complete Components
难度: medium
链接: https://leetcode.cn/problems/count-the-number-of-complete-components/
题目类型: 深度优先搜索、广度优先搜索、并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2685. 统计完全连通分量的数量 - 给你一个整数 n 。现有一个包含 n 个顶点的 无向 图，顶点按从 0 到 n - 1 编号。给你一个二维整数数组 edges 其中 edges[i] = [ai, bi] 表示顶点 ai 和 bi 之间存在一条 无向 边。 返回图中 完全连通分量 的数量。 如果在子图中任意两个顶点之间都存在路径，并且子图中没有任何一个顶点与子图外部的顶点共享边，则称其为 连通分量 。 如果连通分量中每对节点之间都存在一条边，则称其为 完全连通分量 。 示例 1： [https://assets.leetcode.com/uploads/2023/04/11/screenshot-from-2023-04-11-23-31-23.png] 输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4]] 输出：3 解释：如上图所示，可以看到此图所有分量都是完全连通分量。 示例 2： [https://assets.leetcode.com/uploads/2023/04/11/screenshot-from-2023-04-11-23-32-00.png] 输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]] 输出：1 解释：包含节点 0、1 和 2 的分量是完全连通分量，因为每对节点之间都存在一条边。 包含节点 3 、4 和 5 的分量不是完全连通分量，因为节点 4 和 5 之间不存在边。 因此，在图中完全连接分量的数量是 1 。 提示： * 1 <= n <= 50 * 0 <= edges.length <= n * (n - 1) / 2 * edges[i].length == 2 * 0 <= ai, bi <= n - 1 * ai != bi * 不存在重复的边
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来遍历每个连通分量，并检查每个连通分量是否为完全连通分量。

算法步骤:
1. 构建图的邻接表表示。
2. 使用 DFS 遍历每个连通分量，记录每个连通分量中的节点数和边数。
3. 检查每个连通分量是否为完全连通分量：如果一个连通分量有 k 个节点，则它必须有 k * (k - 1) / 2 条边。
4. 统计完全连通分量的数量。

关键点:
- 使用邻接表表示图。
- 使用 DFS 遍历图。
- 检查每个连通分量的节点数和边数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是节点数，m 是边数。我们需要遍历每个节点和每条边。
空间复杂度: O(n + m)，存储图的邻接表和递归栈的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def count_complete_components(n: int, edges: List[List[int]]) -> int:
    # 构建图的邻接表表示
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node: int, visited: List[bool], component_nodes: List[int]) -> None:
        if visited[node]:
            return
        visited[node] = True
        component_nodes.append(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited, component_nodes)

    def is_complete_component(nodes: List[int]) -> bool:
        num_nodes = len(nodes)
        expected_edges = num_nodes * (num_nodes - 1) // 2
        actual_edges = sum(len(graph[node]) for node in nodes) // 2
        return actual_edges == expected_edges

    visited = [False] * n
    complete_components = 0

    for i in range(n):
        if not visited[i]:
            component_nodes = []
            dfs(i, visited, component_nodes)
            if is_complete_component(component_nodes):
                complete_components += 1

    return complete_components

Solution = create_solution(count_complete_components)