# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3560
标题: Maximum Number of Moves to Kill All Pawns
难度: hard
链接: https://leetcode.cn/problems/maximum-number-of-moves-to-kill-all-pawns/
题目类型: 位运算、广度优先搜索、数组、数学、状态压缩、博弈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3283. 吃掉所有兵需要的最多移动次数 - 给你一个 50 x 50 的国际象棋棋盘，棋盘上有 一个 马和一些兵。给你两个整数 kx 和 ky ，其中 (kx, ky) 表示马所在的位置，同时还有一个二维数组 positions ，其中 positions[i] = [xi, yi] 表示第 i 个兵在棋盘上的位置。 Alice 和 Bob 玩一个回合制游戏，Alice 先手。玩家的一次操作中，可以执行以下操作： * 玩家选择一个仍然在棋盘上的兵，然后移动马，通过 最少 的 步数 吃掉这个兵。注意 ，玩家可以选择 任意 一个兵，不一定 要选择从马的位置出发 最少 移动步数的兵。 * 在马吃兵的过程中，马 可能 会经过一些其他兵的位置，但这些兵 不会 被吃掉。只有 选中的兵在这个回合中被吃掉。 Alice 的目标是 最大化 两名玩家的 总 移动次数，直到棋盘上不再存在兵，而 Bob 的目标是 最小化 总移动次数。 假设两名玩家都采用 最优 策略，请你返回可以达到的 最大 总移动次数。 在一次 移动 中，如下图所示，马有 8 个可以移动到的位置，每个移动位置都是沿着坐标轴的一个方向前进 2 格，然后沿着垂直的方向前进 1 格。 [https://assets.leetcode.com/uploads/2024/08/01/chess_knight.jpg] 示例 1： 输入：kx = 1, ky = 1, positions = [[0,0]] 输出：4 解释： [https://assets.leetcode.com/uploads/2024/08/16/gif3.gif] 马需要移动 4 步吃掉 (0, 0) 处的兵。 示例 2： 输入：kx = 0, ky = 2, positions = [[1,1],[2,2],[3,3]] 输出：8 解释： [https://assets.leetcode.com/uploads/2024/08/16/gif4.gif] * Alice 选择 (2, 2) 处的兵，移动马吃掉它需要 2 步：(0, 2) -> (1, 4) -> (2, 2) 。 * Bob 选择 (3, 3) 处的兵，移动马吃掉它需要 2 步：(2, 2) -> (4, 1) -> (3, 3) 。 * Alice 选择 (1, 1) 处的兵，移动马吃掉它需要 4 步：(3, 3) -> (4, 1) -> (2, 2) -> (0, 3) -> (1, 1) 。 示例 3： 输入：kx = 0, ky = 0, positions = [[1,2],[2,4]] 输出：3 解释： * Alice 选择 (2, 4) 处的兵，移动马吃掉它需要 2 步：(0, 0) -> (1, 2) -> (2, 4) 。注意，(1, 2) 处的兵不会被吃掉。 * Bob 选择 (1, 2) 处的兵，移动马吃掉它需要 1 步：(2, 4) -> (1, 2) 。 提示： * 0 <= kx, ky <= 49 * 1 <= positions.length <= 15 * positions[i].length == 2 * 0 <= positions[i][0], positions[i][1] <= 49 * positions[i] 两两互不相同。 * 输入保证对于所有 0 <= i < positions.length ，都有 positions[i] != [kx, ky] 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和状态压缩来解决这个问题。我们可以通过状态压缩来表示当前棋盘的状态，并使用动态规划来计算每一步的最大移动次数。

算法步骤:
1. 定义状态压缩的方式，用一个整数来表示当前棋盘的状态。
2. 初始化动态规划表 dp，dp[状态] 表示当前状态下，Alice 和 Bob 采取最优策略时的最大总移动次数。
3. 使用递归加记忆化搜索的方法来填充 dp 表。
4. 对于每一个状态，枚举所有可能的下一步，计算当前状态下的最大移动次数。
5. 返回初始状态下的最大移动次数。

关键点:
- 使用状态压缩来表示棋盘状态。
- 使用动态规划和记忆化搜索来计算每一步的最大移动次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n * n^2)，其中 n 是 positions 的长度。状态总数为 2^n，每个状态需要 O(n^2) 的时间来计算。
空间复杂度: O(2^n)，用于存储动态规划表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from functools import lru_cache

def get_state(positions: List[List[int]], kx: int, ky: int) -> int:
    state = 0
    for px, py in positions:
        if px == kx and py == ky:
            continue
        state |= 1 << (px * 50 + py)
    return state

@lru_cache(None)
def dp(state: int, kx: int, ky: int, positions: List[List[int]]) -> int:
    if state == 0:
        return 0
    
    max_moves = 0
    for i in range(len(positions)):
        px, py = positions[i]
        if (state & (1 << (px * 50 + py))) == 0:
            continue
        
        new_state = state ^ (1 << (px * 50 + py))
        moves = abs(kx - px) + abs(ky - py)
        next_kx, next_ky = px, py
        max_moves = max(max_moves, moves + dp(new_state, next_kx, next_ky, positions))
    
    return max_moves

def solution_function_name(kx: int, ky: int, positions: List[List[int]]) -> int:
    """
    函数式接口 - 计算吃掉所有兵需要的最多移动次数
    """
    state = get_state(positions, kx, ky)
    return dp(state, kx, ky, tuple(positions))

Solution = create_solution(solution_function_name)