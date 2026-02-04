# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1354
标题: Find Players With Zero or One Losses
难度: medium
链接: https://leetcode.cn/problems/find-players-with-zero-or-one-losses/
题目类型: 数组、哈希表、计数、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2225. 找出输掉零场或一场比赛的玩家 - 给你一个整数数组 matches 其中 matches[i] = [winneri, loseri] 表示在一场比赛中 winneri 击败了 loseri 。 返回一个长度为 2 的列表 answer ： * answer[0] 是所有 没有 输掉任何比赛的玩家列表。 * answer[1] 是所有恰好输掉 一场 比赛的玩家列表。 两个列表中的值都应该按 递增 顺序返回。 注意： * 只考虑那些参与 至少一场 比赛的玩家。 * 生成的测试用例保证 不存在 两场比赛结果 相同 。 示例 1： 输入：matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]] 输出：[[1,2,10],[4,5,7,8]] 解释： 玩家 1、2 和 10 都没有输掉任何比赛。 玩家 4、5、7 和 8 每个都输掉一场比赛。 玩家 3、6 和 9 每个都输掉两场比赛。 因此，answer[0] = [1,2,10] 和 answer[1] = [4,5,7,8] 。 示例 2： 输入：matches = [[2,3],[1,3],[5,4],[6,4]] 输出：[[1,2,5,6],[]] 解释： 玩家 1、2、5 和 6 都没有输掉任何比赛。 玩家 3 和 4 每个都输掉两场比赛。 因此，answer[0] = [1,2,5,6] 和 answer[1] = [] 。 提示： * 1 <= matches.length <= 105 * matches[i].length == 2 * 1 <= winneri, loseri <= 105 * winneri != loseri * 所有 matches[i] 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个玩家的输赢情况，然后筛选出输掉零场或一场比赛的玩家。

算法步骤:
1. 初始化两个哈希表，一个记录每个玩家的胜利次数，另一个记录每个玩家的失败次数。
2. 遍历 matches 数组，更新哈希表中的胜利和失败次数。
3. 遍历失败次数哈希表，筛选出输掉零场或一场比赛的玩家，并将结果按递增顺序排序。

关键点:
- 使用哈希表高效地记录和查询每个玩家的输赢情况。
- 最后对结果进行排序以满足题目要求。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m log m)，其中 n 是 matches 的长度，m 是参与比赛的玩家数量。遍历 matches 数组的时间复杂度是 O(n)，排序的时间复杂度是 O(m log m)。
空间复杂度: O(m)，其中 m 是参与比赛的玩家数量。需要使用两个哈希表来记录每个玩家的胜利和失败次数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_players_with_zero_or_one_losses(matches: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 找出输掉零场或一场比赛的玩家
    """
    # 记录每个玩家的胜利和失败次数
    win_count = {}
    lose_count = {}

    for winner, loser in matches:
        win_count[winner] = win_count.get(winner, 0) + 1
        lose_count[loser] = lose_count.get(loser, 0) + 1

    # 找出输掉零场或一场比赛的玩家
    zero_loss_players = []
    one_loss_players = []

    for player in set(win_count.keys()).union(lose_count.keys()):
        if player not in lose_count:
            zero_loss_players.append(player)
        elif lose_count[player] == 1:
            one_loss_players.append(player)

    # 按递增顺序排序
    zero_loss_players.sort()
    one_loss_players.sort()

    return [zero_loss_players, one_loss_players]


Solution = create_solution(find_players_with_zero_or_one_losses)