# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000254
标题: 验证回文串
难度: easy
链接: https://leetcode.cn/problems/XltzEq/
题目类型: 双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 018. 验证回文串 - 给定一个字符串 s ，验证 s 是否是 回文串 ，只考虑字母和数字字符，可以忽略字母的大小写。 本题中，将空字符串定义为有效的 回文串 。 示例 1： 输入: s = "A man, a plan, a canal: Panama" 输出: true 解释："amanaplanacanalpanama" 是回文串 示例 2： 输入: s = "race a car" 输出: false 解释："raceacar" 不是回文串 提示： * 1 <= s.length <= 2 * 105 * 字符串 s 由 ASCII 字符组成 注意：本题与主站 125 题相同： https://leetcode.cn/problems/valid-palindrome/ [https://leetcode.cn/problems/valid-palindrome/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 双指针从两端向中间收缩，仅比较字母数字并忽略大小写

算法步骤:
1. 初始化 left=0, right=len(s)-1
2. 当 left < right：
   - 若 s[left] 不是字母数字，left += 1
   - 若 s[right] 不是字母数字，right -= 1
   - 否则比较 s[left].lower() 与 s[right].lower()：
       * 不相等返回 False
       * 相等则 left += 1, right -= 1
3. 遍历结束返回 True

关键点:
- 只考虑字母和数字字符
- 比较时需要忽略大小写
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
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
    函数式接口 - 验证回文串
    """
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


Solution = create_solution(is_palindrome)
