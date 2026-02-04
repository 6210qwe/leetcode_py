# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3492
标题: Count Submatrices With Equal Frequency of X and Y
难度: medium
链接: https://leetcode.cn/problems/count-submatrices-with-equal-frequency-of-x-and-y/
题目类型: 数组、矩阵、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3212. 统计 X 和 Y 频数相等的子矩阵数量 - 给你一个二维字符矩阵 grid，其中 grid[i][j] 可能是 'X'、'Y' 或 '.'，返回满足以下条件的子矩阵数量： * 包含 grid[0][0] * 'X' 和 'Y' 的频数相等。 * 至少包含一个 'X'。 示例 1： 输入： grid = [["X","Y","."],["Y",".","."]] 输出： 3 解释： [https://assets.leetcode.com/uploads/2024/06/07/examplems.png] 示例 2： 输入： grid = [["X","X"],["X","Y"]] 输出： 0 解释： 不存在满足 'X' 和 'Y' 频数相等的子矩阵。 示例 3： 输入： grid = [[".","."],[".","."]] 输出： 0 解释： 不存在满足至少包含一个 'X' 的子矩阵。 提示： * 1 <= grid.length, grid[i].length <= 1000 * grid[i][j] 可能是 'X'、'Y' 或 '.'.
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和来快速计算子矩阵中 'X' 和 'Y' 的频数，并通过双指针法来遍历所有可能的子矩阵。

算法步骤:
1. 计算每一行的前缀和数组，记录从左到右 'X' 和 'Y' 的频数。
2. 对于每一列，使用双指针法遍历所有可能的子矩阵，检查 'X' 和 'Y' 的频数是否相等。

关键点:
- 使用前缀和可以快速计算任意子矩阵中 'X' 和 'Y' 的频数。
- 双指针法可以高效地遍历所有可能的子矩阵。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m^2)，其中 n 是矩阵的行数，m 是矩阵的列数。
空间复杂度: O(n * m)，用于存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def count_submatrices_with_equal_frequency(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    
    n, m = len(grid), len(grid[0])
    prefix_sum = [[[0, 0] for _ in range(m + 1)] for _ in range(n)]
    
    # 计算每一行的前缀和
    for i in range(n):
        for j in range(1, m + 1):
            if grid[i][j - 1] == 'X':
                prefix_sum[i][j][0] = prefix_sum[i][j - 1][0] + 1
                prefix_sum[i][j][1] = prefix_sum[i][j - 1][1]
            elif grid[i][j - 1] == 'Y':
                prefix_sum[i][j][0] = prefix_sum[i][j - 1][0]
                prefix_sum[i][j][1] = prefix_sum[i][j - 1][1] + 1
            else:
                prefix_sum[i][j][0] = prefix_sum[i][j - 1][0]
                prefix_sum[i][j][1] = prefix_sum[i][j - 1][1]
    
    count = 0
    
    # 双指针法遍历所有可能的子矩阵
    for start_col in range(m):
        for end_col in range(start_col + 1, m + 1):
            x_count, y_count = 0, 0
            for row in range(n):
                x_count += prefix_sum[row][end_col][0] - prefix_sum[row][start_col][0]
                y_count += prefix_sum[row][end_col][1] - prefix_sum[row][start_col][1]
                if x_count == y_count and x_count > 0:
                    count += 1
    
    return count

Solution = create_solution(count_submatrices_with_equal_frequency)