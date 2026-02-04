# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1442
标题: Number of Operations to Make Network Connected
难度: medium
链接: https://leetcode.cn/problems/number-of-operations-to-make-network-connected/
题目类型: 深度优先搜索、广度优先搜索、并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1319. 连通网络的操作次数 - 用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。 网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。 给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/11/sample_1_1677.png] 输入：n = 4, connections = [[0,1],[0,2],[1,2]] 输出：1 解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/11/sample_2_1677.png] 输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]] 输出：2 示例 3： 输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2]] 输出：-1 解释：线缆数量不足。 示例 4： 输入：n = 5, connections = [[0,1],[0,2],[3,4],[2,3]] 输出：0 提示： * 1 <= n <= 10^5 * 1 <= connections.length <= min(n*(n-1)/2, 10^5) * connections[i].length == 2 * 0 <= connections[i][0], connections[i][1] < n * connections[i][0] != connections[i][1] * 没有重复的连接。 * 两台计算机不会通过多条线缆连接。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集（Union-Find）来解决这个问题。我们需要找到所有的连通分量，并计算需要多少次操作才能将所有节点连通。

算法步骤:
1. 初始化并查集，记录每个节点的父节点和秩。
2. 遍历所有连接，将连接的两个节点进行合并。
3. 计算连通分量的数量。
4. 如果连接数小于 n-1，说明线缆数量不足，返回 -1。
5. 否则，返回连通分量的数量减 1，即为所需的操作次数。

关键点:
- 使用路径压缩和按秩合并优化并查集操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m * α(m, n))，其中 n 是节点数，m 是连接数，α 是阿克曼函数的反函数。
空间复杂度: O(n)，用于存储并查集的数据结构。
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

    def get_count(self):
        return self.count


def solution_function_name(n: int, connections: List[List[int]]) -> int:
    """
    函数式接口 - 计算使所有计算机都连通所需的最少操作次数
    """
    if len(connections) < n - 1:
        return -1

    uf = UnionFind(n)
    for a, b in connections:
        uf.union(a, b)

    return uf.get_count() - 1


Solution = create_solution(solution_function_name)