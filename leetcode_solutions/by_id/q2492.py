# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2492
标题: Length of the Longest Alphabetical Continuous Substring
难度: medium
链接: https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/
题目类型: 字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2414. 最长的字母序连续子字符串的长度 - 字母序连续字符串 是由字母表中连续字母组成的字符串。换句话说，字符串 "abcdefghijklmnopqrstuvwxyz" 的任意子字符串都是 字母序连续字符串 。 * 例如，"abc" 是一个字母序连续字符串，而 "acb" 和 "za" 不是。 给你一个仅由小写英文字母组成的字符串 s ，返回其 最长 的 字母序连续子字符串 的长度。 示例 1： 输入：s = "abacaba" 输出：2 解释：共有 4 个不同的字母序连续子字符串 "a"、"b"、"c" 和 "ab" 。 "ab" 是最长的字母序连续子字符串。 示例 2： 输入：s = "abcde" 输出：5 解释："abcde" 是最长的字母序连续子字符串。 提示： * 1 <= s.length <= 105 * s 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到最长的字母序连续子字符串。

算法步骤:
1. 初始化两个变量 `max_length` 和 `current_length`，分别记录最长子字符串的长度和当前子字符串的长度。
2. 遍历字符串 `s`，检查当前字符和前一个字符是否连续。
3. 如果连续，则增加 `current_length`。
4. 如果不连续，则更新 `max_length` 并重置 `current_length`。
5. 最后返回 `max_length` 和 `current_length` 中的最大值。

关键点:
- 使用 ASCII 值来判断字符是否连续。
- 通过滑动窗口技术，一次遍历即可找到最长的字母序连续子字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。我们只需要遍历字符串一次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_alphabetical_substring(s: str) -> int:
    """
    函数式接口 - 找到最长的字母序连续子字符串的长度
    """
    if not s:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(s)):
        if ord(s[i]) == ord(s[i - 1]) + 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length


Solution = create_solution(longest_alphabetical_substring)