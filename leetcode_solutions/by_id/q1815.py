# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1815
标题: Checking Existence of Edge Length Limited Paths
难度: hard
链接: https://leetcode.cn/problems/checking-existence-of-edge-length-limited-paths/
题目类型: 并查集、图、数组、双指针、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1697. 检查边长度限制的路径是否存在 - 给你一个 n 个点组成的无向图边集 edgeList ，其中 edgeList[i] = [ui, vi, disi] 表示点 ui 和点 vi 之间有一条长度为 disi 的边。请注意，两个点之间可能有 超过一条边 。 给你一个查询数组queries ，其中 queries[j] = [pj, qj, limitj] ，你的任务是对于每个查询 queries[j] ，判断是否存在从 pj 到 qj 的路径，且这条路径上的每一条边都 严格小于 limitj 。 请你返回一个 布尔数组 answer ，其中 answer.length == queries.length ，当 queries[j] 的查询结果为 true 时， answer 第 j 个值为 true ，否则为 false 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/12/19/h.png] 输入：n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]] 输出：[false,true] 解释：上图为给定的输入数据。注意到 0 和 1 之间有两条重边，分别为 2 和 16 。 对于第一个查询，0 和 1 之间没有小于 2 的边，所以我们返回 false 。 对于第二个查询，有一条路径（0 -> 1 -> 2）两条边都小于 5 ，所以这个查询我们返回 true 。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/12/19/q.png] 输入：n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]] 输出：[true,false] 解释：上图为给定数据。 提示： * 2 <= n <= 105 * 1 <= edgeList.length, queries.length <= 105 * edgeList[i].length == 3 * queries[j].length == 3 * 0 <= ui, vi, pj, qj <= n - 1 * ui != vi * pj != qj * 1 <= disi, limitj <= 109 * 两个点之间可能有 多条 边。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来处理边和查询。首先将所有边按长度从小到大排序，然后将所有查询按限制长度从小到大排序。遍历查询，同时逐步加入符合条件的边，使用并查集来判断两点是否连通。

算法步骤:
1. 将 `edgeList` 按边长从小到大排序。
2. 将 `queries` 按限制长度从小到大排序，并记录每个查询的原始索引。
3. 初始化并查集。
4. 遍历排序后的查询，对于每个查询：
   - 逐步加入所有长度小于当前查询限制的边。
   - 使用并查集检查查询中的两个点是否连通。
5. 返回查询结果。

关键点:
- 使用并查集高效地处理连通性问题。
- 通过排序和双指针方法，确保每次只加入符合条件的边。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((E + Q) log E)，其中 E 是边的数量，Q 是查询的数量。排序操作的时间复杂度是 O(E log E) 和 O(Q log Q)，而并查集的操作是近似 O(1)。
空间复杂度: O(n + Q)，其中 n 是节点数量，Q 是查询数量。需要存储并查集的数据结构和查询结果。
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

def solution_function_name(n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
    # 将边按长度从小到大排序
    edgeList.sort(key=lambda x: x[2])
    
    # 将查询按限制长度从小到大排序，并记录原始索引
    queries_with_index = sorted(enumerate(queries), key=lambda x: x[1][2])
    
    # 初始化并查集
    uf = UnionFind(n)
    
    # 结果数组
    result = [False] * len(queries)
    
    # 当前处理的边的索引
    edge_index = 0
    
    for original_index, (p, q, limit) in queries_with_index:
        # 加入所有长度小于当前查询限制的边
        while edge_index < len(edgeList) and edgeList[edge_index][2] < limit:
            u, v, _ = edgeList[edge_index]
            uf.union(u, v)
            edge_index += 1
        
        # 检查查询中的两个点是否连通
        result[original_index] = uf.find(p) == uf.find(q)
    
    return result

Solution = create_solution(solution_function_name)