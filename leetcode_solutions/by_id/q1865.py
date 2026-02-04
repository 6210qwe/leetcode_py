# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1865
标题: Checking Existence of Edge Length Limited Paths II
难度: hard
链接: https://leetcode.cn/problems/checking-existence-of-edge-length-limited-paths-ii/
题目类型: 深度优先搜索、并查集、图、设计、最小生成树、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1724. 检查边长度限制的路径是否存在 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来维护连通性，并按边的权重从小到大处理。

算法步骤:
1. 初始化并查集，将所有节点初始化为独立集合。
2. 将所有边按权重从小到大排序。
3. 对于每个查询，使用二分查找找到满足条件的最大边权重。
4. 在并查集中合并小于等于该最大边权重的所有边。
5. 检查查询中的两个节点是否在同一个集合中。

关键点:
- 使用并查集来高效管理连通性。
- 通过二分查找和并查集结合，实现高效的查询。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((E + Q) * α(N))，其中 E 是边的数量，Q 是查询的数量，N 是节点的数量，α 是反阿克曼函数。
空间复杂度: O(N)，用于存储并查集的数据结构。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import bisect

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

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 按边的权重排序
        edgeList.sort(key=lambda x: x[2])
        
        # 为每个查询添加索引
        for i, query in enumerate(queries):
            query.append(i)
        
        # 按查询的限制排序
        queries.sort(key=lambda x: x[2])
        
        # 初始化并查集
        uf = UnionFind(n)
        
        # 结果数组
        result = [False] * len(queries)
        
        # 处理查询
        edge_index = 0
        for u, v, limit, query_index in queries:
            # 合并所有小于等于当前查询限制的边
            while edge_index < len(edgeList) and edgeList[edge_index][2] < limit:
                a, b, _ = edgeList[edge_index]
                uf.union(a, b)
                edge_index += 1
            
            # 检查查询中的两个节点是否在同一个集合中
            result[query_index] = uf.find(u) == uf.find(v)
        
        return result

Solution = create_solution(Solution)