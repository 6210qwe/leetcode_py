# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2577
标题: Count Palindromic Subsequences
难度: hard
链接: https://leetcode.cn/problems/count-palindromic-subsequences/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2484. 统计回文子序列数目 - 给你数字字符串 s ，请你返回 s 中长度为 5 的 回文子序列 数目。由于答案可能很大，请你将答案对 109 + 7 取余 后返回。 提示： * 如果一个字符串从前往后和从后往前读相同，那么它是 回文字符串 。 * 子序列是一个字符串中删除若干个字符后，不改变字符顺序，剩余字符构成的字符串。 示例 1： 输入：s = "103301" 输出：2 解释： 总共有 6 长度为 5 的子序列："10330" ，"10331" ，"10301" ，"10301" ，"13301" ，"03301" 。 它们中有两个（都是 "10301"）是回文的。 示例 2： 输入：s = "0000000" 输出：21 解释：所有 21 个长度为 5 的子序列都是 "00000" ，都是回文的。 示例 3： 输入：s = "9999900000" 输出：2 解释：仅有的两个回文子序列是 "99999" 和 "00000" 。 提示： * 1 <= s.length <= 104 * s 只包含数字字符。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来统计长度为5的回文子序列。

算法步骤:
1. 初始化一个三维数组 dp，其中 dp[i][j][k] 表示从 i 到 j 的子串中，以 k 为中间字符的回文子序列数目。
2. 遍历字符串 s，对于每个字符 s[i]，更新 dp 数组。
3. 最后，累加 dp 数组中所有长度为5的回文子序列数目。

关键点:
- 使用动态规划来避免重复计算。
- 通过预处理前缀和来快速计算子串中的字符出现次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是字符串 s 的长度。
空间复杂度: O(n^2)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_palindromic_subsequences(s: str) -> int:
    MOD = 10**9 + 7
    n = len(s)
    if n < 5:
        return 0

    # 前缀和数组，prefix_count[i][d] 表示从 0 到 i-1 的子串中字符 d 出现的次数
    prefix_count = [[0] * 10 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for d in range(10):
            prefix_count[i][d] = prefix_count[i - 1][d]
        prefix_count[i][int(s[i - 1])] += 1

    # dp[i][j][k] 表示从 i 到 j 的子串中，以 k 为中间字符的回文子序列数目
    dp = [[[0] * 10 for _ in range(n)] for _ in range(n)]

    # 初始化 dp 数组
    for i in range(n):
        dp[i][i][int(s[i])] = 1

    # 动态规划填表
    for length in range(2, 6):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(10):
                if s[i] == str(k):
                    dp[i][j][k] = (dp[i][j][k] + prefix_count[j + 1][k] - prefix_count[i + 1][k]) % MOD
                if s[j] == str(k):
                    dp[i][j][k] = (dp[i][j][k] + prefix_count[j][k] - prefix_count[i][k]) % MOD
                if s[i] == s[j] == str(k):
                    dp[i][j][k] = (dp[i][j][k] - (prefix_count[j + 1][k] - prefix_count[i + 1][k])) % MOD
                dp[i][j][k] = (dp[i][j][k] + dp[i + 1][j - 1][k]) % MOD

    # 计算结果
    result = 0
    for i in range(n - 4):
        for k in range(10):
            result = (result + dp[i][i + 4][k]) % MOD

    return result


Solution = create_solution(count_palindromic_subsequences)