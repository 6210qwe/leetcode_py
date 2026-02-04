# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3491
标题: Find the Maximum Length of Valid Subsequence II
难度: medium
链接: https://leetcode.cn/problems/find-the-maximum-length-of-valid-subsequence-ii/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3202. 找出有效子序列的最大长度 II - 给你一个整数数组 nums 和一个 正 整数 k 。 nums 的一个 子序列 sub 的长度为 x ，如果其满足以下条件，则称其为 有效子序列 ： * (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k 返回 nums 的 最长有效子序列 的长度。 示例 1： 输入：nums = [1,2,3,4,5], k = 2 输出：5 解释： 最长有效子序列是 [1, 2, 3, 4, 5] 。 示例 2： 输入：nums = [1,4,2,3,1,4], k = 3 输出：4 解释： 最长有效子序列是 [1, 4, 1, 4] 。 提示： * 2 <= nums.length <= 103 * 1 <= nums[i] <= 107 * 1 <= k <= 103
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和哈希表来记录每个余数的最长子序列长度。

算法步骤:
1. 初始化一个字典 `dp`，其中 `dp[remainder][i]` 表示以 `nums[i]` 结尾且余数为 `remainder` 的最长子序列长度。
2. 遍历数组 `nums`，对于每个元素 `nums[i]`，计算其与前面所有元素的余数，并更新 `dp` 字典。
3. 最后返回 `dp` 字典中的最大值。

关键点:
- 使用哈希表来存储每个余数的最长子序列长度，避免重复计算。
- 动态规划的状态转移方程为 `dp[remainder][i] = max(dp[remainder][i], dp[remainder][j] + 1)`，其中 `remainder = (nums[i] + nums[j]) % k`。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是数组 `nums` 的长度。因为我们需要遍历数组并计算每个元素与前面所有元素的余数。
空间复杂度: O(n * k)，其中 n 是数组 `nums` 的长度，k 是给定的正整数。因为我们需要存储每个余数的最长子序列长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def find_max_length(nums: List[int], k: int) -> int:
    """
    函数式接口 - 找出有效子序列的最大长度
    """
    n = len(nums)
    dp = [{} for _ in range(n)]
    max_length = 1

    for i in range(n):
        for j in range(i):
            remainder = (nums[i] + nums[j]) % k
            if remainder in dp[j]:
                if remainder not in dp[i]:
                    dp[i][remainder] = 0
                dp[i][remainder] = max(dp[i][remainder], dp[j][remainder] + 1)
                max_length = max(max_length, dp[i][remainder])
        
        # Initialize the current element's remainder
        remainder = nums[i] % k
        if remainder not in dp[i]:
            dp[i][remainder] = 1
        else:
            dp[i][remainder] = max(dp[i][remainder], 1)

    return max_length

Solution = create_solution(find_max_length)