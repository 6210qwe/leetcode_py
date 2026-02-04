# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3989
标题: Sum of Beautiful Subsequences
难度: hard
链接: https://leetcode.cn/problems/sum-of-beautiful-subsequences/
题目类型: 树、数组、数学、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3671. 子序列美丽值求和 - 给你一个长度为 n 的整数数组 nums。 对于每个 正整数 g，定义 g 的 美丽值 为 g 与 nums 中符合要求的子序列数量的乘积，子序列需要 严格递增 且最大公约数（GCD）恰好为 g 。 请返回所有正整数 g 的 美丽值 之和。 由于答案可能非常大，请返回结果对 109 + 7 取模后的值。 子序列 是一个 非空 数组，可以通过从另一个数组中删除某些元素（或不删除任何元素）而保持剩余元素顺序不变得到。 示例 1： 输入：nums = [1,2,3] 输出：10 解释： 所有严格递增子序列及其 GCD 如下： 子序列 GCD [1] 1 [2] 2 [3] 3 [1,2] 1 [1,3] 1 [2,3] 1 [1,2,3] 1 计算每个 GCD 的美丽值： GCD 子序列数量 美丽值 (GCD × 数量) 1 5 1 × 5 = 5 2 1 2 × 1 = 2 3 1 3 × 1 = 3 美丽值总和为 5 + 2 + 3 = 10。 示例 2： 输入：nums = [4,6] 输出：12 解释： 所有严格递增子序列及其 GCD 如下： 子序列 GCD [4] 4 [6] 6 [4,6] 2 计算每个 GCD 的美丽值： GCD 子序列数量 美丽值 (GCD × 数量) 2 1 2 × 1 = 2 4 1 4 × 1 = 4 6 1 6 × 1 = 6 美丽值总和为 2 + 4 + 6 = 12。 提示： * 1 <= n == nums.length <= 104 * 1 <= nums[i] <= 7 × 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来计算每个 GCD 的美丽值。

算法步骤:
1. 初始化一个字典 dp，用于存储以某个 GCD 结尾的子序列的数量。
2. 遍历数组 nums，对于每个元素 num，更新 dp 字典。
3. 对于每个 num，遍历 dp 字典中的所有 GCD，如果当前 GCD 能整除 num，则更新 dp[num]。
4. 最后，计算所有 GCD 的美丽值之和，并取模 10^9 + 7。

关键点:
- 动态规划的状态转移方程：dp[gcd] += dp[prev_gcd]，其中 prev_gcd 是 gcd 的因子。
- 使用字典来存储每个 GCD 的子序列数量，减少空间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * sqrt(max(nums)))，其中 n 是 nums 的长度，max(nums) 是 nums 中的最大值。
空间复杂度: O(max(nums))，用于存储 dp 字典。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def sum_of_beautiful_subsequences(nums: List[int]) -> int:
    MOD = 10**9 + 7
    max_num = max(nums)
    dp = {i: 0 for i in range(1, max_num + 1)}
    dp[1] = 1  # 单个元素的子序列数量为 1

    for num in nums:
        new_dp = dp.copy()
        for gcd, count in dp.items():
            if num % gcd == 0:
                new_gcd = gcd
                new_dp[new_gcd] = (new_dp[new_gcd] + count) % MOD
                if new_gcd != num:
                    new_dp[num] = (new_dp[num] + count) % MOD
        dp = new_dp

    result = sum(gcd * count for gcd, count in dp.items()) % MOD
    return result


Solution = create_solution(sum_of_beautiful_subsequences)