# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3881
标题: Minimize Maximum Component Cost
难度: medium
链接: https://leetcode.cn/problems/minimize-maximum-component-cost/
题目类型: 并查集、图、二分查找、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3613. 最小化连通分量的最大成本 - 给你一个无向连通图，包含 n 个节点，节点编号从 0 到 n - 1，以及一个二维整数数组 edges，其中 edges[i] = [ui, vi, wi] 表示一条连接节点 ui 和节点 vi 的无向边，边权为 wi，另有一个整数 k。 你可以从图中移除任意数量的边，使得最终的图中 最多 只包含 k 个连通分量。 连通分量的 成本 定义为该分量中边权的 最大值 。如果一个连通分量没有边，则其代价为 0。 请返回在移除这些边之后，在所有连通分量之中的 最大成本 的 最小可能值 。 示例 1： 输入： n = 5, edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], k = 2 输出： 4 解释： [https://assets.leetcode.com/uploads/2025/04/19/minimizemaximumm.jpg] * 移除节点 3 和节点 4 之间的边（权值为 6）。 * 最终的连通分量成本分别为 0 和 4，因此最大代价为 4。 示例 2： 输入： n = 4, edges = [[0,1,5],[1,2,5],[2,3,5]], k = 1 输出： 5 解释： [https://assets.leetcode.com/uploads/2025/04/19/minmax2.jpg] * 无法移除任何边，因为只允许一个连通分量（k = 1），图必须保持完全连通。 * 该连通分量的成本等于其最大边权，即 5。 提示： * 1 <= n <= 5 * 104 * 0 <= edges.length <= 105 * edges[i].length == 3 * 0 <= ui, vi < n * 1 <= wi <= 106 * 1 <= k <= n * 输入图是连通图。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集和二分查找来找到最小的最大成本。

算法步骤:
1. 将所有边按权重从小到大排序。
2. 使用二分查找来确定最小的最大成本。
3. 在每次二分查找的过程中，使用并查集来判断当前成本是否可以满足最多 k 个连通分量的要求。

关键点:
- 通过二分查找来优化搜索过程，减少不必要的计算。
- 使用并查集来高效地管理连通分量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log E + E log W)，其中 E 是边的数量，W 是边权的最大值。
空间复杂度: O(n)，其中 n 是节点的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

def min_max_cost(n: int, edges: List[List[int]], k: int) -> int:
    def is_valid(max_cost):
        uf = UnionFind(n)
        for u, v, w in sorted_edges:
            if w <= max_cost:
                uf.union(u, v)
        return uf.count <= k

    sorted_edges = sorted(edges, key=lambda x: x[2])
    left, right = 0, max(edge[2] for edge in edges)

    while left < right:
        mid = (left + right) // 2
        if is_valid(mid):
            right = mid
        else:
            left = mid + 1

    return left

Solution = create_solution(min_max_cost)