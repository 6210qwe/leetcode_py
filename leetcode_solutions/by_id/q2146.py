# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2146
标题: Check if Word Can Be Placed In Crossword
难度: medium
链接: https://leetcode.cn/problems/check-if-word-can-be-placed-in-crossword/
题目类型: 数组、枚举、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2018. 判断单词是否能放入填字游戏内 - 给你一个 m x n 的矩阵 board ，它代表一个填字游戏 当前 的状态。填字游戏格子中包含小写英文字母（已填入的单词），表示 空 格的 ' ' 和表示 障碍 格子的 '#' 。 如果满足以下条件，那么我们可以 水平 （从左到右 或者 从右到左）或 竖直 （从上到下 或者 从下到上）填入一个单词： * 该单词不占据任何 '#' 对应的格子。 * 每个字母对应的格子要么是 ' ' （空格）要么与 board 中已有字母 匹配 。 * 如果单词是 水平 放置的，那么该单词左边和右边 相邻 格子不能为 ' ' 或小写英文字母。 * 如果单词是 竖直 放置的，那么该单词上边和下边 相邻 格子不能为 ' ' 或小写英文字母。 给你一个字符串 word ，如果 word 可以被放入 board 中，请你返回 true ，否则请返回 false 。 示例 1： [https://assets.leetcode.com/uploads/2021/09/18/crossword-1.png] 输入：board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc" 输出：true 解释：单词 "abc" 可以如上图放置（从上往下）。 示例 2： [https://assets.leetcode.com/uploads/2021/09/18/c2.png] 输入：board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac" 输出：false 解释：无法放置单词，因为放置该单词后上方或者下方相邻格会有空格。 示例 3： [https://assets.leetcode.com/uploads/2021/09/18/crossword-2.png] 输入：board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca" 输出：true 解释：单词 "ca" 可以如上图放置（从右到左）。 提示： * m == board.length * n == board[i].length * 1 <= m * n <= 2 * 105 * board[i][j] 可能为 ' ' ，'#' 或者一个小写英文字母。 * 1 <= word.length <= max(m, n) * word 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 检查每个可能的位置，尝试水平和竖直方向放置单词，并检查是否满足条件。

算法步骤:
1. 遍历整个 board，找到所有可能的起始位置。
2. 对于每个起始位置，尝试水平和竖直方向放置单词。
3. 检查放置后的单词是否满足边界条件和字符匹配条件。

关键点:
- 使用两个辅助函数分别检查水平和竖直方向的放置。
- 在检查时，需要确保单词的每个字符都匹配或为空格，并且单词的两端不能是空格或字母。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * (m + n))，其中 m 和 n 分别是 board 的行数和列数。最坏情况下，每个位置都需要检查水平和竖直方向。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_place_word(board: List[List[str]], word: str) -> bool:
    def check_horizontal(row: int, col: int) -> bool:
        for i in range(len(word)):
            if col + i >= len(board[0]) or (board[row][col + i] != ' ' and board[row][col + i] != word[i]):
                return False
        return (col == 0 or board[row][col - 1] == '#') and (col + len(word) == len(board[0]) or board[row][col + len(word)] == '#')

    def check_vertical(row: int, col: int) -> bool:
        for i in range(len(word)):
            if row + i >= len(board) or (board[row + i][col] != ' ' and board[row + i][col] != word[i]):
                return False
        return (row == 0 or board[row - 1][col] == '#') and (row + len(word) == len(board) or board[row + len(word)][col] == '#')

    def check_reverse_horizontal(row: int, col: int) -> bool:
        for i in range(len(word)):
            if col - i < 0 or (board[row][col - i] != ' ' and board[row][col - i] != word[i]):
                return False
        return (col == len(board[0]) - 1 or board[row][col + 1] == '#') and (col - len(word) == -1 or board[row][col - len(word) - 1] == '#')

    def check_reverse_vertical(row: int, col: int) -> bool:
        for i in range(len(word)):
            if row - i < 0 or (board[row - i][col] != ' ' and board[row - i][col] != word[i]):
                return False
        return (row == len(board) - 1 or board[row + 1][col] == '#') and (row - len(word) == -1 or board[row - len(word) - 1][col] == '#')

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ' ' or board[i][j] == word[0]:
                if check_horizontal(i, j) or check_vertical(i, j) or check_reverse_horizontal(i, j) or check_reverse_vertical(i, j):
                    return True
    return False


Solution = create_solution(can_place_word)