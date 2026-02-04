```python
# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2678
标题: Design Graph With Shortest Path Calculator
难度: hard
链接: https://leetcode.cn/problems/design-graph-with-shortest-path-calculator/
题目类型: 图、设计、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2642. 设计可以求最短路径的图类 - 给你一个有 n 个节点的 有向带权 图，节点编号为 0 到 n - 1 。图中的初始边用数组 edges 表示，其中 edges[i] = [fromi, toi, edgeCosti] 表示从 fromi 到 toi 有一条代价为 edgeCosti 的边。 请你实现一个 Graph 类： * Graph(int n, int[][] edges) 初始化图有 n 个节点，并输入初始边。 * addEdge(int[] edge) 向边集中添加一条边，其中 edge = [from, to, edgeCost] 。数据保证添加这条边之前对应的两个节点之间没有有向边。 * int shortestPath(int node1, int node2) 返回从节点 node1 到 node2 的路径 最小 代价。如果路径不存在，返回 -1 。一条路径的代价是路径中所有边代价之和。 示例 1： [https://assets.leetcode.com/uploads/2023/01/11/graph3drawio-2.png] 输入： ["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"] [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]] 输出： [null, 6, -1, null, 6] 解释： Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]); g.shortestPath(3, 2); // 返回 6 。从 3 到 2 的最短路径如第一幅图所示：3 -> 0 -> 1 -> 2 ，总代价为 3 + 2 + 1 = 6 。 g.shortestPath(0, 3); // 返回 -1 。没有从 0 到 3 的路径。 g.addEdge([1, 3, 4]); // 添加一条节点 1 到节点 3 的边，得到第二幅图。 g.shortestPath(0, 3); // 返回 6 。从 0 到 3 的最短路径为 0 -> 1 -> 3 ，总代价为 2 + 4 = 6 。 提示： * 1 <= n <= 100 * 0 <= edges.length <= n * (n - 1) * edges[i].length == edge.length == 3 * 0 <= fromi, toi, from, to, node1, node2 <= n - 1 * 1 <= edgeCosti, edgeCost <= 106 * 图中任何时候都不会有重边和自环。 * 调用 addEdge 至多 100 次。 * 调用 shortestPath 至多 100 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Dijkstra 算法来计算最短路径。

算法步骤:
1. 初始化图时，构建邻接表表示图。
2. 在 `addEdge` 方法中，更新邻接表。
3. 在 `shortestPath` 方法中，使用 Dijkstra 算法计算从 `node1` 到 `node2` 的最短路径。

关键点:
- 使用优先队列（最小堆）来优化 Dijkstra 算法的时间复杂度。
- 通过邻接表来存储图的结构，便于快速查找和更新。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((E + V) log V)，其中 E 是边的数量，V 是节点的数量。Dijkstra 算法的时间复杂度主要由优先队列的操作决定。
空间复杂度: O(E + V)，用于存储邻接表和优先队列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj_list = [[] for _ in range(n)]
        for u, v, cost in edges:
            self.adj_list[u].append((v, cost))

    def addEdge(self, edge: List[int]) -> None:
        u, v, cost = edge
        self.adj_list[u].append((v, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            return 0

        # Dijkstra's algorithm
        dist = [float('inf')] * self.n
        dist[node1] = 0
        pq = [(0, node1)]  # (distance, node)

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, cost in self.adj_list[u]:
                if dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
                    heapq.heappush(pq, (dist[v], v))

        return dist[node2] if dist[node2] != float('inf') else -1

# Example usage
if __name__ == "__main__":
    g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    print(g.shortestPath(3, 2))  # Output: 6
    print(g.shortestPath(0, 3))  # Output: -1
    g.addEdge([1, 3, 4])
    print(g.shortestPath(0, 3))  # Output: 6
```

这个实现使用了 Dijkstra 算法来计算最短路径，并且在初始化和添加边时使用邻接表来存储图的结构。时间复杂度和空间复杂度都符合题目要求。