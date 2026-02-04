# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3902
标题: Maximize Spanning Tree Stability with Upgrades
难度: hard
链接: https://leetcode.cn/problems/maximize-spanning-tree-stability-with-upgrades/
题目类型: 贪心、并查集、图、二分查找、最小生成树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3600. 升级后最大生成树稳定性 - 给你一个整数 n，表示编号从 0 到 n - 1 的 n 个节点，以及一个 edges 列表，其中 edges[i] = [ui, vi, si, musti]：
* ui 和 vi 表示节点 ui 和 vi 之间的一条无向边。
* si 是该边的强度。
* musti 是一个整数（0 或 1）。如果 musti == 1，则该边 必须 包含在生成树中，且 不能升级 。
你还有一个整数 k，表示你可以执行的最多 升级 次数。每次升级会使边的强度 翻倍 ，且每条可升级边（即 musti == 0）最多只能升级一次。
一个生成树的 稳定性 定义为其中所有边的 最小 强度。
返回任何有效生成树可能达到的 最大 稳定性。如果无法连接所有节点，返回 -1。
注意： 图的一个 生成树（spanning tree）是该图中边的一个子集，它满足以下条件：
* 将所有节点连接在一起（即图是 连通的 ）。
* 不 形成任何环。
* 包含 恰好 n - 1 条边，其中 n 是图中节点的数量。
示例 1：
输入： n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1
输出： 2
解释：
* 边 [0,1] 强度为 2，必须包含在生成树中。
* 边 [1,2] 是可选的，可以使用一次升级将其强度从 3 提升到 6。
* 最终的生成树包含这两条边，强度分别为 2 和 6。
* 生成树中的最小强度是 2，即最大可能稳定性。
示例 2：
输入： n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2
输出： 6
解释：
* 所有边都是可选的，且最多可以进行 k = 2 次升级。
* 将边 [0,1] 从 4 升级到 8，将边 [1,2] 从 3 升级到 6。
* 生成树包含这两条边，强度分别为 8 和 6。
* 生成树中的最小强度是 6，即最大可能稳定性。
示例 3：
输入： n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0
输出： -1
解释：
* 所有边都是必选的，构成了一个环，这违反了生成树无环的性质。因此返回 -1。
提示：
* 2 <= n <= 105
* 1 <= edges.length <= 105
* edges[i] = [ui, vi, si, musti]
* 0 <= ui, vi < n
* ui != vi
* 1 <= si <= 105
* musti 是 0 或 1。
* 0 <= k <= n
* 没有重复的边。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集和二分查找来找到最大稳定性。

算法步骤:
1. 初始化并查集，并将所有必须包含的边加入并查集中。
2. 如果此时并查集中已经形成了一个连通块，则返回 -1。
3. 对于剩余的边，使用二分查找来确定最大稳定性。
4. 在每次二分查找的过程中，使用并查集来判断当前稳定性是否可行。
5. 返回最终的最大稳定性。

关键点:
- 使用并查集来管理连通性。
- 使用二分查找来优化查找最大稳定性的过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log E + E log S)，其中 E 是边的数量，S 是边强度的最大值。
空间复杂度: O(n + E)，其中 n 是节点数量，E 是边的数量。
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
            return True
        return False


def solution_function_name(n: int, edges: List[List[int]], k: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    # 初始化并查集
    uf = UnionFind(n)
    mandatory_edges = []
    optional_edges = []

    # 分离必须包含的边和可选的边
    for u, v, s, must in edges:
        if must == 1:
            mandatory_edges.append((u, v, s))
        else:
            optional_edges.append((u, v, s))

    # 将所有必须包含的边加入并查集中
    for u, v, s in mandatory_edges:
        if not uf.union(u, v):
            return -1

    # 如果此时并查集中已经形成了一个连通块，则返回 -1
    if len(set(uf.find(i) for i in range(n))) != 1:
        return -1

    # 对于剩余的边，使用二分查找来确定最大稳定性
    def is_valid(strength):
        uf_copy = UnionFind(n)
        for u, v, s in mandatory_edges:
            uf_copy.union(u, v)
        upgrades_used = 0
        for u, v, s in optional_edges:
            if s >= strength or (s * 2 >= strength and upgrades_used < k):
                if s * 2 >= strength:
                    upgrades_used += 1
                if not uf_copy.union(u, v):
                    return False
        return len(set(uf_copy.find(i) for i in range(n))) == 1

    low, high = 1, max(s for _, _, s, _ in edges) * 2
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if is_valid(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result


Solution = create_solution(solution_function_name)