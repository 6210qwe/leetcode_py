# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 911
标题: Profitable Schemes
难度: hard
链接: https://leetcode.cn/problems/profitable-schemes/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
879. 盈利计划 - 集团里有 n 名员工，他们可以完成各种各样的工作创造利润。 第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。 工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。 有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。 示例 1： 输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3] 输出：2 解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。 总的来说，有两种计划。 示例 2： 输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8] 输出：7 解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。 有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。 提示： * 1 <= n <= 100 * 0 <= minProfit <= 100 * 1 <= group.length <= 100 * 1 <= group[i] <= 100 * profit.length == group.length * 0 <= profit[i] <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义一个三维数组 dp，其中 dp[i][j][k] 表示前 i 个工作，使用 j 个人，至少获得 k 利润的方案数。

算法步骤:
1. 初始化一个三维数组 dp，大小为 (m+1) x (n+1) x (minProfit+1)，其中 m 是工作的数量。
2. 设置初始条件 dp[0][0][0] = 1，表示没有工作时，0 人可以获得 0 利润的方案数为 1。
3. 遍历每个工作，对于每个工作，遍历所有可能的人数和利润，更新 dp 数组。
4. 最后，dp[m][i][minProfit] 的和即为所求的结果。

关键点:
- 动态规划的状态转移方程为：
  - 如果选择当前工作，则 dp[i+1][j+group[i]][max(k-profit[i], 0)] += dp[i][j][k]
  - 如果不选择当前工作，则 dp[i+1][j][k] += dp[i][j][k]
- 最终结果需要对 10^9 + 7 取模。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * minProfit)，其中 m 是工作的数量，n 是员工的数量，minProfit 是最小利润。
空间复杂度: O(m * n * minProfit)，用于存储动态规划数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

MOD = 10**9 + 7

def profitable_schemes(n: int, min_profit: int, group: List[int], profit: List[int]) -> int:
    m = len(group)
    dp = [[[0] * (min_profit + 1) for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][0][0] = 1

    for i in range(m):
        for j in range(n + 1):
            for k in range(min_profit + 1):
                # 不选择当前工作
                dp[i + 1][j][k] = dp[i][j][k]
                if j + group[i] <= n:
                    # 选择当前工作
                    dp[i + 1][j + group[i]][max(k - profit[i], 0)] += dp[i][j][k]
                    dp[i + 1][j + group[i]][max(k - profit[i], 0)] %= MOD

    result = sum(dp[m][i][min_profit] for i in range(n + 1)) % MOD
    return result

Solution = create_solution(profitable_schemes)