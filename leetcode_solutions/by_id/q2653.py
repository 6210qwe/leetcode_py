# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2653
标题: Check if There is a Path With Equal Number of 0's And 1's
难度: medium
链接: https://leetcode.cn/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/
题目类型: 数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2510. 检查是否有路径经过相同数量的 0 和 1 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来记录从起点到每个点的 0 和 1 的差值。

算法步骤:
1. 初始化一个二维数组 `dp`，其中 `dp[i][j]` 表示从起点 (0, 0) 到 (i, j) 的路径上 0 和 1 的差值集合。
2. 遍历整个矩阵，更新 `dp` 数组。
3. 如果在某个点 (i, j) 上，差值为 0，则说明存在一条路径使得 0 和 1 的数量相等。

关键点:
- 使用集合来存储从起点到每个点的 0 和 1 的差值，以处理不同的路径。
- 通过动态规划来避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是矩阵的行数和列数。
空间复杂度: O(m * n)，用于存储 `dp` 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def check_path_with_equal_zeros_and_ones(grid: List[List[int]]) -> bool:
    """
    函数式接口 - 检查是否存在一条路径使得 0 和 1 的数量相等
    """
    if not grid or not grid[0]:
        return False

    m, n = len(grid), len(grid[0])
    dp = [[set() for _ in range(n)] for _ in range(m)]

    # 初始化起点
    dp[0][0].add(1 if grid[0][0] == 1 else -1)

    # 动态规划填充 dp 数组
    for i in range(m):
        for j in range(n):
            if i > 0:
                for diff in dp[i-1][j]:
                    dp[i][j].add(diff + (1 if grid[i][j] == 1 else -1))
            if j > 0:
                for diff in dp[i][j-1]:
                    dp[i][j].add(diff + (1 if grid[i][j] == 1 else -1))

            # 检查是否存在差值为 0 的路径
            if 0 in dp[i][j]:
                return True

    return False


Solution = create_solution(check_path_with_equal_zeros_and_ones)