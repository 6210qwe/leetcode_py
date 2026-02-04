# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1094
标题: Matrix Cells in Distance Order
难度: easy
链接: https://leetcode.cn/problems/matrix-cells-in-distance-order/
题目类型: 几何、数组、数学、矩阵、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1030. 距离顺序排列矩阵单元格 - 给定四个整数 rows , cols , rCenter 和 cCenter 。有一个 rows x cols 的矩阵，你在单元格上的坐标是 (rCenter, cCenter) 。 返回矩阵中的所有单元格的坐标，并按与 (rCenter, cCenter) 的 距离 从最小到最大的顺序排。你可以按 任何 满足此条件的顺序返回答案。 单元格(r1, c1) 和 (r2, c2) 之间的距离为|r1 - r2| + |c1 - c2|。 示例 1： 输入：rows = 1, cols = 2, rCenter = 0, cCenter = 0 输出：[[0,0],[0,1]] 解释：从 (r0, c0) 到其他单元格的距离为：[0,1] 示例 2： 输入：rows = 2, cols = 2, rCenter = 0, cCenter = 1 输出：[[0,1],[0,0],[1,1],[1,0]] 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2] [[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。 示例 3： 输入：rows = 2, cols = 3, rCenter = 1, cCenter = 2 输出：[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]] 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3] 其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。 提示： * 1 <= rows, cols <= 100 * 0 <= rCenter < rows * 0 <= cCenter < cols
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用曼哈顿距离对所有单元格进行排序。

算法步骤:
1. 生成所有单元格的坐标。
2. 计算每个单元格与中心点的曼哈顿距离。
3. 按照曼哈顿距离对单元格进行排序。

关键点:
- 使用列表推导式生成所有单元格的坐标。
- 使用 `sorted` 函数并自定义排序键来实现按曼哈顿距离排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(rows * cols * log(rows * cols))
空间复杂度: O(rows * cols)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def all_cells_distance_order(rows: int, cols: int, r_center: int, c_center: int) -> List[List[int]]:
    """
    返回矩阵中的所有单元格的坐标，并按与 (rCenter, cCenter) 的 距离 从最小到最大的顺序排。
    """
    # 生成所有单元格的坐标
    cells = [(r, c) for r in range(rows) for c in range(cols)]
    
    # 按照曼哈顿距离对单元格进行排序
    sorted_cells = sorted(cells, key=lambda cell: abs(cell[0] - r_center) + abs(cell[1] - c_center))
    
    return sorted_cells


Solution = create_solution(all_cells_distance_order)