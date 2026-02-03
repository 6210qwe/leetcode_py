# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 273
标题: Integer to English Words
难度: hard
链接: https://leetcode.cn/problems/integer-to-english-words/
题目类型: 递归、数学、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
273. 整数转换英文表示 - 将非负整数 num 转换为其对应的英文表示。 示例 1： 输入：num = 123 输出："One Hundred Twenty Three" 示例 2： 输入：num = 12345 输出："Twelve Thousand Three Hundred Forty Five" 示例 3： 输入：num = 1234567 输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven" 提示： * 0 <= num <= 231 - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归处理，将数字分成千位、百万位、十亿位等

算法步骤:
1. 定义0-19的英文单词
2. 定义20-90的十位数字
3. 定义单位（Thousand, Million, Billion）
4. 递归处理每三位数字

关键点:
- 递归处理
- 注意空格处理
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - n为数字大小
空间复杂度: O(log n) - 递归栈空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def number_to_words(num: int) -> str:
    """
    函数式接口 - 整数转换英文表示
    
    实现思路:
    递归处理：将数字分成千位、百万位、十亿位等。
    
    Args:
        num: 非负整数
        
    Returns:
        英文表示
        
    Example:
        >>> number_to_words(123)
        'One Hundred Twenty Three'
    """
    if num == 0:
        return "Zero"
    
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]
    
    def helper(n: int) -> str:
        """处理三位数字"""
        if n == 0:
            return ""
        
        result = []
        if n >= 100:
            result.append(ones[n // 100])
            result.append("Hundred")
            n %= 100
        
        if n >= 20:
            result.append(tens[n // 10])
            n %= 10
        
        if n > 0:
            result.append(ones[n])
        
        return " ".join(result)
    
    result = []
    i = 0
    
    while num > 0:
        if num % 1000 != 0:
            part = helper(num % 1000)
            if i > 0:
                part += " " + thousands[i]
            result.insert(0, part)
        num //= 1000
        i += 1
    
    return " ".join(result)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(number_to_words)
