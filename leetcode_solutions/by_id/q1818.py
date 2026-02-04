# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1818
标题: Maximum Score From Removing Substrings
难度: medium
链接: https://leetcode.cn/problems/maximum-score-from-removing-substrings/
题目类型: 栈、贪心、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1717. 删除子字符串的最大得分 - 给你一个字符串 s 和两个整数 x 和 y 。你可以执行下面两种操作任意次。 * 删除子字符串 "ab" 并得到 x 分。 * 比方说，从 "cabxbae" 删除 ab ，得到 "cxbae" 。 * 删除子字符串"ba" 并得到 y 分。 * 比方说，从 "cabxbae" 删除 ba ，得到 "cabxe" 。 请返回对 s 字符串执行上面操作若干次能得到的最大得分。 示例 1： 输入：s = "cdbcbbaaabab", x = 4, y = 5 输出：19 解释： - 删除 "cdbcbbaaabab" 中加粗的 "ba" ，得到 s = "cdbcbbaaab" ，加 5 分。 - 删除 "cdbcbbaaab" 中加粗的 "ab" ，得到 s = "cdbcbbaa" ，加 4 分。 - 删除 "cdbcbbaa" 中加粗的 "ba" ，得到 s = "cdbcba" ，加 5 分。 - 删除 "cdbcba" 中加粗的 "ba" ，得到 s = "cdbc" ，加 5 分。 总得分为 5 + 4 + 5 + 5 = 19 。 示例 2： 输入：s = "aabbaaxybbaabb", x = 5, y = 4 输出：20 提示： * 1 <= s.length <= 105 * 1 <= x, y <= 104 * s 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和栈来处理字符串，优先删除得分较高的子字符串。

算法步骤:
1. 如果 x >= y，先删除所有 "ab" 子字符串，再删除所有 "ba" 子字符串。
2. 如果 x < y，先删除所有 "ba" 子字符串，再删除所有 "ab" 子字符串。
3. 使用栈来记录当前未匹配的字符，并在匹配时计算得分。

关键点:
- 使用栈来跟踪未匹配的字符。
- 优先删除得分较高的子字符串以最大化得分。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。每个字符最多只会被处理两次（一次入栈，一次出栈）。
空间复杂度: O(n)，最坏情况下栈中可能存储所有字符。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_score_from_removing_substrings(s: str, x: int, y: int) -> int:
    """
    函数式接口 - 计算删除子字符串的最大得分
    """
    def remove_substrings(s: str, sub: str, score: int) -> (str, int):
        stack = []
        total_score = 0
        for char in s:
            if stack and stack[-1] + char == sub:
                stack.pop()
                total_score += score
            else:
                stack.append(char)
        return ''.join(stack), total_score

    if x >= y:
        s, score_ab = remove_substrings(s, "ab", x)
        s, score_ba = remove_substrings(s, "ba", y)
    else:
        s, score_ba = remove_substrings(s, "ba", y)
        s, score_ab = remove_substrings(s, "ab", x)

    return score_ab + score_ba


Solution = create_solution(max_score_from_removing_substrings)