# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 28
标题: Find the Index of the First Occurrence in a String
难度: easy
链接: https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
题目类型: 双指针、字符串、字符串匹配
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
28. 找出字符串中第一个匹配项的下标 - 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回 -1 。 示例 1： 输入：haystack = "sadbutsad", needle = "sad" 输出：0 解释："sad" 在下标 0 和 6 处匹配。 第一个匹配项的下标是 0 ，所以返回 0 。 示例 2： 输入：haystack = "leetcode", needle = "leeto" 输出：-1 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。 提示： * 1 <= haystack.length, needle.length <= 104 * haystack 和 needle 仅由小写英文字符组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 暴力匹配法，遍历haystack的每个可能起始位置，检查是否匹配needle

算法步骤:
1. 如果needle为空，返回0
2. 遍历haystack的每个可能起始位置i（0到len(haystack)-len(needle)）
3. 对于每个起始位置，检查haystack[i:i+len(needle)]是否等于needle
4. 如果匹配，返回i
5. 如果遍历完都没有匹配，返回-1

关键点:
- 暴力匹配法简单直接，对于小规模数据效率足够
- 时间复杂度O(mn)，m和n分别为haystack和needle的长度
- 可以使用KMP算法优化到O(m+n)，但实现复杂度较高
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(mn) - m为haystack长度，n为needle长度，最坏情况下需要比较mn次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from leetcode_solutions.utils.solution import create_solution


def str_str(haystack: str, needle: str) -> int:
    """
    函数式接口 - 暴力匹配法实现
    
    实现思路:
    遍历haystack的每个可能起始位置，检查是否匹配needle。
    
    Args:
        haystack: 主字符串
        needle: 模式字符串
        
    Returns:
        第一个匹配项的下标，如果不存在则返回-1
        
    Example:
        >>> str_str("sadbutsad", "sad")
        0
        >>> str_str("leetcode", "leeto")
        -1
    """
    if not needle:
        return 0
    
    n = len(needle)
    m = len(haystack)
    
    for i in range(m - n + 1):
        if haystack[i:i + n] == needle:
            return i
    
    return -1


# 自动生成Solution类（无需手动编写）
Solution = create_solution(str_str)
