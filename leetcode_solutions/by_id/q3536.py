# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3536
标题: Find the Count of Monotonic Pairs II
难度: hard
链接: https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-ii/
题目类型: 数组、数学、动态规划、组合数学、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3251. 单调数组对的数目 II - 给你一个长度为 n 的 正 整数数组 nums 。 如果两个 非负 整数数组 (arr1, arr2) 满足以下条件，我们称它们是 单调 数组对： * 两个数组的长度都是 n 。 * arr1 是单调 非递减 的，换句话说 arr1[0] <= arr1[1] <= ... <= arr1[n - 1] 。 * arr2 是单调 非递增 的，换句话说 arr2[0] >= arr2[1] >= ... >= arr2[n - 1] 。 * 对于所有的 0 <= i <= n - 1 都有 arr1[i] + arr2[i] == nums[i] 。 请你返回所有 单调 数组对的数目。 由于答案可能很大，请你将它对 109 + 7 取余 后返回。 示例 1： 输入：nums = [2,3,2] 输出：4 解释： 单调数组对包括： 1. ([0, 1, 1], [2, 2, 1]) 2. ([0, 1, 2], [2, 2, 0]) 3. ([0, 2, 2], [2, 1, 0]) 4. ([1, 2, 2], [1, 1, 0]) 示例 2： 输入：nums = [5,5,5,5] 输出：126 提示： * 1 <= n == nums.length <= 2000 * 1 <= nums[i] <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和组合数学来计算单调数组对的数量。

算法步骤:
1. 初始化一个 DP 数组 `dp`，其中 `dp[i][j]` 表示以 `i` 结尾且最大值为 `j` 的单调非递减数组的数量。
2. 遍历数组 `nums`，对于每个元素 `nums[i]`，更新 `dp` 数组。
3. 计算每个位置的组合数，并累加结果。

关键点:
- 使用动态规划来维护单调非递减数组的数量。
- 使用组合数学来计算单调非递增数组的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是数组 `nums` 的长度，m 是 `nums` 中的最大值。
空间复杂度: O(n * m)，用于存储 DP 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import math

def count_monotonic_pairs(nums: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    max_val = max(nums)
    
    # 初始化 DP 数组
    dp = [[0] * (max_val + 1) for _ in range(n)]
    dp[0][nums[0]] = 1
    
    # 动态规划更新 DP 数组
    for i in range(1, n):
        for j in range(max_val + 1):
            if j <= nums[i]:
                dp[i][j] = sum(dp[i - 1][:j + 1]) % MOD
            else:
                dp[i][j] = sum(dp[i - 1][:nums[i] + 1]) % MOD
    
    # 计算组合数
    def comb(n, k):
        return math.comb(n, k) % MOD
    
    result = 0
    for i in range(n):
        for j in range(max_val + 1):
            if dp[i][j] > 0:
                remaining_sum = sum(nums[i:]) - j
                if remaining_sum >= 0:
                    result += dp[i][j] * comb(remaining_sum + i - i, i) % MOD
                    result %= MOD
    
    return result

Solution = create_solution(count_monotonic_pairs)