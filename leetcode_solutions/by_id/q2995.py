# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2995
标题: Number of Unique Categories
难度: medium
链接: https://leetcode.cn/problems/number-of-unique-categories/
题目类型: 并查集、计数、交互
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2782. 唯一类别的数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来合并类别，并统计唯一类别的数量。

算法步骤:
1. 初始化并查集，将每个类别初始化为一个独立的集合。
2. 遍历所有类别关系，使用并查集进行合并。
3. 统计并查集中根节点的数量，即为唯一类别的数量。

关键点:
- 使用路径压缩和按秩合并优化并查集操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * α(n))，其中 n 是类别的数量，α 是反阿克曼函数。
空间复杂度: O(n)，用于存储并查集的数据结构。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

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
            self.count -= 1

def solution_function_name(categories: List[List[int]]) -> int:
    """
    函数式接口 - 使用并查集来合并类别，并统计唯一类别的数量。
    """
    n = len(categories)
    uf = UnionFind(n)
    
    for i in range(n):
        for j in range(i + 1, n):
            if categories[i] == categories[j]:
                uf.union(i, j)
    
    return uf.count

Solution = create_solution(solution_function_name)