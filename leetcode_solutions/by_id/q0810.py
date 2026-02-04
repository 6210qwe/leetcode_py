# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 810
标题: Valid Tic-Tac-Toe State
难度: medium
链接: https://leetcode.cn/problems/valid-tic-tac-toe-state/
题目类型: 数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
794. 有效的井字游戏 - 给你一个字符串数组 board 表示井字游戏的棋盘。当且仅当在井字游戏过程中，棋盘有可能达到 board 所显示的状态时，才返回 true 。 井字游戏的棋盘是一个 3 x 3 数组，由字符 ' '，'X' 和 'O' 组成。字符 ' ' 代表一个空位。 以下是井字游戏的规则： * 玩家轮流将字符放入空位（' '）中。 * 玩家 1 总是放字符 'X' ，而玩家 2 总是放字符 'O' 。 * 'X' 和 'O' 只允许放置在空位中，不允许对已放有字符的位置进行填充。 * 当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。 * 当所有位置非空时，也算为游戏结束。 * 如果游戏结束，玩家不允许再放置字符。 示例 1： [https://assets.leetcode.com/uploads/2021/05/15/tictactoe1-grid.jpg] 输入：board = ["O "," "," "] 输出：false 解释：玩家 1 总是放字符 "X" 。 示例 2： [https://assets.leetcode.com/uploads/2021/05/15/tictactoe2-grid.jpg] 输入：board = ["XOX"," X "," "] 输出：false 解释：玩家应该轮流放字符。 示例 3: [https://assets.leetcode.com/uploads/2021/05/15/tictactoe4-grid.jpg] 输入：board = ["XOX","O O","XOX"] 输出：true 提示： * board.length == 3 * board[i].length == 3 * board[i][j] 为 'X'、'O' 或 ' '
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 检查棋盘状态是否符合井字游戏的规则。

算法步骤:
1. 计算 'X' 和 'O' 的数量。
2. 检查 'X' 和 'O' 的数量是否符合规则（'X' 的数量必须等于 'O' 的数量或比 'O' 多一个）。
3. 检查是否有三个连续的 'X' 或 'O' 在行、列或对角线上。
4. 根据上述检查结果判断棋盘状态是否有效。

关键点:
- 'X' 的数量必须等于 'O' 的数量或比 'O' 多一个。
- 如果 'X' 赢了，'X' 的数量必须比 'O' 多一个。
- 如果 'O' 赢了，'X' 的数量必须等于 'O' 的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 固定大小的棋盘，检查次数固定。
空间复杂度: O(1) - 使用常数级额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def valid_tic_tac_toe(board: List[str]) -> bool:
    """
    检查给定的井字游戏棋盘是否有效。
    """
    # 计算 'X' 和 'O' 的数量
    count_x = sum(row.count('X') for row in board)
    count_o = sum(row.count('O') for row in board)

    # 检查 'X' 和 'O' 的数量是否符合规则
    if count_x != count_o and count_x != count_o + 1:
        return False

    # 检查是否有三个连续的 'X' 或 'O' 在行、列或对角线上
    def check_winner(player: str) -> bool:
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):  # 检查行
                return True
            if all(board[j][i] == player for j in range(3)):  # 检查列
                return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):  # 检查对角线
            return True
        return False

    # 根据上述检查结果判断棋盘状态是否有效
    if check_winner('X') and count_x != count_o + 1:
        return False
    if check_winner('O') and count_x != count_o:
        return False

    return True


Solution = create_solution(valid_tic_tac_toe)