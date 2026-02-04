# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2884
标题: Length of the Longest Valid Substring
难度: hard
链接: https://leetcode.cn/problems/length-of-the-longest-valid-substring/
题目类型: 数组、哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2781. 最长合法子字符串的长度 - 给你一个字符串 word 和一个字符串数组 forbidden 。 如果一个字符串不包含 forbidden 中的任何字符串，我们称这个字符串是 合法 的。 请你返回字符串 word 的一个 最长合法子字符串 的长度。 子字符串 指的是一个字符串中一段连续的字符，它可以为空。 示例 1： 输入：word = "cbaaaabc", forbidden = ["aaa","cb"] 输出：4 解释：总共有 11 个合法子字符串："c", "b", "a", "ba", "aa", "bc", "baa", "aab", "ab", "abc" 和 "aabc"。最长合法子字符串的长度为 4 。 其他子字符串都要么包含 "aaa" ，要么包含 "cb" 。 示例 2： 输入：word = "leetcode", forbidden = ["de","le","e"] 输出：4 解释：总共有 11 个合法子字符串："l" ，"t" ，"c" ，"o" ，"d" ，"tc" ，"co" ，"od" ，"tco" ，"cod" 和 "tcod" 。最长合法子字符串的长度为 4 。 所有其他子字符串都至少包含 "de" ，"le" 和 "e" 之一。 提示： * 1 <= word.length <= 105 * word 只包含小写英文字母。 * 1 <= forbidden.length <= 105 * 1 <= forbidden[i].length <= 10 * forbidden[i] 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和字典树（Trie）来高效地检查子字符串是否包含禁用词。

算法步骤:
1. 构建一个 Trie 树，将所有禁用词插入到 Trie 中。
2. 使用滑动窗口遍历字符串 `word`，维护一个左指针 `left` 和右指针 `right`。
3. 对于每个右指针 `right`，检查从 `left` 到 `right` 的子字符串是否包含禁用词。
4. 如果包含禁用词，移动左指针 `left`，直到子字符串不再包含禁用词。
5. 更新最长合法子字符串的长度。

关键点:
- 使用 Trie 树可以高效地检查子字符串是否包含禁用词。
- 滑动窗口技术可以在 O(n) 时间复杂度内遍历字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是字符串 `word` 的长度，m 是禁用词的最大长度。
空间复杂度: O(k * m)，其中 k 是禁用词的数量，m 是禁用词的最大长度。
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
        self.is_end = False

def build_trie(forbidden: List[str]) -> TrieNode:
    root = TrieNode()
    for word in forbidden:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    return root

def is_forbidden(trie: TrieNode, s: str, start: int, end: int) -> bool:
    node = trie
    for i in range(start, end + 1):
        if s[i] not in node.children:
            return False
        node = node.children[s[i]]
        if node.is_end:
            return True
    return False

def solution_function_name(word: str, forbidden: List[str]) -> int:
    """
    函数式接口 - 返回最长合法子字符串的长度
    """
    trie = build_trie(forbidden)
    left = 0
    max_length = 0
    n = len(word)

    for right in range(n):
        while is_forbidden(trie, word, left, right):
            left += 1
        max_length = max(max_length, right - left + 1)

    return max_length

Solution = create_solution(solution_function_name)