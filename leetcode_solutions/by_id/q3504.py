# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3504
标题: Minimum Moves to Get a Peaceful Board
难度: medium
链接: https://leetcode.cn/problems/minimum-moves-to-get-a-peaceful-board/
题目类型: 贪心、数组、计数排序、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3189. 得到一个和平棋盘的最少步骤 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过贪心算法和计数排序来最小化移动次数。

算法步骤:
1. 统计每种颜色的数量。
2. 通过计数排序将颜色按数量从多到少排序。
3. 依次放置颜色，确保相邻颜色不同，并计算移动次数。

关键点:
- 使用计数排序来优化时间复杂度。
- 通过贪心策略确保每次放置的颜色是最优选择。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + k log k)，其中 n 是棋盘长度，k 是颜色种类数。统计颜色数量为 O(n)，排序为 O(k log k)。
空间复杂度: O(k)，用于存储颜色的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_moves_to_peaceful_board(board: List[int]) -> int:
    """
    函数式接口 - 计算得到一个和平棋盘的最少步骤
    """
    # 统计每种颜色的数量
    color_count = {}
    for color in board:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    # 按数量从多到少排序
    sorted_colors = sorted(color_count.items(), key=lambda x: x[1], reverse=True)

    # 依次放置颜色，确保相邻颜色不同，并计算移动次数
    moves = 0
    prev_color = None
    for color, count in sorted_colors:
        while count > 0:
            if prev_color != color:
                prev_color = color
                count -= 1
            else:
                # 找到下一个可用的颜色
                for next_color, next_count in sorted_colors:
                    if next_color != color and next_count > 0:
                        prev_color = next_color
                        next_count -= 1
                        moves += 1
                        break
                count -= 1

    return moves


Solution = create_solution(min_moves_to_peaceful_board)