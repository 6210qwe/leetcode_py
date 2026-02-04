# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1100
标题: Connecting Cities With Minimum Cost
难度: medium
链接: https://leetcode.cn/problems/connecting-cities-with-minimum-cost/
题目类型: 并查集、图、最小生成树、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1135. 最低成本连通所有城市 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Kruskal 算法和并查集来构建最小生成树。

算法步骤:
1. 初始化并查集，将每个城市视为一个独立的集合。
2. 将所有边按权重从小到大排序。
3. 遍历所有边，如果当前边连接的两个城市不在同一个集合中，则将这条边加入最小生成树，并合并这两个集合。
4. 如果最小生成树中的边数达到 n-1，则停止遍历，返回最小生成树的总权重。

关键点:
- 使用并查集来高效地判断和合并集合。
- 按权重排序边以确保最小生成树的总权重最小。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log E)，其中 E 是边的数量。排序操作的时间复杂度为 O(E log E)，并查集的操作接近 O(1)。
空间复杂度: O(V + E)，其中 V 是顶点数量，E 是边的数量。存储并查集和排序后的边需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def minimumCost(n: int, connections: List[List[int]]) -> int:
    """
    函数式接口 - 使用 Kruskal 算法和并查集来构建最小生成树
    """
    # 按权重排序边
    connections.sort(key=lambda x: x[2])
    
    # 初始化并查集
    uf = UnionFind(n)
    
    total_cost = 0
    for u, v, cost in connections:
        if uf.find(u - 1) != uf.find(v - 1):
            uf.union(u - 1, v - 1)
            total_cost += cost
            n -= 1
            if n == 1:
                break
    
    return total_cost if n == 1 else -1

Solution = create_solution(minimumCost)