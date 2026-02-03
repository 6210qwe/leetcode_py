# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000250
标题: 字符串的排列
难度: medium
链接: https://leetcode.cn/problems/MPnaiL/
题目类型: 哈希表、双指针、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 014. 字符串的排列 - 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的某个变位词。 换句话说，第一个字符串的排列之一是第二个字符串的 子串 。 示例 1： 输入: s1 = "ab" s2 = "eidbaooo" 输出: True 解释: s2 包含 s1 的排列之一 ("ba"). 示例 2： 输入: s1= "ab" s2 = "eidboaoo" 输出: False 提示： * 1 <= s1.length, s2.length <= 104 * s1 和 s2 仅包含小写字母 注意：本题与主站 567 题相同： https://leetcode.cn/problems/permutation-in-string/ [https://leetcode.cn/problems/permutation-in-string/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 滑动窗口 + 26 维计数差分

算法步骤:
1. 统计 s1 的字符频次 need[26]
2. 用固定长度为 len(s1) 的滑动窗口遍历 s2，维护窗口频次 window[26]
3. 每次窗口右移一位更新 window，并在窗口长度达到 len(s1) 时比较 need 与 window
4. 若某个窗口频次完全相同，说明 s2 包含 s1 的变位词子串，返回 True

关键点:
- 窗口长度固定为 len(s1)
- 用 26 个小写字母频次对比即可判断是否为变位词
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n 为 s2 长度（每步 O(1)，比较可用匹配计数优化，这里 26 常数）
空间复杂度: O(1) - 26 个计数数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def check_inclusion(s1: str, s2: str) -> bool:
    """
    函数式接口 - 字符串的排列
    """
    m, n = len(s1), len(s2)
    if m > n:
        return False

    need = [0] * 26
    window = [0] * 26
    for ch in s1:
        need[ord(ch) - 97] += 1

    for i, ch in enumerate(s2):
        window[ord(ch) - 97] += 1
        if i >= m:
            window[ord(s2[i - m]) - 97] -= 1
        if i >= m - 1 and window == need:
            return True
    return False


Solution = create_solution(check_inclusion)
