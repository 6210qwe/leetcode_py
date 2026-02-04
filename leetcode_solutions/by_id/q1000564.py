# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000564
标题: 魔法棋盘
难度: hard
链接: https://leetcode.cn/problems/1ybDKD/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 76. 魔法棋盘 - 在大小为 `n * m` 的棋盘中，有两种不同的棋子：黑色，红色。当两颗颜色不同的棋子同时满足以下两种情况时，将会产生魔法共鸣： - 两颗异色棋子在同一行或者同一列 - 两颗异色棋子之间恰好只有一颗棋子 > 注：异色棋子之间可以有空位 由于棋盘上被施加了魔法禁制，棋盘上的部分格子变成问号。`chessboard[i][j]` 表示棋盘第 `i` 行 `j` 列的状态： - 若为 `.` ，表示当前格子确定为空 - 若为 `B` ，表示当前格子确定为 黑棋 - 若为 `R` ，表示当前格子确定为 红棋 - 若为 `?` ，表示当前格子待定 现在，探险家小扣的任务是确定所有问号位置的状态（留空/放黑棋/放红棋），使最终的棋盘上，任意两颗棋子间都 **无法** 产生共鸣。请返回可以满足上述条件的放置方案数量。 **示例1：** > 输入：`n = 3, m = 3, chessboard = ["..R","..B","?R?"]` > > 输出：`5` > > 解释：给定的棋盘如图： >![image.png](https://pic.leetcode.cn/1681714583-unbRox-image.png){:height=150px} > 所有符合题意的最终局面如图： >![image.png](https://pic.leetcode.cn/1681714596-beaOHK-image.png){:height=150px} **示例2：** > 输入：`n = 3, m = 3, chessboard = ["?R?","B?B","?R?"]` > > 输出：`105` **提示：** - `n == chessboard.length` - `m == chessboard[i].length` - `1 <= n*m <= 30` - `chessboard` 中仅包含 `"."、"B"、"R"、"?"`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法来尝试所有可能的填充方案，并检查每种方案是否满足条件。

算法步骤:
1. 初始化一个计数器 `count` 用于记录有效方案的数量。
2. 定义一个递归函数 `backtrack`，该函数接受当前处理的行索引 `row` 和当前棋盘状态 `board`。
3. 如果 `row` 达到棋盘的高度 `n`，则检查当前棋盘是否满足条件，如果满足则增加计数器 `count`。
4. 否则，遍历当前行的所有列，对于每个列：
   - 如果当前格子是 `?`，则尝试填入 `B` 和 `R`，并递归调用 `backtrack` 处理下一行。
   - 如果当前格子不是 `?`，则直接递归调用 `backtrack` 处理下一行。
5. 在递归过程中，使用辅助函数 `is_valid` 检查当前棋盘是否满足条件。

关键点:
- 使用回溯法穷举所有可能的填充方案。
- 在每次递归调用后恢复棋盘状态，以避免影响后续的递归调用。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(3^(n*m))，其中 n 是棋盘的高度，m 是棋盘的宽度。最坏情况下，每个问号位置都有三种选择（留空、放黑棋、放红棋）。
空间复杂度: O(n*m)，递归调用栈的深度最多为 n*m。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(n: int, m: int, chessboard: List[str]) -> int:
    def is_valid(board: List[str]) -> bool:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'B':
                    # 检查同一行和同一列
                    for k in range(j + 1, m):
                        if board[i][k] == 'R' and (k - j == 2 or all(board[i][l] == '.' for l in range(j + 1, k))):
                            return False
                    for k in range(i + 1, n):
                        if board[k][j] == 'R' and (k - i == 2 or all(board[l][j] == '.' for l in range(i + 1, k))):
                            return False
                elif board[i][j] == 'R':
                    # 检查同一行和同一列
                    for k in range(j + 1, m):
                        if board[i][k] == 'B' and (k - j == 2 or all(board[i][l] == '.' for l in range(j + 1, k))):
                            return False
                    for k in range(i + 1, n):
                        if board[k][j] == 'B' and (k - i == 2 or all(board[l][j] == '.' for l in range(i + 1, k))):
                            return False
        return True

    def backtrack(row: int, board: List[str]):
        nonlocal count
        if row == n:
            if is_valid(board):
                count += 1
            return
        for col in range(m):
            if board[row][col] == '?':
                board[row] = board[row][:col] + 'B' + board[row][col + 1:]
                backtrack(row + 1, board)
                board[row] = board[row][:col] + 'R' + board[row][col + 1:]
                backtrack(row + 1, board)
                board[row] = board[row][:col] + '.' + board[row][col + 1:]
                backtrack(row + 1, board)
            else:
                backtrack(row + 1, board)

    count = 0
    backtrack(0, chessboard)
    return count


Solution = create_solution(solution_function_name)