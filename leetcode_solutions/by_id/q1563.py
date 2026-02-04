# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1563
标题: Maximum Number of Darts Inside of a Circular Dartboard
难度: hard
链接: https://leetcode.cn/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/
题目类型: 几何、数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1453. 圆形靶内的最大飞镖数量 - Alice 向一面非常大的墙上掷出 n 支飞镖。给你一个数组 darts ，其中 darts[i] = [xi, yi] 表示 Alice 掷出的第 i 支飞镖落在墙上的位置。 Bob 知道墙上所有 n 支飞镖的位置。他想要往墙上放置一个半径为 r 的圆形靶。使 Alice 掷出的飞镖尽可能多地落在靶上。 给你整数 r ，请返回能够落在 任意 半径为 r 的圆形靶内或靶上的最大飞镖数。 示例 1 ： [https://assets.leetcode.com/uploads/2020/04/29/sample_1_1806.png] 输入：darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2 输出：4 解释：如果圆形靶的圆心为 (0,0) ，半径为 2 ，所有的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 4 。 示例 2 ： [https://assets.leetcode.com/uploads/2020/04/29/sample_2_1806.png] 输入：darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5 输出：5 解释：如果圆形靶的圆心为 (0,4) ，半径为 5 ，则除了 (7,8) 之外的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 5 。 提示： * 1 <= darts.length <= 100 * darts[i].length == 2 * -104 <= xi, yi <= 104 * darts 中的元素互不相同 * 1 <= r <= 5000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用几何方法计算两个点之间的中垂线，并检查每个可能的圆心是否能包含最多的飞镖。

算法步骤:
1. 对于每一对飞镖，计算它们之间的中垂线。
2. 对于每条中垂线，计算可能的圆心位置。
3. 检查每个可能的圆心位置，统计落在该圆心的圆内的飞镖数量。
4. 返回最大飞镖数量。

关键点:
- 使用复数表示点和向量，简化几何计算。
- 通过枚举所有可能的圆心位置，确保找到最优解。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^3)，其中 n 是飞镖的数量。需要枚举所有点对，并检查每个可能的圆心。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def num_points(darts: List[List[int]], r: int) -> int:
    def in_circle(center, radius, point):
        return (point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2 <= radius ** 2

    def get_circle_center(p1, p2, r):
        x1, y1 = p1
        x2, y2 = p2
        q = (x2 - x1) ** 2 + (y2 - y1) ** 2
        x3 = (x1 + x2) / 2
        y3 = (y1 + y2) / 2
        d = (r ** 2 - (q / 4)) / q
        if d < 0:
            return []
        sqrt_d = d ** 0.5
        cx1 = x3 - sqrt_d * (y2 - y1)
        cy1 = y3 + sqrt_d * (x2 - x1)
        cx2 = x3 + sqrt_d * (y2 - y1)
        cy2 = y3 - sqrt_d * (x2 - x1)
        return [(cx1, cy1), (cx2, cy2)]

    max_points = 0
    for i in range(len(darts)):
        for j in range(i + 1, len(darts)):
            centers = get_circle_center(darts[i], darts[j], r)
            for center in centers:
                count = sum(in_circle(center, r, dart) for dart in darts)
                max_points = max(max_points, count)

    # Check if all points can be inside a single circle
    if max_points == 0:
        for i in range(len(darts)):
            count = sum(in_circle(darts[i], r, dart) for dart in darts)
            max_points = max(max_points, count)

    return max_points

Solution = create_solution(num_points)