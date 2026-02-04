# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 612
标题: Shortest Distance in a Plane
难度: medium
链接: https://leetcode.cn/problems/shortest-distance-in-a-plane/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
612. 平面上的最近距离 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用分治法（Divide and Conquer）来解决平面上的最近点对问题。具体来说，使用平面扫描算法（Plane Sweep Algorithm）。

算法步骤:
1. 将所有点按照 x 坐标排序。
2. 递归地将点集分成两部分，分别求出每部分的最近点对。
3. 合并时，找到跨越中线的最近点对，并更新全局最小距离。

关键点:
- 分治法可以有效地减少比较次数。
- 使用平面扫描算法可以在合并阶段优化时间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def closest_pair(points: List[List[int]]) -> float:
    def distance(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def closest_util(strip, d_min, point_p):
        strip.sort(key=lambda point: point[1])
        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if (strip[j][1] - strip[i][1]) ** 2 >= d_min:
                    break
                d = distance(strip[i], strip[j])
                if d < d_min:
                    d_min = d
                    point_p[0] = strip[i]
                    point_p[1] = strip[j]
        return d_min

    def closest_recursive(points, n):
        if n <= 3:
            min_val = float('inf')
            for i in range(n):
                for j in range(i + 1, n):
                    if distance(points[i], points[j]) < min_val:
                        min_val = distance(points[i], points[j])
                        point_p[0] = points[i]
                        point_p[1] = points[j]
            return min_val

        mid = n // 2
        mid_point = points[mid]
        dl = closest_recursive(points[:mid], mid)
        dr = closest_recursive(points[mid:], n - mid)
        d = min(dl, dr)

        strip = [point for point in points if (point[0] - mid_point[0]) ** 2 < d]
        return closest_util(strip, d, point_p)

    points.sort(key=lambda point: point[0])
    point_p = [None, None]
    d_min = closest_recursive(points, len(points))
    return d_min ** 0.5


Solution = create_solution(closest_pair)