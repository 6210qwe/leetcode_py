# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1144
标题: Optimize Water Distribution in a Village
难度: hard
链接: https://leetcode.cn/problems/optimize-water-distribution-in-a-village/
题目类型: 并查集、图、最小生成树、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1168. 水资源分配优化 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Kruskal 算法来构建最小生成树 (MST)。首先将所有边按权重从小到大排序，然后使用并查集 (Union-Find) 来合并连通分量，直到所有的房子都连通。

算法步骤:
1. 初始化并查集，并将所有边按权重从小到大排序。
2. 遍历所有边，如果当前边连接的两个节点不在同一个连通分量中，则将它们合并，并将该边的权重加入总成本。
3. 如果所有节点都已连通，返回总成本；否则，返回 -1。

关键点:
- 使用并查集来高效地管理连通分量。
- 通过 Kruskal 算法构建最小生成树。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log E)，其中 E 是边的数量。排序操作的时间复杂度为 O(E log E)，遍历和合并操作的时间复杂度为 O(E)。
空间复杂度: O(V + E)，其中 V 是节点数量，E 是边的数量。需要存储并查集和边的信息。
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

def minCostToSupplyWater(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    # 添加虚拟节点 0 到每个房子的边
    for i, cost in enumerate(wells, 1):
        pipes.append([0, i, cost])

    # 按权重从小到大排序
    pipes.sort(key=lambda x: x[2])

    uf = UnionFind(n + 1)
    total_cost = 0

    for u, v, cost in pipes:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            total_cost += cost

    return total_cost

Solution = create_solution(minCostToSupplyWater)