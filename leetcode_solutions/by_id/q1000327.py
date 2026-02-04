# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000327
标题: 单词替换
难度: medium
链接: https://leetcode.cn/problems/UhWRSj/
题目类型: 字典树、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 063. 单词替换 - 在英语中，有一个叫做 词根(root) 的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。 现在，给定一个由许多词根组成的词典和一个句子，需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。 需要输出替换之后的句子。 示例 1： 输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery" 输出："the cat was rat by the bat" 示例 2： 输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs" 输出："a a b c" 示例 3： 输入：dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa" 输出："a a a a a a a a bbb baba a" 示例 4： 输入：dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery" 输出："the cat was rat by the bat" 示例 5： 输入：dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted" 输出："it is ab that this solution is ac" 提示： * 1 <= dictionary.length <= 1000 * 1 <= dictionary[i].length <= 100 * dictionary[i] 仅由小写字母组成。 * 1 <= sentence.length <= 10^6 * sentence 仅由小写字母和空格组成。 * sentence 中单词的总量在范围 [1, 1000] 内。 * sentence 中每个单词的长度在范围 [1, 1000] 内。 * sentence 中单词之间由一个空格隔开。 * sentence 没有前导或尾随空格。 注意：本题与主站 648 题相同： https://leetcode.cn/problems/replace-words/ [https://leetcode.cn/problems/replace-words/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储词根，并通过查找字典树来替换句子中的继承词。

算法步骤:
1. 构建字典树，将所有词根插入字典树。
2. 将句子按空格分割成单词列表。
3. 对于每个单词，在字典树中查找其最短前缀词根，如果找到则替换该单词。
4. 将处理后的单词重新拼接成句子并返回。

关键点:
- 使用字典树高效地查找词根。
- 替换时选择最短的词根。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m * L)，其中 n 是句子的长度，m 是词根的数量，L 是词根的平均长度。
空间复杂度: O(m * L)，用于存储字典树。
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

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search_prefix(self, word: str) -> str:
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            prefix += char
            if node.is_end:
                return prefix
        return word

def replace_words(dictionary: List[str], sentence: str) -> str:
    trie = Trie()
    for root in dictionary:
        trie.insert(root)
    
    words = sentence.split()
    for i, word in enumerate(words):
        words[i] = trie.search_prefix(word)
    
    return ' '.join(words)

Solution = create_solution(replace_words)