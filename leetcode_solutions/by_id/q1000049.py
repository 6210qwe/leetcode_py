# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000049
标题: Word Rectangle LCCI
难度: hard
链接: https://leetcode.cn/problems/word-rectangle-lcci/
题目类型: 字典树、数组、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 17.25. 单词矩阵 - 给定一份单词的清单，设计一个算法，创建由字母组成的面积最大的矩形，其中每一行组成一个单词(自左向右)，每一列也组成一个单词(自上而下)。不要求这些单词在清单里连续出现，但要求所有行等长，所有列等高。 如果有多个面积最大的矩形，输出任意一个均可。一个单词可以重复使用。 示例 1： 输入：["this", "real", "hard", "trh", "hea", "iar", "sld"] 输出： [ "this", "real", "hard" ] 示例 2： 输入：["aa"] 输出：["aa","aa"] 说明： * words.length <= 1000 * words[i].length <= 100 * 数据保证单词足够随机
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储所有单词，并通过回溯法构建可能的矩形。

算法步骤:
1. 构建字典树，将所有单词插入字典树。
2. 从最长的单词开始，尝试构建矩形。
3. 使用回溯法逐行构建矩形，确保每一列也是一个有效的单词。
4. 如果找到一个有效矩形，记录其面积和内容。
5. 返回面积最大的矩形。

关键点:
- 使用字典树高效地检查单词的有效性。
- 通过回溯法逐行构建矩形，并确保每一列也是有效的单词。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m^2 * 26^m)，其中 n 是单词数量，m 是单词的最大长度。
空间复杂度: O(n * m)，用于存储字典树和中间结果。
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

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end


def solution_function_name(words: List[str]) -> List[str]:
    """
    函数式接口 - 实现
    """
    if not words:
        return []

    # 构建字典树
    trie = Trie()
    for word in words:
        trie.insert(word)

    max_area = 0
    result = []

    # 从最长的单词开始尝试构建矩形
    max_length = max(len(word) for word in words)
    for length in range(max_length, 0, -1):
        for word in words:
            if len(word) != length:
                continue
            matrix = [word]
            if backtrack(trie, matrix, length, words):
                area = length * len(matrix)
                if area > max_area:
                    max_area = area
                    result = matrix
        if result:
            break

    return result


def backtrack(trie: Trie, matrix: List[str], length: int, words: List[str]) -> bool:
    if len(matrix) == length:
        return True

    next_row = [''] * length
    for i in range(length):
        col_word = ''.join(matrix[j][i] for j in range(len(matrix)))
        if not trie.search(col_word):
            return False

    for word in words:
        if len(word) != length:
            continue
        next_row = word
        for i in range(length):
            col_word = ''.join(matrix[j][i] + next_row[i] for j in range(len(matrix)))
            if not trie.search(col_word):
                break
        else:
            matrix.append(next_row)
            if backtrack(trie, matrix, length, words):
                return True
            matrix.pop()

    return False


Solution = create_solution(solution_function_name)