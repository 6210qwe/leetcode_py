# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 420
标题: Strong Password Checker
难度: hard
链接: https://leetcode.cn/problems/strong-password-checker/
题目类型: 贪心、字符串、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
420. 强密码检验器 - 满足以下条件的密码被认为是强密码： * 由至少 6 个，至多 20 个字符组成。 * 包含至少 一个小写 字母，至少 一个大写 字母，和至少 一个数字 。 * 不包含连续三个重复字符 (比如 "Baaabb0" 是弱密码, 但是 "Baaba0" 是强密码)。 给你一个字符串 password ，返回 将 password 修改到满足强密码条件需要的最少修改步数。如果 password 已经是强密码，则返回 0 。 在一步修改操作中，你可以： * 插入一个字符到 password ， * 从 password 中删除一个字符，或 * 用另一个字符来替换 password 中的某个字符。 示例 1： 输入：password = "a" 输出：5 示例 2： 输入：password = "aA1" 输出：3 示例 3： 输入：password = "1337C0d3" 输出：0 提示： * 1 <= password.length <= 50 * password 由字母、数字、点 '.' 或者感叹号 '!' 组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，根据密码长度和字符要求进行优化

算法步骤:
1. 分析密码长度是否在 [6, 20] 之间，如果不是则计算需要插入或删除的字符数。
2. 检查密码是否包含小写字母、大写字母和数字，记录缺失的字符类型。
3. 检查密码中是否存在连续三个重复字符，记录需要替换的字符数。
4. 根据需要插入、删除和替换的字符数，使用贪心算法进行优化。

关键点:
- 优先处理长度问题，再处理字符类型问题，最后处理重复字符问题。
- 优化时间和空间复杂度，尽量减少不必要的操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历密码字符串
空间复杂度: O(1) - 只使用常数级额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def strong_password_checker(password: str) -> int:
    """
    函数式接口 - 计算将密码修改为强密码所需的最少修改步数
    
    实现思路:
    1. 检查密码长度是否在 [6, 20] 之间，如果不是则计算需要插入或删除的字符数。
    2. 检查密码是否包含小写字母、大写字母和数字，记录缺失的字符类型。
    3. 检查密码中是否存在连续三个重复字符，记录需要替换的字符数。
    4. 根据需要插入、删除和替换的字符数，使用贪心算法进行优化。

    Args:
        password (str): 输入的密码字符串
        
    Returns:
        int: 将密码修改为强密码所需的最少修改步数
        
    Example:
        >>> strong_password_checker("a")
        5
        >>> strong_password_checker("aA1")
        3
        >>> strong_password_checker("1337C0d3")
        0
    """
    n = len(password)
    if n < 6:
        return max(6 - n, 3 - check_requirements(password))
    
    if n > 20:
        # 删除字符
        to_delete = n - 20
        one, two, three = 0, 0, 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            if length >= 3:
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
                else:
                    three += 1
            i = j
        delete_used = min(to_delete, one * 1 + two * 2 + three * 3)
        to_delete -= delete_used
        one = max(0, one - to_delete // 3)
        two = max(0, two - to_delete // 3)
        three = max(0, three - to_delete // 3)
        to_replace = one + two * 2 + three * 3
        return to_delete + max(to_replace, 3 - check_requirements(password))
    
    # 长度在 [6, 20] 之间
    return max(3 - check_requirements(password), count_repeats(password))

def check_requirements(password: str) -> int:
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return sum([has_lower, has_upper, has_digit])

def count_repeats(password: str) -> int:
    to_replace = 0
    i = 0
    while i < len(password):
        j = i + 1
        while j < len(password) and password[j] == password[i]:
            j += 1
        length = j - i
        if length >= 3:
            to_replace += length // 3
        i = j
    return to_replace

# 自动生成Solution类（无需手动编写）
Solution = create_solution(strong_password_checker)