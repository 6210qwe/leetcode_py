# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3348
标题: Minimum Cost Walk in Weighted Graph
难度: hard
链接: https://leetcode.cn/problems/minimum-cost-walk-in-weighted-graph/
题目类型: 位运算、并查集、图、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3108. 带权图里旅途的最小代价 - 给你一个 n 个节点的带权无向图，节点编号为 0 到 n - 1 。 给你一个整数 n 和一个数组 edges ，其中 edges[i] = [ui, vi, wi] 表示节点 ui 和 vi 之间有一条权值为 wi 的无向边。 在图中，一趟旅途包含一系列节点和边。旅途开始和结束点都是图中的节点，且图中存在连接旅途中相邻节点的边。注意，一趟旅途可能访问同一条边或者同一个节点多次。 如果旅途开始于节点 u ，结束于节点 v ，我们定义这一趟旅途的 代价 是经过的边权按位与 AND 的结果。换句话说，如果经过的边对应的边权为 w0, w1, w2, ..., wk ，那么代价为w0 & w1 & w2 & ... & wk ，其中 & 表示按位与 AND 操作。 给你一个二维数组 query ，其中 query[i] = [si, ti] 。对于每一个查询，你需要找出从节点开始 si ，在节点 ti 处结束的旅途的最小代价。如果不存在这样的旅途，答案为 -1 。 返回数组 answer ，其中 answer[i] 表示对于查询 i 的 最小 旅途代价。 示例 1： 输入：n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]] 输出：[1,-1] 解释： [https://assets.leetcode.com/uploads/2024/01/31/q4_example1-1.png] 第一个查询想要得到代价为 1 的旅途，我们依次访问：0->1（边权为 7 ）1->2 （边权为 1 ）2->1（边权为 1 ）1->3 （边权为 7 ）。 第二个查询中，无法从节点 3 到节点 4 ，所以答案为 -1 。 示例 2： 输入：n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]] 输出：[0] 解释： [https://assets.leetcode.com/uploads/2024/01/31/q4_example2e.png] 第一个查询想要得到代价为 0 的旅途，我们依次访问：1->2（边权为 1 ），2->1（边权 为 6 ），1->2（边权为 1 ）。 提示： * 1 <= n <= 105 * 0 <= edges.length <= 105 * edges[i].length == 3 * 0 <= ui, vi <= n - 1 * ui != vi * 0 <= wi <= 105 * 1 <= query.length <= 105 * query[i].length == 2 * 0 <= si, ti <= n - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来合并具有相同按位与结果的边，并使用深度优先搜索 (DFS) 来检查连通性。

算法步骤:
1. 初始化并查集，将所有节点初始化为独立集合。
2. 遍历所有边，按位与计算每条边的权重，并将具有相同按位与结果的边合并到同一个集合中。
3. 对于每个查询，使用并查集检查起点和终点是否在同一集合中，如果是，则返回该集合的按位与结果；否则返回 -1。

关键点:
- 使用并查集来高效地管理连通性。
- 按位与操作的性质使得我们可以将具有相同按位与结果的边合并。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E + Q * α(n))，其中 E 是边的数量，Q 是查询的数量，α 是反阿克曼函数。
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
        self.min_cost = [float('inf')] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, cost):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.min_cost[root_x] &= cost
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.min_cost[root_y] &= cost
            else:
                self.parent[root_y] = root_x
                self.min_cost[root_x] &= cost
                self.rank[root_x] += 1

def min_cost_walk(n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
    uf = UnionFind(n)
    
    for u, v, w in edges:
        uf.union(u, v, w)
    
    result = []
    for s, t in query:
        if uf.find(s) == uf.find(t):
            result.append(uf.min_cost[uf.find(s)])
        else:
            result.append(-1)
    
    return result

Solution = create_solution(min_cost_walk)