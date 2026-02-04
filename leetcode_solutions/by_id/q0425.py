# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 425
标题: Word Squares
难度: hard
链接: https://leetcode.cn/problems/word-squares/
题目类型: 字典树、数组、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
425. 单词方块 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）和回溯法来生成单词方块

算法步骤:
1. 构建字典树（Trie），将所有单词插入字典树中
2. 使用回溯法生成单词方块
3. 在回溯过程中，利用字典树快速查找前缀匹配的单词

关键点:
- 使用字典树优化前缀匹配的时间复杂度
- 通过回溯法生成所有可能的单词方块
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(N * M^2) - N 是单词的数量，M 是单词的长度
空间复杂度: O(N * M) - 存储字典树和递归调用栈
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word)

    def starts_with(self, prefix: str) -> List[str]:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.words

def word_squares(words: List[str]) -> List[List[str]]:
    """
    函数式接口 - 生成单词方块
    
    实现思路:
    使用字典树（Trie）和回溯法来生成单词方块
    
    Args:
        words: 单词列表
        
    Returns:
        所有可能的单词方块列表
        
    Example:
        >>> word_squares(["area", "lead", "wall", "lady", "ball"])
        [["wall", "area", "lead", "lady"], ["ball", "area", "lead", "lady"]]
    """
    def backtrack(path: List[str], res: List[List[str]], trie: Trie, n: int) -> None:
        if len(path) == n:
            res.append(path[:])
            return
        prefix = ''.join([path[i][len(path)] for i in range(len(path))])
        for word in trie.starts_with(prefix):
            path.append(word)
            backtrack(path, res, trie, n)
            path.pop()

    n = len(words[0])
    trie = Trie()
    for word in words:
        trie.insert(word)

    res = []
    for word in words:
        backtrack([word], res, trie, n)
    return res

# 自动生成Solution类（无需手动编写）
Solution = create_solution(word_squares)