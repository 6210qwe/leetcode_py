# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2403
标题: Count Unreachable Pairs of Nodes in an Undirected Graph
难度: medium
链接: https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/
题目类型: 深度优先搜索、广度优先搜索、并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2316. 统计无向图中无法互相到达点对数 - 给你一个整数 n ，表示一张 无向图 中有 n 个节点，编号为 0 到 n - 1 。同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 无向 边。 请你返回 无法互相到达 的不同 点对数目 。 示例 1： [https://assets.leetcode.com/uploads/2022/05/05/tc-3.png] 输入：n = 3, edges = [[0,1],[0,2],[1,2]] 输出：0 解释：所有点都能互相到达，意味着没有点对无法互相到达，所以我们返回 0 。 示例 2： [https://assets.leetcode.com/uploads/2022/05/05/tc-2.png] 输入：n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]] 输出：14 解释：总共有 14 个点对互相无法到达： [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]] 所以我们返回 14 。 提示： * 1 <= n <= 105 * 0 <= edges.length <= 2 * 105 * edges[i].length == 2 * 0 <= ai, bi < n * ai != bi * 不会有重复边。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来找到图中的连通分量，并计算每个连通分量的大小。然后通过组合数学计算无法互相到达的点对数。

算法步骤:
1. 初始化并查集。
2. 遍历所有边，将每条边的两个节点合并到同一个集合中。
3. 计算每个连通分量的大小。
4. 通过组合数学公式计算无法互相到达的点对数。

关键点:
- 并查集用于高效地管理和查询连通分量。
- 使用组合数学公式计算点对数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是节点数，m 是边数。初始化并查集和遍历边的时间复杂度是 O(n + m)。
空间复杂度: O(n)，并查集需要 O(n) 的空间来存储每个节点的父节点和秩。
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
                self.rank[root_x] += 1
                self.size[root_x] += self.size[root_y]

def count_unreachable_pairs(n: int, edges: List[List[int]]) -> int:
    """
    函数式接口 - 计算无法互相到达的点对数
    """
    # 初始化并查集
    uf = UnionFind(n)
    
    # 遍历所有边，将每条边的两个节点合并到同一个集合中
    for u, v in edges:
        uf.union(u, v)
    
    # 计算每个连通分量的大小
    component_sizes = []
    for i in range(n):
        if uf.find(i) == i:
            component_sizes.append(uf.size[i])
    
    # 通过组合数学公式计算无法互相到达的点对数
    total_pairs = n * (n - 1) // 2
    reachable_pairs = sum(size * (size - 1) // 2 for size in component_sizes)
    unreachable_pairs = total_pairs - reachable_pairs
    
    return unreachable_pairs

Solution = create_solution(count_unreachable_pairs)