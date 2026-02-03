# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1501
标题: Circle and Rectangle Overlapping
难度: medium
链接: https://leetcode.cn/problems/circle-and-rectangle-overlapping/
题目类型: 几何、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1401. 圆和矩形是否有重叠 - 给你一个以 (radius, xCenter, yCenter) 表示的圆和一个与坐标轴平行的矩形 (x1, y1, x2, y2) ，其中 (x1, y1) 是矩形左下角的坐标，而 (x2, y2) 是右上角的坐标。 如果圆和矩形有重叠的部分，请你返回 true ，否则返回 false 。 换句话说，请你检测是否 存在 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。 示例 1 ： [https://assets.leetcode.com/uploads/2020/02/20/sample_4_1728.png] 输入：radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1 输出：true 解释：圆和矩形存在公共点 (1,0) 。 示例 2 ： 输入：radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1 输出：false 示例 3 ： [https://assets.leetcode.com/uploads/2020/02/20/sample_2_1728.png] 输入：radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1 输出：true 提示： * 1 <= radius <= 2000 * -104 <= xCenter, yCenter <= 104 * -104 <= x1 < x2 <= 104 * -104 <= y1 < y2 <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
