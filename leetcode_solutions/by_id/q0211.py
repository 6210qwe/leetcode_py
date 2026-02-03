# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 211
标题: Design Add and Search Words Data Structure
难度: medium
链接: https://leetcode.cn/problems/design-add-and-search-words-data-structure/
题目类型: 深度优先搜索、设计、字典树、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
211. 添加与搜索单词 - 数据结构设计 - 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。 实现词典类 WordDictionary ： * WordDictionary() 初始化词典对象 * void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配 * bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回 false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。 示例： 输入： ["WordDictionary","addWord","addWord","addWord","search","search","search","search"] [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]] 输出： [null,null,null,null,false,true,true,true] 解释： WordDictionary wordDictionary = new WordDictionary(); wordDictionary.addWord("bad"); wordDictionary.addWord("dad"); wordDictionary.addWord("mad"); wordDictionary.search("pad"); // 返回 False wordDictionary.search("bad"); // 返回 True wordDictionary.search(".ad"); // 返回 True wordDictionary.search("b.."); // 返回 True 提示： * 1 <= word.length <= 25 * addWord 中的 word 由小写英文字母组成 * search 中的 word 由 '.' 或小写英文字母组成 * 最多调用 104 次 addWord 和 search
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用Trie树存储单词，搜索时支持通配符'.'

算法步骤:
1. 使用Trie树存储单词
2. addWord: 正常插入到Trie树
3. search: 使用DFS搜索，遇到'.'时遍历所有子节点

关键点:
- 使用Trie树和DFS处理通配符
- 时间复杂度：addWord O(m)，search O(m*26^k)，m为单词长度，k为'.'数量
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: addWord O(m)，search O(m*26^k)
空间复杂度: O(ALPHABET_SIZE * N * M) - N为单词数，M为平均长度
"""

# ============================================================================
# 代码实现
# ============================================================================

from leetcode_solutions.utils.solution import create_solution


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    """
    添加与搜索单词数据结构实现类
    """
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        """添加单词"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        """搜索单词，支持'.'通配符"""
        def dfs(node, index):
            if index == len(word):
                return node.is_end
            
            char = word[index]
            if char == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)
        
        return dfs(self.root, 0)


def design_add_and_search_words_data_structure() -> WordDictionary:
    """
    函数式接口 - 创建添加与搜索单词数据结构
    
    实现思路:
    使用Trie树存储单词，搜索时支持通配符'.'。
    
    Returns:
        WordDictionary实例
        
    Example:
        >>> wordDict = design_add_and_search_words_data_structure()
        >>> wordDict.addWord("bad")
        >>> wordDict.search("bad")
        True
    """
    return WordDictionary()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(design_add_and_search_words_data_structure)
