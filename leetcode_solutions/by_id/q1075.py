# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1075
标题: Index Pairs of a String
难度: easy
链接: https://leetcode.cn/problems/index-pairs-of-a-string/
题目类型: 字典树、数组、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一个文本字符串 text 和一个单词列表 words，返回所有索引对 [i, j] 使得 text[i...j]（包括 i 和 j）是 words 中的某个单词。答案可以以任意顺序返回。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储单词列表，并在文本中查找这些单词。

算法步骤:
1. 构建字典树，将单词列表中的每个单词插入到字典树中。
2. 遍历文本字符串，对于每个字符，尝试从该字符开始在字典树中查找单词。
3. 如果找到一个单词，则记录其起始和结束索引。

关键点:
- 使用字典树可以高效地查找前缀。
- 在遍历文本时，使用双指针来记录当前匹配的起始位置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m + k)，其中 n 是文本字符串的长度，m 是单词列表中单词的平均长度，k 是单词列表的长度。
空间复杂度: O(k * m)，字典树的空间复杂度取决于单词列表的大小。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

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

    def search(self, text: str, start: int) -> List[List[int]]:
        node = self.root
        results = []
        for end in range(start, len(text)):
            if text[end] not in node.children:
                break
            node = node.children[text[end]]
            if node.is_end_of_word:
                results.append([start, end])
        return results

def index_pairs(text: str, words: List[str]) -> List[List[int]]:
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    results = []
    for start in range(len(text)):
        results.extend(trie.search(text, start))
    return results

Solution = create_solution(index_pairs)