# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 212
标题: Word Search II
难度: hard
链接: https://leetcode.cn/problems/word-search-ii/
题目类型: 字典树、数组、字符串、回溯、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
212. 单词搜索 II - 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。 单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。 示例 1： [https://assets.leetcode.com/uploads/2020/11/07/search1.jpg] 输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"] 输出：["eat","oath"] 示例 2： [https://assets.leetcode.com/uploads/2020/11/07/search2.jpg] 输入：board = [["a","b"],["c","d"]], words = ["abcb"] 输出：[] 提示： * m == board.length * n == board[i].length * 1 <= m, n <= 12 * board[i][j] 是一个小写英文字母 * 1 <= words.length <= 3 * 104 * 1 <= words[i].length <= 10 * words[i] 由小写英文字母组成 * words 中的所有字符串互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 字典树+回溯，使用Trie树存储所有单词，然后DFS搜索

算法步骤:
1. 构建Trie树存储所有单词
2. 对每个位置，使用DFS+回溯搜索
3. 如果找到单词，加入结果并标记已找到（避免重复）

关键点:
- Trie树优化查找
- DFS回溯搜索
- 时间复杂度O(m*n*4^L)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m*n*4^L) - m*n为网格大小，L为单词最大长度
空间复杂度: O(k*L) - k为单词数，L为平均长度
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
        self.word = None


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    """
    函数式接口 - 单词搜索 II
    
    实现思路:
    字典树+回溯：使用Trie树存储所有单词，然后DFS搜索。
    
    Args:
        board: 字符网格
        words: 单词列表
        
    Returns:
        所有能在网格中找到的单词
        
    Example:
        >>> find_words([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])
        ['eat', 'oath']
    """
    # 构建Trie树
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
    
    m, n = len(board), len(board[0])
    result = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(i: int, j: int, node: TrieNode):
        """DFS搜索"""
        char = board[i][j]
        curr_node = node.children.get(char)
        
        if not curr_node:
            return
        
        # 如果找到单词
        if curr_node.word:
            result.append(curr_node.word)
            curr_node.word = None  # 避免重复
        
        # 标记已访问
        board[i][j] = '#'
        
        # 搜索四个方向
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                dfs(ni, nj, curr_node)
        
        # 恢复
        board[i][j] = char
        
        # 优化：如果节点没有子节点，可以删除
        if not curr_node.children:
            node.children.pop(char)
    
    # 对每个位置开始搜索
    for i in range(m):
        for j in range(n):
            dfs(i, j, root)
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(find_words)
