# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 291
标题: Word Pattern II
难度: medium
链接: https://leetcode.cn/problems/word-pattern-ii/
题目类型: 哈希表、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
291. 单词规律 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯，枚举所有可能的单词分割方式

算法步骤:
1. 回溯枚举所有可能的单词分割
2. 检查是否满足pattern映射
3. 使用双向映射确保唯一性

关键点:
- 回溯枚举
- 双向映射检查
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n) - 最坏情况
空间复杂度: O(n) - 递归栈空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def word_pattern_match(pattern: str, s: str) -> bool:
    """
    函数式接口 - 单词规律 II
    
    实现思路:
    回溯：枚举所有可能的单词分割方式。
    
    Args:
        pattern: 模式字符串
        s: 字符串
        
    Returns:
        是否匹配
        
    Example:
        >>> word_pattern_match("abab", "redblueredblue")
        True
    """
    char_to_word = {}
    word_to_char = {}
    
    def backtrack(p_idx: int, s_idx: int) -> bool:
        """回溯函数"""
        if p_idx == len(pattern) and s_idx == len(s):
            return True
        
        if p_idx == len(pattern) or s_idx == len(s):
            return False
        
        char = pattern[p_idx]
        
        # 如果char已经有映射
        if char in char_to_word:
            word = char_to_word[char]
            if s[s_idx:s_idx+len(word)] != word:
                return False
            return backtrack(p_idx + 1, s_idx + len(word))
        
        # 枚举所有可能的单词
        for i in range(s_idx + 1, len(s) + 1):
            word = s[s_idx:i]
            
            # 检查word是否已经被映射
            if word in word_to_char and word_to_char[word] != char:
                continue
            
            # 建立映射
            char_to_word[char] = word
            word_to_char[word] = char
            
            if backtrack(p_idx + 1, i):
                return True
            
            # 回溯
            del char_to_word[char]
            if word_to_char[word] == char:
                del word_to_char[word]
        
        return False
    
    return backtrack(0, 0)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(word_pattern_match)
