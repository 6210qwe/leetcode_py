# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 320
标题: Generalized Abbreviation
难度: medium
链接: https://leetcode.cn/problems/generalized-abbreviation/
题目类型: 位运算、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
320. 列举单词的全部缩写 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯，每个字符可以选择保留或缩写

算法步骤:
1. 回溯枚举每个字符的选择
2. 如果选择缩写，累加计数
3. 如果选择保留，先输出计数（如果有），再输出字符

关键点:
- 回溯枚举
- 处理连续缩写
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n) - n为字符串长度
空间复杂度: O(n) - 递归栈空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def generate_abbreviations(word: str) -> List[str]:
    """
    函数式接口 - 列举单词的全部缩写
    
    实现思路:
    回溯：每个字符可以选择保留或缩写。
    
    Args:
        word: 单词字符串
        
    Returns:
        所有可能的缩写
        
    Example:
        >>> generate_abbreviations("word")
        ['word', 'wor1', 'wo1d', 'wo2', 'w1rd', 'w1r1', 'w2d', 'w3', '1ord', '1or1', '1o1d', '1o2', '2rd', '2r1', '3d', '4']
    """
    result = []
    
    def backtrack(index: int, path: str, count: int):
        """回溯函数"""
        if index == len(word):
            if count > 0:
                path += str(count)
            result.append(path)
            return
        
        # 选择缩写当前字符
        backtrack(index + 1, path, count + 1)
        
        # 选择保留当前字符
        new_path = path + (str(count) if count > 0 else "") + word[index]
        backtrack(index + 1, new_path, 0)
    
    backtrack(0, "", 0)
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(generate_abbreviations)
