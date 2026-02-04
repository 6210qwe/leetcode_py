# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3716
标题: Longest Subsequence With Decreasing Adjacent Difference
难度: medium
链接: https://leetcode.cn/problems/longest-subsequence-with-decreasing-adjacent-difference/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3409. 最长相邻绝对差递减子序列 - 给你一个整数数组 nums 。 你的任务是找到 nums 中的 最长 子序列 seq ，这个子序列中相邻元素的 绝对差 构成一个 非递增 整数序列。换句话说，nums 中的序列 seq0, seq1, seq2, ..., seqm 满足 |seq1 - seq0| >= |seq2 - seq1| >= ... >= |seqm - seqm - 1| 。 请你返回这个子序列的长度。 示例 1： 输入：nums = [16,6,3] 输出：3 解释： 最长子序列是 [16, 6, 3] ，相邻绝对差值为 [10, 3] 。 示例 2： 输入：nums = [6,5,3,4,2,1] 输出：4 解释： 最长子序列是 [6, 4, 2, 1] ，相邻绝对差值为 [2, 2, 1] 。 示例 3： 输入：nums = [10,20,10,19,10,20] 输出：5 解释： 最长子序列是 [10, 20, 10, 19, 10] ，相邻绝对差值为 [10, 10, 9, 9] 。 提示： * 2 <= nums.length <= 104 * 1 <= nums[i] <= 300
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i][d] 表示以第 i 个元素结尾且相邻绝对差为 d 的最长子序列长度。

算法步骤:
1. 初始化一个二维数组 dp，其中 dp[i][d] 表示以第 i 个元素结尾且相邻绝对差为 d 的最长子序列长度。
2. 遍历数组，对于每个元素 nums[i]，遍历它之前的所有元素 nums[j]，计算它们的绝对差 d = abs(nums[i] - nums[j])。
3. 更新 dp[i][d] 的值为 max(dp[i][d], dp[j][k] + 1)，其中 k 是所有满足 k >= d 的值。
4. 最后，返回 dp 数组中的最大值。

关键点:
- 使用二维数组 dp 来记录状态，避免重复计算。
- 动态更新 dp 数组，确保每次更新时都考虑了所有可能的前驱状态。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * D)，其中 n 是数组的长度，D 是可能的绝对差的最大值（在本题中为 300）。
空间复杂度: O(n * D)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_subsequence_with_decreasing_adjacent_difference(nums: List[int]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    n = len(nums)
    if n == 0:
        return 0

    # 定义 dp 数组
    dp = [[1] * 301 for _ in range(n)]
    max_length = 1

    for i in range(1, n):
        for j in range(i):
            diff = abs(nums[i] - nums[j])
            for d in range(diff, 301):
                dp[i][diff] = max(dp[i][diff], dp[j][d] + 1)
                max_length = max(max_length, dp[i][diff])

    return max_length


Solution = create_solution(longest_subsequence_with_decreasing_adjacent_difference)