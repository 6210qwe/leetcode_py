# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100354
标题: Best Line LCCI
难度: medium
链接: https://leetcode.cn/problems/best-line-lcci/
题目类型: 几何、数组、哈希表、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 16.14. 最佳直线 - 给定一个二维平面及平面上的 N 个点列表Points，其中第i个点的坐标为Points[i]=[Xi,Yi]。请找出一条直线，其通过的点的数目最多。 设穿过最多点的直线所穿过的全部点编号从小到大排序的列表为S，你仅需返回[S[0],S[1]]作为答案，若有多条直线穿过了相同数量的点，则选择S[0]值较小的直线返回，S[0]相同则选择S[1]值较小的直线返回。 示例： 输入： [[0,0],[1,1],[1,0],[2,0]] 输出： [0,2] 解释： 所求直线穿过的3个点的编号为[0,2,3] 提示： * 2 <= len(Points) <= 300 * len(Points[i]) = 2
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每条直线上的点的数量，并找到通过最多点的直线。

算法步骤:
1. 初始化一个哈希表来存储每条直线上的点的数量。
2. 遍历所有点对，计算每条直线的斜率和截距。
3. 将每条直线的斜率和截距作为键，点的索引作为值存储在哈希表中。
4. 找出通过最多点的直线，并返回对应的点的索引。

关键点:
- 使用浮点数表示斜率时，可能会遇到精度问题，因此使用分数表示斜率。
- 使用哈希表来高效地统计每条直线上的点的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是点的数量。需要遍历所有点对。
空间复杂度: O(n^2)，哈希表在最坏情况下可能存储所有点对。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from fractions import Fraction


def solution_function_name(points: List[List[int]]) -> List[int]:
    """
    函数式接口 - 找出通过最多点的直线，并返回对应的点的索引。
    """
    if not points or len(points) < 2:
        return []

    n = len(points)
    max_count = 0
    best_line = (0, 1)

    for i in range(n):
        line_count = {}
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2:
                slope = float('inf')
                intercept = x1
            else:
                slope = Fraction(y2 - y1, x2 - x1)
                intercept = y1 - slope * x1
            key = (slope, intercept)
            if key not in line_count:
                line_count[key] = []
            line_count[key].append(j)

            if len(line_count[key]) > max_count:
                max_count = len(line_count[key])
                best_line = (i, min(line_count[key]))

    return [best_line[0], best_line[1]]


Solution = create_solution(solution_function_name)