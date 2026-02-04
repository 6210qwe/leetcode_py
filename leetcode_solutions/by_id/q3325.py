# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3325
标题: Find the Largest Area of Square Inside Two Rectangles
难度: medium
链接: https://leetcode.cn/problems/find-the-largest-area-of-square-inside-two-rectangles/
题目类型: 几何、数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3047. 求交集区域内的最大正方形面积 - 在二维平面上存在 n 个矩形。给你两个下标从 0 开始的二维整数数组 bottomLeft 和 topRight，两个数组的大小都是 n x 2 ，其中 bottomLeft[i] 和 topRight[i] 分别代表第 i 个矩形的 左下角 和 右上角 坐标。 我们定义 向右 的方向为 x 轴正半轴（x 坐标增加），向左 的方向为 x 轴负半轴（x 坐标减少）。同样地，定义 向上 的方向为 y 轴正半轴（y 坐标增加），向下 的方向为 y 轴负半轴（y 坐标减少）。 你可以选择一个区域，该区域由两个矩形的 交集 形成。你需要找出能够放入该区域 内 的 最大 正方形面积，并选择最优解。 返回能够放入交集区域的正方形的 最大 可能面积，如果矩形之间不存在任何交集区域，则返回 0。 示例 1： [https://assets.leetcode.com/uploads/2024/01/05/example12.png] 输入：bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]] 输出：1 解释：边长为 1 的正方形可以放入矩形 0 和矩形 1 的交集区域，或矩形 1 和矩形 2 的交集区域。因此最大面积是边长 * 边长，即 1 * 1 = 1。 可以证明，边长更大的正方形无法放入任何交集区域。 示例 2： [https://assets.leetcode.com/uploads/2024/01/04/rectanglesexample2.png] 输入：bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]] 输出：1 解释：边长为 1 的正方形可以放入矩形 0 和矩形 1，矩形 1 和矩形 2，或所有三个矩形的交集区域。因此最大面积是边长 * 边长，即 1 * 1 = 1。 可以证明，边长更大的正方形无法放入任何交集区域。 请注意，区域可以由多于两个矩形的交集构成。 示例 3： [https://assets.leetcode.com/uploads/2024/01/04/rectanglesexample3.png] 输入：bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]] 输出：0 解释：不存在相交的矩形，因此，返回 0 。 提示： * n == bottomLeft.length == topRight.length * 2 <= n <= 103 * bottomLeft[i].length == topRight[i].length == 2 * 1 <= bottomLeft[i][0], bottomLeft[i][1] <= 107 * 1 <= topRight[i][0], topRight[i][1] <= 107 * bottomLeft[i][0] < topRight[i][0] * bottomLeft[i][1] < topRight[i][1]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 计算每对矩形的交集区域。
- 对于每个交集区域，找到能够放入的最大正方形面积。

算法步骤:
1. 定义一个函数 `get_intersection` 来计算两个矩形的交集区域。
2. 遍历所有矩形对，计算它们的交集区域。
3. 对于每个交集区域，计算能够放入的最大正方形面积。
4. 返回所有交集区域中最大的正方形面积。

关键点:
- 交集区域的计算需要考虑矩形的边界。
- 最大正方形的边长取决于交集区域的最小维度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - 需要遍历所有矩形对。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def get_intersection(rect1, rect2):
    """计算两个矩形的交集区域"""
    x1 = max(rect1[0][0], rect2[0][0])
    y1 = max(rect1[0][1], rect2[0][1])
    x2 = min(rect1[1][0], rect2[1][0])
    y2 = min(rect1[1][1], rect2[1][1])
    if x1 < x2 and y1 < y2:
        return (x1, y1), (x2, y2)
    return None

def solution_function_name(bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
    """
    函数式接口 - 求交集区域内的最大正方形面积
    """
    n = len(bottomLeft)
    max_area = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            intersection = get_intersection((bottomLeft[i], topRight[i]), (bottomLeft[j], topRight[j]))
            if intersection:
                width = intersection[1][0] - intersection[0][0]
                height = intersection[1][1] - intersection[0][1]
                side = min(width, height)
                max_area = max(max_area, side * side)
    
    return max_area

Solution = create_solution(solution_function_name)