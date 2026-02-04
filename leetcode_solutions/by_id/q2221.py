# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2221
标题: Check if a Parentheses String Can Be Valid
难度: medium
链接: https://leetcode.cn/problems/check-if-a-parentheses-string-can-be-valid/
题目类型: 栈、贪心、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2116. 判断一个括号字符串是否有效 - 一个括号字符串是只由 '(' 和 ')' 组成的 非空 字符串。如果一个字符串满足下面 任意 一个条件，那么它就是有效的： * 字符串为 (). * 它可以表示为 AB（A 与 B 连接），其中A 和 B 都是有效括号字符串。 * 它可以表示为 (A) ，其中 A 是一个有效括号字符串。 给你一个括号字符串 s 和一个字符串 locked ，两者长度都为 n 。locked 是一个二进制字符串，只包含 '0' 和 '1' 。对于 locked 中 每一个 下标 i ： * 如果 locked[i] 是 '1' ，你 不能 改变 s[i] 。 * 如果 locked[i] 是 '0' ，你 可以 将 s[i] 变为 '(' 或者 ')' 。 如果你可以将 s 变为有效括号字符串，请你返回 true ，否则返回 false 。 示例 1： [https://assets.leetcode.com/uploads/2021/11/06/eg1.png] 输入：s = "))()))", locked = "010100" 输出：true 解释：locked[1] == '1' 和 locked[3] == '1' ，所以我们无法改变 s[1] 或者 s[3] 。 我们可以将 s[0] 和 s[4] 变为 '(' ，不改变 s[2] 和 s[5] ，使 s 变为有效字符串。 示例 2： 输入：s = "()()", locked = "0000" 输出：true 解释：我们不需要做任何改变，因为 s 已经是有效字符串了。 示例 3： 输入：s = ")", locked = "0" 输出：false 解释：locked 允许改变 s[0] 。 但无论将 s[0] 变为 '(' 或者 ')' 都无法使 s 变为有效字符串。 示例 4： 输入：s = "(((())(((())", locked = "111111010111" 输出：true 解释：locked 允许我们改变 s[6] 和 s[8]。 我们将 s[6] 和 s[8] 改为 ')' 使 s 变为有效字符串。 提示： * n == s.length == locked.length * 1 <= n <= 105 * s[i] 要么是 '(' 要么是 ')' 。 * locked[i] 要么是 '0' 要么是 '1' 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个栈来分别记录左括号和可变位置的数量。通过遍历字符串，检查每个字符是否可以形成有效的括号对。

算法步骤:
1. 初始化两个栈，分别用于存储左括号和可变位置的数量。
2. 遍历字符串：
   - 如果当前字符是左括号且锁定，增加左括号栈的计数。
   - 如果当前字符是右括号且锁定，尝试匹配左括号栈中的左括号；如果没有足够的左括号，尝试使用可变位置栈中的位置。
   - 如果当前字符是可变位置，增加可变位置栈的计数。
3. 最后，检查剩余的左括号是否可以用可变位置来匹配。

关键点:
- 使用两个栈分别记录左括号和可变位置的数量。
- 在遍历过程中动态调整栈的计数，确保每个右括号都能找到匹配的左括号或可变位置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度。我们需要遍历整个字符串一次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_be_valid(s: str, locked: str) -> bool:
    """
    判断一个括号字符串是否可以通过改变某些字符变为有效的括号字符串。
    :param s: 括号字符串
    :param locked: 锁定字符串
    :return: 是否可以变为有效括号字符串
    """
    if len(s) % 2 != 0:
        return False

    open_brackets = 0
    flexible_positions = 0

    for i in range(len(s)):
        if locked[i] == '0':
            flexible_positions += 1
        elif s[i] == '(':
            open_brackets += 1
        else:
            if open_brackets > 0:
                open_brackets -= 1
            elif flexible_positions > 0:
                flexible_positions -= 1
            else:
                return False

    close_brackets = 0
    flexible_positions = 0

    for i in range(len(s) - 1, -1, -1):
        if locked[i] == '0':
            flexible_positions += 1
        elif s[i] == ')':
            close_brackets += 1
        else:
            if close_brackets > 0:
                close_brackets -= 1
            elif flexible_positions > 0:
                flexible_positions -= 1
            else:
                return False

    return True


Solution = create_solution(can_be_valid)