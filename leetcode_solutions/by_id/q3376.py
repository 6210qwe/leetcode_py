# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3376
标题: Longest Common Suffix Queries
难度: hard
链接: https://leetcode.cn/problems/longest-common-suffix-queries/
题目类型: 字典树、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3093. 最长公共后缀查询 - 给你两个字符串数组 wordsContainer 和 wordsQuery 。 对于每个 wordsQuery[i] ，你需要从 wordsContainer 中找到一个与 wordsQuery[i] 有 最长公共后缀 的字符串。如果 wordsContainer 中有两个或者更多字符串有最长公共后缀，那么答案为长度 最短 的。如果有超过两个字符串有 相同 最短长度，那么答案为它们在 wordsContainer 中出现 更早 的一个。 请你返回一个整数数组 ans ，其中 ans[i]是 wordsContainer中与 wordsQuery[i] 有 最长公共后缀 字符串的下标。 示例 1： 输入：wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"] 输出：[1,1,1] 解释： 我们分别来看每一个 wordsQuery[i] ： * 对于 wordsQuery[0] = "cd" ，wordsContainer 中有最长公共后缀 "cd" 的字符串下标分别为 0 ，1 和 2 。这些字符串中，答案是下标为 1 的字符串，因为它的长度为 3 ，是最短的字符串。 * 对于 wordsQuery[1] = "bcd" ，wordsContainer 中有最长公共后缀 "bcd" 的字符串下标分别为 0 ，1 和 2 。这些字符串中，答案是下标为 1 的字符串，因为它的长度为 3 ，是最短的字符串。 * 对于 wordsQuery[2] = "xyz" ，wordsContainer 中没有字符串跟它有公共后缀，所以最长公共后缀为 "" ，下标为 0 ，1 和 2 的字符串都得到这一公共后缀。这些字符串中， 答案是下标为 1 的字符串，因为它的长度为 3 ，是最短的字符串。 示例 2： 输入：wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"] 输出：[2,0,2] 解释： 我们分别来看每一个 wordsQuery[i] ： * 对于 wordsQuery[0] = "gh" ，wordsContainer 中有最长公共后缀 "gh" 的字符串下标分别为 0 ，1 和 2 。这些字符串中，答案是下标为 2 的字符串，因为它的长度为 6 ，是最短的字符串。 * 对于 wordsQuery[1] = "acbfgh" ，只有下标为 0 的字符串有最长公共后缀 "fgh" 。所以尽管下标为 2 的字符串是最短的字符串，但答案是 0 。 * 对于 wordsQuery[2] = "acbfegh" ，wordsContainer 中有最长公共后缀 "gh" 的字符串下标分别为 0 ，1 和 2 。这些字符串中，答案是下标为 2 的字符串，因为它的长度为 6 ，是最短的字符串。 提示： * 1 <= wordsContainer.length, wordsQuery.length <= 104 * 1 <= wordsContainer[i].length <= 5 * 103 * 1 <= wordsQuery[i].length <= 5 * 103 * wordsContainer[i] 只包含小写英文字母。 * wordsQuery[i] 只包含小写英文字母。 * wordsContainer[i].length 的和至多为 5 * 105 。 * wordsQuery[i].length 的和至多为 5 * 105 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储 wordsContainer 中的字符串，并在 Trie 中进行查询。

算法步骤:
1. 构建 Trie 树，将 wordsContainer 中的每个字符串反向插入到 Trie 中。
2. 对于每个 wordsQuery 中的字符串，反向遍历 Trie 树，找到最长公共后缀。
3. 如果有多个字符串具有相同的最长公共后缀，则选择最短的那个；如果长度相同，则选择最早出现的那个。

关键点:
- 反向插入字符串以方便查找最长公共后缀。
- 在 Trie 节点中存储最短的字符串及其索引。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m + q * k)，其中 n 是 wordsContainer 的长度，m 是 wordsContainer 中字符串的平均长度，q 是 wordsQuery 的长度，k 是 wordsQuery 中字符串的平均长度。
空间复杂度: O(n * m)，用于存储 Trie 树。
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
        self.length = float('inf')

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index):
        node = self.root
        for char in reversed(word):
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if len(word) < node.length:
                node.length = len(word)
                node.index = index

    def search(self, word):
        node = self.root
        for char in reversed(word):
            if char not in node.children:
                break
            node = node.children[char]
        return node.index if node.index != -1 else 0

def longest_common_suffix_queries(wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
    trie = Trie()
    for i, word in enumerate(wordsContainer):
        trie.insert(word, i)

    result = []
    for query in wordsQuery:
        result.append(trie.search(query))

    return result

Solution = create_solution(longest_common_suffix_queries)