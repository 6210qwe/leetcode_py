# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 821
标题: Bricks Falling When Hit
难度: hard
链接: https://leetcode.cn/problems/bricks-falling-when-hit/
题目类型: 并查集、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
803. 打砖块 - 有一个 m x n 的二元网格 grid ，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是： * 一块砖直接连接到网格的顶部，或者 * 至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时 给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而 掉落 。一旦砖块掉落，它会 立即 从网格 grid 中消失（即，它不会落在其他稳定的砖块上）。 返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。 注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。 示例 1： 输入：grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]] 输出：[2] 解释：网格开始为： [[1,0,0,0]， [1,1,1,0]] 消除 (1,0) 处加粗的砖块，得到网格： [[1,0,0,0] [0,1,1,0]] 两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格： [[1,0,0,0], [0,0,0,0]] 因此，结果为 [2] 。 示例 2： 输入：grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]] 输出：[0,0] 解释：网格开始为： [[1,0,0,0], [1,1,0,0]] 消除 (1,1) 处加粗的砖块，得到网格： [[1,0,0,0], [1,0,0,0]] 剩下的砖都很稳定，所以不会掉落。网格保持不变： [[1,0,0,0], [1,0,0,0]] 接下来消除 (1,0) 处加粗的砖块，得到网格： [[1,0,0,0], [0,0,0,0]] 剩下的砖块仍然是稳定的，所以不会有砖块掉落。 因此，结果为 [0,0] 。 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 200 * grid[i][j] 为 0 或 1 * 1 <= hits.length <= 4 * 104 * hits[i].length == 2 * 0 <= xi <= m - 1 * 0 <= yi <= n - 1 * 所有 (xi, yi) 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来维护砖块的连通性，并通过逆序处理 hits 来模拟砖块掉落的过程。

算法步骤:
1. 初始化并查集，将所有砖块和一个虚拟节点（表示顶部）加入并查集。
2. 逆序处理 hits，先将所有要敲掉的砖块标记为 0。
3. 遍历整个网格，将剩余的砖块加入并查集中。
4. 逆序处理 hits，恢复被敲掉的砖块，并检查其连通性，计算掉落的砖块数量。

关键点:
- 使用并查集来高效地管理砖块的连通性。
- 通过逆序处理 hits 来模拟砖块掉落的过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n + k)，其中 m 和 n 分别是网格的行数和列数，k 是 hits 的长度。
空间复杂度: O(m * n)，并查集的空间开销。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
            self.count -= 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

def hitBricks(grid: List[List[int]], hits: List[List[int]]) -> List[int]:
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 将所有要敲掉的砖块标记为 0
    for i, j in hits:
        if grid[i][j] == 1:
            grid[i][j] = 2  # 标记为 2 表示被敲掉的砖块
    
    # 初始化并查集
    uf = UnionFind(m * n + 1)  # 虚拟节点表示顶部
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                idx = i * n + j
                if i == 0:
                    uf.union(idx, m * n)  # 连接到顶部
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        uf.union(idx, ni * n + nj)
    
    # 逆序处理 hits，恢复被敲掉的砖块
    result = []
    for i, j in reversed(hits):
        if grid[i][j] == 2:
            grid[i][j] = 1  # 恢复砖块
            idx = i * n + j
            before = uf.size[uf.find(m * n)] - 1  # 当前连通的砖块数
            if i == 0:
                uf.union(idx, m * n)  # 连接到顶部
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    uf.union(idx, ni * n + nj)
            after = uf.size[uf.find(m * n)] - 1  # 修复后的连通砖块数
            result.append(max(0, after - before - 1))  # 计算掉落的砖块数
        else:
            result.append(0)  # 如果该位置本来就没有砖块，则掉落的砖块数为 0
    
    return result[::-1]

Solution = create_solution(hitBricks)