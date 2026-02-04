# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000024
标题: Multi Search LCCI
难度: medium
链接: https://leetcode.cn/problems/multi-search-lcci/
题目类型: 字典树、数组、哈希表、字符串、字符串匹配、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 17.17. 多次搜索 - 给定一个较长字符串big和一个包含较短字符串的数组smalls，设计一个方法，根据smalls中的每一个较短字符串，对big进行搜索。输出smalls中的字符串在big里出现的所有位置positions，其中positions[i]为smalls[i]出现的所有位置。 示例： 输入： big = "mississippi" smalls = ["is","ppi","hi","sis","i","ssippi"] 输出： [[1,4],[8],[],[3],[1,4,7,10],[5]] 提示： * 0 <= len(big) <= 1000 * 0 <= len(smalls[i]) <= 1000 * smalls的总字符数不会超过 106。 * 你可以认为smalls中没有重复字符串。 * 所有出现的字符均为英文小写字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储所有的小字符串，然后遍历大字符串，查找每个子串在大字符串中的位置。

算法步骤:
1. 构建字典树，将所有小字符串插入到字典树中。
2. 遍历大字符串，对于每个起始位置，使用字典树查找该位置开始的所有子串。
3. 记录每个小字符串在大字符串中的位置。

关键点:
- 使用字典树可以高效地查找多个子串。
- 通过一次遍历大字符串，避免了多次重复扫描。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m * k)，其中 n 是 big 的长度，m 是 smalls 的长度，k 是 smalls 中最长字符串的长度。
空间复杂度: O(m * k)，字典树的空间复杂度取决于 smalls 的总字符数。
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
        self.index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, index: int):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.index = index

def multi_search(big: str, smalls: List[str]) -> List[List[int]]:
    trie = Trie()
    for i, small in enumerate(smalls):
        trie.insert(small, i)

    result = [[] for _ in range(len(smalls))]
    for i in range(len(big)):
        node = trie.root
        for j in range(i, len(big)):
            if big[j] not in node.children:
                break
            node = node.children[big[j]]
            if node.index != -1:
                result[node.index].append(i)
    return result

Solution = create_solution(multi_search)