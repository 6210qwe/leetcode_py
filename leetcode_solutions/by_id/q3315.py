# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3315
标题: Maximum Number of Intersections on the Chart
难度: hard
链接: https://leetcode.cn/problems/maximum-number-of-intersections-on-the-chart/
题目类型: 树状数组、几何、数组、哈希表、数学、排序、扫描线
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3009. 折线图上的最大交点数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用扫描线算法结合树状数组来统计交点数量。

算法步骤:
1. 将所有折线段的起点和终点按 x 坐标排序。
2. 使用一个字典记录每个 x 坐标上的折线段变化情况（增加或减少）。
3. 遍历排序后的 x 坐标，使用树状数组更新当前 y 坐标的折线段数量，并计算交点数量。

关键点:
- 使用树状数组来高效地更新和查询当前 y 坐标的折线段数量。
- 通过扫描线算法处理折线段的变化。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是折线段的数量。排序操作的时间复杂度为 O(n log n)，树状数组的更新和查询操作为 O(log n)。
空间复杂度: O(n)，用于存储折线段的变化情况和树状数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import bisect

class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

def solution_function_name(lines: List[List[int]]) -> int:
    """
    函数式接口 - 计算折线图上的最大交点数量
    """
    events = []
    for i, (x1, y1, x2, y2) in enumerate(lines):
        events.append((x1, 'start', y1, y2, i))
        events.append((x2, 'end', y1, y2, i))
    events.sort()

    active_lines = {}
    bit = BIT(10**6)
    max_intersections = 0

    for x, event_type, y1, y2, i in events:
        if event_type == 'start':
            if y1 not in active_lines:
                active_lines[y1] = set()
            active_lines[y1].add(i)
            bit.update(y1, 1)
        else:
            active_lines[y1].remove(i)
            if not active_lines[y1]:
                del active_lines[y1]
            bit.update(y1, -1)

        current_intersections = 0
        for y in active_lines:
            if y1 < y < y2 or y2 < y < y1:
                current_intersections += bit.query(y) - bit.query(y - 1)
        max_intersections = max(max_intersections, current_intersections)

    return max_intersections

Solution = create_solution(solution_function_name)