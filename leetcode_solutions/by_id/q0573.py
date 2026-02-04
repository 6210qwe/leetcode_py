# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 573
标题: Squirrel Simulation
难度: medium
链接: https://leetcode.cn/problems/squirrel-simulation/
题目类型: 数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
573. 松鼠模拟 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算松鼠从起点到坚果再到树的最短路径，并找到一个坚果使得松鼠先吃这个坚果再回到树的总距离最小。

算法步骤:
1. 计算每个坚果到树的距离。
2. 计算松鼠从起点到每个坚果再到树的总距离。
3. 找到一个坚果，使得松鼠先吃这个坚果再回到树的总距离最小。

关键点:
- 使用曼哈顿距离计算两点之间的距离。
- 通过比较不同坚果的选择，找到最优解。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_distance_to_tree(height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
    def manhattan_distance(p1: List[int], p2: List[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    # 计算每个坚果到树的距离
    nut_to_tree_distances = [manhattan_distance(nut, tree) for nut in nuts]

    # 计算松鼠从起点到每个坚果再到树的总距离
    min_distance = float('inf')
    for i, nut in enumerate(nuts):
        distance_to_nut = manhattan_distance(squirrel, nut)
        total_distance = (distance_to_nut - nut_to_tree_distances[i]) + 2 * sum(nut_to_tree_distances)
        min_distance = min(min_distance, total_distance)

    return min_distance


Solution = create_solution(min_distance_to_tree)