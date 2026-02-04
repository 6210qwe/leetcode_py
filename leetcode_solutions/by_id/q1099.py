# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1099
标题: Path With Maximum Minimum Value
难度: medium
链接: https://leetcode.cn/problems/path-with-maximum-minimum-value/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、二分查找、矩阵、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一个整数矩阵 grid 其中每个单元格的值为 [0, 100]。返回从左上角 (0,0) 到右下角 (rows-1, columns-1) 的路径上的最小值的最大值。
注意：路径可以向上下左右四个方向移动。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找和并查集来解决这个问题。

算法步骤:
1. 初始化二分查找的范围，left 为 0，right 为 100。
2. 在每次二分查找的过程中，使用并查集来判断是否存在一条路径使得路径上的所有值都大于等于 mid。
3. 如果存在这样的路径，则更新 left 为 mid + 1，否则更新 right 为 mid - 1。
4. 最终返回 left - 1 作为结果。

关键点:
- 使用并查集来判断路径连通性。
- 二分查找的时间复杂度较低。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * log(max_value))，其中 m 和 n 分别是矩阵的行数和列数，max_value 是矩阵中的最大值。
空间复杂度: O(m * n)，并查集的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.union_find import UnionFind

def maximumMinimumPath(grid: List[List[int]]) -> int:
    def can_traverse(mid: int) -> bool:
        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] < mid:
                    continue
                index = i * n + j
                if i > 0 and grid[i - 1][j] >= mid:
                    uf.union(index, (i - 1) * n + j)
                if j > 0 and grid[i][j - 1] >= mid:
                    uf.union(index, i * n + (j - 1))
        return uf.find(0) == uf.find(m * n - 1)

    m, n = len(grid), len(grid[0])
    left, right = 0, 100
    while left <= right:
        mid = (left + right) // 2
        if can_traverse(mid):
            left = mid + 1
        else:
            right = mid - 1
    return right

Solution = create_solution(maximumMinimumPath)