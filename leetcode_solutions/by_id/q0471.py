# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 471
标题: Encode String with Shortest Length
难度: hard
链接: https://leetcode.cn/problems/encode-string-with-shortest-length/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
471. 编码最短长度的字符串 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 动态规划，找到最短编码

算法步骤:
1. 使用DP记录每个子串的最短编码
2. 对于每个子串，尝试所有可能的重复模式
3. 选择最短的编码方式

关键点:
- DP + 字符串匹配
- 时间复杂度O(n^3)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^3) - n为字符串长度
空间复杂度: O(n^2) - DP数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from functools import lru_cache
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def encode_string_with_shortest_length(s: str) -> str:
    """
    函数式接口 - 编码最短长度的字符串
    
    实现思路:
    动态规划：找到最短编码方式。
    
    Args:
        s: 输入字符串
        
    Returns:
        最短编码字符串
        
    Example:
        >>> encode_string_with_shortest_length("aaa")
        'aaa'
    """
    @lru_cache(maxsize=None)
    def dp(i: int, j: int) -> str:
        """返回s[i:j+1]的最短编码"""
        if i > j:
            return ""
        if i == j:
            return s[i]
        
        substr = s[i:j+1]
        # 尝试所有可能的重复模式
        for k in range(1, (j - i + 1) // 2 + 1):
            pattern = s[i:i+k]
            if len(substr) % len(pattern) == 0:
                repeat = len(substr) // len(pattern)
                if pattern * repeat == substr:
                    encoded = f"{repeat}[{dp(i, i+k-1)}]"
                    if len(encoded) < len(substr):
                        return encoded
        
        # 尝试分割
        result = substr
        for k in range(i, j):
            left = dp(i, k)
            right = dp(k+1, j)
            if len(left) + len(right) < len(result):
                result = left + right
        
        return result
    
    return dp(0, len(s) - 1)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(encode_string_with_shortest_length)
