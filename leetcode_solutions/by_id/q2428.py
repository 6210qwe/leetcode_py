# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2428
标题: Equal Row and Column Pairs
难度: medium
链接: https://leetcode.cn/problems/equal-row-and-column-pairs/
题目类型: 数组、哈希表、矩阵、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2352. 相等行列对 - 给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。 如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。 示例 1： [https://assets.leetcode.com/uploads/2022/06/01/ex1.jpg] 输入：grid = [[3,2,1],[1,7,6],[2,7,7]] 输出：1 解释：存在一对相等行列对： - (第 2 行，第 1 列)：[2,7,7] 示例 2： [https://assets.leetcode.com/uploads/2022/06/01/ex2.jpg] 输入：grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]] 输出：3 解释：存在三对相等行列对： - (第 0 行，第 0 列)：[3,1,2,2] - (第 2 行, 第 2 列)：[2,4,2,2] - (第 3 行, 第 2 列)：[2,4,2,2] 提示： * n == grid.length == grid[i].length * 1 <= n <= 200 * 1 <= grid[i][j] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储每行的出现次数，然后遍历每一列，检查该列是否与某一行相等。

算法步骤:
1. 初始化一个哈希表 `row_count`，用于存储每行的字符串表示及其出现次数。
2. 遍历每一行，将行转换为字符串并存储在 `row_count` 中。
3. 初始化结果计数器 `count` 为 0。
4. 遍历每一列，将列转换为字符串，并在 `row_count` 中查找该字符串，将其出现次数累加到 `count` 中。
5. 返回 `count` 作为结果。

关键点:
- 使用哈希表存储每行的字符串表示及其出现次数，可以快速查找和计数。
- 将行和列转换为字符串表示，方便比较。
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


def equal_row_and_column_pairs(grid: List[List[int]]) -> int:
    """
    函数式接口 - 返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目
    """
    n = len(grid)
    row_count = {}
    
    # 存储每行的字符串表示及其出现次数
    for row in grid:
        row_str = tuple(row)
        if row_str in row_count:
            row_count[row_str] += 1
        else:
            row_count[row_str] = 1
    
    count = 0
    
    # 遍历每一列，检查该列是否与某一行相等
    for col in range(n):
        col_str = tuple(grid[row][col] for row in range(n))
        if col_str in row_count:
            count += row_count[col_str]
    
    return count


Solution = create_solution(equal_row_and_column_pairs)