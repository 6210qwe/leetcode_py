# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100353
标题: Bisect Squares LCCI
难度: medium
链接: https://leetcode.cn/problems/bisect-squares-lcci/
题目类型: 几何、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 16.13. 平分正方形 - 给定两个正方形及一个二维平面。请找出将这两个正方形分割成两半的一条直线。假设正方形顶边和底边与 x 轴平行。 每个正方形的数据square包含3个数值，正方形的左下顶点坐标[X,Y] = [square[0],square[1]]，以及正方形的边长square[2]。所求直线穿过两个正方形会形成4个交点，请返回4个交点形成线段的两端点坐标（两个端点即为4个交点中距离最远的2个点，这2个点所连成的线段一定会穿过另外2个交点）。2个端点坐标[X1,Y1]和[X2,Y2]的返回格式为{X1,Y1,X2,Y2}，要求若X1 != X2，需保证X1 < X2，否则需保证Y1 <= Y2。 若同时有多条直线满足要求，则选择斜率最大的一条计算并返回（与Y轴平行的直线视为斜率无穷大）。 示例： 输入： square1 = {-1, -1, 2} square2 = {0, -1, 2} 输出： {-1,0,2,0} 解释： 直线 y = 0 能将两个正方形同时分为等面积的两部分，返回的两线段端点为[-1,0]和[2,0] 提示： * square.length == 3 * square[2] > 0
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过计算两个正方形的中心点，找到平分两个正方形的直线。这条直线要么是水平线，要么是垂直线，或者斜率为正或负。

算法步骤:
1. 计算两个正方形的中心点。
2. 根据中心点的位置关系，确定平分直线的方向。
3. 计算平分直线与两个正方形的交点。
4. 返回距离最远的两个交点作为结果。

关键点:
- 中心点的计算。
- 交点的计算。
- 选择斜率最大的直线。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def bisect_squares(square1: List[int], square2: List[int]) -> List[int]:
    """
    函数式接口 - 找到平分两个正方形的直线，并返回四个交点中最远的两个点。
    """
    # 计算两个正方形的中心点
    center1 = (square1[0] + square1[2] / 2, square1[1] + square1[2] / 2)
    center2 = (square2[0] + square2[2] / 2, square2[1] + square2[2] / 2)

    # 判断平分直线的方向
    if center1[1] == center2[1]:
        # 水平线
        y = center1[1]
        x1 = min(square1[0], square2[0])
        x2 = max(square1[0] + square1[2], square2[0] + square2[2])
        return [x1, y, x2, y]
    elif center1[0] == center2[0]:
        # 垂直线
        x = center1[0]
        y1 = min(square1[1], square2[1])
        y2 = max(square1[1] + square1[2], square2[1] + square2[2])
        return [x, y1, x, y2]
    else:
        # 斜率为正或负
        slope = (center2[1] - center1[1]) / (center2[0] - center1[0])
        intercept = center1[1] - slope * center1[0]

        def intersect(x1, y1, x2, y2):
            if slope == 0:
                return (intercept, y1) if x1 <= intercept <= x2 else None
            if slope == float('inf'):
                return (x1, intercept) if y1 <= intercept <= y2 else None
            x_intersect = (y1 - intercept) / slope
            if x1 <= x_intersect <= x2:
                return (x_intersect, y1)
            y_intersect = slope * x1 + intercept
            if y1 <= y_intersect <= y2:
                return (x1, y_intersect)
            return None

        points = []
        for square in [square1, square2]:
            x1, y1, side = square
            x2, y2 = x1 + side, y1 + side
            for p in [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]:
                point = intersect(*p, *p)
                if point:
                    points.append(point)

        # 选择距离最远的两个点
        points.sort(key=lambda p: (p[0], p[1]))
        return [points[0][0], points[0][1], points[-1][0], points[-1][1]]


Solution = create_solution(bisect_squares)