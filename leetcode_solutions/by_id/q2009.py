# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2009
标题: Longest Word With All Prefixes
难度: medium
链接: https://leetcode.cn/problems/longest-word-with-all-prefixes/
题目类型: 深度优先搜索、字典树、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1858. 包含所有前缀的最长单词 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储所有单词，并在插入过程中检查每个前缀是否已经存在于字典树中。

算法步骤:
1. 构建一个字典树类，包含插入和查找方法。
2. 遍历所有单词，依次插入字典树，并在插入过程中检查每个前缀是否已经存在。
3. 如果某个单词的所有前缀都存在，则更新最长单词。

关键点:
- 使用字典树可以高效地存储和查找前缀。
- 在插入过程中检查每个前缀是否存在。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是单词的数量，m 是单词的最大长度。
空间复杂度: O(n * m)，字典树的空间复杂度取决于单词的数量和长度。
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

    def insert(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        return True

    def search_prefix(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def solution_function_name(words: List[str]) -> str:
    """
    函数式接口 - 找到包含所有前缀的最长单词
    """
    trie = Trie()
    longest_word = ""
    
    for word in words:
        is_valid = True
        for i in range(1, len(word) + 1):
            if not trie.search_prefix(word[:i]):
                is_valid = False
                break
        if is_valid:
            if len(word) > len(longest_word):
                longest_word = word
        trie.insert(word)
    
    return longest_word

Solution = create_solution(solution_function_name)