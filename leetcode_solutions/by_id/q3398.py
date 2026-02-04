# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3398
标题: Make a Square with the Same Color
难度: easy
链接: https://leetcode.cn/problems/make-a-square-with-the-same-color/
题目类型: 数组、枚举、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3127. 构造相同颜色的正方形 - 给你一个二维 3 x 3 的矩阵 grid ，每个格子都是一个字符，要么是 'B' ，要么是 'W' 。字符 'W' 表示白色，字符 'B' 表示黑色。 你的任务是改变 至多一个 格子的颜色，使得矩阵中存在一个 2 x 2 颜色完全相同的正方形。 如果可以得到一个相同颜色的 2 x 2 正方形，那么返回 true ，否则返回 false 。 示例 1： 输入：grid = [["B","W","B"],["B","W","W"],["B","W","B"]] 输出：true 解释： 修改 grid[0][2] 的颜色，可以满足要求。 示例 2： 输入：grid = [["B","W","B"],["W","B","W"],["B","W","B"]] 输出：false 解释： 只改变一个格子颜色无法满足要求。 示例 3： 输入：grid = [["B","W","B"],["B","W","W"],["B","W","W"]] 输出：true 解释： grid 已经包含一个 2 x 2 颜色相同的正方形了。 提示： * grid.length == 3 * grid[i].length == 3 * grid[i][j] 要么是 'W' ，要么是 'B' 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 检查所有可能的 2x2 子矩阵，并尝试通过改变一个格子的颜色来使其成为同色正方形。

算法步骤:
1. 遍历所有可能的 2x2 子矩阵。
2. 对于每个 2x2 子矩阵，检查是否已经是同色正方形。
3. 如果不是同色正方形，检查是否可以通过改变一个格子的颜色使其成为同色正方形。

关键点:
- 通过遍历所有 2x2 子矩阵并检查每个子矩阵的状态来解决问题。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 固定大小的矩阵，最多有 4 个 2x2 子矩阵需要检查。
空间复杂度: O(1) - 不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_make_square(grid: List[List[str]]) -> bool:
    """
    检查是否可以通过改变一个格子的颜色来构造一个 2x2 同色正方形。
    """
    def is_same_color(subgrid: List[List[str]], color: str) -> bool:
        for row in subgrid:
            for cell in row:
                if cell != color:
                    return False
        return True

    def can_change_one_cell_to_same_color(subgrid: List[List[str]]) -> bool:
        count_w = sum(cell == 'W' for row in subgrid for cell in row)
        count_b = sum(cell == 'B' for row in subgrid for cell in row)
        return count_w == 3 or count_b == 3

    for i in range(2):
        for j in range(2):
            subgrid = [row[j:j+2] for row in grid[i:i+2]]
            if is_same_color(subgrid, 'W') or is_same_color(subgrid, 'B'):
                return True
            if can_change_one_cell_to_same_color(subgrid):
                return True
    return False


Solution = create_solution(can_make_square)