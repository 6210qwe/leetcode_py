# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 290
标题: Word Pattern
难度: easy
链接: https://leetcode.cn/problems/word-pattern/
题目类型: 哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
290. 单词规律 - 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。具体来说： * pattern 中的每个字母都 恰好 映射到 s 中的一个唯一单词。 * s 中的每个唯一单词都 恰好 映射到 pattern 中的一个字母。 * 没有两个字母映射到同一个单词，也没有两个单词映射到同一个字母。 示例1: 输入: pattern = "abba", s = "dog cat cat dog" 输出: true 示例 2: 输入:pattern = "abba", s = "dog cat cat fish" 输出: false 示例 3: 输入: pattern = "aaaa", s = "dog cat cat dog" 输出: false 提示: * 1 <= pattern.length <= 300 * pattern 只包含小写英文字母 * 1 <= s.length <= 3000 * s 只包含小写英文字母和 ' ' * s 不包含 任何前导或尾随对空格 * s 中每个单词都被 单个空格 分隔
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 双向映射，使用两个哈希表

算法步骤:
1. 将pattern和s分割成数组
2. 检查长度是否相等
3. 使用两个哈希表建立双向映射
4. 检查映射是否一致

关键点:
- 双向映射
- 时间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n为pattern长度
空间复杂度: O(n) - 哈希表空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def word_pattern(pattern: str, s: str) -> bool:
    """
    函数式接口 - 单词规律
    
    实现思路:
    双向映射：使用两个哈希表建立双向映射。
    
    Args:
        pattern: 模式字符串
        s: 字符串
        
    Returns:
        是否遵循规律
        
    Example:
        >>> word_pattern("abba", "dog cat cat dog")
        True
    """
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True


# 自动生成Solution类（无需手动编写）
Solution = create_solution(word_pattern)
