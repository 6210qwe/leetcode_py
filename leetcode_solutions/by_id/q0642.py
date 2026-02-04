# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 642
标题: Design Search Autocomplete System
难度: hard
链接: https://leetcode.cn/problems/design-search-autocomplete-system/
题目类型: 深度优先搜索、设计、字典树、字符串、数据流、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
642. 设计搜索自动补全系统 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储句子，并使用小顶堆来维护前缀匹配的句子。

算法步骤:
1. 初始化 Trie 和 小顶堆。
2. 在输入字符时，更新当前节点并检查是否需要更新小顶堆。
3. 当用户输入 '#' 时，将当前句子添加到 Trie 中，并重置当前节点和前缀。
4. 提供一个方法来获取前缀匹配的句子。

关键点:
- 使用 Trie 来高效存储和查找句子。
- 使用小顶堆来维护前缀匹配的句子，确保每次都能快速获取 top 3 的句子。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(L + k log k)，其中 L 是句子的长度，k 是前缀匹配的句子数量。
空间复杂度: O(N)，其中 N 是所有句子的总长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.data = None
        self.rank = 0

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.keyword = ""
        self.current_node = self.root
        self.build_trie(sentences, times)

    def build_trie(self, sentences: List[str], times: List[int]):
        for i, sentence in enumerate(sentences):
            self.insert(sentence, times[i])

    def insert(self, sentence: str, time: int):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.data = sentence
        node.rank -= time  # Use negative rank to simulate a min-heap

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.insert(self.keyword, 1)
            self.keyword = ""
            self.current_node = self.root
            return []

        self.keyword += c
        if self.current_node is None:
            return []

        if c not in self.current_node.children:
            self.current_node = None
            return []

        self.current_node = self.current_node.children[c]
        results = []
        self.dfs(self.current_node, results)
        return [item[1] for item in heapq.nsmallest(3, results)]

    def dfs(self, node, results):
        if node:
            if node.is_end:
                results.append((node.rank, node.data))
            for child in node.children.values():
                self.dfs(child, results)

# 示例用法
if __name__ == "__main__":
    sentences = ["i love you", "island", "ironman", "i love leetcode"]
    times = [5, 3, 2, 2]
    autocomplete_system = AutocompleteSystem(sentences, times)
    print(autocomplete_system.input('i'))  # 返回 ["i love you", "island", "i love leetcode"]
    print(autocomplete_system.input(' '))  # 返回 ["i love you", "i love leetcode"]
    print(autocomplete_system.input('a'))  # 返回 []
    print(autocomplete_system.input('#'))  # 返回 []，并将 "i love you" 添加到系统中
    print(autocomplete_system.input('i'))  # 返回 ["i love you", "island", "i love leetcode"]，顺序可以不同
    print(autocomplete_system.input(' '))  # 返回 ["i love you", "i love leetcode"]，顺序可以不同
    print(autocomplete_system.input('a'))  # 返回 []
    print(autocomplete_system.input('#'))  # 返回 []，并将 "i a" 添加到系统中