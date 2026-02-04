# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3649
标题: Minimum Time to Break Locks I
难度: medium
链接: https://leetcode.cn/problems/minimum-time-to-break-locks-i/
题目类型: 位运算、深度优先搜索、数组、动态规划、回溯、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3376. 破解锁的最少时间 I - Bob 被困在了一个地窖里，他需要破解 n 个锁才能逃出地窖，每一个锁都需要一定的 能量 才能打开。每一个锁需要的能量存放在一个数组 strength 里，其中 strength[i] 表示打开第 i 个锁需要的能量。 Bob 有一把剑，它具备以下的特征： * 一开始剑的能量为 0 。 * 剑的能量增加因子 X 一开始的值为 1 。 * 每分钟，剑的能量都会增加当前的 X 值。 * 打开第 i 把锁，剑的能量需要到达 至少 strength[i] 。 * 打开一把锁以后，剑的能量会变回 0 ，X 的值会增加一个给定的值 K 。 你的任务是打开所有 n 把锁并逃出地窖，请你求出需要的 最少 分钟数。 请你返回 Bob 打开所有 n 把锁需要的 最少 时间。 示例 1： 输入：strength = [3,4,1], K = 1 输出：4 解释： 时间 能量 X 操作 更新后的 X 0 0 1 什么也不做 1 1 1 1 打开第 3 把锁 2 2 2 2 什么也不做 2 3 4 2 打开第 2 把锁 3 4 3 3 打开第 1 把锁 3 无法用少于 4 分钟打开所有的锁，所以答案为 4 。 示例 2： 输入：strength = [2,5,4], K = 2 输出：5 解释： 时间 能量 X 操作 更新后的 X 0 0 1 什么也不做 1 1 1 1 什么也不做 1 2 2 1 打开第 1 把锁 3 3 3 3 什么也不做 3 4 6 3 打开第 2 把锁 5 5 5 5 打开第 3 把锁 7 无法用少于 5 分钟打开所有的锁，所以答案为 5 。 提示： * n == strength.length * 1 <= n <= 8 * 1 <= K <= 10 * 1 <= strength[i] <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和状态压缩来解决这个问题。我们使用一个二维数组 dp 来记录每种状态下的最小时间。dp[mask][i] 表示已经打开了 mask 中表示的锁，并且最后一个打开的锁是 i 时的最小时间。

算法步骤:
1. 初始化 dp 数组，大小为 (1 << n) x n，初始值为无穷大。
2. 设置初始状态 dp[0][0] = 0。
3. 遍历所有可能的状态 mask 和每个锁 i。
4. 对于每个状态 mask 和锁 i，遍历所有之前的锁 j，更新 dp[mask][i]。
5. 最后，找到 dp[(1 << n) - 1][i] 中的最小值作为结果。

关键点:
- 使用状态压缩来表示已经打开的锁。
- 动态规划来记录每种状态下的最小时间。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * 2^n)
空间复杂度: O(n * 2^n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_time_to_break_locks(strength: List[int], k: int) -> int:
    n = len(strength)
    max_value = float('inf')
    dp = [[max_value] * n for _ in range(1 << n)]
    
    # Initialize the dp array
    for i in range(n):
        dp[1 << i][i] = (strength[i] + k - 1) // k
    
    # Fill the dp array
    for mask in range(1, 1 << n):
        for i in range(n):
            if mask & (1 << i):
                for j in range(n):
                    if i != j and mask & (1 << j):
                        prev_mask = mask ^ (1 << i)
                        time_to_open_i = (strength[i] + (k * (dp[prev_mask][j] + 1)) - 1) // (k * (dp[prev_mask][j] + 1))
                        dp[mask][i] = min(dp[mask][i], dp[prev_mask][j] + time_to_open_i)
    
    # Find the minimum time to open all locks
    return min(dp[(1 << n) - 1])

Solution = create_solution(minimum_time_to_break_locks)