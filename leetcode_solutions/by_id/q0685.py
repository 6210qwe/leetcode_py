# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 685
标题: Redundant Connection II
难度: hard
链接: https://leetcode.cn/problems/redundant-connection-ii/
题目类型: 深度优先搜索、广度优先搜索、并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
685. 冗余连接 II - 在本问题中，有根树指满足以下条件的 有向 图。该树只有一个根节点，所有其他节点都是该根节点的后继。该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。 输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）的树及一条附加的有向边构成。附加的边包含在 1 到 n 中的两个不同顶点间，这条附加的边不属于树中已存在的边。 结果图是一个以边组成的二维数组 edges 。 每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点 ui 和顶点 vi 的边，其中 ui 是 vi 的一个父节点。 返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。 示例 1： [https://assets.leetcode.com/uploads/2020/12/20/graph1.jpg] 输入：edges = [[1,2],[1,3],[2,3]] 输出：[2,3] 示例 2： [https://assets.leetcode.com/uploads/2020/12/20/graph2.jpg] 输入：edges = [[1,2],[2,3],[3,4],[4,1],[1,5]] 输出：[4,1] 提示： * n == edges.length * 3 <= n <= 1000 * edges[i].length == 2 * 1 <= ui, vi <= n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来检测环，并处理入度为2的情况。

算法步骤:
1. 初始化并查集和入度数组。
2. 遍历所有边，记录每个节点的入度。
3. 如果某个节点的入度为2，尝试删除这两条边之一，检查是否形成有根树。
4. 如果没有入度为2的节点，找到形成环的边并删除。

关键点:
- 使用并查集来检测环。
- 处理入度为2的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY
            return True
        return False

def solution_function_name(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    uf = UnionFind(n + 1)
    indegree = [0] * (n + 1)
    candidateA, candidateB = None, None
    
    for u, v in edges:
        if indegree[v] == 1:
            candidateA = [u, v]
        else:
            indegree[v] += 1
            if not uf.union(u, v):
                candidateB = [u, v]
    
    def is_valid_tree(edges_to_remove):
        uf = UnionFind(n + 1)
        for u, v in edges:
            if [u, v] == edges_to_remove:
                continue
            if not uf.union(u, v):
                return False
        return True
    
    if candidateA and is_valid_tree(candidateA):
        return candidateA
    return candidateB

Solution = create_solution(solution_function_name)