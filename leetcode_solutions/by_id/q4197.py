# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4197
标题: Minimum Cost to Repair Edges to Traverse a Graph
难度: medium
链接: https://leetcode.cn/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/
题目类型: 广度优先搜索、图、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3807. 修复边以遍历图的最小成本 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Kruskal 算法和并查集来找到最小生成树，并计算修复边的成本。

算法步骤:
1. 初始化并查集，将所有节点初始化为独立集合。
2. 将所有未损坏的边加入到边列表中，并按成本从小到大排序。
3. 使用 Kruskal 算法，依次尝试添加每条边，如果这条边连接的两个节点不在同一个集合中，则合并这两个集合，并将这条边的成本加入总成本中。
4. 如果所有节点都已连通，则返回总成本；否则，返回 -1。

关键点:
- 使用并查集来高效地判断和合并集合。
- 通过 Kruskal 算法来构建最小生成树。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log E)，其中 E 是边的数量。排序操作的时间复杂度是 O(E log E)，而并查集的操作是接近 O(1) 的。
空间复杂度: O(V + E)，其中 V 是节点数量，E 是边的数量。需要存储并查集和边列表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

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

def min_cost_to_repair_edges(n: int, edges: List[List[int]], edgesToRepair: List[List[int]]) -> int:
    # 初始化并查集
    uf = UnionFind(n)

    # 将所有未损坏的边加入到边列表中
    all_edges = []
    for u, v in edges:
        all_edges.append((u - 1, v - 1, 0))
    for u, v, cost in edgesToRepair:
        all_edges.append((u - 1, v - 1, cost))

    # 按成本从小到大排序
    all_edges.sort(key=lambda x: x[2])

    total_cost = 0
    for u, v, cost in all_edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            total_cost += cost

    # 检查是否所有节点都已连通
    root = uf.find(0)
    for i in range(n):
        if uf.find(i) != root:
            return -1

    return total_cost

Solution = create_solution(min_cost_to_repair_edges)