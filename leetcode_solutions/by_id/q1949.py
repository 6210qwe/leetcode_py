# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1949
标题: Implement Trie II (Prefix Tree)
难度: medium
链接: https://leetcode.cn/problems/implement-trie-ii-prefix-tree/
题目类型: 设计、字典树、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1804. 实现 Trie （前缀树）II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用嵌套字典来实现 Trie，并在每个节点上记录插入和删除的次数。

算法步骤:
1. 初始化 Trie 根节点为空字典，并初始化插入和删除计数器。
2. 插入单词时，遍历每个字符，更新路径上的节点，并增加插入计数。
3. 删除单词时，遍历每个字符，更新路径上的节点，并减少删除计数。
4. 查询单词时，遍历每个字符，检查路径上的节点，并返回最终节点的插入计数减去删除计数。
5. 查询前缀时，遍历每个字符，检查路径上的节点，并返回最终节点的插入计数减去删除计数。

关键点:
- 使用嵌套字典来表示 Trie 节点。
- 在每个节点上记录插入和删除的次数。
- 查询时，返回插入计数减去删除计数的结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(L)，其中 L 是单词的长度。每次插入、删除或查询操作的时间复杂度都是线性的。
空间复杂度: O(N * L)，其中 N 是插入的单词数量，L 是单词的平均长度。每个单词需要存储其路径上的所有节点。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional


class Trie:
    def __init__(self):
        self.root = {}
        self.insert_count = 0
        self.delete_count = 0

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        if 'end' not in node:
            node['end'] = 0
        node['end'] += 1
        self.insert_count += 1

    def delete(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                return
            node = node[char]
        if 'end' in node and node['end'] > 0:
            node['end'] -= 1
            self.delete_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node:
                return 0
            node = node[char]
        return node.get('end', 0) - self.delete_count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node:
                return 0
            node = node[char]
        return self._count_all_words(node)

    def _count_all_words(self, node: dict) -> int:
        count = 0
        if 'end' in node:
            count += node['end']
        for char in node:
            if char != 'end':
                count += self._count_all_words(node[char])
        return count - self.delete_count

    def erase(self, word: str) -> None:
        self.delete(word)


Solution = create_solution(Trie)