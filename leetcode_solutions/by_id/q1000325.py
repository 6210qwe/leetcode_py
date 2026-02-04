# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000325
标题: 实现 Trie (前缀树)
难度: medium
链接: https://leetcode.cn/problems/QC3q1f/
题目类型: 设计、字典树、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 062. 实现 Trie (前缀树) - Trie [https://baike.baidu.com/item/字典树/9825209?fr=aladdin]（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。 请你实现 Trie 类： * Trie() 初始化前缀树对象。 * void insert(String word) 向前缀树中插入字符串 word 。 * boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。 * boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。 示例： 输入 inputs = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"] inputs = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]] 输出 [null, null, true, false, true, null, true] 解释 Trie trie = new Trie(); trie.insert("apple"); trie.search("apple"); // 返回 True trie.search("app"); // 返回 False trie.startsWith("app"); // 返回 True trie.insert("app"); trie.search("app"); // 返回 True 提示： * 1 <= word.length, prefix.length <= 2000 * word 和 prefix 仅由小写英文字母组成 * insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次 注意：本题与主站 208 题相同：https://leetcode.cn/problems/implement-trie-prefix-tree/ [https://leetcode.cn/problems/implement-trie-prefix-tree/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用嵌套字典来表示 Trie 树的节点，每个节点包含一个子节点字典和一个标记是否为单词结尾的布尔值。

算法步骤:
1. 初始化 Trie 树时，创建一个根节点。
2. 插入单词时，从根节点开始逐字符遍历，如果当前字符不在子节点字典中，则创建一个新的子节点。
3. 搜索单词时，从根节点开始逐字符遍历，如果某个字符不在子节点字典中，则返回 False；如果遍历完整个单词且最后一个字符是单词结尾，则返回 True。
4. 检查前缀时，从根节点开始逐字符遍历，如果某个字符不在子节点字典中，则返回 False；如果遍历完整个前缀，则返回 True。

关键点:
- 使用嵌套字典来表示 Trie 树的节点。
- 每个节点包含一个子节点字典和一个标记是否为单词结尾的布尔值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m)，其中 m 是单词或前缀的长度。
空间复杂度: O(n * m)，其中 n 是插入的单词数量，m 是单词的平均长度。
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

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


Solution = create_solution(Trie)