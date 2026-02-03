# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000255
标题: 验证回文串 II
难度: easy
链接: https://leetcode.cn/problems/RQku0D/
题目类型: 贪心、双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 019. 验证回文串 II - 给定一个非空字符串 s，请判断如果 最多 从字符串中删除一个字符能否得到一个回文字符串。 示例 1： 输入: s = "aba" 输出: true 示例 2： 输入: s = "abca" 输出: true 解释: 可以删除 "c" 字符 或者 "b" 字符 示例 3： 输入: s = "abc" 输出: false 提示： * 1 <= s.length <= 105 * s 由小写英文字母组成 注意：本题与主站 680 题相同： https://leetcode.cn/problems/valid-palindrome-ii/ [https://leetcode.cn/problems/valid-palindrome-ii/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 双指针，遇到不匹配时尝试跳过左或右一个字符

算法步骤:
1. 使用两个指针 left, right 从两端向中间移动
2. 若 s[left] == s[right]，继续收缩
3. 第一次遇到不相等时：
   - 判断跳过 left（即检查 s[left+1:right+1] 是否回文）
   - 或跳过 right（检查 s[left:right] 是否回文）
   - 只要有一个为真则返回 True，否则 False
4. 若遍历结束未出现冲突，返回 True

关键点:
- 只允许删除最多一个字符，因此只在第一次不匹配处做两次子串回文检查
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


def valid_palindrome(s: str) -> bool:
    """
    函数式接口 - 验证回文串 II
    """
    def is_pal(l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return is_pal(left + 1, right) or is_pal(left, right - 1)
    return True


Solution = create_solution(valid_palindrome)
