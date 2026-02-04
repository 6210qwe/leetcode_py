# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3570
标题: Count of Substrings Containing Every Vowel and K Consonants I
难度: medium
链接: https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3305. 元音辅音字符串计数 I - 给你一个字符串 word 和一个 非负 整数 k。 返回 word 的 子字符串 中，每个元音字母（'a'、'e'、'i'、'o'、'u'）至少 出现一次，并且 恰好 包含 k 个辅音字母的子字符串的总数。 示例 1： 输入：word = "aeioqq", k = 1 输出：0 解释： 不存在包含所有元音字母的子字符串。 示例 2： 输入：word = "aeiou", k = 0 输出：1 解释： 唯一一个包含所有元音字母且不含辅音字母的子字符串是 word[0..4]，即 "aeiou"。 示例 3： 输入：word = "ieaouqqieaouqq", k = 1 输出：3 解释： 包含所有元音字母并且恰好含有一个辅音字母的子字符串有： * word[0..5]，即 "ieaouq"。 * word[6..11]，即 "qieaou"。 * word[7..12]，即 "ieaouq"。 提示： * 5 <= word.length <= 250 * word 仅由小写英文字母组成。 * 0 <= k <= word.length - 5
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到满足条件的子字符串。

算法步骤:
1. 初始化两个指针 left 和 right，分别表示滑动窗口的左右边界。
2. 使用一个计数器来记录当前窗口内各个字符的数量。
3. 移动右指针扩展窗口，直到窗口内的子字符串包含所有元音字母。
4. 当窗口包含所有元音字母时，移动左指针收缩窗口，直到窗口不再包含所有元音字母。
5. 在每次移动右指针时，检查当前窗口内的辅音字母数量是否为 k，如果是，则计数加一。

关键点:
- 使用滑动窗口来高效地找到满足条件的子字符串。
- 通过计数器来快速判断窗口内是否包含所有元音字母和辅音字母的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 word 的长度。每个字符最多被访问两次（一次通过右指针，一次通过左指针）。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_vowels_and_consonants(word: str, k: int) -> int:
    """
    返回 word 的子字符串中，每个元音字母至少出现一次，并且恰好包含 k 个辅音字母的子字符串的总数。
    """
    vowels = set('aeiou')
    n = len(word)
    left, right = 0, 0
    vowel_count = 0
    consonant_count = 0
    result = 0
    char_count = [0] * 26

    while right < n:
        if word[right] in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
        char_count[ord(word[right]) - ord('a')] += 1

        while vowel_count == 5 and consonant_count > k:
            if word[left] in vowels:
                vowel_count -= 1
            else:
                consonant_count -= 1
            char_count[ord(word[left]) - ord('a')] -= 1
            left += 1

        if vowel_count == 5 and consonant_count == k:
            result += 1

        right += 1

    return result


Solution = create_solution(count_vowels_and_consonants)