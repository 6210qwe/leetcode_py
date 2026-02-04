# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2114
标题: Minimum Number of Work Sessions to Finish the Tasks
难度: medium
链接: https://leetcode.cn/problems/minimum-number-of-work-sessions-to-finish-the-tasks/
题目类型: 位运算、数组、动态规划、回溯、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1986. 完成任务的最少工作时间段 - 你被安排了 n 个任务。任务需要花费的时间用长度为 n 的整数数组 tasks 表示，第 i 个任务需要花费 tasks[i] 小时完成。一个 工作时间段 中，你可以 至多 连续工作 sessionTime 个小时，然后休息一会儿。 你需要按照如下条件完成给定任务： * 如果你在某一个时间段开始一个任务，你需要在 同一个 时间段完成它。 * 完成一个任务后，你可以 立马 开始一个新的任务。 * 你可以按 任意顺序 完成任务。 给你 tasks 和 sessionTime ，请你按照上述要求，返回完成所有任务所需要的 最少 数目的 工作时间段 。 测试数据保证 sessionTime 大于等于 tasks[i] 中的 最大值 。 示例 1： 输入：tasks = [1,2,3], sessionTime = 3 输出：2 解释：你可以在两个工作时间段内完成所有任务。 - 第一个工作时间段：完成第一和第二个任务，花费 1 + 2 = 3 小时。 - 第二个工作时间段：完成第三个任务，花费 3 小时。 示例 2： 输入：tasks = [3,1,3,1,1], sessionTime = 8 输出：2 解释：你可以在两个工作时间段内完成所有任务。 - 第一个工作时间段：完成除了最后一个任务以外的所有任务，花费 3 + 1 + 3 + 1 = 8 小时。 - 第二个工作时间段，完成最后一个任务，花费 1 小时。 示例 3： 输入：tasks = [1,2,3,4,5], sessionTime = 15 输出：1 解释：你可以在一个工作时间段以内完成所有任务。 提示： * n == tasks.length * 1 <= n <= 14 * 1 <= tasks[i] <= 10 * max(tasks[i]) <= sessionTime <= 15
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和状态压缩来解决这个问题。我们使用一个二维数组 dp，其中 dp[mask][i] 表示在当前状态下（由 mask 表示的任务集合）和当前时间段剩余时间 i 的最小工作时间段数。

算法步骤:
1. 初始化 dp 数组，dp[0][0] = 0，表示没有任务且剩余时间为 0 的情况下，不需要任何工作时间段。
2. 对于每个可能的状态 mask，遍历所有任务，更新 dp 数组。
3. 对于每个状态 mask，如果当前任务不在 mask 中，则尝试将该任务加入当前时间段或新开一个时间段。
4. 最终结果是 dp[(1 << n) - 1][0]，表示所有任务都完成且当前时间段剩余时间为 0 的最小工作时间段数。

关键点:
- 使用状态压缩来表示任务集合。
- 动态规划转移方程：
  - 如果当前任务可以加入当前时间段：dp[mask | (1 << j)][i - tasks[j]] = min(dp[mask | (1 << j)][i - tasks[j]], dp[mask][i])
  - 如果当前任务不能加入当前时间段：dp[mask | (1 << j)][sessionTime - tasks[j]] = min(dp[mask | (1 << j)][sessionTime - tasks[j]], dp[mask][i] + 1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n * n * sessionTime)，其中 n 是任务数量，sessionTime 是每个时间段的最大时间。
空间复杂度: O(2^n * sessionTime)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_sessions(tasks: List[int], session_time: int) -> int:
    """
    返回完成所有任务所需的最少工作时间段数。
    """
    n = len(tasks)
    dp = [[float('inf')] * (session_time + 1) for _ in range(1 << n)]
    dp[0][0] = 0

    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i):
                continue
            for j in range(session_time + 1):
                if j >= tasks[i]:
                    dp[mask | (1 << i)][j - tasks[i]] = min(dp[mask | (1 << i)][j - tasks[i]], dp[mask][j])
                else:
                    dp[mask | (1 << i)][session_time - tasks[i]] = min(dp[mask | (1 << i)][session_time - tasks[i]], dp[mask][j] + 1)

    return min(dp[(1 << n) - 1])


Solution = create_solution(min_sessions)