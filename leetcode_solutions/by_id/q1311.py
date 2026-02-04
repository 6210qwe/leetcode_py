# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1311
标题: Largest Magic Square
难度: medium
链接: https://leetcode.cn/problems/largest-magic-square/
题目类型: 数组、矩阵、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1895. 最大的幻方 - 一个 k x k 的 幻方 指的是一个 k x k 填满整数的方格阵，且每一行、每一列以及两条对角线的和 全部相等 。幻方中的整数 不需要互不相同 。显然，每个 1 x 1 的方格都是一个幻方。 给你一个 m x n 的整数矩阵 grid ，请你返回矩阵中 最大幻方 的 尺寸 （即边长 k）。 示例 1： [https://assets.leetcode.com/uploads/2021/05/29/magicsquare-grid.jpg] 输入：grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]] 输出：3 解释：最大幻方尺寸为 3 。 每一行，每一列以及两条对角线的和都等于 12 。 - 每一行的和：5+1+6 = 5+4+3 = 2+7+3 = 12 - 每一列的和：5+5+2 = 1+4+7 = 6+3+3 = 12 - 对角线的和：5+4+3 = 6+4+2 = 12 示例 2： [https://assets.leetcode.com/uploads/2021/05/29/magicsquare2-grid.jpg] 输入：grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]] 输出：2 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 50 * 1 <= grid[i][j] <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和来快速计算子矩阵的行、列和对角线的和。

算法步骤:
1. 计算行前缀和。
2. 计算列前缀和。
3. 计算主对角线前缀和。
4. 计算副对角线前缀和。
5. 从大到小枚举可能的幻方尺寸，检查每个子矩阵是否满足幻方条件。

关键点:
- 使用前缀和可以快速计算任意子矩阵的行、列和对角线的和。
- 从大到小枚举尺寸可以尽早找到最大的幻方。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * min(m, n))
空间复杂度: O(m * n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def largest_magic_square(grid: List[List[int]]) -> int:
    def is_magic_square(r1, c1, r2, c2):
        target = row_sum[r1][c2 + 1] - row_sum[r1][c1]
        for r in range(r1, r2 + 1):
            if row_sum[r][c2 + 1] - row_sum[r][c1] != target:
                return False
        for c in range(c1, c2 + 1):
            if col_sum[r2 + 1][c] - col_sum[r1][c] != target:
                return False
        if diag_sum[r2][c2] - (diag_sum[r1 - 1][c1 - 1] if r1 > 0 and c1 > 0 else 0) != target:
            return False
        if anti_diag_sum[r2][c1] - (anti_diag_sum[r1 - 1][c2 + 1] if r1 > 0 and c2 < n - 1 else 0) != target:
            return False
        return True

    m, n = len(grid), len(grid[0])
    row_sum = [[0] * (n + 1) for _ in range(m)]
    col_sum = [[0] * n for _ in range(m + 1)]
    diag_sum = [[0] * n for _ in range(m)]
    anti_diag_sum = [[0] * (n + 1) for _ in range(m)]

    for r in range(m):
        for c in range(n):
            row_sum[r][c + 1] = row_sum[r][c] + grid[r][c]
            col_sum[r + 1][c] = col_sum[r][c] + grid[r][c]
            diag_sum[r][c] = (diag_sum[r - 1][c - 1] if r > 0 and c > 0 else 0) + grid[r][c]
            anti_diag_sum[r][c] = (anti_diag_sum[r - 1][c + 1] if r > 0 and c < n - 1 else 0) + grid[r][c]

    for size in range(min(m, n), 0, -1):
        for r in range(m - size + 1):
            for c in range(n - size + 1):
                if is_magic_square(r, c, r + size - 1, c + size - 1):
                    return size
    return 1

Solution = create_solution(largest_magic_square)