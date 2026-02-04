# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4113
标题: Find Kth Character in Expanded String
难度: medium
链接: https://leetcode.cn/problems/find-kth-character-in-expanded-string/
题目类型: 字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3744. 在展开字符串中查找第 K 个字符 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归和二分查找来找到第 k 个字符

算法步骤:
1. 定义一个递归函数 `get_length` 来计算展开后的字符串长度。
2. 定义一个递归函数 `get_kth_character` 来找到第 k 个字符。
3. 在 `get_kth_character` 中，使用二分查找来减少递归的深度。

关键点:
- 通过递归计算展开后的字符串长度，避免直接展开字符串。
- 使用二分查找来减少递归的深度，提高效率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n)
空间复杂度: O(log n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def get_length(s: str) -> int:
    """
    计算展开后的字符串长度
    """
    if s.isdigit():
        return int(s)
    length = 0
    i = 0
    while i < len(s):
        if s[i] == '[':
            j = i
            while s[j] != ']':
                j += 1
            repeat = int(s[i-1])
            length += repeat * get_length(s[i+1:j])
            i = j + 1
        else:
            length += 1
            i += 1
    return length

def get_kth_character(s: str, k: int) -> str:
    """
    找到展开后的第 k 个字符
    """
    if s.isdigit():
        return ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            repeat = int(s[i])
            j = i + 1
            while s[j] != ']':
                j += 1
            substring = s[i+2:j]
            expanded_length = get_length(substring)
            if k <= repeat * expanded_length:
                return get_kth_character(substring, (k - 1) % expanded_length + 1)
            k -= repeat * expanded_length
            i = j + 1
        else:
            if k == 1:
                return s[i]
            k -= 1
            i += 1
    return ""

def solution_function_name(s: str, k: int) -> str:
    """
    函数式接口 - 实现
    """
    return get_kth_character(s, k)

Solution = create_solution(solution_function_name)