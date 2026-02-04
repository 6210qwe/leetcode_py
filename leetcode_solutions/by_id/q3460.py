# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3460
标题: Count the Number of Inversions
难度: hard
链接: https://leetcode.cn/problems/count-the-number-of-inversions/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3193. 统计逆序对的数目 - 给你一个整数 n 和一个二维数组 requirements ，其中 requirements[i] = [endi, cnti] 表示这个要求中的末尾下标和 逆序对 的数目。 整数数组 nums 中一个下标对 (i, j) 如果满足以下条件，那么它们被称为一个 逆序对 ： * i < j 且 nums[i] > nums[j] 请你返回 [0, 1, 2, ..., n - 1] 的 排列 perm 的数目，满足对 所有 的 requirements[i] 都满足 perm[0..endi] 中恰好有 cnti 个逆序对。 由于答案可能会很大，将它对 109 + 7 取余 后返回。 示例 1： 输入：n = 3, requirements = [[2,2],[0,0]] 输出：2 解释： 两个排列为： * [2, 0, 1] * 前缀 [2, 0, 1] 的逆序对为 (0, 1) 和 (0, 2) 。 * 前缀 [2] 的逆序对数目为 0 个。 * [1, 2, 0] * 前缀 [1, 2, 0] 的逆序对为 (0, 2) 和 (1, 2) 。 * 前缀 [1] 的逆序对数目为 0 个。 示例 2： 输入：n = 3, requirements = [[2,2],[1,1],[0,0]] 输出：1 解释： 唯一满足要求的排列是 [2, 0, 1] ： * 前缀 [2, 0, 1] 的逆序对为 (0, 1) 和 (0, 2) 。 * 前缀 [2, 0] 的逆序对为 (0, 1) 。 * 前缀 [2] 的逆序对数目为 0 。 示例 3： 输入：n = 2, requirements = [[0,0],[1,0]] 输出：1 解释： 唯一满足要求的排列为 [0, 1] ： * 前缀 [0] 的逆序对数目为 0 。 * 前缀 [0, 1] 没有逆序对。 提示： * 2 <= n <= 300 * 1 <= requirements.length <= n * requirements[i] = [endi, cnti] * 0 <= endi <= n - 1 * 0 <= cnti <= 400 * 输入保证至少有一个 i 满足 endi == n - 1 。 * 输入保证所有的 endi 互不相同。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i][j] 表示前 i 个元素中恰好有 j 个逆序对的排列数目。通过递推关系，我们可以逐步计算出所有可能的排列数目。

算法步骤:
1. 初始化 dp 数组，dp[0][0] = 1，表示没有元素时，逆序对数目为 0 的排列数目为 1。
2. 对于每个位置 i，遍历从 0 到 i-1 的所有位置 k，更新 dp[i][j]。
3. 根据 requirements 更新 dp 数组。
4. 最终结果为 dp[n][cnti]，其中 cnti 是 requirements 中最后一个元素的逆序对数目。

关键点:
- 动态规划的状态转移方程。
- 处理 requirements 的更新。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * max(cnti))，其中 n 是数组长度，max(cnti) 是 requirements 中的最大逆序对数目。
空间复杂度: O(n * max(cnti))，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_inversions(n: int, requirements: List[List[int]]) -> int:
    MOD = 10**9 + 7
    max_cnt = max(cnt for _, cnt in requirements)
    dp = [[0] * (max_cnt + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            for k in range(max_cnt + 1):
                if k + (i - 1 - j) <= max_cnt:
                    dp[i][k + (i - 1 - j)] = (dp[i][k + (i - 1 - j)] + dp[i - 1][k]) % MOD

    for end, cnt in requirements:
        dp[end + 1][:] = [0] * (max_cnt + 1)
        dp[end + 1][cnt] = dp[end][cnt]

    return dp[n][requirements[-1][1]]


Solution = create_solution(count_inversions)