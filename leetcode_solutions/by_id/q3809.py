# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3809
标题: Properties Graph
难度: medium
链接: https://leetcode.cn/problems/properties-graph/
题目类型: 深度优先搜索、广度优先搜索、并查集、图、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3493. 属性图 - 给你一个二维整数数组 properties，其维度为 n x m，以及一个整数 k。 定义一个函数 intersect(a, b)，它返回数组 a 和 b 中 共有的不同整数的数量 。 构造一个 无向图，其中每个索引 i 对应 properties[i]。如果且仅当 intersect(properties[i], properties[j]) >= k（其中 i 和 j 的范围为 [0, n - 1] 且 i != j），节点 i 和节点 j 之间有一条边。 返回结果图中 连通分量 的数量。 示例 1： 输入： properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], k = 1 输出： 3 解释： 生成的图有 3 个连通分量： [https://pic.leetcode.cn/1742665594-CDVPWz-image.png] 示例 2： 输入： properties = [[1,2,3],[2,3,4],[4,3,5]], k = 2 输出： 1 解释： 生成的图有 1 个连通分量： [https://pic.leetcode.cn/1742665565-NzYlYH-screenshot-from-2025-02-27-23-58-34.png] 示例 3： 输入： properties = [[1,1],[1,1]], k = 2 输出： 2 解释： intersect(properties[0], properties[1]) = 1，小于 k。因此在图中 properties[0] 和 properties[1] 之间没有边。 提示： * 1 <= n == properties.length <= 100 * 1 <= m == properties[i].length <= 100 * 1 <= properties[i][j] <= 100 * 1 <= k <= m
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来管理连通分量，并通过集合操作计算交集。

算法步骤:
1. 初始化并查集。
2. 计算每对节点之间的交集，如果交集大小大于等于 k，则将这两个节点合并到同一个连通分量中。
3. 最后返回并查集中连通分量的数量。

关键点:
- 使用并查集高效地管理连通分量。
- 通过集合操作快速计算交集。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * m)，其中 n 是 properties 的长度，m 是每个属性数组的长度。
空间复杂度: O(n)，并查集需要 O(n) 的空间。
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


def solution_function_name(properties: List[List[int]], k: int) -> int:
    """
    函数式接口 - 计算属性图中的连通分量数量
    """
    n = len(properties)
    uf = UnionFind(n)

    for i in range(n):
        for j in range(i + 1, n):
            if len(set(properties[i]) & set(properties[j])) >= k:
                uf.union(i, j)

    return uf.get_count()


Solution = create_solution(solution_function_name)