# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 870
标题: Magic Squares In Grid
难度: medium
链接: https://leetcode.cn/problems/magic-squares-in-grid/
题目类型: 数组、哈希表、数学、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
840. 矩阵中的幻方 - 3 x 3 的幻方是一个填充有 从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。 给定一个由整数组成的row x col 的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？ 注意：虽然幻方只能包含 1 到 9 的数字，但 grid 可以包含最多15的数字。 示例 1： [https://assets.leetcode.com/uploads/2020/09/11/magic_main.jpg] 输入: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2] 输出: 1 解释: 下面的子矩阵是一个 3 x 3 的幻方： [https://assets.leetcode.com/uploads/2020/09/11/magic_valid.jpg] 而这一个不是： [https://assets.leetcode.com/uploads/2020/09/11/magic_invalid.jpg] 总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。 示例 2: 输入: grid = [[8]] 输出: 0 提示: * row == grid.length * col == grid[i].length * 1 <= row, col <= 10 * 0 <= grid[i][j] <= 15
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 检查每个 3x3 子矩阵是否为幻方。

算法步骤:
1. 遍历网格中的每个 3x3 子矩阵。
2. 对于每个子矩阵，检查其是否包含 1 到 9 的所有数字且每行、每列和对角线的和均为 15。
3. 如果满足条件，则计数器加一。

关键点:
- 使用集合来检查子矩阵是否包含 1 到 9 的所有数字。
- 计算每行、每列和对角线的和，确保它们都等于 15。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 和 m 分别是网格的行数和列数。我们需要遍历每个 3x3 子矩阵。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_magic_square(subgrid: List[List[int]]) -> bool:
    # 检查子矩阵是否包含 1 到 9 的所有数字
    if set(sum(subgrid, [])) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        return False
    
    # 检查每行、每列和对角线的和是否为 15
    for i in range(3):
        if sum(subgrid[i]) != 15 or sum(subgrid[j][i] for j in range(3)) != 15:
            return False
    if subgrid[0][0] + subgrid[1][1] + subgrid[2][2] != 15 or subgrid[0][2] + subgrid[1][1] + subgrid[2][0] != 15:
        return False
    
    return True


def solution_function_name(grid: List[List[int]]) -> int:
    """
    函数式接口 - 统计网格中 3x3 幻方的数量
    """
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    for i in range(rows - 2):
        for j in range(cols - 2):
            subgrid = [grid[i + k][j:j + 3] for k in range(3)]
            if is_magic_square(subgrid):
                count += 1
    
    return count


Solution = create_solution(solution_function_name)