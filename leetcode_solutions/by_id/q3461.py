# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3461
标题: Find the Minimum Area to Cover All Ones I
难度: medium
链接: https://leetcode.cn/problems/find-the-minimum-area-to-cover-all-ones-i/
题目类型: 数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3195. 包含所有 1 的最小矩形面积 I - 给你一个二维 二进制 数组 grid。请你找出一个边在水平方向和竖直方向上、面积 最小 的矩形，并且满足 grid 中所有的 1 都在矩形的内部。 返回这个矩形可能的 最小 面积。 示例 1： 输入： grid = [[0,1,0],[1,0,1]] 输出： 6 解释： [https://assets.leetcode.com/uploads/2024/05/08/examplerect0.png] 这个最小矩形的高度为 2，宽度为 3，因此面积为 2 * 3 = 6。 示例 2： 输入： grid = [[0,0],[1,0]] 输出： 1 解释： [https://assets.leetcode.com/uploads/2024/05/08/examplerect1.png] 这个最小矩形的高度和宽度都是 1，因此面积为 1 * 1 = 1。 提示： * 1 <= grid.length, grid[i].length <= 1000 * grid[i][j] 是 0 或 1。 * 输入保证 grid 中至少有一个 1 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 找到所有 1 的最小边界框

算法步骤:
1. 初始化行和列的最小值和最大值为无穷大和负无穷大
2. 遍历整个网格，更新行和列的最小值和最大值
3. 计算边界框的宽度和高度，返回面积

关键点:
- 通过遍历一次网格找到所有 1 的边界
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是网格的行数和列数
空间复杂度: O(1)，只使用了常数级的额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_min_area_to_cover_ones(grid: List[List[int]]) -> int:
    """
    函数式接口 - 找到包含所有 1 的最小矩形面积
    """
    if not grid or not grid[0]:
        return 0

    min_row, max_row = float('inf'), float('-inf')
    min_col, max_col = float('inf'), float('-inf')

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                min_row = min(min_row, i)
                max_row = max(max_row, i)
                min_col = min(min_col, j)
                max_col = max(max_col, j)

    if min_row == float('inf'):
        return 0  # 没有 1 存在

    height = max_row - min_row + 1
    width = max_col - min_col + 1
    return height * width


Solution = create_solution(find_min_area_to_cover_ones)