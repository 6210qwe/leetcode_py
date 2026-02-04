# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3573
标题: Count Substrings That Can Be Rearranged to Contain a String I
难度: medium
链接: https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3297. 统计重新排列后包含另一个字符串的子字符串数目 I - 给你两个字符串 word1 和 word2 。 如果一个字符串 x 重新排列后，word2 是重排字符串的 前缀 ，那么我们称字符串 x 是 合法的 。 请你返回 word1 中 合法 子字符串 的数目。 示例 1： 输入：word1 = "bcca", word2 = "abc" 输出：1 解释： 唯一合法的子字符串是 "bcca" ，可以重新排列得到 "abcc" ，"abc" 是它的前缀。 示例 2： 输入：word1 = "abcabc", word2 = "abc" 输出：10 解释： 除了长度为 1 和 2 的所有子字符串都是合法的。 示例 3： 输入：word1 = "abcabc", word2 = "aaabc" 输出：0 解释： * 1 <= word1.length <= 105 * 1 <= word2.length <= 104 * word1 和 word2 都只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和哈希表来统计满足条件的子字符串。

算法步骤:
1. 初始化两个哈希表，分别记录 word2 中字符的频率和当前窗口中字符的频率。
2. 使用滑动窗口遍历 word1，窗口大小为 word2 的长度。
3. 在每次移动窗口时，更新窗口中的字符频率，并检查是否满足条件。
4. 如果满足条件，增加计数器。

关键点:
- 使用滑动窗口减少重复计算。
- 使用哈希表高效地比较字符频率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 word1 的长度，m 是 word2 的长度。
空间复杂度: O(1)，因为字符集是固定的（小写字母）。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_valid_substrings(word1: str, word2: str) -> int:
    """
    函数式接口 - 统计 word1 中可以重新排列成以 word2 为前缀的子字符串数目。
    """
    from collections import Counter

    # 如果 word2 比 word1 长，直接返回 0
    if len(word2) > len(word2):
        return 0

    # 计算 word2 中字符的频率
    target_freq = Counter(word2)
    window_freq = Counter()
    valid_count = 0
    n, m = len(word1), len(word2)

    # 初始化第一个窗口
    for i in range(m):
        window_freq[word1[i]] += 1

    # 检查初始窗口是否有效
    if window_freq == target_freq:
        valid_count += 1

    # 滑动窗口
    for i in range(m, n):
        window_freq[word1[i]] += 1
        window_freq[word1[i - m]] -= 1
        if window_freq[word1[i - m]] == 0:
            del window_freq[word1[i - m]]

        if window_freq == target_freq:
            valid_count += 1

    return valid_count


Solution = create_solution(count_valid_substrings)