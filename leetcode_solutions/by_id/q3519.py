# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3519
标题: Find the Number of Winning Players
难度: easy
链接: https://leetcode.cn/problems/find-the-number-of-winning-players/
题目类型: 数组、哈希表、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3238. 求出胜利玩家的数目 - 给你一个整数 n ，表示在一个游戏中的玩家数目。同时给你一个二维整数数组 pick ，其中 pick[i] = [xi, yi] 表示玩家 xi 获得了一个颜色为 yi 的球。 如果玩家 i 获得的球中任何一种颜色球的数目 严格大于 i 个，那么我们说玩家 i 是胜利玩家。换句话说： * 如果玩家 0 获得了任何的球，那么玩家 0 是胜利玩家。 * 如果玩家 1 获得了至少 2 个相同颜色的球，那么玩家 1 是胜利玩家。 * ... * 如果玩家 i 获得了至少 i + 1 个相同颜色的球，那么玩家 i 是胜利玩家。 请你返回游戏中 胜利玩家 的数目。 注意，可能有多个玩家是胜利玩家。 示例 1： 输入：n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]] 输出：2 解释： 玩家 0 和玩家 1 是胜利玩家，玩家 2 和玩家 3 不是胜利玩家。 示例 2： 输入：n = 5, pick = [[1,1],[1,2],[1,3],[1,4]] 输出：0 解释： 没有胜利玩家。 示例 3： 输入：n = 5, pick = [[1,1],[2,4],[2,4],[2,4]] 输出：1 解释： 玩家 2 是胜利玩家，因为玩家 2 获得了 3 个颜色为 4 的球。 提示： * 2 <= n <= 10 * 1 <= pick.length <= 100 * pick[i].length == 2 * 0 <= xi <= n - 1 * 0 <= yi <= 10
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个玩家获得的每种颜色球的数量，然后检查每个玩家是否满足胜利条件。

算法步骤:
1. 初始化一个字典 `ball_count`，用于记录每个玩家获得的每种颜色球的数量。
2. 遍历 `pick` 数组，更新 `ball_count` 字典。
3. 遍历 `ball_count` 字典，检查每个玩家是否满足胜利条件，并统计胜利玩家的数量。

关键点:
- 使用嵌套字典来记录每个玩家获得的每种颜色球的数量。
- 检查每个玩家是否满足胜利条件时，只需要遍历一次 `ball_count` 字典。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(p)，其中 p 是 `pick` 数组的长度。我们需要遍历 `pick` 数组来更新 `ball_count` 字典，然后遍历 `ball_count` 字典来检查每个玩家是否满足胜利条件。
空间复杂度: O(n * m)，其中 n 是玩家数量，m 是颜色数量。最坏情况下，每个玩家都获得了所有颜色的球，因此需要 O(n * m) 的空间来存储 `ball_count` 字典。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_number_of_winning_players(n: int, pick: List[List[int]]) -> int:
    """
    函数式接口 - 计算胜利玩家的数量
    """
    # 初始化一个字典来记录每个玩家获得的每种颜色球的数量
    ball_count = {}

    # 遍历 pick 数组，更新 ball_count 字典
    for player, color in pick:
        if player not in ball_count:
            ball_count[player] = {}
        if color not in ball_count[player]:
            ball_count[player][color] = 0
        ball_count[player][color] += 1

    # 统计胜利玩家的数量
    winning_players = 0
    for player, colors in ball_count.items():
        for color, count in colors.items():
            if count > player:
                winning_players += 1
                break

    return winning_players


Solution = create_solution(find_number_of_winning_players)