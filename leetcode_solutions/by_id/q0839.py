# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 839
标题: Short Encoding of Words
难度: medium
链接: https://leetcode.cn/problems/short-encoding-of-words/
题目类型: 字典树、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
820. 单词的压缩编码 - 单词数组 words 的 有效编码 由任意助记字符串 s 和下标数组 indices 组成，且满足： * words.length == indices.length * 助记字符串 s 以 '#' 字符结尾 * 对于每个下标 indices[i] ，s 的一个从 indices[i] 开始、到下一个 '#' 字符结束（但不包括 '#'）的 子字符串 恰好与 words[i] 相等 给你一个单词数组 words ，返回成功对 words 进行编码的最小助记字符串 s 的长度 。 示例 1： 输入：words = ["time", "me", "bell"] 输出：10 解释：一组有效编码为 s = "time#bell#" 和 indices = [0, 2, 5] 。 words[0] = "time" ，s 开始于 indices[0] = 0 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#" words[1] = "me" ，s 开始于 indices[1] = 2 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#" words[2] = "bell" ，s 开始于 indices[2] = 5 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#" 示例 2： 输入：words = ["t"] 输出：2 解释：一组有效编码为 s = "t#" 和 indices = [0] 。 提示： * 1 <= words.length <= 2000 * 1 <= words[i].length <= 7 * words[i] 仅由小写字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储单词，并通过反向插入单词来避免重复前缀。

算法步骤:
1. 创建一个 Trie 根节点。
2. 将所有单词反向插入 Trie 中。
3. 计算每个单词在 Trie 中的唯一后缀长度，并累加这些长度加上 '#' 的长度。

关键点:
- 反向插入单词可以确保较短的单词不会被较长的单词覆盖。
- 通过 Trie 的结构，可以高效地找到每个单词的唯一后缀。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是单词的数量，m 是单词的最大长度。
空间复杂度: O(n * m)，Trie 的空间复杂度取决于所有单词的总长度。
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

    def is_unique_suffix(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return True
            node = node.children[char]
        return len(node.children) == 0


def solution_function_name(words: List[str]) -> int:
    """
    函数式接口 - 返回成功对 words 进行编码的最小助记字符串 s 的长度
    """
    trie = Trie()
    for word in words:
        trie.insert(word[::-1])

    total_length = 0
    for word in words:
        if trie.is_unique_suffix(word[::-1]):
            total_length += len(word) + 1

    return total_length


Solution = create_solution(solution_function_name)