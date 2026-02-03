# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 345
标题: Reverse Vowels of a String
难度: easy
链接: https://leetcode.cn/problems/reverse-vowels-of-a-string/
题目类型: 双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
345. 反转字符串中的元音字母 - 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。 元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。 示例 1： 输入：s = "IceCreAm" 输出："AceCreIm" 解释： s 中的元音是 ['I', 'e', 'e', 'A']。反转这些元音，s 变为 "AceCreIm". 示例 2： 输入：s = "leetcode" 输出："leotcede" 提示： * 1 <= s.length <= 3 * 105 * s 由 可打印的 ASCII 字符组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 双指针，找到元音字母后交换

算法步骤:
1. 使用双指针left和right
2. 找到左右两个元音字母
3. 交换它们

关键点:
- 双指针
- 元音字母判断
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n为字符串长度
空间复杂度: O(n) - 字符数组空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def reverse_vowels(s: str) -> str:
    """
    函数式接口 - 反转字符串中的元音字母
    
    实现思路:
    双指针：找到元音字母后交换。
    
    Args:
        s: 字符串
        
    Returns:
        反转元音后的字符串
        
    Example:
        >>> reverse_vowels("leetcode")
        'leotcede'
    """
    vowels = set('aeiouAEIOU')
    s_list = list(s)
    left, right = 0, len(s_list) - 1
    
    while left < right:
        while left < right and s_list[left] not in vowels:
            left += 1
        while left < right and s_list[right] not in vowels:
            right -= 1
        
        if left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    
    return ''.join(s_list)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(reverse_vowels)
