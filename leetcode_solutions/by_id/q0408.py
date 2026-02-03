# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 408
标题: Valid Word Abbreviation
难度: easy
链接: https://leetcode.cn/problems/valid-word-abbreviation/
题目类型: 双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
408. 有效单词缩写 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 双指针解析缩写

算法步骤:
1. 使用两个指针分别遍历word和abbr
2. 如果abbr中是数字，解析数字并跳过word中对应数量的字符
3. 如果abbr中是字母，与word中对应位置比较
4. 检查是否完全匹配

关键点:
- 数字不能以0开头（除非就是0）
- 需要处理数字的解析
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n+m) - n和m为字符串长度
空间复杂度: O(1) - 只使用常数空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def valid_word_abbreviation(word: str, abbr: str) -> bool:
    """
    函数式接口 - 有效单词缩写
    
    实现思路:
    使用双指针解析缩写，数字表示跳过的字符数，字母需要匹配。
    
    Args:
        word: 单词
        abbr: 缩写
        
    Returns:
        缩写是否有效
        
    Example:
        >>> valid_word_abbreviation("internationalization", "i12iz4n")
        True
    """
    i, j = 0, 0
    
    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            if abbr[j] == '0':  # 数字不能以0开头
                return False
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
        else:
            if word[i] != abbr[j]:
                return False
            i += 1
            j += 1
    
    return i == len(word) and j == len(abbr)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(valid_word_abbreviation)
