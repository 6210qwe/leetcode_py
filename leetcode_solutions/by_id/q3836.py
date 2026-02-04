# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3836
标题: Phone Number Prefix
难度: easy
链接: https://leetcode.cn/problems/phone-number-prefix/
题目类型: 字典树、数组、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3491. 电话号码前缀 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储电话号码，并在查询时快速找到前缀。

算法步骤:
1. 构建字典树：将所有电话号码插入字典树中。
2. 查询前缀：对于每个查询，从根节点开始遍历字典树，直到找到最长的前缀。

关键点:
- 使用字典树可以高效地存储和查询前缀。
- 每个节点存储一个字符，并且有一个标志位表示是否是一个完整的电话号码。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是电话号码的数量，m 是电话号码的最大长度。
空间复杂度: O(n * m)，字典树的空间复杂度取决于所有电话号码的总长度。
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

    def search_prefix(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def solution_function_name(phones: List[str], queries: List[str]) -> List[str]:
    """
    函数式接口 - 实现
    """
    trie = Trie()
    for phone in phones:
        trie.insert(phone)
    
    results = []
    for query in queries:
        for i in range(len(query), 0, -1):
            if trie.search_prefix(query[:i]):
                results.append(query[:i])
                break
        else:
            results.append("")
    return results

Solution = create_solution(solution_function_name)