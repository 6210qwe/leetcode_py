# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2231
标题: Find First Palindromic String in the Array
难度: easy
链接: https://leetcode.cn/problems/find-first-palindromic-string-in-the-array/
题目类型: 数组、双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2108. 找出数组中的第一个回文字符串 - 给你一个字符串数组 words ，找出并返回数组中的 第一个回文字符串 。如果不存在满足要求的字符串，返回一个 空字符串 "" 。 回文字符串 的定义为：如果一个字符串正着读和反着读一样，那么该字符串就是一个 回文字符串 。 示例 1： 输入：words = ["abc","car","ada","racecar","cool"] 输出："ada" 解释：第一个回文字符串是 "ada" 。 注意，"racecar" 也是回文字符串，但它不是第一个。 示例 2： 输入：words = ["notapalindrome","racecar"] 输出："racecar" 解释：第一个也是唯一一个回文字符串是 "racecar" 。 示例 3： 输入：words = ["def","ghi"] 输出："" 解释：不存在回文字符串，所以返回一个空字符串。 提示： * 1 <= words.length <= 100 * 1 <= words[i].length <= 100 * words[i] 仅由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 遍历字符串数组，检查每个字符串是否为回文字符串。

算法步骤:
1. 定义一个辅助函数 `is_palindrome` 来判断一个字符串是否为回文。
2. 遍历字符串数组 `words`，使用 `is_palindrome` 函数检查每个字符串。
3. 返回第一个回文字符串，如果没有找到则返回空字符串。

关键点:
- 使用双指针方法来判断一个字符串是否为回文。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是字符串数组的长度，m 是字符串的平均长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def is_palindrome(s: str) -> bool:
    """
    判断一个字符串是否为回文字符串。
    """
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def solution_function_name(words: List[str]) -> str:
    """
    函数式接口 - 找出数组中的第一个回文字符串
    """
    for word in words:
        if is_palindrome(word):
            return word
    return ""

Solution = create_solution(solution_function_name)