# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 686
标题: Repeated String Match
难度: medium
链接: https://leetcode.cn/problems/repeated-string-match/
题目类型: 字符串、字符串匹配
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
686. 重复叠加字符串匹配 - 给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。 注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。 示例 1： 输入：a = "abcd", b = "cdabcdab" 输出：3 解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。 示例 2： 输入：a = "a", b = "aa" 输出：2 示例 3： 输入：a = "a", b = "a" 输出：1 示例 4： 输入：a = "abc", b = "wxyz" 输出：-1 提示： * 1 <= a.length <= 104 * 1 <= b.length <= 104 * a 和 b 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 KMP 算法进行字符串匹配，通过计算 a 重复叠加的最小次数来构建目标字符串。

算法步骤:
1. 计算 a 重复叠加的最小次数，使得叠加后的字符串长度大于等于 b。
2. 构建叠加后的字符串。
3. 使用 KMP 算法在叠加后的字符串中查找 b。

关键点:
- 计算 a 重复叠加的最小次数。
- 使用 KMP 算法进行高效字符串匹配。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是字符串 a 的长度，m 是字符串 b 的长度。
空间复杂度: O(m)，KMP 算法的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def repeated_string_match(a: str, b: str) -> int:
    """
    函数式接口 - 寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串。
    """
    def compute_lps(pattern: str) -> List[int]:
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def kmp_search(text: str, pattern: str) -> bool:
        lps = compute_lps(pattern)
        i = j = 0
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
                if j == len(pattern):
                    return True
            elif j > 0:
                j = lps[j - 1]
            else:
                i += 1
        return False

    # 计算 a 重复叠加的最小次数
    min_repeats = (len(b) + len(a) - 1) // len(a)
    max_repeats = min_repeats + 1

    # 构建叠加后的字符串
    for repeats in range(min_repeats, max_repeats + 1):
        repeated_a = a * repeats
        if kmp_search(repeated_a, b):
            return repeats

    return -1


Solution = create_solution(repeated_string_match)