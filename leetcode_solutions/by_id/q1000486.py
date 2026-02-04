# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000486
标题: 集水器
难度: hard
链接: https://leetcode.cn/problems/kskhHQ/
题目类型: 并查集、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 71. 集水器 - 字符串数组 `shape` 描述了一个二维平面中的矩阵形式的集水器，`shape[i][j]` 表示集水器的第 `i` 行 `j` 列为： - `'l'`表示向左倾斜的隔板（即从左上到右下）； - `'r'`表示向右倾斜的隔板（即从左下到右上）； - `'.'` 表示此位置没有隔板 ![image.png](https://pic.leetcode.cn/1664424667-wMnPja-image.png){:width=200px} 已知当隔板构成存储容器可以存水，每个方格代表的蓄水量为 `2`。集水器初始浸泡在水中，除内部密闭空间外，所有位置均被水填满。 现将其从水中竖直向上取出，请返回集水器最终的蓄水量。 **注意：** - 隔板具有良好的透气性，因此空气可以穿过隔板，但水无法穿过 **示例 1：** > 输入： > `shape = ["....rl","l.lr.r",".l..r.","..lr.."]` > > 输出：`18` > > 解释：如下图所示，由于空气会穿过隔板，因此红框区域没有水 ![image.png](https://pic.leetcode.cn/1664436239-eyYxeP-image.png){:width="280px"} **示例 2：** > 输入： > `shape = [".rlrlrlrl","ll..rl..r",".llrrllrr","..lr..lr."]` > 输出：`18` > > 解释：如图所示。由于红框右侧未闭合，因此多余的水会从该处流走。 ![image.png](https://pic.leetcode.cn/1664436082-SibVMv-image.png){:width="400px"} **示例 3：** > 输入： > `shape = ["rlrr","llrl","llr."]` > 输出：`6` > > 解释：如图所示。 ![image.png](https://pic.leetcode.cn/1664424855-dwpUHO-image.png){:width="230px"} **示例 4：** > 输入： > `shape = ["...rl...","..r..l..",".r.rl.l.","r.r..l.l","l.l..rl.",".l.lr.r.","..l..r..","...lr..."]` > > 输出：`30` > > 解释：如下图所示。由于中间为内部密闭空间，无法蓄水。 ![image.png](https://pic.leetcode.cn/1664424894-mClEXh-image.png){:width="350px"} **提示**： - `1 <= shape.length <= 50` - `1 <= shape[i].length <= 50` - `shape[i][j]` 仅为 `'l'`、`'r'` 或 `'.'`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来处理连通性问题，将每行和每列的隔板进行合并，并计算最终的蓄水量。

算法步骤:
1. 初始化并查集，将每个位置视为一个节点。
2. 遍历每一行，将相邻的 'l' 和 'r' 连接起来。
3. 遍历每一列，将相邻的 'l' 和 'r' 连接起来。
4. 计算每个连通分量的蓄水量，排除与边界相连的连通分量。

关键点:
- 使用并查集来处理连通性问题。
- 通过遍历每一行和每一列来连接相邻的 'l' 和 'r'。
- 计算连通分量的蓄水量时，排除与边界相连的连通分量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 shape 的行数，m 是 shape 的列数。
空间复杂度: O(n * m)，用于存储并查集的数据结构。
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


def solution_function_name(shape: List[str]) -> int:
    """
    函数式接口 - 计算集水器的最终蓄水量
    """
    n, m = len(shape), len(shape[0])
    uf = UnionFind(n * m + 1)  # 多一个虚拟节点表示边界
    directions = [(0, 1), (1, 0)]

    for i in range(n):
        for j in range(m):
            if shape[i][j] == '.':
                continue
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and shape[ni][nj] == shape[i][j]:
                    uf.union(i * m + j, ni * m + nj)

    # 将边界上的 'l' 和 'r' 连接到虚拟节点
    for i in range(n):
        if shape[i][0] == 'l':
            uf.union(i * m, n * m)
        if shape[i][m - 1] == 'r':
            uf.union(i * m + m - 1, n * m)
    for j in range(m):
        if shape[0][j] == 'l':
            uf.union(j, n * m)
        if shape[n - 1][j] == 'r':
            uf.union((n - 1) * m + j, n * m)

    water = 0
    visited = set()
    for i in range(n):
        for j in range(m):
            if shape[i][j] == '.':
                continue
            root = uf.find(i * m + j)
            if root not in visited and root != n * m:
                visited.add(root)
                water += 2

    return water


Solution = create_solution(solution_function_name)