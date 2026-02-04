# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 524
标题: Longest Word in Dictionary through Deleting
难度: medium
链接: https://leetcode.cn/problems/longest-word-in-dictionary-through-deleting/
题目类型: 数组、双指针、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
524. 通过删除字母匹配到字典里最长单词 - 给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。 如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。 示例 1： 输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"] 输出："apple" 示例 2： 输入：s = "abpcplea", dictionary = ["a","b","c"] 输出："a" 提示： * 1 <= s.length <= 1000 * 1 <= dictionary.length <= 1000 * 1 <= dictionary[i].length <= 1000 * s 和 dictionary[i] 仅由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针方法来检查每个字典中的单词是否是 s 的子序列，并记录最长且字母序最小的单词。

算法步骤:
1. 对字典进行排序，首先按长度降序，然后按字母序升序。
2. 遍历排序后的字典，使用双指针方法检查每个单词是否是 s 的子序列。
3. 如果找到一个满足条件的单词，立即返回该单词。
4. 如果遍历完字典没有找到满足条件的单词，返回空字符串。

关键点:
- 排序字典以确保优先返回最长且字母序最小的单词。
- 使用双指针方法高效地检查子序列关系。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m + k log k)，其中 n 是 s 的长度，m 是 dictionary 中单词的平均长度，k 是 dictionary 的长度。排序操作的时间复杂度为 O(k log k)，双指针检查子序列的时间复杂度为 O(n * m)。
空间复杂度: O(1)，除了输入和输出外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_longest_word(s: str, dictionary: List[str]) -> str:
    """
    函数式接口 - 找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
    如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。
    """
    # 对字典进行排序，首先按长度降序，然后按字母序升序
    dictionary.sort(key=lambda x: (-len(x), x))
    
    def is_subsequence(word: str, s: str) -> bool:
        """检查 word 是否是 s 的子序列"""
        i, j = 0, 0
        while i < len(word) and j < len(s):
            if word[i] == s[j]:
                i += 1
            j += 1
        return i == len(word)
    
    # 遍历排序后的字典，使用双指针方法检查每个单词是否是 s 的子序列
    for word in dictionary:
        if is_subsequence(word, s):
            return word
    
    # 如果遍历完字典没有找到满足条件的单词，返回空字符串
    return ""


Solution = create_solution(find_longest_word)