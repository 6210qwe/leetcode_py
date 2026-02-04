# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1233
标题: Number of Ships in a Rectangle
难度: hard
链接: https://leetcode.cn/problems/number-of-ships-in-a-rectangle/
题目类型: 数组、分治、交互
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1274. 矩形内船只的数目 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用分治法（四分法）来递归地划分矩形区域，并在每个子区域中检查是否存在船只。

算法步骤:
1. 定义一个递归函数 `countShips`，该函数接收四个参数：左下角坐标 (top, left) 和右上角坐标 (bottom, right)。
2. 如果当前矩形区域内没有船只，返回 0。
3. 如果当前矩形区域只有一个点，且该点有船只，返回 1。
4. 将当前矩形区域划分为四个子区域，递归计算每个子区域中的船只数量。
5. 返回所有子区域的船只数量之和。

关键点:
- 使用 Sea.hasShips 方法来判断当前矩形区域内是否有船只。
- 通过递归将大问题分解为小问题，逐步缩小搜索范围。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(max(top, bottom, left, right)))
空间复杂度: O(log(max(top, bottom, left, right))) - 递归调用栈的深度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Sea:
    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        # 假设这个方法是由 LeetCode 提供的
        pass


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def countShips(sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
    """
    递归地划分矩形区域，并在每个子区域中检查是否存在船只。
    """
    if not sea.hasShips(topRight, bottomLeft):
        return 0
    if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
        return 1
    
    mid_x = (topRight.x + bottomLeft.x) // 2
    mid_y = (topRight.y + bottomLeft.y) // 2
    
    # 分成四个子区域
    top_left = countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1))
    top_right = countShips(sea, topRight, Point(mid_x + 1, mid_y + 1))
    bottom_left = countShips(sea, Point(mid_x, mid_y), bottomLeft)
    bottom_right = countShips(sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))
    
    return top_left + top_right + bottom_left + bottom_right


Solution = create_solution(countShips)