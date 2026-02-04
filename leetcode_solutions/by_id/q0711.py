# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 711
标题: Number of Distinct Islands II
难度: hard
链接: https://leetcode.cn/problems/number-of-distinct-islands-ii/
题目类型: 深度优先搜索、广度优先搜索、并查集、哈希表、哈希函数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
711. 不同岛屿的数量 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来合并相邻的陆地，并使用哈希集合来存储每个岛屿的形状。

算法步骤:
1. 初始化并查集和一个字典来记录每个岛屿的形状。
2. 遍历整个网格，对于每个陆地单元格，将其与相邻的陆地单元格进行合并。
3. 对于每个连通分量，计算其形状，并将其加入哈希集合中。
4. 返回哈希集合的大小，即不同岛屿的数量。

关键点:
- 使用并查集来合并相邻的陆地。
- 使用哈希集合来存储每个岛屿的形状，确保唯一性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m * log(n * m))，其中 n 和 m 分别是网格的行数和列数。最坏情况下，并查集的操作时间复杂度为 O(log(n * m))。
空间复杂度: O(n * m)，用于存储并查集和岛屿形状的哈希集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict

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

def get_island_shape(grid, n, m, i, j, offset):
    shape = []
    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
            grid[x][y] = 0
            shape.append((x - offset[0], y - offset[1]))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                stack.append((x + dx, y + dy))
    return tuple(sorted(shape))

def solution_function_name(grid: List[List[int]]) -> int:
    """
    函数式接口 - 计算不同岛屿的数量
    """
    n, m = len(grid), len(grid[0])
    uf = UnionFind(n * m)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                        uf.union(i * m + j, ni * m + nj)
    
    island_shapes = defaultdict(set)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                root = uf.find(i * m + j)
                shape = get_island_shape(grid, n, m, i, j, (i, j))
                island_shapes[root].add(shape)
    
    return len(island_shapes)

Solution = create_solution(solution_function_name)