# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2363
标题: Maximum Trailing Zeros in a Cornered Path
难度: medium
链接: https://leetcode.cn/problems/maximum-trailing-zeros-in-a-cornered-path/
题目类型: 数组、矩阵、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2245. 转角路径的乘积中最多能有几个尾随零 - 给你一个二维整数数组 grid ，大小为 m x n，其中每个单元格都含一个正整数。 转角路径 定义为：包含至多一个弯的一组相邻单元。具体而言，路径应该完全 向水平方向 或者 向竖直方向 移动过弯（如果存在弯），而不能访问之前访问过的单元格。在过弯之后，路径应当完全朝 另一个 方向行进：如果之前是向水平方向，那么就应该变为向竖直方向；反之亦然。当然，同样不能访问之前已经访问过的单元格。 一条路径的 乘积 定义为：路径上所有值的乘积。 请你从 grid 中找出一条乘积中尾随零数目最多的转角路径，并返回该路径中尾随零的数目。 注意： * 水平 移动是指向左或右移动。 * 竖直 移动是指向上或下移动。 示例 1： [https://assets.leetcode.com/uploads/2022/03/23/ex1new2.jpg] 输入：grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]] 输出：3 解释：左侧的图展示了一条有效的转角路径。 其乘积为 15 * 20 * 6 * 1 * 10 = 18000 ，共计 3 个尾随零。 可以证明在这条转角路径的乘积中尾随零数目最多。 中间的图不是一条有效的转角路径，因为它有不止一个弯。 右侧的图也不是一条有效的转角路径，因为它需要重复访问已经访问过的单元格。 示例 2： [https://assets.leetcode.com/uploads/2022/03/25/ex2.jpg] 输入：grid = [[4,3,2],[7,6,1],[8,8,8]] 输出：0 解释：网格如上图所示。 不存在乘积含尾随零的转角路径。 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 105 * 1 <= m * n <= 105 * 1 <= grid[i][j] <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 通过计算每个单元格中因数 2 和 5 的数量，使用前缀和来快速计算路径上的因数 2 和 5 的数量。
- 通过四个方向的前缀和来计算不同路径的尾随零数量。

算法步骤:
1. 计算每个单元格中因数 2 和 5 的数量。
2. 计算四个方向（上、下、左、右）的前缀和。
3. 对于每个单元格，计算其作为拐点时的路径尾随零数量。
4. 返回最大尾随零数量。

关键点:
- 使用前缀和来快速计算路径上的因数 2 和 5 的数量。
- 通过四个方向的前缀和来计算不同路径的尾随零数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)
空间复杂度: O(m * n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def count_factors(num: int, factor: int) -> int:
    count = 0
    while num % factor == 0:
        num //= factor
        count += 1
    return count

def max_trailing_zeros(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    # 计算每个单元格中因数 2 和 5 的数量
    factors = [[[0, 0] for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            factors[i][j][0] = count_factors(grid[i][j], 2)
            factors[i][j][1] = count_factors(grid[i][j], 5)
    
    # 计算四个方向的前缀和
    prefix_sum_up = [[[0, 0] for _ in range(n)] for _ in range(m + 1)]
    prefix_sum_left = [[[0, 0] for _ in range(n + 1)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            prefix_sum_up[i + 1][j][0] = prefix_sum_up[i][j][0] + factors[i][j][0]
            prefix_sum_up[i + 1][j][1] = prefix_sum_up[i][j][1] + factors[i][j][1]
            prefix_sum_left[i][j + 1][0] = prefix_sum_left[i][j][0] + factors[i][j][0]
            prefix_sum_left[i][j + 1][1] = prefix_sum_left[i][j][1] + factors[i][j][1]
    
    # 计算每个单元格作为拐点时的路径尾随零数量
    max_zeros = 0
    for i in range(m):
        for j in range(n):
            up = prefix_sum_up[i][j]
            down = [prefix_sum_up[m][j][k] - prefix_sum_up[i + 1][j][k] for k in range(2)]
            left = prefix_sum_left[i][j]
            right = [prefix_sum_left[i][n][k] - prefix_sum_left[i][j + 1][k] for k in range(2)]
            
            paths = [
                (up, left),
                (up, right),
                (down, left),
                (down, right)
            ]
            
            for (p1, p2) in paths:
                zeros = min(p1[0] + p2[0], p1[1] + p2[1]) + factors[i][j][0] + factors[i][j][1]
                max_zeros = max(max_zeros, zeros)
    
    return max_zeros

Solution = max_trailing_zeros