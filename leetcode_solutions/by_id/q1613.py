# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1613
标题: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
难度: hard
链接: https://leetcode.cn/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
题目类型: 并查集、图、最小生成树、排序、强连通分量
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1489. 找到最小生成树里的关键边和伪关键边 - 给你一个 n 个点的带权无向连通图，节点编号为 0 到 n-1 ，同时还有一个数组 edges ，其中 edges[i] = [fromi, toi, weighti] 表示在 fromi 和 toi 节点之间有一条带权无向边。最小生成树 (MST) 是给定图中边的一个子集，它连接了所有节点且没有环，而且这些边的权值和最小。 请你找到给定图中最小生成树的所有关键边和伪关键边。如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。伪关键边则是可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。 请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/06/21/ex1.png] 输入：n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]] 输出：[[0,1],[2,3,4,5]] 解释：上图描述了给定图。 下图是所有的最小生成树。 [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/06/21/msts.png] 注意到第 0 条边和第 1 条边出现在了所有最小生成树中，所以它们是关键边，我们将这两个下标作为输出的第一个列表。 边 2，3，4 和 5 是所有 MST 的剩余边，所以它们是伪关键边。我们将它们作为输出的第二个列表。 示例 2 ： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/06/21/ex2.png] 输入：n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]] 输出：[[],[0,1,2,3]] 解释：可以观察到 4 条边都有相同的权值，任选它们中的 3 条可以形成一棵 MST 。所以 4 条边都是伪关键边。 提示： * 2 <= n <= 100 * 1 <= edges.length <= min(200, n * (n - 1) / 2) * edges[i].length == 3 * 0 <= fromi < toi < n * 1 <= weighti <= 1000 * 所有 (fromi, toi) 数对都是互不相同的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Kruskal 算法来找到最小生成树，并通过检查每条边是否是关键边或伪关键边来确定结果。

算法步骤:
1. 将所有边按权重从小到大排序，并记录每条边的原始索引。
2. 使用并查集（Union-Find）来构建最小生成树，并计算其总权重。
3. 对于每条边，尝试将其排除在外，重新构建最小生成树，如果新生成树的权重大于原生成树，则该边是关键边。
4. 对于每条边，尝试将其强制包含在内，重新构建最小生成树，如果新生成树的权重等于原生成树，则该边是伪关键边。

关键点:
- 使用并查集高效地管理连通性。
- 通过两次运行 Kruskal 算法来判断每条边的关键性和伪关键性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log E + E^2)，其中 E 是边的数量。排序操作的时间复杂度是 O(E log E)，每次构建最小生成树的时间复杂度是 O(E)，总共需要进行 E 次构建。
空间复杂度: O(E + V)，其中 E 是边的数量，V 是节点的数量。主要空间消耗在于并查集的数据结构和排序后的边列表。
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

def kruskal(edges, n, exclude=None, include=None):
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = 0
    if include:
        u, v, w = include
        uf.union(u, v)
        mst_weight += w
        mst_edges += 1
    for i, (u, v, w, _) in enumerate(edges):
        if exclude is not None and i == exclude:
            continue
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += w
            mst_edges += 1
            if mst_edges == n - 1:
                break
    return mst_weight if mst_edges == n - 1 else float('inf')

def find_critical_and_pseudo_critical_edges(n: int, edges: List[List[int]]) -> List[List[int]]:
    # 添加原始索引
    edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
    # 按权重排序
    edges.sort(key=lambda x: x[2])
    
    # 计算最小生成树的权重
    mst_weight = kruskal(edges, n)
    
    critical = []
    pseudo_critical = []
    
    for i, (u, v, w, _) in enumerate(edges):
        # 排除当前边，重新计算最小生成树
        if kruskal(edges, n, exclude=i) > mst_weight:
            critical.append(i)
        else:
            # 包含当前边，重新计算最小生成树
            if kruskal(edges, n, include=(u, v, w, i)) == mst_weight:
                pseudo_critical.append(i)
    
    return [critical, pseudo_critical]

Solution = create_solution(find_critical_and_pseudo_critical_edges)