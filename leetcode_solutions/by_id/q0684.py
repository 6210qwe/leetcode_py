# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 684
标题: Redundant Connection
难度: medium
链接: https://leetcode.cn/problems/redundant-connection/
题目类型: 深度优先搜索、广度优先搜索、并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
684. 冗余连接 - 树可以看成是一个连通且 无环 的 无向 图。 给定一个图，该图从一棵 n 个节点 (节点值 1～n) 的树中添加一条边后获得。添加的边的两个不同顶点编号在 1 到 n 中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 n 的二维数组 edges ，edges[i] = [ai, bi] 表示图中在 ai 和 bi 之间存在一条边。 请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。如果有多个答案，则返回数组 edges 中最后出现的那个。 示例 1： [https://pic.leetcode.cn/1626676174-hOEVUL-image.png] 输入: edges = [[1,2], [1,3], [2,3]] 输出: [2,3] 示例 2： [https://pic.leetcode.cn/1626676179-kGxcmu-image.png] 输入: edges = [[1,2], [2,3], [3,4], [1,4], [1,5]] 输出: [1,4] 提示: * n == edges.length * 3 <= n <= 1000 * edges[i].length == 2 * 1 <= ai < bi <= edges.length * ai != bi * edges 中无重复元素 * 给定的图是连通的
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集（Union-Find）来检测图中的环。

算法步骤:
1. 初始化并查集，每个节点的父节点指向自己。
2. 遍历每条边，尝试将两个节点合并。
3. 如果发现两个节点已经在同一个集合中，说明形成了环，返回这条边。
4. 否则，继续合并节点。

关键点:
- 并查集的路径压缩和按秩合并可以优化查找和合并操作的时间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * α(n))，其中 n 是节点数，α 是反阿克曼函数，接近常数。
空间复杂度: O(n)，存储并查集的数据结构。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

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

def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    uf = UnionFind(n + 1)
    
    for edge in edges:
        u, v = edge
        if uf.find(u) == uf.find(v):
            return edge
        uf.union(u, v)

Solution = create_solution(find_redundant_connection)