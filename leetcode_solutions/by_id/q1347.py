# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1347
标题: Distance to a Cycle in Undirected Graph
难度: hard
链接: https://leetcode.cn/problems/distance-to-a-cycle-in-undirected-graph/
题目类型: 深度优先搜索、广度优先搜索、并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2204. 无向图中到环的距离 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来检测环，并使用广度优先搜索（BFS）来计算每个节点到环的距离。

算法步骤:
1. 使用 DFS 检测图中的环，并记录环上的所有节点。
2. 使用 BFS 计算每个节点到环的距离。

关键点:
- 使用一个访问数组 `visited` 来记录每个节点的访问状态。
- 使用一个父节点数组 `parent` 来记录每个节点的父节点，以便在检测环时回溯路径。
- 使用一个队列来进行 BFS，计算每个节点到环的距离。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(V + E)，其中 V 是节点数，E 是边数。DFS 和 BFS 的时间复杂度都是 O(V + E)。
空间复杂度: O(V)，存储访问数组、父节点数组和队列所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(n: int, edges: List[List[int]]) -> List[int]:
    """
    函数式接口 - 实现
    """
    def dfs(node: int, parent: int) -> None:
        visited[node] = 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                parents[neighbor] = node
                dfs(neighbor, node)
            elif visited[neighbor] == 1 and neighbor != parent:
                # 检测到环
                cycle_start = neighbor
                while node != cycle_start:
                    cycle_nodes.add(node)
                    node = parents[node]
                cycle_nodes.add(cycle_start)

    def bfs() -> None:
        queue = list(cycle_nodes)
        for node in queue:
            distances[node] = 0
        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[node] + 1
                    queue.append(neighbor)

    # 构建图
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 初始化变量
    visited = [0] * n
    parents = [-1] * n
    cycle_nodes = set()
    distances = [-1] * n

    # 执行 DFS 检测环
    for i in range(n):
        if not visited[i]:
            dfs(i, -1)

    # 执行 BFS 计算距离
    bfs()

    return distances


Solution = create_solution(solution_function_name)