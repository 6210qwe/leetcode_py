# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1239
标题: Largest 1-Bordered Square
难度: medium
链接: https://leetcode.cn/problems/largest-1-bordered-square/
题目类型: 数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1139. 最大的以 1 为边界的正方形 - 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。 示例 1： 输入：grid = [[1,1,1],[1,0,1],[1,1,1]] 输出：9 示例 2： 输入：grid = [[1,1,0,0]] 输出：1 提示： * 1 <= grid.length <= 100 * 1 <= grid[0].length <= 100 * grid[i][j] 为 0 或 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来计算每个位置的左边和上边连续 1 的长度，然后通过这些信息来找到最大的以 1 为边界的正方形。

算法步骤:
1. 初始化两个二维数组 `left` 和 `up`，分别记录每个位置左边和上边连续 1 的长度。
2. 遍历整个网格，填充 `left` 和 `up` 数组。
3. 对于每个位置 (i, j)，如果 grid[i][j] 为 1，检查以 (i, j) 为右下角的最大正方形的边长，更新最大边长。
4. 返回最大边长的平方。

关键点:
- 使用 `left` 和 `up` 数组来快速计算每个位置的左边和上边连续 1 的长度。
- 通过遍历和比较来找到最大的以 1 为边界的正方形。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是网格的行数，m 是网格的列数。
空间复杂度: O(n * m)，用于存储 `left` 和 `up` 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def largest1BorderedSquare(grid: List[List[int]]) -> int:
    """
    函数式接口 - 找出边界全部由 1 组成的最大正方形子网格，并返回该子网格中的元素数量。
    """
    if not grid or not grid[0]:
        return 0

    n, m = len(grid), len(grid[0])
    left = [[0] * m for _ in range(n)]
    up = [[0] * m for _ in range(n)]
    max_side = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                left[i][j] = (left[i][j - 1] + 1) if j > 0 else 1
                up[i][j] = (up[i - 1][j] + 1) if i > 0 else 1

                min_len = min(left[i][j], up[i][j])
                while min_len > max_side:
                    if up[i][j - min_len + 1] >= min_len and left[i - min_len + 1][j] >= min_len:
                        max_side = min_len
                        break
                    min_len -= 1

    return max_side ** 2


Solution = create_solution(largest1BorderedSquare)