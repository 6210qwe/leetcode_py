# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 999
标题: Regions Cut By Slashes
难度: medium
链接: https://leetcode.cn/problems/regions-cut-by-slashes/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、哈希表、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
959. 由斜杠划分区域 - 在由 1 x 1 方格组成的 n x n 网格 grid 中，每个 1 x 1 方块由 '/'、'\' 或空格构成。这些字符会将方块划分为一些共边的区域。 给定网格 grid 表示为一个字符串数组，返回 区域的数量 。 请注意，反斜杠字符是转义的，因此 '\' 用 '\\' 表示。 示例 1： [https://assets.leetcode.com/uploads/2018/12/15/1.png] 输入：grid = [" /","/ "] 输出：2 示例 2： [https://assets.leetcode.com/uploads/2018/12/15/2.png] 输入：grid = [" /"," "] 输出：1 示例 3： [https://assets.leetcode.com/uploads/2018/12/15/4.png] 输入：grid = ["/\\","\\/"] 输出：5 解释：回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。 提示： * n == grid.length == grid[i].length * 1 <= n <= 30 * grid[i][j] 是 '/'、'\'、或 ' '
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来合并相邻的区域，并计算最终的连通分量数量。

算法步骤:
1. 初始化并查集，大小为 (n+1) * (n+1)，每个方格分成四个小三角形。
2. 遍历每个方格，根据斜杠的方向合并相应的三角形。
3. 计算并查集中的连通分量数量，即为区域的数量。

关键点:
- 将每个方格分成四个小三角形，使用并查集来管理这些三角形的连通性。
- 根据斜杠的方向，合并相应的小三角形。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * α(n^2))，其中 n 是网格的边长，α 是反阿克曼函数。
空间复杂度: O(n^2)，并查集需要存储 n^2 个节点。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.count = size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        if self.rank[root_p] > self.rank[root_q]:
            self.parent[root_q] = root_p
        elif self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q
        else:
            self.parent[root_q] = root_p
            self.rank[root_p] += 1
        self.count -= 1

def regions_by_slashes(grid: List[str]) -> int:
    n = len(grid)
    uf = UnionFind(4 * n * n)

    for i in range(n):
        for j in range(n):
            idx = 4 * (i * n + j)
            if grid[i][j] == '/':
                uf.union(idx, idx + 3)
                uf.union(idx + 1, idx + 2)
            elif grid[i][j] == '\\':
                uf.union(idx, idx + 1)
                uf.union(idx + 2, idx + 3)
            else:
                uf.union(idx, idx + 1)
                uf.union(idx + 1, idx + 2)
                uf.union(idx + 2, idx + 3)

            if i < n - 1:
                uf.union(idx + 3, idx + 4 * n)
            if j < n - 1:
                uf.union(idx + 2, idx + 4 + 1)

    return uf.count

Solution = create_solution(regions_by_slashes)