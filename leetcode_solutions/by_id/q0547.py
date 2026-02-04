# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 547
标题: Number of Provinces
难度: medium
链接: https://leetcode.cn/problems/number-of-provinces/
题目类型: 深度优先搜索、广度优先搜索、并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
547. 省份数量 - 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。 返回矩阵中 省份 的数量。 示例 1： [https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg] 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]] 输出：2 示例 2： [https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg] 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]] 输出：3 提示： * 1 <= n <= 200 * n == isConnected.length * n == isConnected[i].length * isConnected[i][j] 为 1 或 0 * isConnected[i][i] == 1 * isConnected[i][j] == isConnected[j][i]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集（Union-Find）来解决这个问题。

算法步骤:
1. 初始化并查集，每个城市初始时都是独立的集合。
2. 遍历连接矩阵，将直接相连的城市合并到同一个集合中。
3. 最后统计并查集中不同集合的数量，即为省份数量。

关键点:
- 并查集的路径压缩和按秩合并可以优化查找和合并操作的时间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * α(n))，其中 n 是城市的数量，α 是反阿克曼函数，接近于常数。
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


def solution_function_name(isConnected: List[List[int]]) -> int:
    """
    函数式接口 - 使用并查集计算省份数量
    """
    n = len(isConnected)
    uf = UnionFind(n)

    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                uf.union(i, j)

    return uf.get_count()


Solution = create_solution(solution_function_name)