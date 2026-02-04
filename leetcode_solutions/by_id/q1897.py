# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1897
标题: Maximize Palindrome Length From Subsequences
难度: hard
链接: https://leetcode.cn/problems/maximize-palindrome-length-from-subsequences/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1771. 由子序列构造的最长回文串的长度 - 给你两个字符串 word1 和 word2 ，请你按下述方法构造一个字符串： * 从 word1 中选出某个 非空 子序列 subsequence1 。 * 从 word2 中选出某个 非空 子序列 subsequence2 。 * 连接两个子序列 subsequence1 + subsequence2 ，得到字符串。 返回可按上述方法构造的最长 回文串 的 长度 。如果无法构造回文串，返回 0 。 字符串 s 的一个 子序列 是通过从 s 中删除一些（也可能不删除）字符而不更改其余字符的顺序生成的字符串。 回文串 是正着读和反着读结果一致的字符串。 示例 1： 输入：word1 = "cacb", word2 = "cbba" 输出：5 解释：从 word1 中选出 "ab" ，从 word2 中选出 "cba" ，得到回文串 "abcba" 。 示例 2： 输入：word1 = "ab", word2 = "ab" 输出：3 解释：从 word1 中选出 "ab" ，从 word2 中选出 "a" ，得到回文串 "aba" 。 示例 3： 输入：word1 = "aa", word2 = "bb" 输出：0 解释：无法按题面所述方法构造回文串，所以返回 0 。 提示： * 1 <= word1.length, word2.length <= 1000 * word1 和 word2 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i][j] 表示从 word1 的第 i 个字符到 word2 的第 j 个字符之间可以构成的最长回文子序列的长度。

算法步骤:
1. 初始化 dp 数组，dp[i][j] 表示从 word1 的第 i 个字符到 word2 的第 j 个字符之间可以构成的最长回文子序列的长度。
2. 遍历 word1 和 word2 的所有字符，更新 dp 数组。
3. 最后，找到 dp 数组中最大的值，即为所求的最长回文子序列的长度。

关键点:
- 动态规划的状态转移方程：dp[i][j] = max(dp[i+1][j], dp[i][j-1]) if word1[i] != word2[j] else 2 + dp[i+1][j-1]
- 边界条件：dp[i][i] = 1，表示单个字符本身就是回文
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 和 m 分别是 word1 和 word2 的长度。
空间复杂度: O(n * m)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(word1: str, word2: str) -> int:
    """
    函数式接口 - 计算由子序列构造的最长回文串的长度
    """
    n, m = len(word1), len(word2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 初始化 dp 数组
    for i in range(n):
        dp[i][m] = 1
    for j in range(m):
        dp[n][j] = 1
    
    # 填充 dp 数组
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = 2 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    
    # 找到最大值
    max_length = 0
    for i in range(n):
        for j in range(m):
            if word1[i] == word2[j]:
                max_length = max(max_length, 2 + dp[i + 1][j + 1])
    
    return max_length


Solution = create_solution(solution_function_name)