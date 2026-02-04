# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1134
标题: Shortest Distance to Target Color
难度: medium
链接: https://leetcode.cn/problems/shortest-distance-to-target-color/
题目类型: 数组、二分查找、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1182. 与目标颜色间的最短距离 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个字典分别记录每个颜色从左到右和从右到左的最近位置，然后通过查询这两个字典来找到最短距离。

算法步骤:
1. 初始化两个字典 `left` 和 `right`，分别记录每个颜色从左到右和从右到左的最近位置。
2. 遍历数组，更新 `left` 字典。
3. 反向遍历数组，更新 `right` 字典。
4. 对于每个查询，计算 `left` 和 `right` 字典中对应颜色的位置，并取最小值。

关键点:
- 使用两个字典分别记录每个颜色的最近位置，可以快速查询并计算最短距离。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q)，其中 n 是数组长度，q 是查询的数量。遍历数组的时间复杂度是 O(n)，处理每个查询的时间复杂度是 O(1)。
空间复杂度: O(n)，需要额外的空间来存储 `left` 和 `right` 字典。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def shortest_distance_color(colors: List[int], queries: List[List[int]]) -> List[int]:
    """
    函数式接口 - 计算与目标颜色间的最短距离
    """
    n = len(colors)
    left = {}
    right = {}

    # 从左到右遍历，记录每个颜色的最近位置
    for i in range(n):
        if colors[i] not in left:
            left[colors[i]] = [i]
        else:
            left[colors[i]].append(i)

    # 从右到左遍历，记录每个颜色的最近位置
    for i in range(n - 1, -1, -1):
        if colors[i] not in right:
            right[colors[i]] = [i]
        else:
            right[colors[i]].append(i)

    result = []
    for index, color in queries:
        if color not in left:
            result.append(-1)
            continue

        left_pos = None
        right_pos = None

        # 二分查找找到左边最近的颜色位置
        left_idx = bisect.bisect_left(left[color], index)
        if left_idx < len(left[color]):
            right_pos = left[color][left_idx]
        if left_idx > 0:
            left_pos = left[color][left_idx - 1]

        # 二分查找找到右边最近的颜色位置
        right_idx = bisect.bisect_right(right[color], index) - 1
        if right_idx >= 0:
            right_pos = right[color][right_idx]
        if right_idx < len(right[color]) - 1:
            left_pos = right[color][right_idx + 1]

        if left_pos is None and right_pos is None:
            result.append(-1)
        elif left_pos is None:
            result.append(abs(index - right_pos))
        elif right_pos is None:
            result.append(abs(index - left_pos))
        else:
            result.append(min(abs(index - left_pos), abs(index - right_pos)))

    return result


Solution = create_solution(shortest_distance_color)