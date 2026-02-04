# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3456
标题: Find the Maximum Length of a Good Subsequence I
难度: medium
链接: https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-i/
题目类型: 数组、哈希表、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3176. 求出最长好子序列 I - 给你一个整数数组 nums 和一个 非负 整数 k 。如果一个整数序列 seq 满足在下标范围 [0, seq.length - 2] 中 最多只有 k 个下标 i 满足 seq[i] != seq[i + 1] ，那么我们称这个整数序列为 好 序列。 请你返回 nums 中 好 子序列 的最长长度。 示例 1： 输入：nums = [1,2,1,1,3], k = 2 输出：4 解释： 最长好子序列为 [1,2,1,1,3] 。 示例 2： 输入：nums = [1,2,3,4,5,1], k = 0 输出：2 解释： 最长好子序列为 [1,2,3,4,5,1] 。 提示： * 1 <= nums.length <= 500 * 1 <= nums[i] <= 109 * 0 <= k <= min(nums.length, 25)
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i][j] 表示以 nums[i] 结尾的最长好子序列，且最多有 j 个不连续的元素。

算法步骤:
1. 初始化 dp 数组，dp[i][j] 表示以 nums[i] 结尾的最长好子序列，且最多有 j 个不连续的元素。
2. 遍历数组，对于每个元素 nums[i]，更新 dp[i][j]。
3. 如果 nums[i] == nums[i-1]，则 dp[i][j] = dp[i-1][j] + 1。
4. 如果 nums[i] != nums[i-1]，则 dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j])。
5. 最后，取 dp 数组中的最大值作为结果。

关键点:
- 使用二维 dp 数组来记录状态。
- 处理边界情况，特别是当 j == 0 时的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * k)，其中 n 是 nums 的长度，k 是给定的非负整数。
空间复杂度: O(n * k)，使用了二维 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int], k: int) -> int:
    """
    函数式接口 - 返回 nums 中好子序列的最长长度
    """
    n = len(nums)
    if n == 0:
        return 0

    # 初始化 dp 数组
    dp = [[0] * (k + 1) for _ in range(n)]
    dp[0][0] = 1

    # 动态规划填表
    for i in range(1, n):
        for j in range(k + 1):
            if nums[i] == nums[i - 1]:
                dp[i][j] = dp[i - 1][j] + 1
            else:
                if j > 0:
                    dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j])
                else:
                    dp[i][j] = 1

    # 取 dp 数组中的最大值
    return max(max(row) for row in dp)


Solution = create_solution(solution_function_name)