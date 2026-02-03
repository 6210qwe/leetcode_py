# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 673
标题: Number of Longest Increasing Subsequence
难度: medium
链接: https://leetcode.cn/problems/number-of-longest-increasing-subsequence/
题目类型: 树状数组、线段树、数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
673. 最长递增子序列的个数 - 给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。 注意 这个数列必须是 严格 递增的。 示例 1: 输入: [1,3,5,4,7] 输出: 2 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。 示例 2: 输入: [2,2,2,2,2] 输出: 5 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。 提示: * 1 <= nums.length <= 2000 * -106 <= nums[i] <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 动态规划，记录每个位置的 LIS 长度和对应的个数

算法步骤:
1. 定义数组 len_dp[i] 为以 nums[i] 结尾的最长递增子序列长度
2. 定义数组 cnt_dp[i] 为以 nums[i] 结尾的最长递增子序列的个数
3. 初始化 len_dp[i] = 1, cnt_dp[i] = 1
4. 对每个 i，从 0..i-1 枚举 j：
   - 若 nums[i] > nums[j] 且 len_dp[j] + 1 > len_dp[i]：
       更新 len_dp[i] = len_dp[j] + 1，cnt_dp[i] = cnt_dp[j]
   - 若 nums[i] > nums[j] 且 len_dp[j] + 1 == len_dp[i]：
       累加 cnt_dp[i] += cnt_dp[j]
5. 遍历 len_dp 找到全局最长长度 max_len，再将所有 len_dp[i] == max_len 的 cnt_dp[i] 累加即为答案

关键点:
- 同时维护“长度”和“个数”两个 DP 数组
- 当发现更长的序列时重置计数，长度相等时累加计数
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - 双重循环枚举子序列结尾
空间复杂度: O(n) - 两个长度为 n 的 DP 数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_number_of_lis(nums: List[int]) -> int:
    """
    函数式接口 - 最长递增子序列的个数
    """
    n = len(nums)
    if n == 0:
        return 0

    len_dp = [1] * n
    cnt_dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if len_dp[j] + 1 > len_dp[i]:
                    len_dp[i] = len_dp[j] + 1
                    cnt_dp[i] = cnt_dp[j]
                elif len_dp[j] + 1 == len_dp[i]:
                    cnt_dp[i] += cnt_dp[j]

    max_len = max(len_dp)
    return sum(c for l, c in zip(len_dp, cnt_dp) if l == max_len)


Solution = create_solution(find_number_of_lis)
