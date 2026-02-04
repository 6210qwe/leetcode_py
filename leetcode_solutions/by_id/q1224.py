# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1224
标题: Minimum Falling Path Sum II
难度: hard
链接: https://leetcode.cn/problems/minimum-falling-path-sum-ii/
题目类型: 数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1289. 下降路径最小和 II - 给你一个 n x n 整数矩阵 grid ，请你返回 非零偏移下降路径 数字和的最小值。 非零偏移下降路径 定义为：从 grid 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。 示例 1： [https://assets.leetcode.com/uploads/2021/08/10/falling-grid.jpg] 输入：grid = [[1,2,3],[4,5,6],[7,8,9]] 输出：13 解释： 所有非零偏移下降路径包括： [1,5,9], [1,5,7], [1,6,7], [1,6,8], [2,4,8], [2,4,9], [2,6,7], [2,6,8], [3,4,8], [3,4,9], [3,5,7], [3,5,9] 下降路径中数字和最小的是 [1,5,7] ，所以答案是 13 。 示例 2： 输入：grid = [[7]] 输出：7 提示： * n == grid.length == grid[i].length * 1 <= n <= 200 * -99 <= grid[i][j] <= 99
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们维护一个二维数组 dp，其中 dp[i][j] 表示到达第 i 行第 j 列的最小路径和。为了确保相邻行的元素不在同一列，我们需要在每一行找到两个最小值。

算法步骤:
1. 初始化 dp 数组，dp[0] 为 grid 的第一行。
2. 对于每一行，找到前一行的两个最小值及其索引。
3. 更新当前行的 dp 值，确保不使用前一行的最小值所在的列。
4. 最后一行的最小值即为所求。

关键点:
- 使用前一行的两个最小值来更新当前行的 dp 值。
- 确保相邻行的元素不在同一列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O(n^2)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_falling_path_sum(grid: List[List[int]]) -> int:
    """
    函数式接口 - 返回非零偏移下降路径的最小和
    """
    n = len(grid)
    if n == 1:
        return grid[0][0]

    dp = [row[:] for row in grid]

    for i in range(1, n):
        first_min, second_min = float('inf'), float('inf')
        first_idx, second_idx = -1, -1

        # 找到前一行的两个最小值及其索引
        for j in range(n):
            if dp[i - 1][j] < first_min:
                second_min, second_idx = first_min, first_idx
                first_min, first_idx = dp[i - 1][j], j
            elif dp[i - 1][j] < second_min:
                second_min, second_idx = dp[i - 1][j], j

        # 更新当前行的 dp 值
        for j in range(n):
            if j == first_idx:
                dp[i][j] += second_min
            else:
                dp[i][j] += first_min

    return min(dp[-1])


Solution = create_solution(min_falling_path_sum)