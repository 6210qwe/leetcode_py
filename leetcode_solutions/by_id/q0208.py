# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 208
标题: Implement Trie (Prefix Tree)
难度: medium
链接: https://leetcode.cn/problems/implement-trie-prefix-tree/
题目类型: 设计、字典树、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
208. 实现 Trie (前缀树) - Trie [https://baike.baidu.com/item/字典树/9825209?fr=aladdin]（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。 请你实现 Trie 类： * Trie() 初始化前缀树对象。 * void insert(String word) 向前缀树中插入字符串 word 。 * boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。 * boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。 示例： 输入 ["Trie", "insert", "search", "search", "startsWith", "insert", "search"] [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]] 输出 [null, null, true, false, true, null, true] 解释 Trie trie = new Trie(); trie.insert("apple"); trie.search("apple"); // 返回 True trie.search("app"); // 返回 False trie.startsWith("app"); // 返回 True trie.insert("app"); trie.search("app"); // 返回 True 提示： * 1 <= word.length, prefix.length <= 2000 * word 和 prefix 仅由小写英文字母组成 * insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）结构，每个节点存储26个子节点和结束标志

算法步骤:
1. 定义TrieNode类，包含children字典和is_end标志
2. insert: 遍历字符串，创建或访问节点，最后标记结束
3. search: 遍历字符串，检查是否存在且标记为结束
4. startsWith: 遍历前缀，检查是否存在路径

关键点:
- 使用字典树高效存储和检索字符串
- 时间复杂度O(m)，m为字符串长度，空间复杂度O(ALPHABET_SIZE * N * M)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m) - m为字符串长度
空间复杂度: O(ALPHABET_SIZE * N * M) - N为字符串数量，M为平均长度
"""

# ============================================================================
# 代码实现
# ============================================================================

from leetcode_solutions.utils.solution import create_solution


class TrieNode:
    """Trie节点"""
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    """
    Trie（前缀树）实现类
    """
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """插入单词"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        """搜索单词"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def startsWith(self, prefix: str) -> bool:
        """检查是否有以prefix为前缀的单词"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def implement_trie_prefix_tree() -> Trie:
    """
    函数式接口 - 创建Trie（前缀树）
    
    实现思路:
    使用字典树结构，每个节点存储子节点和结束标志。
    
    Returns:
        Trie实例
        
    Example:
        >>> trie = implement_trie_prefix_tree()
        >>> trie.insert("apple")
        >>> trie.search("apple")
        True
    """
    return Trie()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(implement_trie_prefix_tree)
