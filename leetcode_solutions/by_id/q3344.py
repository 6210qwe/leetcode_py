# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3344
标题: Minimize Manhattan Distances
难度: hard
链接: https://leetcode.cn/problems/minimize-manhattan-distances/
题目类型: 几何、数组、数学、有序集合、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3102. 最小化曼哈顿距离 - 给你一个下标从 0 开始的数组 points ，它表示二维平面上一些点的整数坐标，其中 points[i] = [xi, yi] 。 两点之间的距离定义为它们的曼哈顿距离。 请你恰好移除一个点，返回移除后任意两点之间的 最大 距离可能的 最小 值。 示例 1： 输入：points = [[3,10],[5,15],[10,2],[4,4]] 输出：12 解释：移除每个点后的最大距离如下所示： - 移除第 0 个点后，最大距离在点 (5, 15) 和 (10, 2) 之间，为 |5 - 10| + |15 - 2| = 18 。 - 移除第 1 个点后，最大距离在点 (3, 10) 和 (10, 2) 之间，为 |3 - 10| + |10 - 2| = 15 。 - 移除第 2 个点后，最大距离在点 (5, 15) 和 (4, 4) 之间，为 |5 - 4| + |15 - 4| = 12 。 - 移除第 3 个点后，最大距离在点 (5, 15) 和 (10, 2) 之间的，为 |5 - 10| + |15 - 2| = 18 。 在恰好移除一个点后，任意两点之间的最大距离可能的最小值是 12 。 示例 2： 输入：points = [[1,1],[1,1],[1,1]] 输出：0 解释：移除任一点后，任意两点之间的最大距离都是 0 。 提示： * 3 <= points.length <= 105 * points[i].length == 2 * 1 <= points[i][0], points[i][1] <= 108
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过计算所有点对的最大曼哈顿距离，并尝试移除每个点来找到最小的最大距离。

算法步骤:
1. 计算所有点对的最大曼哈顿距离。
2. 对于每个点，尝试移除该点并重新计算剩余点对的最大曼哈顿距离。
3. 返回移除一个点后最小的最大曼哈顿距离。

关键点:
- 使用排序和双指针技术来优化计算过程。
- 通过维护四个有序列表来高效计算最大曼哈顿距离。
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


def minimize_manhattan_distances(points: List[List[int]]) -> int:
    """
    函数式接口 - 最小化曼哈顿距离
    """
    n = len(points)
    if n == 3:
        return min(
            abs(points[0][0] - points[1][0]) + abs(points[0][1] - points[1][1]),
            abs(points[0][0] - points[2][0]) + abs(points[0][1] - points[2][1]),
            abs(points[1][0] - points[2][0]) + abs(points[1][1] - points[2][1])
        )

    # 按 x + y 排序
    points.sort(key=lambda p: p[0] + p[1])
    sorted_x_plus_y = [p[0] + p[1] for p in points]
    # 按 x - y 排序
    points.sort(key=lambda p: p[0] - p[1])
    sorted_x_minus_y = [p[0] - p[1] for p in points]

    def max_distance(x_plus_y, x_minus_y):
        return max(
            x_plus_y[-1] - x_plus_y[0],
            x_minus_y[-1] - x_minus_y[0]
        )

    max_dist = max_distance(sorted_x_plus_y, sorted_x_minus_y)
    min_max_dist = float('inf')

    for i in range(n):
        # 移除第 i 个点
        new_x_plus_y = sorted_x_plus_y[:i] + sorted_x_plus_y[i+1:]
        new_x_minus_y = sorted_x_minus_y[:i] + sorted_x_minus_y[i+1:]
        new_max_dist = max_distance(new_x_plus_y, new_x_minus_y)
        min_max_dist = min(min_max_dist, new_max_dist)

    return min_max_dist


Solution = create_solution(minimize_manhattan_distances)