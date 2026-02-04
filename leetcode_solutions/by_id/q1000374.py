# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000374
标题: 无限棋局
难度: hard
链接: https://leetcode.cn/problems/fsa7oZ/
题目类型: 数组、数学、枚举、博弈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 48. 无限棋局 - 小力正在通过残局练习来备战「力扣挑战赛」中的「五子棋」项目，他想请你能帮他预测当前残局的输赢情况。棋盘中的棋子分布信息记录于二维数组 `pieces` 中，其中 `pieces[i] = [x,y,color]` 表示第 `i` 枚棋子的横坐标为 `x`，纵坐标为 `y`，棋子颜色为 `color`(`0` 表示黑棋，`1` 表示白棋)。假如黑棋先行，并且黑棋和白棋都按最优策略落子，请你求出当前棋局在三步（按 **黑、白、黑** 的落子顺序）之内的输赢情况（三步之内先构成同行、列或对角线连续同颜色的至少 5 颗即为获胜）： - 黑棋胜, 请返回 `"Black"` - 白棋胜, 请返回 `"White"` - 仍无胜者, 请返回 `"None"` **注意：** - 和传统的五子棋项目不同，「力扣挑战赛」中的「五子棋」项目 **不存在边界限制**，即可在 **任意位置** 落子； - 黑棋和白棋均按 3 步内的输赢情况进行最优策略的选择 - 测试数据保证所给棋局目前无胜者； - 测试数据保证不会存在坐标一样的棋子。 **示例 1：** > 输入： > `pieces = [[0,0,1],[1,1,1],[2,2,0]]` > > 输出：`"None"` > > 解释：无论黑、白棋以何种方式落子，三步以内都不会产生胜者。 **示例 2：** > 输入： > `pieces = [[1,2,1],[1,4,1],[1,5,1],[2,1,0],[2,3,0],[2,4,0],[3,2,1],[3,4,0],[4,2,1],[5,2,1]]` > > 输出：`"Black"` > > 解释：三步之内黑棋必胜，以下是一种可能的落子情况： >![902b87df29998b1c181146c8fdb3a4b6.gif](https://pic.leetcode.cn/1629800639-KabOfY-902b87df29998b1c181146c8fdb3a4b6.gif){:width="300px"} **提示：** - `0 <= pieces.length <= 1000` - `pieces[i].length = 3` - `-10^9 <= pieces[i][0], pieces[i][1] <=10^9` - `0 <= pieces[i][2] <=1`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 检查当前棋盘是否有已经连成5个相同颜色的棋子。
2. 模拟黑棋和白棋的下一步落子，检查是否能形成5个相同颜色的棋子。
3. 如果黑棋能在两步内获胜，则返回 "Black"。
4. 如果白棋能在一步内获胜，则返回 "White"。
5. 如果以上条件都不满足，则返回 "None"。

算法步骤:
1. 使用字典记录每行、每列、每条对角线上的棋子数量。
2. 检查当前棋盘是否有已经连成5个相同颜色的棋子。
3. 模拟黑棋和白棋的下一步落子，更新字典并检查是否能形成5个相同颜色的棋子。
4. 根据模拟结果返回相应的结果。

关键点:
- 使用字典高效地记录和更新每行、每列、每条对角线上的棋子数量。
- 通过模拟落子来判断胜负。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是 pieces 的长度。最坏情况下需要遍历所有可能的落子位置。
空间复杂度: O(n)，使用字典记录每行、每列、每条对角线上的棋子数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(pieces: List[List[int]]) -> str:
    """
    函数式接口 - 实现最优解法
    """
    def check_winner(board, color):
        for key, count in board.items():
            if count[color] >= 5:
                return True
        return False

    def update_board(board, x, y, color):
        board[(x, 'r')][color] += 1
        board[(y, 'c')][color] += 1
        board[(x - y, 'd1')][color] += 1
        board[(x + y, 'd2')][color] += 1

    def remove_board(board, x, y, color):
        board[(x, 'r')][color] -= 1
        board[(y, 'c')][color] -= 1
        board[(x - y, 'd1')][color] -= 1
        board[(x + y, 'd2')][color] -= 1

    board = {}
    for x, y, color in pieces:
        if (x, 'r') not in board:
            board[(x, 'r')] = {0: 0, 1: 0}
        if (y, 'c') not in board:
            board[(y, 'c')] = {0: 0, 1: 0}
        if (x - y, 'd1') not in board:
            board[(x - y, 'd1')] = {0: 0, 1: 0}
        if (x + y, 'd2') not in board:
            board[(x + y, 'd2')] = {0: 0, 1: 0}
        update_board(board, x, y, color)

    if check_winner(board, 0):
        return "Black"
    if check_winner(board, 1):
        return "White"

    for x, y, _ in pieces:
        for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            for i in range(1, 5):
                nx, ny = x + dx * i, y + dy * i
                if (nx, ny, 0) not in pieces and (nx, ny, 1) not in pieces:
                    update_board(board, nx, ny, 0)
                    if check_winner(board, 0):
                        return "Black"
                    remove_board(board, nx, ny, 0)
                    update_board(board, nx, ny, 1)
                    if check_winner(board, 1):
                        return "White"
                    remove_board(board, nx, ny, 1)

    return "None"


Solution = create_solution(solution_function_name)