# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 267
标题: Palindrome Permutation II
难度: medium
链接: https://leetcode.cn/problems/palindrome-permutation-ii/
题目类型: 哈希表、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
267. 回文排列 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯生成所有回文排列

算法步骤:
1. 统计字符频率
2. 检查是否可以排列成回文
3. 构造左半部分，回溯生成所有排列
4. 拼接成完整回文

关键点:
- 回溯生成排列
- 去重处理
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((n/2)!) - 排列数
空间复杂度: O(n) - 递归栈空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import Counter
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def generate_palindromes(s: str) -> List[str]:
    """
    函数式接口 - 回文排列 II
    
    实现思路:
    回溯生成所有回文排列。
    
    Args:
        s: 字符串
        
    Returns:
        所有回文排列
        
    Example:
        >>> generate_palindromes("aabb")
        ['abba', 'baab']
    """
    counter = Counter(s)
    odd_chars = [char for char, count in counter.items() if count % 2 == 1]
    
    # 检查是否可以排列成回文
    if len(odd_chars) > 1:
        return []
    
    # 构造左半部分字符列表
    chars = []
    mid_char = odd_chars[0] if odd_chars else ''
    
    for char, count in counter.items():
        chars.extend([char] * (count // 2))
    
    # 回溯生成左半部分的所有排列
    result = []
    used = [False] * len(chars)
    
    def backtrack(path: List[str]):
        """回溯函数"""
        if len(path) == len(chars):
            left = ''.join(path)
            right = left[::-1]
            result.append(left + mid_char + right)
            return
        
        for i in range(len(chars)):
            if used[i] or (i > 0 and chars[i] == chars[i-1] and not used[i-1]):
                continue
            used[i] = True
            path.append(chars[i])
            backtrack(path)
            path.pop()
            used[i] = False
    
    backtrack([])
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(generate_palindromes)
