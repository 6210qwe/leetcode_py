# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2494
标题: Sum of Prefix Scores of Strings
难度: hard
链接: https://leetcode.cn/problems/sum-of-prefix-scores-of-strings/
题目类型: 字典树、数组、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2416. 字符串的前缀分数和 - 给你一个长度为 n 的数组 words ，该数组由 非空 字符串组成。 定义字符串 term 的 分数 等于以 term 作为 前缀 的 words[i] 的数目。 * 例如，如果 words = ["a", "ab", "abc", "cab"] ，那么 "ab" 的分数是 2 ，因为 "ab" 是 "ab" 和 "abc" 的一个前缀。 返回一个长度为 n 的数组 answer ，其中 answer[i] 是 words[i] 的每个非空前缀的分数 总和 。 注意：字符串视作它自身的一个前缀。 示例 1： 输入：words = ["abc","ab","bc","b"] 输出：[5,4,3,2] 解释：对应每个字符串的答案如下： - "abc" 有 3 个前缀："a"、"ab" 和 "abc" 。 - 2 个字符串的前缀为 "a" ，2 个字符串的前缀为 "ab" ，1 个字符串的前缀为 "abc" 。 总计 answer[0] = 2 + 2 + 1 = 5 。 - "ab" 有 2 个前缀："a" 和 "ab" 。 - 2 个字符串的前缀为 "a" ，2 个字符串的前缀为 "ab" 。 总计 answer[1] = 2 + 2 = 4 。 - "bc" 有 2 个前缀："b" 和 "bc" 。 - 2 个字符串的前缀为 "b" ，1 个字符串的前缀为 "bc" 。 总计 answer[2] = 2 + 1 = 3 。 - "b" 有 1 个前缀："b"。 - 2 个字符串的前缀为 "b" 。 总计 answer[3] = 2 。 示例 2： 输入：words = ["abcd"] 输出：[4] 解释： "abcd" 有 4 个前缀 "a"、"ab"、"abc" 和 "abcd"。 每个前缀的分数都是 1 ，总计 answer[0] = 1 + 1 + 1 + 1 = 4 。 提示： * 1 <= words.length <= 1000 * 1 <= words[i].length <= 1000 * words[i] 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储所有单词，并在插入过程中记录每个节点的前缀出现次数。

算法步骤:
1. 构建字典树并插入所有单词，在插入过程中记录每个节点的前缀出现次数。
2. 遍历每个单词，计算其所有前缀的分数总和。

关键点:
- 使用字典树来高效地存储和查询前缀。
- 在插入过程中记录每个节点的前缀出现次数，以便后续计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是单词的数量，m 是单词的最大长度。
空间复杂度: O(n * m)，字典树的空间复杂度。
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
        self.prefix_count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1

    def get_prefix_score(self, word: str) -> int:
        score = 0
        node = self.root
        for char in word:
            node = node.children[char]
            score += node.prefix_count
        return score


def sum_of_prefix_scores(words: List[str]) -> List[int]:
    trie = Trie()
    for word in words:
        trie.insert(word)

    result = []
    for word in words:
        result.append(trie.get_prefix_score(word))
    return result


Solution = create_solution(sum_of_prefix_scores)