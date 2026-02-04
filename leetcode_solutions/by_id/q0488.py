# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 488
标题: Zuma Game
难度: hard
链接: https://leetcode.cn/problems/zuma-game/
题目类型: 栈、广度优先搜索、记忆化搜索、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
488. 祖玛游戏 - 你正在参与祖玛游戏的一个变种。 在这个祖玛游戏变体中，桌面上有 一排 彩球，每个球的颜色可能是：红色 'R'、黄色 'Y'、蓝色 'B'、绿色 'G' 或白色 'W' 。你的手中也有一些彩球。 你的目标是 清空 桌面上所有的球。每一回合： * 从你手上的彩球中选出 任意一颗 ，然后将其插入桌面上那一排球中：两球之间或这一排球的任一端。 * 接着，如果有出现 三个或者三个以上 且 颜色相同 的球相连的话，就把它们移除掉。 * 如果这种移除操作同样导致出现三个或者三个以上且颜色相同的球相连，则可以继续移除这些球，直到不再满足移除条件。 * 如果桌面上所有球都被移除，则认为你赢得本场游戏。 * 重复这个过程，直到你赢了游戏或者手中没有更多的球。 给你一个字符串 board ，表示桌面上最开始的那排球。另给你一个字符串 hand ，表示手里的彩球。请你按上述操作步骤移除掉桌上所有球，计算并返回所需的 最少 球数。如果不能移除桌上所有的球，返回 -1 。 示例 1： 输入：board = "WRRBBW", hand = "RB" 输出：-1 解释：无法移除桌面上的所有球。可以得到的最好局面是： - 插入一个 'R' ，使桌面变为 WRRRBBW 。WRRRBBW -> WBBW - 插入一个 'B' ，使桌面变为 WBBBW 。WBBBW -> WW 桌面上还剩着球，没有其他球可以插入。 示例 2： 输入：board = "WWRRBBWW", hand = "WRBRW" 输出：2 解释：要想清空桌面上的球，可以按下述步骤： - 插入一个 'R' ，使桌面变为 WWRRRBBWW 。WWRRRBBWW -> WWBBWW - 插入一个 'B' ，使桌面变为 WWBBBWW 。WWBBBWW -> WWWW -> empty 只需从手中出 2 个球就可以清空桌面。 示例 3： 输入：board = "G", hand = "GGGGG" 输出：2 解释：要想清空桌面上的球，可以按下述步骤： - 插入一个 'G' ，使桌面变为 GG 。 - 插入一个 'G' ，使桌面变为 GGG 。GGG -> empty 只需从手中出 2 个球就可以清空桌面。 示例 4： 输入：board = "RBYYBBRRB", hand = "YRBGB" 输出：3 解释：要想清空桌面上的球，可以按下述步骤： - 插入一个 'Y' ，使桌面变为 RBYYYBBRRB 。RBYYYBBRRB -> RBBBRRB -> RRRB -> B - 插入一个 'B' ，使桌面变为 BB 。 - 插入一个 'B' ，使桌面变为 BBB 。BBB -> empty 只需从手中出 3 个球就可以清空桌面。 提示： * 1 <= board.length <= 16 * 1 <= hand.length <= 5 * board 和 hand 由字符 'R'、'Y'、'B'、'G' 和 'W' 组成 * 桌面上一开始的球中，不会有三个及三个以上颜色相同且连着的球
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）结合记忆化搜索来找到最少的球数。

算法步骤:
1. 初始化队列和访问集合，将初始状态 (board, hand) 加入队列。
2. 对于队列中的每个状态，尝试在每个可能的位置插入每种颜色的球，并检查是否可以移除连续的球。
3. 如果可以移除球，更新新的 board 和 hand，并将新状态加入队列。
4. 如果 board 为空，返回当前使用的球数。
5. 如果队列为空且未找到解，返回 -1。

关键点:
- 使用记忆化搜索避免重复计算。
- 优化时间和空间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(5^n) - 其中 n 是 board 的长度，因为每次插入球最多有 5 种选择。
空间复杂度: O(5^n) - 记忆化搜索的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from collections import deque
from functools import lru_cache

def zuma_game(board: str, hand: str) -> int:
    """
    函数式接口 - 计算移除桌上所有球所需的最少球数
    
    实现思路:
    使用广度优先搜索（BFS）结合记忆化搜索来找到最少的球数。
    
    Args:
        board: 桌面上的球序列
        hand: 手中的球序列
        
    Returns:
        最少需要的球数，如果无法移除所有球则返回 -1
        
    Example:
        >>> zuma_game("WRRBBW", "RB")
        -1
        >>> zuma_game("WWRRBBWW", "WRBRW")
        2
    """
    # 将 hand 转换为计数字典
    hand_count = {c: hand.count(c) for c in set(hand)}
    
    @lru_cache(None)
    def remove_consecutive_balls(s: str) -> str:
        """移除连续的三个或更多相同颜色的球"""
        stack = []
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == 3:
                    stack.pop()
        return ''.join(char * count for char, count in stack)
    
    @lru_cache(None)
    def bfs() -> int:
        queue = deque([(board, hand_count)])
        visited = set([(board, tuple(sorted(hand_count.items())))])

        steps = 0
        while queue:
            for _ in range(len(queue)):
                current_board, current_hand = queue.popleft()

                if not current_board:
                    return steps

                for i in range(len(current_board) + 1):
                    for color, count in current_hand.items():
                        if count > 0:
                            new_board = current_board[:i] + color + current_board[i:]
                            new_board = remove_consecutive_balls(new_board)
                            new_hand = current_hand.copy()
                            new_hand[color] -= 1
                            new_state = (new_board, tuple(sorted(new_hand.items())))

                            if new_state not in visited:
                                visited.add(new_state)
                                queue.append((new_board, new_hand))

            steps += 1
        return -1

    return bfs()

# 自动生成Solution类（无需手动编写）
Solution = create_solution(zuma_game)