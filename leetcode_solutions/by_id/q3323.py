# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3323
标题: Maximum Number of Removal Queries That Can Be Processed I
难度: hard
链接: https://leetcode.cn/problems/maximum-number-of-removal-queries-that-can-be-processed-i/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3018. 可处理的最大删除操作数 I - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集（Union-Find）来维护连通性，并使用一个计数器来记录每个连通块的大小。

算法步骤:
1. 初始化并查集和计数器。
2. 遍历所有查询，按顺序处理每个查询。
3. 对于每个查询，检查删除该元素后是否会导致连通块分离。如果是，则更新计数器。
4. 返回可以处理的最大删除操作数。

关键点:
- 使用并查集来高效地管理连通块。
- 使用计数器来记录每个连通块的大小。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q * α(n))，其中 n 是数组长度，q 是查询数量，α 是反阿克曼函数。
空间复杂度: O(n)，用于存储并查集和计数器。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
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
                self.size[root_x] += self.size[root_y]
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
                self.rank[root_x] += 1
    
    def get_size(self, x):
        return self.size[self.find(x)]

def max_removal_queries(nums: List[int], queries: List[List[int]]) -> int:
    n = len(nums)
    uf = UnionFind(n)
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            uf.union(i, i - 1)
    
    result = []
    for l, r in queries:
        if l > 0 and nums[l] == nums[l - 1]:
            uf.union(l, l - 1)
        if r + 1 < n and nums[r] == nums[r + 1]:
            uf.union(r, r + 1)
        
        size_before = uf.get_size(l)
        uf.union(l, r)
        size_after = uf.get_size(l)
        
        if size_after > size_before:
            result.append(0)
        else:
            result.append(1)
            uf.union(l, l - 1) if l > 0 and nums[l] == nums[l - 1] else None
            uf.union(r, r + 1) if r + 1 < n and nums[r] == nums[r + 1] else None
    
    return sum(result)

Solution = create_solution(max_removal_queries)