# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1888
标题: Find Nearest Point That Has the Same X or Y Coordinate
难度: easy
链接: https://leetcode.cn/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1779. 找到最近的有相同 X 或 Y 坐标的点 - 给你两个整数 x 和 y ，表示你在一个笛卡尔坐标系下的 (x, y) 处。同时，在同一个坐标系下给你一个数组 points ，其中 points[i] = [ai, bi] 表示在 (ai, bi) 处有一个点。当一个点与你所在的位置有相同的 x 坐标或者相同的 y 坐标时，我们称这个点是 有效的 。 请返回距离你当前位置 曼哈顿距离 最近的 有效 点的下标（下标从 0 开始）。如果有多个最近的有效点，请返回下标 最小 的一个。如果没有有效点，请返回 -1 。 两个点 (x1, y1) 和 (x2, y2) 之间的 曼哈顿距离 为 abs(x1 - x2) + abs(y1 - y2) 。 示例 1： 输入：x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]] 输出：2 解释：所有点中，[3,1]，[2,4] 和 [4,4] 是有效点。有效点中，[2,4] 和 [4,4] 距离你当前位置的曼哈顿距离最小，都为 1 。[2,4] 的下标最小，所以返回 2 。 示例 2： 输入：x = 3, y = 4, points = [[3,4]] 输出：0 提示：答案可以与你当前所在位置坐标相同。 示例 3： 输入：x = 3, y = 4, points = [[2,3]] 输出：-1 解释：没有 有效点。 提示： * 1 <= points.length <= 104 * points[i].length == 2 * 1 <= x, y, ai, bi <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 遍历所有点，找到与给定点有相同 x 或 y 坐标的点，并记录最小曼哈顿距离及其索引。

算法步骤:
1. 初始化最小距离 `min_distance` 为无穷大，索引 `result_index` 为 -1。
2. 遍历所有点，对于每个点：
   - 如果该点的 x 或 y 坐标与给定点相同，则计算其曼哈顿距离。
   - 如果该距离小于当前最小距离，则更新最小距离和索引。
   - 如果该距离等于当前最小距离且索引更小，则更新索引。
3. 返回结果索引。

关键点:
- 只需遍历一次所有点，时间复杂度为 O(n)。
- 使用变量记录最小距离和索引，空间复杂度为 O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_nearest_point(x: int, y: int, points: List[List[int]]) -> int:
    """
    找到最近的有相同 X 或 Y 坐标的点
    """
    min_distance = float('inf')
    result_index = -1
    
    for i, (px, py) in enumerate(points):
        if px == x or py == y:
            distance = abs(px - x) + abs(py - y)
            if distance < min_distance:
                min_distance = distance
                result_index = i
            elif distance == min_distance and i < result_index:
                result_index = i
    
    return result_index


Solution = create_solution(find_nearest_point)