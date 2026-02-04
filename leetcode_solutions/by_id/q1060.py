# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1060
标题: Longest Repeating Substring
难度: medium
链接: https://leetcode.cn/problems/longest-repeating-substring/
题目类型: 字符串、二分查找、动态规划、后缀数组、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1062. 最长重复子串的长度 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找和滚动哈希来找到最长重复子串。

算法步骤:
1. 定义一个辅助函数 `has_duplicate_of_length`，用于检查字符串中是否存在长度为 `length` 的重复子串。
2. 使用二分查找来确定最长重复子串的长度。初始范围是 `[1, n-1]`，其中 `n` 是字符串的长度。
3. 在每次二分查找中，使用 `has_duplicate_of_length` 函数来检查当前长度是否可行。
4. 如果存在重复子串，则更新下界；否则，更新上界。
5. 最终返回上界，即为最长重复子串的长度。

关键点:
- 使用滚动哈希来高效地检查子串是否重复。
- 二分查找的时间复杂度为 O(log n)，每次检查的时间复杂度为 O(n)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def has_duplicate_of_length(s: str, length: int, mod: int, base: int) -> bool:
    """
    检查字符串 s 中是否存在长度为 length 的重复子串。
    """
    n = len(s)
    if length == 0:
        return False
    
    hash_value = 0
    for i in range(length):
        hash_value = (hash_value * base + ord(s[i])) % mod
    
    seen = {hash_value}
    
    mult = pow(base, length - 1, mod)
    
    for i in range(1, n - length + 1):
        hash_value = (hash_value * base - ord(s[i - 1]) * mult + ord(s[i + length - 1])) % mod
        if hash_value in seen:
            return True
        seen.add(hash_value)
    
    return False

def solution_function_name(s: str) -> int:
    """
    函数式接口 - 找到最长重复子串的长度
    """
    n = len(s)
    left, right = 1, n - 1
    mod = 10**9 + 7
    base = 26  # 假设字符集为小写字母
    
    while left <= right:
        mid = (left + right) // 2
        if has_duplicate_of_length(s, mid, mod, base):
            left = mid + 1
        else:
            right = mid - 1
    
    return right

Solution = create_solution(solution_function_name)