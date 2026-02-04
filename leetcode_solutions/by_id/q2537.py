# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2537
标题: Minimum Time to Kill All Monsters
难度: hard
链接: https://leetcode.cn/problems/minimum-time-to-kill-all-monsters/
题目类型: 位运算、数组、动态规划、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2403. 杀死所有怪物的最短时间 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和状态压缩来解决这个问题。我们使用一个二维DP数组dp[i][j]表示在第i秒时，杀死状态为j的怪物所需的最小时间。

算法步骤:
1. 初始化DP数组，dp[0][0] = 0，其他值设为无穷大。
2. 遍历每一秒，对于每一个可能的状态，计算杀死当前状态下的怪物所需的最小时间。
3. 更新DP数组，选择最小的时间。
4. 最终结果是dp[n][all_monsters_state]，其中n是总时间，all_monsters_state是所有怪物都被杀死的状态。

关键点:
- 使用位运算来表示和操作怪物的状态。
- 动态规划的状态转移方程需要考虑当前时间和当前状态。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * 2^m)，其中n是总时间，m是怪物的数量。
空间复杂度: O(n * 2^m)，用于存储DP数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_time_to_kill_monsters(n: int, m: int, monsters: List[int]) -> int:
    """
    函数式接口 - 计算杀死所有怪物的最短时间
    """
    # 初始化DP数组
    dp = [[float('inf')] * (1 << m) for _ in range(n + 1)]
    dp[0][0] = 0

    # 遍历每一秒
    for i in range(1, n + 1):
        for state in range(1 << m):
            # 如果当前状态已经全部杀死怪物
            if state == (1 << m) - 1:
                dp[i][state] = min(dp[i][state], dp[i - 1][state])
            else:
                # 尝试杀死当前状态下的每个怪物
                for j in range(m):
                    if not (state & (1 << j)):
                        new_state = state | (1 << j)
                        time_needed = (monsters[j] - 1) // i + 1
                        dp[i][new_state] = min(dp[i][new_state], dp[i - 1][state] + time_needed)

    return dp[n][(1 << m) - 1]


Solution = create_solution(min_time_to_kill_monsters)