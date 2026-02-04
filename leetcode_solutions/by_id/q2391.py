# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2391
标题: Strong Password Checker II
难度: easy
链接: https://leetcode.cn/problems/strong-password-checker-ii/
题目类型: 字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2299. 强密码检验器 II - 如果一个密码满足以下所有条件，我们称它是一个 强 密码： * 它有至少 8 个字符。 * 至少包含 一个小写英文 字母。 * 至少包含 一个大写英文 字母。 * 至少包含 一个数字 。 * 至少包含 一个特殊字符 。特殊字符为："!@#$%^&*()-+" 中的一个。 * 它 不 包含 2 个连续相同的字符（比方说 "aab" 不符合该条件，但是 "aba" 符合该条件）。 给你一个字符串 password ，如果它是一个 强 密码，返回 true，否则返回 false 。 示例 1： 输入：password = "IloveLe3tcode!" 输出：true 解释：密码满足所有的要求，所以我们返回 true 。 示例 2： 输入：password = "Me+You--IsMyDream" 输出：false 解释：密码不包含数字，且包含 2 个连续相同的字符。所以我们返回 false 。 示例 3： 输入：password = "1aB!" 输出：false 解释：密码不符合长度要求。所以我们返回 false 。 提示： * 1 <= password.length <= 100 * password 包含字母，数字和 "!@#$%^&*()-+" 这些特殊字符。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 检查密码是否满足所有给定的条件。

算法步骤:
1. 检查密码长度是否至少为8个字符。
2. 检查密码是否包含至少一个小写字母、一个大写字母、一个数字和一个特殊字符。
3. 检查密码是否包含两个连续相同的字符。

关键点:
- 使用正则表达式来简化字符类型的检查。
- 通过遍历密码字符串来检查连续相同字符。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是密码的长度。我们需要遍历密码字符串一次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def strong_password_checker(password: str) -> bool:
    """
    检查密码是否是强密码
    """
    if len(password) < 8:
        return False
    
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-+" for c in password)
    
    if not (has_lower and has_upper and has_digit and has_special):
        return False
    
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return False
    
    return True


Solution = create_solution(strong_password_checker)