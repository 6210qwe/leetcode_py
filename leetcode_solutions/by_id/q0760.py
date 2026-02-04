# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 760
标题: Bold Words in String
难度: medium
链接: https://leetcode.cn/problems/bold-words-in-string/
题目类型: 字典树、数组、哈希表、字符串、字符串匹配
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一个单词列表和一个字符串，找到所有在字符串中出现的单词，并将这些单词加粗。返回加粗后的字符串。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储单词列表，然后遍历字符串，使用滑动窗口的方法查找所有匹配的单词。

算法步骤:
1. 构建字典树，将所有单词插入字典树。
2. 遍历字符串，使用滑动窗口查找所有匹配的单词，并记录每个字符是否需要加粗。
3. 根据记录的加粗标记，构建最终的加粗字符串。

关键点:
- 使用字典树高效地查找单词。
- 使用滑动窗口避免重复查找。
- 记录每个字符是否需要加粗，最后一次性构建结果字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m + k)，其中 n 是字符串的长度，m 是单词的最大长度，k 是单词列表的长度。
空间复杂度: O(k * m)，字典树的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

def find_bold_words(s: str, words: List[str]) -> str:
    """
    函数式接口 - 找到并加粗字符串中的所有单词
    """
    # 构建字典树
    trie = Trie()
    for word in words:
        trie.insert(word)

    # 记录每个字符是否需要加粗
    bold = [False] * len(s)
    
    # 滑动窗口查找所有匹配的单词
    for i in range(len(s)):
        node = trie.root
        j = i
        while j < len(s) and s[j] in node.children:
            node = node.children[s[j]]
            if node.is_end_of_word:
                for k in range(i, j + 1):
                    bold[k] = True
            j += 1

    # 构建最终的加粗字符串
    result = []
    for i in range(len(s)):
        if bold[i] and (i == 0 or not bold[i - 1]):
            result.append("<b>")
        result.append(s[i])
        if bold[i] and (i == len(s) - 1 or not bold[i + 1]):
            result.append("</b>")

    return "".join(result)

Solution = create_solution(find_bold_words)