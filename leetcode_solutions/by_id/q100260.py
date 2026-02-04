# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100260
标题: Intersection LCCI
难度: hard
链接: https://leetcode.cn/problems/intersection-lcci/
题目类型: 几何、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 16.03. 交点 - 给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。 要求浮点型误差不超过10^-6。若有多个交点（线段重叠）则返回 X 值最小的点，X 坐标相同则返回 Y 值最小的点。 示例 1： 输入： line1 = {0, 0}, {1, 0} line2 = {1, 1}, {0, -1} 输出： {0.5, 0} 示例 2： 输入： line1 = {0, 0}, {3, 3} line2 = {1, 1}, {2, 2} 输出： {1, 1} 示例 3： 输入： line1 = {0, 0}, {1, 1} line2 = {1, 0}, {2, 1} 输出： {}，两条线段没有交点 提示： * 坐标绝对值不会超过 2^7 * 输入的坐标均是有效的二维坐标
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用向量叉乘判断线段是否相交，并通过参数方程求解交点。

算法步骤:
1. 计算线段的方向向量。
2. 使用向量叉乘判断线段是否相交。
3. 如果相交，通过参数方程求解交点。

关键点:
- 使用向量叉乘判断线段是否相交。
- 通过参数方程求解交点。
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


def on_segment(p, q, r):
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
        q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    return False

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def do_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False

def find_intersection(p1, q1, p2, q2):
    if not do_intersect(p1, q1, p2, q2):
        return []

    xdiff = (p1[0] - q1[0], p2[0] - q2[0])
    ydiff = (p1[1] - q1[1], p2[1] - q2[1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return []

    d = (det(p1, q1), det(p2, q2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    return [x, y]

def solution_function_name(line1: List[List[int]], line2: List[List[int]]) -> List[float]:
    """
    函数式接口 - 求解两条线段的交点
    """
    p1, q1 = line1
    p2, q2 = line2
    return find_intersection(p1, q1, p2, q2)

Solution = create_solution(solution_function_name)