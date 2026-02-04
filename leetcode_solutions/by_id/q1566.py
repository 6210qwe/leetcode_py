# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1566
标题: Check If a Word Occurs As a Prefix of Any Word in a Sentence
难度: easy
链接: https://leetcode.cn/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
题目类型: 双指针、字符串、字符串匹配
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1455. 检查单词是否为句中其他单词的前缀 - 给你一个字符串 sentence 作为句子并指定检索词为 searchWord ，其中句子由若干用 单个空格 分隔的单词组成。请你检查检索词 searchWord 是否为句子 sentence 中任意单词的前缀。 如果 searchWord 是某一个单词的前缀，则返回句子 sentence 中该单词所对应的下标（下标从 1 开始）。如果 searchWord 是多个单词的前缀，则返回匹配的第一个单词的下标（最小下标）。如果 searchWord 不是任何单词的前缀，则返回 -1 。 字符串 s 的 前缀 是 s 的任何前导连续子字符串。 示例 1： 输入：sentence = "i love eating burger", searchWord = "burg" 输出：4 解释："burg" 是 "burger" 的前缀，而 "burger" 是句子中第 4 个单词。 示例 2： 输入：sentence = "this problem is an easy problem", searchWord = "pro" 输出：2 解释："pro" 是 "problem" 的前缀，而 "problem" 是句子中第 2 个也是第 6 个单词，但是应该返回最小下标 2 。 示例 3： 输入：sentence = "i am tired", searchWord = "you" 输出：-1 解释："you" 不是句子中任何单词的前缀。 提示： * 1 <= sentence.length <= 100 * 1 <= searchWord.length <= 10 * sentence 由小写英文字母和空格组成。 * searchWord 由小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字符串的 split 方法将句子分割成单词列表，然后遍历每个单词，检查 searchWord 是否是当前单词的前缀。

算法步骤:
1. 将句子按空格分割成单词列表。
2. 遍历单词列表，检查 searchWord 是否是当前单词的前缀。
3. 如果找到匹配的前缀，返回其在句子中的位置（从 1 开始计数）。
4. 如果遍历完所有单词都没有找到匹配的前缀，返回 -1。

关键点:
- 使用字符串的 startswith 方法来检查前缀。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是句子的长度，m 是 searchWord 的长度。最坏情况下需要遍历整个句子。
空间复杂度: O(n)，因为需要存储分割后的单词列表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(sentence: str, searchWord: str) -> int:
    """
    函数式接口 - 检查单词是否为句中其他单词的前缀
    """
    # 将句子按空格分割成单词列表
    words = sentence.split()
    
    # 遍历单词列表，检查 searchWord 是否是当前单词的前缀
    for i, word in enumerate(words):
        if word.startswith(searchWord):
            return i + 1  # 返回匹配单词的位置（从 1 开始计数）
    
    # 如果没有找到匹配的前缀，返回 -1
    return -1


Solution = create_solution(solution_function_name)