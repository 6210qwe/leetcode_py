# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3553
标题: Check if Two Chessboard Squares Have the Same Color
难度: easy
链接: https://leetcode.cn/problems/check-if-two-chessboard-squares-have-the-same-color/
题目类型: 数学、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3274. 检查棋盘方格颜色是否相同 - 给你两个字符串 coordinate1 和 coordinate2，代表 8 x 8 国际象棋棋盘上的两个方格的坐标。 以下是棋盘的参考图。 [https://assets.leetcode.com/uploads/2024/07/17/screenshot-2021-02-20-at-22159-pm.png] 如果这两个方格颜色相同，返回 true，否则返回 false。 坐标总是表示有效的棋盘方格。坐标的格式总是先字母（表示列），再数字（表示行）。 示例 1： 输入： coordinate1 = "a1", coordinate2 = "c3" 输出： true 解释： 两个方格均为黑色。 示例 2： 输入： coordinate1 = "a1", coordinate2 = "h3" 输出： false 解释： 方格 "a1" 是黑色，而 "h3" 是白色。 提示： * coordinate1.length == coordinate2.length == 2 * 'a' <= coordinate1[0], coordinate2[0] <= 'h' * '1' <= coordinate1[1], coordinate2[1] <= '8'
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过计算两个坐标的行列和来判断它们的颜色是否相同。

算法步骤:
1. 将每个坐标的列字符转换为对应的数字。
2. 计算每个坐标的行列和。
3. 判断两个坐标的行列和的奇偶性是否相同，如果相同则颜色相同，否则不同。

关键点:
- 使用 ASCII 码将字母转换为数字。
- 通过奇偶性判断颜色。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(coordinate1: str, coordinate2: str) -> bool:
    """
    函数式接口 - 检查两个棋盘方格颜色是否相同
    """
    # 将列字符转换为数字
    col1 = ord(coordinate1[0]) - ord('a')
    col2 = ord(coordinate2[0]) - ord('a')
    
    # 获取行数字
    row1 = int(coordinate1[1])
    row2 = int(coordinate2[1])
    
    # 计算行列和
    sum1 = col1 + row1
    sum2 = col2 + row2
    
    # 判断奇偶性是否相同
    return sum1 % 2 == sum2 % 2


Solution = create_solution(solution_function_name)