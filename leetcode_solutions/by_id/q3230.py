# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3230
标题: Remove Adjacent Almost-Equal Characters
难度: medium
链接: https://leetcode.cn/problems/remove-adjacent-almost-equal-characters/
题目类型: 贪心、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2957. 消除相邻近似相等字符 - 给你一个下标从 0 开始的字符串 word 。 一次操作中，你可以选择 word 中任意一个下标 i ，将 word[i] 修改成任意一个小写英文字母。 请你返回消除 word 中所有相邻 近似相等 字符的 最少 操作次数。 两个字符 a 和 b 如果满足 a == b 或者 a 和 b 在字母表中是相邻的，那么我们称它们是 近似相等 字符。 示例 1： 输入：word = "aaaaa" 输出：2 解释：我们将 word 变为 "acaca" ，该字符串没有相邻近似相等字符。 消除 word 中所有相邻近似相等字符最少需要 2 次操作。 示例 2： 输入：word = "abddez" 输出：2 解释：我们将 word 变为 "ybdoez" ，该字符串没有相邻近似相等字符。 消除 word 中所有相邻近似相等字符最少需要 2 次操作。 示例 3： 输入：word = "zyxyxyz" 输出：3 解释：我们将 word 变为 "zaxaxaz" ，该字符串没有相邻近似相等字符。 消除 word 中所有相邻近似相等字符最少需要 3 次操作 提示： * 1 <= word.length <= 100 * word 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，遍历字符串并记录当前字符和前一个字符，如果当前字符与前一个字符近似相等，则进行一次操作，并更新前一个字符。

算法步骤:
1. 初始化操作次数 `operations` 为 0。
2. 初始化前一个字符 `prev_char` 为空字符。
3. 遍历字符串 `word`：
   - 如果当前字符与前一个字符近似相等，则增加操作次数 `operations`，并更新前一个字符 `prev_char` 为一个不同于当前字符且不与下一个字符近似相等的字符。
   - 否则，更新前一个字符 `prev_char` 为当前字符。
4. 返回操作次数 `operations`。

关键点:
- 通过贪心算法，每次遇到近似相等字符时，立即进行操作，确保最少操作次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 `word` 的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(word: str) -> int:
    """
    函数式接口 - 消除 word 中所有相邻近似相等字符的最少操作次数
    """
    def is_almost_equal(a: str, b: str) -> bool:
        """判断两个字符是否近似相等"""
        return abs(ord(a) - ord(b)) <= 1

    operations = 0
    prev_char = ''

    for char in word:
        if is_almost_equal(char, prev_char):
            operations += 1
            # 更新前一个字符为一个不同于当前字符且不与下一个字符近似相等的字符
            next_char = 'a' if char != 'a' else 'b'
            prev_char = next_char
        else:
            prev_char = char

    return operations


Solution = create_solution(solution_function_name)