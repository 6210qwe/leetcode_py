# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000318
标题: 冗余连接
难度: medium
链接: https://leetcode.cn/problems/7LpjUW/
题目类型: 深度优先搜索、广度优先搜索、并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 118. 冗余连接 - 树可以看成是一个连通且 无环 的 无向 图。 给定往一棵 n 个节点 (节点值 1～n) 的树中添加一条边后的图。添加的边的两个顶点包含在 1 到 n 中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 n 的二维数组 edges ，edges[i] = [ai, bi] 表示图中在 ai 和 bi 之间存在一条边。 请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。如果有多个答案，则返回数组 edges 中最后出现的边。 示例 1： [https://pic.leetcode.cn/1626676174-hOEVUL-image.png] 输入: edges = [[1,2],[1,3],[2,3]] 输出: [2,3] 示例 2： [https://pic.leetcode.cn/1626676179-kGxcmu-image.png] 输入: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]] 输出: [1,4] 提示: * n == edges.length * 3 <= n <= 1000 * edges[i].length == 2 * 1 <= ai < bi <= edges.length * ai != bi * edges 中无重复元素 * 给定的图是连通的 注意：本题与主站 684 题相同： https://leetcode.cn/problems/redundant-connection/ [https://leetcode.cn/problems/redundant-connection/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来检测图中的环，并找到冗余的边。

算法步骤:
1. 初始化并查集，用于管理节点的连通性。
2. 遍历每条边，如果两个节点已经在同一个集合中，则说明这条边是冗余的，返回这条边。
3. 如果两个节点不在同一个集合中，则将它们合并到同一个集合中。

关键点:
- 并查集的路径压缩和按秩合并优化。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * α(n))，其中 n 是节点数，α 是阿克曼函数的反函数，接近于常数。
空间复杂度: O(n)，并查集需要存储每个节点的父节点信息。
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
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
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