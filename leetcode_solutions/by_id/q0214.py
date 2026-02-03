# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 214
标题: Shortest Palindrome
难度: hard
链接: https://leetcode.cn/problems/shortest-palindrome/
题目类型: 字符串、字符串匹配、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
214. 最短回文串 - 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。 示例 1： 输入：s = "aacecaaa" 输出："aaacecaaa" 示例 2： 输入：s = "abcd" 输出："dcbabcd" 提示： * 0 <= s.length <= 5 * 104 * s 仅由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: KMP算法，找到s的最长回文前缀

算法步骤:
1. 构造字符串s + '#' + reverse(s)
2. 使用KMP计算next数组
3. 找到最长回文前缀的长度
4. 将剩余部分反转后添加到前面

关键点:
- KMP算法找最长回文前缀
- 时间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - KMP算法
空间复杂度: O(n) - next数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def shortest_palindrome(s: str) -> str:
    """
    函数式接口 - 最短回文串
    
    实现思路:
    KMP算法：找到s的最长回文前缀。
    
    Args:
        s: 输入字符串
        
    Returns:
        最短回文串
        
    Example:
        >>> shortest_palindrome("aacecaaa")
        'aaacecaaa'
    """
    if not s:
        return ""
    
    # 构造字符串：s + '#' + reverse(s)
    rev_s = s[::-1]
    combined = s + '#' + rev_s
    
    # KMP计算next数组
    n = len(combined)
    next_arr = [0] * n
    
    j = 0
    for i in range(1, n):
        while j > 0 and combined[i] != combined[j]:
            j = next_arr[j - 1]
        if combined[i] == combined[j]:
            j += 1
        next_arr[i] = j
    
    # 最长回文前缀的长度
    max_len = next_arr[-1]
    
    # 将剩余部分反转后添加到前面
    return rev_s[:len(s) - max_len] + s


# 自动生成Solution类（无需手动编写）
Solution = create_solution(shortest_palindrome)
