# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000022
标题: Longest Word LCCI
难度: medium
链接: https://leetcode.cn/problems/longest-word-lcci/
题目类型: 字典树、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 17.15. 最长单词 - 给定一组单词words，编写一个程序，找出其中的最长单词，且该单词由这组单词中的其他单词组合而成。若有多个长度相同的结果，返回其中字典序最小的一项，若没有符合要求的单词则返回空字符串。 示例： 输入： ["cat","banana","dog","nana","walk","walker","dogwalker"] 输出： "dogwalker" 解释： "dogwalker"可由"dog"和"walker"组成。 提示： * 0 <= len(words) <= 200 * 1 <= len(words[i]) <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归和动态规划来检查每个单词是否可以由其他单词组合而成。

算法步骤:
1. 将所有单词按长度降序排序，如果长度相同则按字典序升序排序。
2. 使用一个集合来存储所有单词，以便快速查找。
3. 定义一个递归函数 `can_form` 来检查一个单词是否可以由其他单词组合而成。
4. 对于每个单词，使用 `can_form` 函数检查它是否可以由其他单词组合而成。
5. 返回第一个满足条件的单词，如果没有找到则返回空字符串。

关键点:
- 使用递归和记忆化搜索来避免重复计算。
- 通过排序确保优先返回最长且字典序最小的单词。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * l^2)，其中 n 是单词的数量，l 是单词的最大长度。
空间复杂度: O(n * l)，用于存储单词集合和递归调用栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_word(words: List[str]) -> str:
    """
    函数式接口 - 找出由其他单词组合而成的最长单词
    """
    # 按长度降序排序，如果长度相同则按字典序升序排序
    words.sort(key=lambda x: (-len(x), x))
    
    # 使用集合存储所有单词，以便快速查找
    word_set = set(words)
    
    def can_form(word: str, memo: dict) -> bool:
        if word in memo:
            return memo[word]
        
        for i in range(1, len(word)):
            prefix, suffix = word[:i], word[i:]
            if prefix in word_set and (suffix in word_set or can_form(suffix, memo)):
                memo[word] = True
                return True
        
        memo[word] = False
        return False
    
    for word in words:
        word_set.remove(word)  # 从集合中移除当前单词
        if can_form(word, {}):
            return word
        word_set.add(word)  # 将当前单词重新加入集合
    
    return ""


Solution = create_solution(longest_word)