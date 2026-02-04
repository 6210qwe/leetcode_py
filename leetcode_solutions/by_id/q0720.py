# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 720
标题: Longest Word in Dictionary
难度: medium
链接: https://leetcode.cn/problems/longest-word-in-dictionary/
题目类型: 字典树、数组、哈希表、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
720. 词典中最长的单词 - 给出一个字符串数组 words 组成的一本英语词典。返回能够通过 words 中其它单词逐步添加一个字母来构造得到的 words 中最长的单词。 若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。 请注意，单词应该从左到右构建，每个额外的字符都添加到前一个单词的结尾。 示例 1： 输入：words = ["w","wo","wor","worl", "world"] 输出："world" 解释： 单词"world"可由"w", "wo", "wor", 和 "worl"逐步添加一个字母组成。 示例 2： 输入：words = ["a", "banana", "app", "appl", "ap", "apply", "apple"] 输出："apple" 解释："apply" 和 "apple" 都能由词典中的单词组成。但是 "apple" 的字典序小于 "apply" 提示： * 1 <= words.length <= 1000 * 1 <= words[i].length <= 30 * 所有输入的字符串 words[i] 都只包含小写字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储所有单词，并在插入过程中检查每个单词是否可以通过逐步添加一个字母来构造。

算法步骤:
1. 构建字典树，将所有单词插入字典树。
2. 在插入过程中，检查每个单词的每个前缀是否已经在字典树中存在。
3. 如果存在，则继续插入；否则，该单词不能通过逐步添加一个字母来构造。
4. 最后，遍历字典树，找到最长且字典序最小的单词。

关键点:
- 使用字典树来高效地存储和查找单词及其前缀。
- 在插入过程中动态检查每个前缀是否存在。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是单词的数量，m 是单词的平均长度。每个单词的插入和查找操作的时间复杂度为 O(m)。
空间复杂度: O(n * m)，字典树的空间复杂度取决于所有单词的总长度。
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
                if not node.is_end_of_word:
                    return False
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        return True

def solution_function_name(words: List[str]) -> str:
    """
    函数式接口 - 返回能够通过逐步添加一个字母来构造得到的最长单词。
    """
    trie = Trie()
    valid_words = []
    
    # 插入单词并记录有效的单词
    for word in words:
        if trie.insert(word):
            valid_words.append(word)
    
    # 按长度降序和字典序升序排序
    valid_words.sort(key=lambda x: (-len(x), x))
    
    return valid_words[0] if valid_words else ""

Solution = create_solution(solution_function_name)