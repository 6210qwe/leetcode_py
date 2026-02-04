# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1457
标题: Minimum Difficulty of a Job Schedule
难度: hard
链接: https://leetcode.cn/problems/minimum-difficulty-of-a-job-schedule/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1335. 工作计划的最低难度 - 你需要制定一份 d 天的工作计划表。工作之间存在依赖，要想执行第 i 项工作，你必须完成全部 j 项工作（ 0 <= j < i）。 你每天 至少 需要完成一项任务。工作计划的总难度是这 d 天每一天的难度之和，而一天的工作难度是当天应该完成工作的最大难度。 给你一个整数数组 jobDifficulty 和一个整数 d，分别代表工作难度和需要计划的天数。第 i 项工作的难度是 jobDifficulty[i]。 返回整个工作计划的 最小难度 。如果无法制定工作计划，则返回 -1 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/26/untitled.png] 输入：jobDifficulty = [6,5,4,3,2,1], d = 2 输出：7 解释：第一天，您可以完成前 5 项工作，总难度 = 6. 第二天，您可以完成最后一项工作，总难度 = 1. 计划表的难度 = 6 + 1 = 7 示例 2： 输入：jobDifficulty = [9,9,9], d = 4 输出：-1 解释：就算你每天完成一项工作，仍然有一天是空闲的，你无法制定一份能够满足既定工作时间的计划表。 示例 3： 输入：jobDifficulty = [1,1,1], d = 3 输出：3 解释：工作计划为每天一项工作，总难度为 3 。 示例 4： 输入：jobDifficulty = [7,1,7,1,7,1], d = 3 输出：15 示例 5： 输入：jobDifficulty = [11,111,22,222,33,333,44,444], d = 6 输出：843 提示： * 1 <= jobDifficulty.length <= 300 * 0 <= jobDifficulty[i] <= 1000 * 1 <= d <= 10
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i][k] 表示在前 i 项工作中分成 k 天的最小难度。

算法步骤:
1. 初始化 dp 数组，dp[i][k] 表示前 i 项工作分成 k 天的最小难度。
2. 遍历所有可能的分割点 j，计算 dp[i][k] 的值。
3. 对于每个分割点 j，更新 dp[i][k] 的值为 min(dp[i][k], dp[j][k-1] + max(jobDifficulty[j:i]))。

关键点:
- 使用动态规划来存储中间结果，避免重复计算。
- 通过遍历所有可能的分割点来找到最优解。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * d)，其中 n 是 jobDifficulty 的长度，d 是天数。
空间复杂度: O(n * d)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_difficulty(jobDifficulty: List[int], d: int) -> int:
    """
    函数式接口 - 计算工作计划的最小难度
    """
    n = len(jobDifficulty)
    if n < d:
        return -1
    
    # 初始化 dp 数组
    dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    # 动态规划填表
    for i in range(1, n + 1):
        for k in range(1, d + 1):
            max_difficulty = 0
            for j in range(i, k - 1, -1):
                max_difficulty = max(max_difficulty, jobDifficulty[j - 1])
                dp[i][k] = min(dp[i][k], dp[j - 1][k - 1] + max_difficulty)
    
    return dp[n][d] if dp[n][d] != float('inf') else -1


Solution = create_solution(min_difficulty)