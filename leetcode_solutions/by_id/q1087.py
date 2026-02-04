# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1087
标题: Longest Arithmetic Subsequence
难度: medium
链接: https://leetcode.cn/problems/longest-arithmetic-subsequence/
题目类型: 数组、哈希表、二分查找、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1027. 最长等差数列 - 给你一个整数数组 nums，返回 nums 中最长等差子序列的长度。 回想一下，nums 的子序列是一个列表 nums[i1], nums[i2], ..., nums[ik] ，且 0 <= i1 < i2 < ... < ik <= nums.length - 1。并且如果 seq[i+1] - seq[i]( 0 <= i < seq.length - 1) 的值都相同，那么序列 seq 是等差的。 示例 1： 输入：nums = [3,6,9,12] 输出：4 解释： 整个数组是公差为 3 的等差数列。 示例 2： 输入：nums = [9,4,7,2,10] 输出：3 解释： 最长的等差子序列是 [4,7,10]。 示例 3： 输入：nums = [20,1,15,3,10,5,8] 输出：4 解释： 最长的等差子序列是 [20,15,10,5]。 提示： * 2 <= nums.length <= 1000 * 0 <= nums[i] <= 500
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和哈希表来记录每个元素作为等差数列结尾时的最大长度。

算法步骤:
1. 初始化一个字典 `dp`，其中 `dp[i][diff]` 表示以 `nums[i]` 结尾且公差为 `diff` 的最长等差子序列的长度。
2. 遍历数组 `nums`，对于每一对 `(i, j)`，计算它们的差值 `diff`。
3. 更新 `dp[j][diff]` 为 `dp[i][diff] + 1`，并更新全局最大长度 `max_length`。

关键点:
- 使用哈希表来存储每个元素作为等差数列结尾时的最大长度。
- 动态规划的状态转移方程为 `dp[j][diff] = dp[i][diff] + 1`。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是数组 `nums` 的长度。需要遍历每一对 `(i, j)`。
空间复杂度: O(n^2)，哈希表 `dp` 的大小最多为 n^2。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_arith_seq_length(nums: List[int]) -> int:
    """
    函数式接口 - 返回数组中最长等差子序列的长度
    """
    if not nums or len(nums) < 2:
        return 0

    n = len(nums)
    dp = [{} for _ in range(n)]
    max_length = 0

    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
            else:
                dp[i][diff] = 2
            max_length = max(max_length, dp[i][diff])

    return max_length


Solution = create_solution(longest_arith_seq_length)