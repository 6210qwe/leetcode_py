# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2605
标题: Count Anagrams
难度: hard
链接: https://leetcode.cn/problems/count-anagrams/
题目类型: 哈希表、数学、字符串、组合数学、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2514. 统计同位异构字符串数目 - 给你一个字符串 s ，它包含一个或者多个单词。单词之间用单个空格 ' ' 隔开。 如果字符串 t 中第 i 个单词是 s 中第 i 个单词的一个 排列 ，那么我们称字符串 t 是字符串 s 的同位异构字符串。 * 比方说，"acb dfe" 是 "abc def" 的同位异构字符串，但是 "def cab" 和 "adc bef" 不是。 请你返回 s 的同位异构字符串的数目，由于答案可能很大，请你将它对 109 + 7 取余 后返回。 示例 1： 输入：s = "too hot" 输出：18 解释：输入字符串的一些同位异构字符串为 "too hot" ，"oot hot" ，"oto toh" ，"too toh" 以及 "too oht" 。 示例 2： 输入：s = "aa" 输出：1 解释：输入字符串只有一个同位异构字符串。 提示： * 1 <= s.length <= 105 * s 只包含小写英文字母和空格 ' ' 。 * 相邻单词之间由单个空格隔开。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用排列组合公式计算每个单词的排列数，并乘以所有单词的排列数。

算法步骤:
1. 将字符串 s 按空格分割成单词列表。
2. 对于每个单词，计算其排列数。
3. 计算所有单词排列数的乘积，并对 10^9 + 7 取余。

关键点:
- 使用阶乘和组合公式计算排列数。
- 使用模运算防止结果溢出。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

MOD = 10**9 + 7

def factorial(n: int) -> int:
    """计算 n! 并对 MOD 取余"""
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % MOD
    return result

def inverse_factorial(n: int) -> int:
    """计算 n! 的逆元并对其取余"""
    return pow(factorial(n), MOD - 2, MOD)

def count_anagrams(s: str) -> int:
    """
    计算字符串 s 的同位异构字符串的数目，并对 10^9 + 7 取余
    """
    words = s.split()
    result = 1
    for word in words:
        char_count = [0] * 26
        for char in word:
            char_count[ord(char) - ord('a')] += 1
        
        # 计算当前单词的排列数
        word_permutations = factorial(len(word))
        for count in char_count:
            if count > 0:
                word_permutations = (word_permutations * inverse_factorial(count)) % MOD
        
        result = (result * word_permutations) % MOD
    
    return result

Solution = create_solution(count_anagrams)