# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3356
标题: Shortest Uncommon Substring in an Array
难度: medium
链接: https://leetcode.cn/problems/shortest-uncommon-substring-in-an-array/
题目类型: 字典树、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3076. 数组中的最短非公共子字符串 - 给你一个数组 arr ，数组中有 n 个 非空 字符串。 请你求出一个长度为 n 的字符串数组 answer ，满足： * answer[i] 是 arr[i] 最短 的子字符串，且它不是 arr 中其他任何字符串的子字符串。如果有多个这样的子字符串存在，answer[i] 应该是它们中字典序最小的一个。如果不存在这样的子字符串，answer[i] 为空字符串。 请你返回数组 answer 。 示例 1： 输入：arr = ["cab","ad","bad","c"] 输出：["ab","","ba",""] 解释：求解过程如下： - 对于字符串 "cab" ，最短没有在其他字符串中出现过的子字符串是 "ca" 或者 "ab" ，我们选择字典序更小的子字符串，也就是 "ab" 。 - 对于字符串 "ad" ，不存在没有在其他字符串中出现过的子字符串。 - 对于字符串 "bad" ，最短没有在其他字符串中出现过的子字符串是 "ba" 。 - 对于字符串 "c" ，不存在没有在其他字符串中出现过的子字符串。 示例 2： 输入：arr = ["abc","bcd","abcd"] 输出：["","","abcd"] 解释：求解过程如下： - 对于字符串 "abc" ，不存在没有在其他字符串中出现过的子字符串。 - 对于字符串 "bcd" ，不存在没有在其他字符串中出现过的子字符串。 - 对于字符串 "abcd" ，最短没有在其他字符串中出现过的子字符串是 "abcd" 。 提示： * n == arr.length * 2 <= n <= 100 * 1 <= arr[i].length <= 20 * arr[i] 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储所有字符串的所有子字符串，并通过遍历字典树找到每个字符串的最短非公共子字符串。

算法步骤:
1. 构建字典树，将所有字符串的所有子字符串插入字典树中。
2. 遍历每个字符串的所有子字符串，检查其是否在字典树中只出现一次。
3. 找到每个字符串的最短非公共子字符串，并选择字典序最小的一个。

关键点:
- 使用字典树高效地存储和查找子字符串。
- 通过遍历字典树找到每个字符串的最短非公共子字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m^2)，其中 n 是数组的长度，m 是字符串的最大长度。构建字典树的时间复杂度为 O(n * m^2)，查找每个字符串的最短非公共子字符串的时间复杂度为 O(m^2)。
空间复杂度: O(n * m^2)，字典树的空间复杂度。
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
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def search(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count

def find_shortest_uncommon_substring(arr: List[str]) -> List[str]:
    trie = Trie()
    for s in arr:
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                trie.insert(s[i:j])

    result = []
    for s in arr:
        shortest = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if trie.search(sub) == 1:
                    if shortest == "" or len(sub) < len(shortest) or (len(sub) == len(shortest) and sub < shortest):
                        shortest = sub
        result.append(shortest)
    return result

Solution = create_solution(find_shortest_uncommon_substring)