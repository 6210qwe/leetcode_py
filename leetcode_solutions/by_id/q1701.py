# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1701
标题: Remove Max Number of Edges to Keep Graph Fully Traversable
难度: hard
链接: https://leetcode.cn/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
题目类型: 并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1579. 保证图可完全遍历 - Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3 种类型的边： * 类型 1：只能由 Alice 遍历。 * 类型 2：只能由 Bob 遍历。 * 类型 3：Alice 和 Bob 都可以遍历。 给你一个数组 edges ，其中 edges[i] = [typei, ui, vi] 表示节点 ui 和 vi 之间存在类型为 typei 的双向边。请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。 返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/09/06/5510ex1.png] 输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]] 输出：2 解释：如果删除 [1,1,2] 和 [1,1,3] 这两条边，Alice 和 Bob 仍然可以完全遍历这个图。再删除任何其他的边都无法保证图可以完全遍历。所以可以删除的最大边数是 2 。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/09/06/5510ex2.png] 输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]] 输出：0 解释：注意，删除任何一条边都会使 Alice 和 Bob 无法完全遍历这个图。 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/09/06/5510ex3.png] 输入：n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]] 输出：-1 解释：在当前图中，Alice 无法从其他节点到达节点 4 。类似地，Bob 也不能达到节点 1 。因此，图无法完全遍历。 提示： * 1 <= n <= 10^5 * 1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2) * edges[i].length == 3 * 1 <= edges[i][0] <= 3 * 1 <= edges[i][1] < edges[i][2] <= n * 所有元组 (typei, ui, vi) 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来管理 Alice 和 Bob 的连通性，并优先处理类型 3 的边以最大化可删除的边数。

算法步骤:
1. 初始化两个并查集，分别用于 Alice 和 Bob。
2. 按照边的类型对 edges 进行排序，优先处理类型 3 的边。
3. 遍历排序后的 edges：
   - 对于类型 3 的边，尝试同时连接 Alice 和 Bob 的并查集。
   - 对于类型 1 和类型 2 的边，分别尝试连接 Alice 和 Bob 的并查集。
4. 如果在处理过程中发现某个并查集已经连通了所有节点，则停止处理剩余的边。
5. 最后检查 Alice 和 Bob 的并查集是否都连通了所有节点，如果是则返回可删除的最大边数，否则返回 -1。

关键点:
- 优先处理类型 3 的边，因为它们可以同时连接 Alice 和 Bob 的图。
- 使用并查集来高效管理连通性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log E + E α(n))，其中 E 是边的数量，n 是节点数量，α 是反阿克曼函数。
空间复杂度: O(n)，并查集需要 O(n) 的空间。
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
            return True
        return False

def max_num_edges_to_remove(n: int, edges: List[List[int]]) -> int:
    alice_uf = UnionFind(n)
    bob_uf = UnionFind(n)
    removed_edges = 0
    
    # Sort edges by type, prioritize type 3
    edges.sort(key=lambda x: -x[0])
    
    for edge in edges:
        t, u, v = edge
        u -= 1
        v -= 1
        if t == 3:
            if not (alice_uf.union(u, v) and bob_uf.union(u, v)):
                removed_edges += 1
        elif t == 1:
            if not alice_uf.union(u, v):
                removed_edges += 1
        elif t == 2:
            if not bob_uf.union(u, v):
                removed_edges += 1
    
    if alice_uf.count == 1 and bob_uf.count == 1:
        return removed_edges
    return -1

Solution = create_solution(max_num_edges_to_remove)