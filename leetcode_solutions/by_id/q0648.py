# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 648
标题: Replace Words
难度: medium
链接: https://leetcode.cn/problems/replace-words/
题目类型: 字典树、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
648. 单词替换 - 在英语中，我们有一个叫做 词根(root) 的概念，可以词根 后面 添加其他一些词组成另一个较长的单词——我们称这个词为 衍生词 (derivative)。例如，词根 help，跟随着 继承词 "ful"，可以形成新的单词 "helpful"。 现在，给定一个由许多 词根 组成的词典 dictionary 和一个用空格分隔单词形成的句子 sentence。你需要将句子中的所有 衍生词 用 词根 替换掉。如果 衍生词 有许多可以形成它的 词根，则用 最短 的 词根 替换它。 你需要输出替换之后的句子。 示例 1： 输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery" 输出："the cat was rat by the bat" 示例 2： 输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs" 输出："a a b c" 提示： * 1 <= dictionary.length <= 1000 * 1 <= dictionary[i].length <= 100 * dictionary[i] 仅由小写字母组成。 * 1 <= sentence.length <= 106 * sentence 仅由小写字母和空格组成。 * sentence 中单词的总量在范围 [1, 1000] 内。 * sentence 中每个单词的长度在范围 [1, 1000] 内。 * sentence 中单词之间由一个空格隔开。 * sentence 没有前导或尾随空格。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储词根，并在遍历句子时查找最短的词根。

算法步骤:
1. 构建字典树：将所有的词根插入到字典树中。
2. 遍历句子中的每个单词，使用字典树查找最短的词根进行替换。
3. 如果找到词根，则替换该单词；否则，保持原单词不变。
4. 将处理后的单词重新组合成句子并返回。

关键点:
- 使用字典树高效地存储和查找词根。
- 在遍历句子时，使用字典树快速查找最短的词根。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是句子的总字符数，m 是词根的总字符数。
空间复杂度: O(m)，字典树的空间复杂度与词根的总字符数相关。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

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
    replaced_words = [trie.search_prefix(word) for word in words]
    return ' '.join(replaced_words)

Solution = create_solution(replace_words)