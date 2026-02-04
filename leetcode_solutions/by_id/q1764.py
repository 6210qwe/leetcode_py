# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1764
标题: Maximum Repeating Substring
难度: easy
链接: https://leetcode.cn/problems/maximum-repeating-substring/
题目类型: 字符串、动态规划、字符串匹配
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1668. 最大重复子字符串 - 给你一个字符串 sequence ，如果字符串 word 连续重复 k 次形成的字符串是 sequence 的一个子字符串，那么单词 word 的 重复值为 k 。单词 word 的 最大重复值 是单词 word 在 sequence 中最大的重复值。如果 word 不是 sequence 的子串，那么重复值 k 为 0 。 给你一个字符串 sequence 和 word ，请你返回 最大重复值 k 。 示例 1： 输入：sequence = "ababc", word = "ab" 输出：2 解释："abab" 是 "ababc" 的子字符串。 示例 2： 输入：sequence = "ababc", word = "ba" 输出：1 解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。 示例 3： 输入：sequence = "ababc", word = "ac" 输出：0 解释："ac" 不是 "ababc" 的子字符串。 提示： * 1 <= sequence.length <= 100 * 1 <= word.length <= 100 * sequence 和 word 都只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 KMP 算法来查找最大重复子字符串。

算法步骤:
1. 构建 KMP 的部分匹配表 (prefix table)。
2. 使用 KMP 算法在 sequence 中查找 word 的所有出现位置。
3. 计算每个出现位置的最大重复值，并返回最大值。

关键点:
- 使用 KMP 算法可以高效地查找子字符串。
- 通过计算每个出现位置的最大重复值来找到最大重复值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 sequence 的长度，m 是 word 的长度。
空间复杂度: O(m)，用于存储 KMP 的部分匹配表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def build_prefix_table(pattern: str) -> List[int]:
    """
    构建 KMP 的部分匹配表
    """
    m = len(pattern)
    prefix_table = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            prefix_table[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix_table[length - 1]
            else:
                prefix_table[i] = 0
                i += 1
    return prefix_table

def kmp_search(text: str, pattern: str) -> List[int]:
    """
    使用 KMP 算法在 text 中查找 pattern 的所有出现位置
    """
    n, m = len(text), len(pattern)
    prefix_table = build_prefix_table(pattern)
    result = []
    i, j = 0, 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                result.append(i - j)
                j = prefix_table[j - 1]
        else:
            if j != 0:
                j = prefix_table[j - 1]
            else:
                i += 1
    return result

def max_repeating(sequence: str, word: str) -> int:
    """
    返回 word 在 sequence 中的最大重复值
    """
    positions = kmp_search(sequence, word)
    max_k = 0
    for pos in positions:
        k = 1
        while pos + k * len(word) <= len(sequence) and sequence[pos:pos + k * len(word)] == word * k:
            k += 1
        max_k = max(max_k, k - 1)
    return max_k

Solution = create_solution(max_repeating)