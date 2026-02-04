# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3868
标题: Find Maximum Area of a Triangle
难度: medium
链接: https://leetcode.cn/problems/find-maximum-area-of-a-triangle/
题目类型: 贪心、几何、数组、哈希表、数学、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3588. 找到最大三角形面积 - 给你一个二维数组 coords，大小为 n x 2，表示一个无限笛卡尔平面上 n 个点的坐标。 找出一个 最大 三角形的 两倍 面积，其中三角形的三个顶点来自 coords 中的任意三个点，并且该三角形至少有一条边与 x 轴或 y 轴平行。严格地说，如果该三角形的最大面积为 A，则返回 2 * A。 如果不存在这样的三角形，返回 -1。 注意，三角形的面积 不能 为零。 示例 1： 输入： coords = [[1,1],[1,2],[3,2],[3,3]] 输出： 2 解释： [https://assets.leetcode.com/uploads/2025/04/19/image-20250420010047-1.png] 图中的三角形的底边为 1，高为 2。因此，它的面积为 1/2 * 底边 * 高 = 1。 示例 2： 输入： coords = [[1,1],[2,2],[3,3]] 输出： -1 解释： 唯一可能的三角形的顶点是 (1, 1)、(2, 2) 和 (3, 3)。它的任意边都不与 x 轴或 y 轴平行。 提示： * 1 <= n == coords.length <= 105 * 1 <= coords[i][0], coords[i][1] <= 106 * 所有 coords[i] 都是 唯一 的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表分别记录每个 x 坐标和 y 坐标对应的点，然后枚举所有可能的垂直和平行于 x 轴或 y 轴的边，计算最大面积。

算法步骤:
1. 使用两个字典分别记录每个 x 坐标和 y 坐标对应的点。
2. 枚举所有可能的垂直和平行于 x 轴或 y 轴的边，计算最大面积。
3. 返回最大面积的两倍，如果没有找到符合条件的三角形，返回 -1。

关键点:
- 使用哈希表高效地记录和查找点。
- 通过枚举所有可能的边来确保找到最大面积。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_max_area_of_triangle(coords: List[List[int]]) -> int:
    """
    函数式接口 - 找到最大三角形面积
    """
    if len(coords) < 3:
        return -1

    # 记录每个 x 坐标和 y 坐标对应的点
    x_coords = {}
    y_coords = {}
    for x, y in coords:
        if x not in x_coords:
            x_coords[x] = []
        if y not in y_coords:
            y_coords[y] = []
        x_coords[x].append(y)
        y_coords[y].append(x)

    max_area = 0

    # 枚举所有可能的垂直于 x 轴的边
    for x, ys in x_coords.items():
        for i in range(len(ys)):
            for j in range(i + 1, len(ys)):
                y1, y2 = ys[i], ys[j]
                base = abs(y1 - y2)
                for other_x in x_coords:
                    if other_x != x:
                        height = abs(other_x - x)
                        area = base * height
                        max_area = max(max_area, area)

    # 枚举所有可能的垂直于 y 轴的边
    for y, xs in y_coords.items():
        for i in range(len(xs)):
            for j in range(i + 1, len(xs)):
                x1, x2 = xs[i], xs[j]
                base = abs(x1 - x2)
                for other_y in y_coords:
                    if other_y != y:
                        height = abs(other_y - y)
                        area = base * height
                        max_area = max(max_area, area)

    return 2 * max_area if max_area > 0 else -1


Solution = create_solution(find_max_area_of_triangle)