# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2468
标题: Valid Palindrome IV
难度: medium
链接: https://leetcode.cn/problems/valid-palindrome-iv/
题目类型: 双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2330. 验证回文串 IV - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针从两端向中间遍历字符串，允许删除一个字符来判断是否可以构成回文串。

算法步骤:
1. 初始化两个指针 left 和 right 分别指向字符串的开头和结尾。
2. 当 left < right 时，比较 s[left] 和 s[right]：
   - 如果 s[left] == s[right]，则 left++，right--。
   - 如果 s[left] != s[right]，则检查 s[left+1:right+1] 和 s[left:right] 是否为回文串。
3. 如果其中一个子串是回文串，则返回 True；否则返回 False。

关键点:
- 通过双指针遍历字符串，允许删除一个字符来判断是否可以构成回文串。
- 使用辅助函数 is_palindrome 来判断子串是否为回文串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度。每个字符最多被访问两次。
空间复杂度: O(1)，只使用了常数级的额外空间。
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
    函数式接口 - 判断字符串在删除一个字符后是否可以构成回文串
    """
    def is_palindrome(s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # 检查删除一个字符后的子串是否为回文串
            return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
        left += 1
        right -= 1
    return True


Solution = create_solution(valid_palindrome)