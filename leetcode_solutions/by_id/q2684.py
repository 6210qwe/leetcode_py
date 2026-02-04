# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2684
标题: Determine the Winner of a Bowling Game
难度: easy
链接: https://leetcode.cn/problems/determine-the-winner-of-a-bowling-game/
题目类型: 数组、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2660. 保龄球游戏的获胜者 - 给你两个下标从 0 开始的整数数组 player1 和 player2 ，分别表示玩家 1 和玩家 2 击中的瓶数。 保龄球比赛由 n 轮组成，每轮的瓶数恰好为 10 。 假设玩家在第 i 轮中击中 xi 个瓶子。玩家第 i 轮的价值为： * 如果玩家在该轮的前两轮的任何一轮中击中了 10 个瓶子，则为 2xi 。 * 否则，为 xi 。 玩家的得分是其 n 轮价值的总和。 返回 * 如果玩家 1 的得分高于玩家 2 的得分，则为 1 ； * 如果玩家 2 的得分高于玩家 1 的得分，则为 2 ； * 如果平局，则为 0 。 示例 1： 输入：player1 = [5,10,3,2], player2 = [6,5,7,3] 输出：1 解释： 玩家 1 的分数为 5 + 10 + 2*3 + 2*2 = 25。 玩家 2 的分数为 6 + 5 + 7 + 3 = 21。 示例 2： 输入：player1 = [3,5,7,6], player2 = [8,10,10,2] 输出：2 解释： 玩家 1 的分数为 3 + 5 + 7 + 6 = 21。 玩家 2 的分数为 8 + 10 + 2*10 + 2*2 = 42。 示例 3： 输入：player1 = [2,3], player2 = [4,1] 输出：0 解释： 玩家 1 的分数为 2 + 3 = 5。 玩家 2 的分数为 4 + 1 = 5。 示例 4： 输入：player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1] 输出：2 解释： 玩家 1 的分数为 1 + 1 + 1 + 10 + 2*10 + 2*10 + 2*10 = 73。 玩家 2 的分数为 is 10 + 2*10 + 2*10 + 2*10 + 2*1 + 2*1 + 1 = 75。 提示： * n == player1.length == player2.length * 1 <= n <= 1000 * 0 <= player1[i], player2[i] <= 10
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算每个玩家的得分，然后比较得分。

算法步骤:
1. 定义一个辅助函数 `calculate_score` 来计算单个玩家的得分。
2. 使用辅助函数计算两个玩家的得分。
3. 比较两个玩家的得分，返回结果。

关键点:
- 在计算得分时，需要考虑前两轮是否击中了 10 个瓶子。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def calculate_score(scores: List[int]) -> int:
    """
    计算单个玩家的得分。
    """
    score = 0
    last_ten_rounds = [False, False]
    
    for i in range(len(scores)):
        if last_ten_rounds[0] or last_ten_rounds[1]:
            score += 2 * scores[i]
        else:
            score += scores[i]
        
        # 更新前两轮是否击中 10 个瓶子的状态
        last_ten_rounds[0] = last_ten_rounds[1]
        last_ten_rounds[1] = (scores[i] == 10)
    
    return score


def solution_function_name(player1: List[int], player2: List[int]) -> int:
    """
    函数式接口 - 计算并比较两个玩家的得分，返回获胜者。
    """
    score1 = calculate_score(player1)
    score2 = calculate_score(player2)
    
    if score1 > score2:
        return 1
    elif score1 < score2:
        return 2
    else:
        return 0


Solution = create_solution(solution_function_name)