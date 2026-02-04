# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3600
标题: Find the K-th Character in String Game I
难度: easy
链接: https://leetcode.cn/problems/find-the-k-th-character-in-string-game-i/
题目类型: 位运算、递归、数学、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3304. 找出第 K 个字符 I - Alice 和 Bob 正在玩一个游戏。最初，Alice 有一个字符串 word = "a"。 给定一个正整数 k。 现在 Bob 会要求 Alice 执行以下操作 无限次 : * 将 word 中的每个字符 更改 为英文字母表中的 下一个 字符来生成一个新字符串，并将其 追加 到原始的 word。 例如，对 "c" 进行操作生成 "cd"，对 "zb" 进行操作生成 "zbac"。 在执行足够多的操作后， word 中 至少 存在 k 个字符，此时返回 word 中第 k 个字符的值。 示例 1: 输入：k = 5 输出："b" 解释： 最初，word = "a"。需要进行三次操作: * 生成的字符串是 "b"，word 变为 "ab"。 * 生成的字符串是 "bc"，word 变为 "abbc"。 * 生成的字符串是 "bccd"，word 变为 "abbcbccd"。 示例 2: 输入：k = 10 输出："c" 提示： * 1 <= k <= 500
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过数学方法直接计算第 k 个字符，避免构造整个字符串。

算法步骤:
1. 计算字符串长度达到 k 时所需的步数。
2. 通过递归或迭代的方法找到第 k 个字符。

关键点:
- 通过数学公式直接计算第 k 个字符的位置，避免构造整个字符串。
- 使用模运算和递归简化问题。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log k)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_kth_character(k: int) -> str:
    """
    函数式接口 - 找出第 k 个字符
    """
    def next_char(c: str) -> str:
        return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))

    def find_char(n: int) -> str:
        if n == 1:
            return 'a'
        length = 1
        step = 1
        while length < n:
            length = 2 * length + step
            step += 1
        if length == n:
            return next_char(find_char(length // 2))
        else:
            return find_char(n - (length - step))

    return find_char(k)


Solution = create_solution(find_kth_character)