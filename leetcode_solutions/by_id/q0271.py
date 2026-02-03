# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 271
标题: Encode and Decode Strings
难度: medium
链接: https://leetcode.cn/problems/encode-and-decode-strings/
题目类型: 设计、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
271. 字符串的编码与解码 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用长度+分隔符编码，解码时按长度提取

算法步骤:
1. 编码：对每个字符串，存储长度+分隔符+字符串
2. 解码：按长度提取每个字符串

关键点:
- 长度前缀编码
- 时间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n为所有字符串总长度
空间复杂度: O(n) - 编码后字符串
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def encode(strs: List[str]) -> str:
    """
    函数式接口 - 字符串的编码
    
    实现思路:
    使用长度+分隔符编码。
    
    Args:
        strs: 字符串数组
        
    Returns:
        编码后的字符串
        
    Example:
        >>> encode(["lint","code","love","you"])
        '4#lint4#code4#love3#you'
    """
    result = []
    for s in strs:
        result.append(str(len(s)) + '#' + s)
    return ''.join(result)


def decode(s: str) -> List[str]:
    """
    函数式接口 - 字符串的解码
    
    实现思路:
    按长度提取每个字符串。
    
    Args:
        s: 编码后的字符串
        
    Returns:
        解码后的字符串数组
        
    Example:
        >>> decode('4#lint4#code4#love3#you')
        ['lint', 'code', 'love', 'you']
    """
    result = []
    i = 0
    while i < len(s):
        # 找到分隔符
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        result.append(s[j+1:j+1+length])
        i = j + 1 + length
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(encode, decode)
