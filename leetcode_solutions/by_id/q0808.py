# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 808
标题: Number of Matching Subsequences
难度: medium
链接: https://leetcode.cn/problems/number-of-matching-subsequences/
题目类型: 字典树、数组、哈希表、字符串、二分查找、动态规划、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
792. 匹配子序列的单词数 - 给定字符串 s 和字符串数组 words, 返回 words[i] 中是s的子序列的单词个数 。 字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。 * 例如， “ace” 是 “abcde” 的子序列。 示例 1: 输入: s = "abcde", words = ["a","bb","acd","ace"] 输出: 3 解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。 Example 2: 输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"] 输出: 2 提示: * 1 <= s.length <= 5 * 104 * 1 <= words.length <= 5000 * 1 <= words[i].length <= 50 * words[i]和 s 都只由小写字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典存储每个字母在字符串 s 中出现的位置，然后遍历 words 数组，检查每个 word 是否是 s 的子序列。

算法步骤:
1. 构建一个字典，键为 s 中的每个字符，值为该字符在 s 中出现的所有位置。
2. 对于每个 word，使用双指针方法检查其是否是 s 的子序列：
   - 初始化两个指针，一个指向 word 的当前字符，另一个指向 s 的当前字符位置。
   - 遍历 word 的每个字符，如果在 s 中找到该字符，则移动 s 的指针；否则，word 不是 s 的子序列。
3. 统计所有是 s 的子序列的 word 的数量。

关键点:
- 使用字典存储字符位置，减少查找时间。
- 使用双指针方法高效检查子序列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m * k)，其中 n 是 s 的长度，m 是 words 的长度，k 是每个 word 的平均长度。
空间复杂度: O(n)，用于存储 s 中每个字符的位置。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def num_matching_subseq(s: str, words: List[str]) -> int:
    """
    函数式接口 - 计算 words 中是 s 的子序列的单词个数
    """
    # 构建字符位置字典
    char_indices = {}
    for i, char in enumerate(s):
        if char not in char_indices:
            char_indices[char] = []
        char_indices[char].append(i)

    def is_subsequence(word: str) -> bool:
        current_index = -1
        for char in word:
            if char not in char_indices:
                return False
            indices = char_indices[char]
            pos = bisect.bisect_right(indices, current_index)
            if pos == len(indices):
                return False
            current_index = indices[pos]
        return True

    # 统计子序列的数量
    count = 0
    for word in words:
        if is_subsequence(word):
            count += 1

    return count


Solution = create_solution(num_matching_subseq)