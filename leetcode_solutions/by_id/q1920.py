# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1920
标题: Determine Color of a Chessboard Square
难度: easy
链接: https://leetcode.cn/problems/determine-color-of-a-chessboard-square/
题目类型: 数学、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1812. 判断国际象棋棋盘中一个格子的颜色 - 给你一个坐标 coordinates ，它是一个字符串，表示国际象棋棋盘中一个格子的坐标。下图是国际象棋棋盘示意图。 [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/04/03/chessboard.png] 如果所给格子的颜色是白色，请你返回 true，如果是黑色，请返回 false 。 给定坐标一定代表国际象棋棋盘上一个存在的格子。坐标第一个字符是字母，第二个字符是数字。 示例 1： 输入：coordinates = "a1" 输出：false 解释：如上图棋盘所示，"a1" 坐标的格子是黑色的，所以返回 false 。 示例 2： 输入：coordinates = "h3" 输出：true 解释：如上图棋盘所示，"h3" 坐标的格子是白色的，所以返回 true 。 示例 3： 输入：coordinates = "c7" 输出：false 提示： * coordinates.length == 2 * 'a' <= coordinates[0] <= 'h' * '1' <= coordinates[1] <= '8'
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过计算行列坐标的奇偶性来判断格子的颜色。

算法步骤:
1. 将字母坐标转换为数字（a -> 0, b -> 1, ... h -> 7）。
2. 计算行和列的和。
3. 如果行和列的和为偶数，则格子为黑色；否则为白色。

关键点:
- 使用 ASCII 码进行字母到数字的转换。
- 利用奇偶性判断颜色。
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


def solution_function_name(coordinates: str) -> bool:
    """
    函数式接口 - 判断国际象棋棋盘中一个格子的颜色
    """
    # 将字母坐标转换为数字
    col = ord(coordinates[0]) - ord('a')
    row = int(coordinates[1]) - 1
    
    # 计算行和列的和
    sum_coords = col + row
    
    # 判断格子的颜色
    return sum_coords % 2 == 0


Solution = create_solution(solution_function_name)