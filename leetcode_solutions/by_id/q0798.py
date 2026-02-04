# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 798
标题: Transform to Chessboard
难度: hard
链接: https://leetcode.cn/problems/transform-to-chessboard/
题目类型: 位运算、数组、数学、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
782. 变为棋盘 - 一个 n x n 的二维网络 board 仅由 0 和 1 组成 。每次移动，你能交换任意两列或是两行的位置。 返回 将这个矩阵变为 “棋盘” 所需的最小移动次数 。如果不存在可行的变换，输出 -1。 “棋盘” 是指任意一格的上下左右四个方向的值均与本身不同的矩阵。 示例 1: [https://assets.leetcode.com/uploads/2021/06/29/chessboard1-grid.jpg] 输入: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]] 输出: 2 解释:一种可行的变换方式如下，从左到右： 第一次移动交换了第一列和第二列。 第二次移动交换了第二行和第三行。 示例 2: [https://assets.leetcode.com/uploads/2021/06/29/chessboard2-grid.jpg] 输入: board = [[0, 1], [1, 0]] 输出: 0 解释: 注意左上角的格值为0时也是合法的棋盘，也是合法的棋盘. 示例 3: [https://assets.leetcode.com/uploads/2021/06/29/chessboard3-grid.jpg] 输入: board = [[1, 0], [1, 0]] 输出: -1 解释: 任意的变换都不能使这个输入变为合法的棋盘。 提示： * n == board.length * n == board[i].length * 2 <= n <= 30 * board[i][j] 将只包含 0或 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 棋盘的每一行和每一列都必须是交替的0和1。我们可以通过检查每一行和每一列的模式来确定是否可以将矩阵转换为棋盘。

算法步骤:
1. 检查每一行和每一列的模式是否符合棋盘的要求。
2. 计算需要交换的行数和列数。
3. 确保行和列的模式一致，并且满足棋盘的要求。

关键点:
- 每一行和每一列的模式必须是交替的0和1。
- 通过计算行和列的差异来确定最小交换次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def moves_to_chessboard(board: List[List[int]]) -> int:
    n = len(board)
    
    # 检查每一行和每一列的模式是否符合棋盘的要求
    def is_valid_pattern(pattern):
        count_0 = pattern.count(0)
        count_1 = pattern.count(1)
        return abs(count_0 - count_1) <= 1 and (count_0 == count_1 or n % 2 == 1)
    
    # 获取每一行和每一列的模式
    row_patterns = [''.join(map(str, row)) for row in board]
    col_patterns = [''.join(map(str, col)) for col in zip(*board)]
    
    # 检查行和列的模式是否有效
    if not all(is_valid_pattern(row) for row in row_patterns) or not all(is_valid_pattern(col) for col in col_patterns):
        return -1
    
    # 计算需要交换的行数和列数
    def count_swaps(pattern):
        count = 0
        for i in range(n):
            if (pattern[i] != '0' and i % 2 == 0) or (pattern[i] != '1' and i % 2 == 1):
                count += 1
        return min(count, n - count) // 2
    
    row_swaps = count_swaps(row_patterns[0])
    col_swaps = count_swaps(col_patterns[0])
    
    return row_swaps + col_swaps

Solution = create_solution(moves_to_chessboard)