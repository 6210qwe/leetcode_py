# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 964
标题: Minimize Malware Spread II
难度: hard
链接: https://leetcode.cn/problems/minimize-malware-spread-ii/
题目类型: 深度优先搜索、广度优先搜索、并查集、图、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
928. 尽量减少恶意软件的传播 II - 给定一个由 n 个节点组成的网络，用 n x n 个邻接矩阵 graph 表示。在节点网络中，只有当 graph[i][j] = 1 时，节点 i 能够直接连接到另一个节点 j。 一些节点 initial 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。 假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。 我们可以从 initial 中 删除一个节点，并完全移除该节点以及从该节点到任何其他节点的任何连接。 请返回移除后能够使 M(initial) 最小化的节点。如果有多个节点满足条件，返回索引 最小的节点 。 示例 1： 输入：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1] 输出：0 示例 2： 输入：graph = [[1,1,0],[1,1,1],[0,1,1]], initial = [0,1] 输出：1 示例 3： 输入：graph = [[1,1,0,0],[1,1,1,0],[0,1,1,1],[0,0,1,1]], initial = [0,1] 输出：1 提示： * n == graph.length * n == graph[i].length * 2 <= n <= 300 * graph[i][j] 是 0 或 1. * graph[i][j] == graph[j][i] * graph[i][i] == 1 * 1 <= initial.length < n * 0 <= initial[i] <= n - 1 * initial 中每个整数都不同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来找到连通分量，并计算每个连通分量中的初始感染节点数量。然后选择移除哪个初始感染节点可以最大程度地减少感染范围。

算法步骤:
1. 初始化并查集，将所有节点初始化为独立的集合。
2. 遍历图，将相连的节点合并到同一个集合中。
3. 计算每个连通分量的大小。
4. 统计每个连通分量中的初始感染节点数量。
5. 对于每个初始感染节点，计算移除它后能减少的感染节点数量。
6. 选择减少感染节点数量最多的初始感染节点，如果有多解，选择索引最小的节点。

关键点:
- 使用并查集来高效地管理连通分量。
- 通过统计每个连通分量中的初始感染节点数量来决定最优解。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * α(n))，其中 n 是节点数，α 是反阿克曼函数。
空间复杂度: O(n)，用于存储并查集和连通分量的信息。
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
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

def minimize_malware_spread(graph: List[List[int]], initial: List[int]) -> int:
    n = len(graph)
    uf = UnionFind(n)

    # 合并连通分量
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1:
                uf.union(i, j)

    # 统计每个连通分量的大小
    component_size = [0] * n
    for i in range(n):
        root = uf.find(i)
        component_size[root] += 1

    # 统计每个连通分量中的初始感染节点数量
    infected_count = {}
    for node in initial:
        root = uf.find(node)
        if root not in infected_count:
            infected_count[root] = []
        infected_count[root].append(node)

    # 找到最优解
    max_reduction = -1
    result = min(initial)
    for node in initial:
        root = uf.find(node)
        if len(infected_count[root]) == 1:
            reduction = component_size[root]
            if reduction > max_reduction or (reduction == max_reduction and node < result):
                max_reduction = reduction
                result = node

    return result

Solution = create_solution(minimize_malware_spread)