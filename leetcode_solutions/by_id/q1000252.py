# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000252
标题: 无重复字符的最长子串
难度: medium
链接: https://leetcode.cn/problems/wtcaE1/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 016. 无重复字符的最长子串 - 给定一个字符串 s ，请你找出其中不含有重复字符的 最长连续子字符串 的长度。 示例 1： 输入: s = "abcabcbb" 输出: 3 解释: 因为无重复字符的最长子字符串是 "abc"，所以其长度为 3。 示例 2： 输入: s = "bbbbb" 输出: 1 解释: 因为无重复字符的最长子字符串是 "b"，所以其长度为 1。 示例 3： 输入: s = "pwwkew" 输出: 3 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。 示例 4： 输入: s = "" 输出: 0 提示： * 0 <= s.length <= 5 * 104 * s 由英文字母、数字、符号和空格组成 注意：本题与主站 3 题相同： https://leetcode.cn/problems/longest-substring-without-repeating-characters/ [https://leetcode.cn/problems/longest-substring-without-repeating-characters/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 滑动窗口 + 哈希表记录字符最近出现位置

算法步骤:
1. 使用哈希表 last 记录每个字符最后出现的下标
2. 维护窗口左边界 left，遍历右边界 right：
   - 若 s[right] 曾出现过且 last[s[right]] >= left，则说明重复落在窗口内，将 left 更新为 last[s[right]] + 1
   - 更新 last[s[right]] = right
   - 更新答案为 max(ans, right - left + 1)
3. 返回 ans

关键点:
- left 只能向右移动，保证总体 O(n)
- 需要判断重复字符是否在当前窗口内（last[ch] >= left）
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(Σ) - Σ 为字符集大小（这里可视为 O(1)）
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def length_of_longest_substring(s: str) -> int:
    """
    函数式接口 - 无重复字符的最长子串
    """
    last = {}
    left = 0
    ans = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        ans = max(ans, right - left + 1)
    return ans


Solution = create_solution(length_of_longest_substring)
