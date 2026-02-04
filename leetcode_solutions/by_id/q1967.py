# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1967
标题: Longest Substring Of All Vowels in Order
难度: medium
链接: https://leetcode.cn/problems/longest-substring-of-all-vowels-in-order/
题目类型: 字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1839. 所有元音按顺序排布的最长子字符串 - 当一个字符串满足如下条件时，我们称它是 美丽的 ： * 所有 5 个英文元音字母（'a' ，'e' ，'i' ，'o' ，'u'）都必须 至少 出现一次。 * 这些元音字母的顺序都必须按照 字典序 升序排布（也就是说所有的 'a' 都在 'e' 前面，所有的 'e' 都在 'i' 前面，以此类推） 比方说，字符串 "aeiou" 和 "aaaaaaeiiiioou" 都是 美丽的 ，但是 "uaeio" ，"aeoiu" 和 "aaaeeeooo" 不是美丽的 。 给你一个只包含英文元音字母的字符串 word ，请你返回 word 中 最长美丽子字符串的长度 。如果不存在这样的子字符串，请返回 0 。 子字符串 是字符串中一个连续的字符序列。 示例 1： 输入：word = "aeiaaioaaaaeiiiiouuuooaauuaeiu" 输出：13 解释：最长子字符串是 "aaaaeiiiiouuu" ，长度为 13 。 示例 2： 输入：word = "aeeeiiiioooauuuaeiou" 输出：5 解释：最长子字符串是 "aeiou" ，长度为 5 。 示例 3： 输入：word = "a" 输出：0 解释：没有美丽子字符串，所以返回 0 。 提示： * 1 <= word.length <= 5 * 105 * word 只包含字符 'a'，'e'，'i'，'o' 和 'u' 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到所有元音按顺序排布的最长子字符串。

算法步骤:
1. 初始化两个指针 `left` 和 `right`，分别指向当前窗口的起始和结束位置。
2. 遍历字符串 `word`，使用 `right` 指针扩展窗口。
3. 如果当前字符不是下一个期望的元音字母，则重置 `left` 指针到 `right` 位置。
4. 如果当前窗口包含了所有五个元音字母且顺序正确，则更新最长子字符串的长度。
5. 返回最长美丽子字符串的长度。

关键点:
- 使用滑动窗口来维护当前的子字符串，并检查其是否包含所有五个元音字母且顺序正确。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 `word` 的长度。每个字符最多被处理两次（一次通过 `right` 指针，一次通过 `left` 指针）。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_beautiful_substring(word: str) -> int:
    """
    返回 word 中最长美丽子字符串的长度。
    """
    if len(word) < 5:
        return 0

    vowels = "aeiou"
    max_length = 0
    left = 0
    right = 0
    current_vowel_index = 0

    while right < len(word):
        if word[right] == vowels[current_vowel_index]:
            if current_vowel_index == 4:
                max_length = max(max_length, right - left + 1)
            right += 1
        else:
            if word[right] == vowels[current_vowel_index + 1]:
                current_vowel_index += 1
                right += 1
            else:
                left = right
                current_vowel_index = 0
                if word[left] == 'a':
                    current_vowel_index = 1
                    right = left + 1
                else:
                    right += 1

    return max_length


Solution = create_solution(longest_beautiful_substring)