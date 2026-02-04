# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2854
标题: Decremental String Concatenation
难度: medium
链接: https://leetcode.cn/problems/decremental-string-concatenation/
题目类型: 数组、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2746. 字符串连接删减字母 - 给你一个下标从 0 开始的数组 words ，它包含 n 个字符串。 定义 连接 操作 join(x, y) 表示将字符串 x 和 y 连在一起，得到 xy 。如果 x 的最后一个字符与 y 的第一个字符相等，连接后两个字符中的一个会被 删除 。 比方说 join("ab", "ba") = "aba" ， join("ab", "cde") = "abcde" 。 你需要执行 n - 1 次 连接 操作。令 str0 = words[0] ，从 i = 1 直到 i = n - 1 ，对于第 i 个操作，你可以执行以下操作之一： * 令 stri = join(stri - 1, words[i]) * 令 stri = join(words[i], stri - 1) 你的任务是使 strn - 1 的长度 最小 。 请你返回一个整数，表示 strn - 1 的最小长度。 示例 1： 输入：words = ["aa","ab","bc"] 输出：4 解释：这个例子中，我们按以下顺序执行连接操作，得到 str2 的最小长度： str0 = "aa" str1 = join(str0, "ab") = "aab" str2 = join(str1, "bc") = "aabc" str2 的最小长度为 4 。 示例 2： 输入：words = ["ab","b"] 输出：2 解释：这个例子中，str0 = "ab"，可以得到两个不同的 str1： join(str0, "b") = "ab" 或者 join("b", str0) = "bab" 。 第一个字符串 "ab" 的长度最短，所以答案为 2 。 示例 3： 输入：words = ["aaa","c","aba"] 输出：6 解释：这个例子中，我们按以下顺序执行连接操作，得到 str2 的最小长度： str0 = "aaa" str1 = join(str0, "c") = "aaac" str2 = join("aba", str1) = "abaaac" str2 的最小长度为 6 。 提示： * 1 <= words.length <= 1000 * 1 <= words[i].length <= 50 * words[i] 中只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来记录每个子问题的最优解。

算法步骤:
1. 初始化一个二维数组 dp，其中 dp[i][j] 表示以 words[i] 为前缀且最后一个字符为 j 的最小长度。
2. 遍历每个单词，更新 dp 数组。
3. 返回最终结果。

关键点:
- 使用动态规划来避免重复计算。
- 通过比较不同连接方式的结果来更新 dp 数组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * 26^2)，其中 n 是 words 的长度，26 是字母表的大小。
空间复杂度: O(n * 26)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def minimum_string_length(words: List[str]) -> int:
    n = len(words)
    # dp[i][j] 表示以 words[i] 为前缀且最后一个字符为 j 的最小长度
    dp = [[float('inf')] * 26 for _ in range(n)]
    
    # 初始化第一个单词
    for j in range(26):
        if j == ord(words[0][-1]) - ord('a'):
            dp[0][j] = len(words[0])
        else:
            dp[0][j] = float('inf')
    
    for i in range(1, n):
        word = words[i]
        first_char = ord(word[0]) - ord('a')
        last_char = ord(word[-1]) - ord('a')
        
        for j in range(26):
            # 连接方式1: words[i] + prev
            if j == last_char:
                dp[i][j] = min(dp[i][j], dp[i-1][first_char] + len(word) - 1)
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][first_char] + len(word))
            
            # 连接方式2: prev + words[i]
            if j == first_char:
                dp[i][j] = min(dp[i][j], dp[i-1][last_char] + len(word) - 1)
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][last_char] + len(word))
    
    return min(dp[n-1])

Solution = create_solution(minimum_string_length)