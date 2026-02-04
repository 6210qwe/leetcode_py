# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3516
标题: Design Neighbor Sum Service
难度: easy
链接: https://leetcode.cn/problems/design-neighbor-sum-service/
题目类型: 设计、数组、哈希表、矩阵、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3242. 设计相邻元素求和服务 - 给你一个 n x n 的二维数组 grid，它包含范围 [0, n2 - 1] 内的不重复元素。 实现 neighborSum 类： * neighborSum(int [][]grid) 初始化对象。 * int adjacentSum(int value) 返回在 grid 中与 value 相邻的元素之和，相邻指的是与 value 在上、左、右或下的元素。 * int diagonalSum(int value) 返回在 grid 中与 value 对角线相邻的元素之和，对角线相邻指的是与 value 在左上、右上、左下或右下的元素。 [https://assets.leetcode.com/uploads/2024/06/24/design.png] 示例 1： 输入： ["neighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"] [[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]] 输出： [null, 6, 16, 16, 4] 解释： [https://assets.leetcode.com/uploads/2024/06/24/designexample0.png] * 1 的相邻元素是 0、2 和 4。 * 4 的相邻元素是 1、3、5 和 7。 * 4 的对角线相邻元素是 0、2、6 和 8。 * 8 的对角线相邻元素是 4。 示例 2： 输入： ["neighborSum", "adjacentSum", "diagonalSum"] [[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]]], [15], [9]] 输出： [null, 23, 45] 解释： [https://assets.leetcode.com/uploads/2024/06/24/designexample2.png] * 15 的相邻元素是 0、10、7 和 6。 * 9 的对角线相邻元素是 4、12、14 和 15。 提示： * 3 <= n == grid.length == grid[0].length <= 10 * 0 <= grid[i][j] <= n2 - 1 * 所有 grid[i][j] 值均不重复。 * adjacentSum 和 diagonalSum 中的 value 均在范围 [0, n2 - 1] 内。 * 最多会调用 adjacentSum 和 diagonalSum 总共 2 * n2 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用一个字典来存储每个值的位置，以便快速查找。
- 计算相邻元素和对角线相邻元素时，通过位置直接访问。

算法步骤:
1. 初始化时，遍历网格，将每个值的位置存储在字典中。
2. 在 `adjacentSum` 方法中，找到给定值的位置，计算其上下左右的相邻元素之和。
3. 在 `diagonalSum` 方法中，找到给定值的位置，计算其左上、右上、左下、右下的对角线相邻元素之和。

关键点:
- 使用字典存储值的位置，以实现 O(1) 时间复杂度的查找。
- 通过位置直接访问相邻和对角线相邻元素。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每次查询的时间复杂度为常数级。
空间复杂度: O(n^2) - 存储网格中每个值的位置。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional

class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.value_to_pos = {}
        for i in range(self.n):
            for j in range(self.n):
                self.value_to_pos[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        if value not in self.value_to_pos:
            return 0
        i, j = self.value_to_pos[value]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        total = 0
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.n:
                total += self.grid[ni][nj]
        return total

    def diagonalSum(self, value: int) -> int:
        if value not in self.value_to_pos:
            return 0
        i, j = self.value_to_pos[value]
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        total = 0
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.n:
                total += self.grid[ni][nj]
        return total

# 工厂函数
def create_solution() -> NeighborSum:
    return NeighborSum

# 示例使用
if __name__ == "__main__":
    grid = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    ns = NeighborSum(grid)
    print(ns.adjacentSum(1))  # 输出 6
    print(ns.adjacentSum(4))  # 输出 16
    print(ns.diagonalSum(4))  # 输出 16
    print(ns.diagonalSum(8))  # 输出 4