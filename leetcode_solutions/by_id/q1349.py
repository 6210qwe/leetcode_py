# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1349
标题: Check If It Is a Straight Line
难度: easy
链接: https://leetcode.cn/problems/check-if-it-is-a-straight-line/
题目类型: 几何、数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1232. 缀点成线 - 给定一个整数数组 coordinates ，其中 coordinates[i] = [x, y] ， [x, y] 表示横坐标为 x、纵坐标为 y 的点。请你来判断，这些点是否在该坐标系中属于同一条直线上。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/10/19/untitled-diagram-2.jpg] 输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]] 输出：true 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/10/19/untitled-diagram-1.jpg] 输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]] 输出：false 提示： * 2 <= coordinates.length <= 1000 * coordinates[i].length == 2 * -104 <= coordinates[i][0], coordinates[i][1] <= 104 * coordinates 中不含重复的点
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用斜率公式判断所有点是否在同一条直线上。

算法步骤:
1. 计算前两个点之间的斜率。
2. 遍历剩余的点，检查它们与第一个点之间的斜率是否相同。
3. 如果所有点的斜率都相同，则这些点在同一条直线上。

关键点:
- 使用斜率公式 (y2 - y1) / (x2 - x1)，为了避免除法运算中的精度问题，可以使用乘法形式 (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1) 进行比较。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是坐标点的数量。我们需要遍历所有点来检查斜率。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def check_straight_line(coordinates: List[List[int]]) -> bool:
    """
    判断给定的坐标点是否在同一条直线上。
    """
    if len(coordinates) < 2:
        return False

    # 计算前两个点之间的斜率
    (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
    for i in range(2, len(coordinates)):
        (x, y) = coordinates[i]
        # 检查当前点与第一个点之间的斜率是否与前两个点的斜率相同
        if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):
            return False

    return True


Solution = create_solution(check_straight_line)