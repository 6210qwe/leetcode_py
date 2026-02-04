# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 897
标题: Prime Palindrome
难度: medium
链接: https://leetcode.cn/problems/prime-palindrome/
题目类型: 数学、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
866. 回文质数 - 给你一个整数 n ，返回大于或等于 n 的最小 回文质数。 一个整数如果恰好有两个除数：1 和它本身，那么它是 质数 。注意，1 不是质数。 * 例如，2、3、5、7、11 和 13 都是质数。 一个整数如果从左向右读和从右向左读是相同的，那么它是 回文数 。 * 例如，101 和 12321 都是回文数。 测试用例保证答案总是存在，并且在 [2, 2 * 108] 范围内。 示例 1： 输入：n = 6 输出：7 示例 2： 输入：n = 8 输出：11 示例 3： 输入：n = 13 输出：101 提示： * 1 <= n <= 108
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 生成大于或等于 n 的所有回文数，并检查它们是否为质数。

算法步骤:
1. 如果 n 在 [8, 11) 范围内，直接返回 11。
2. 从 n 开始，生成下一个回文数。
3. 检查该回文数是否为质数。
4. 如果是质数，返回该数；否则继续生成下一个回文数。

关键点:
- 生成回文数时，只需要生成奇数长度的回文数（除了 11）。
- 使用高效的质数检查方法。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(sqrt(N) * log N)，其中 N 是答案的范围。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def next_palindrome(n: int) -> int:
    if n < 10:
        return n + 1
    str_n = str(n)
    length = len(str_n)
    if all(c == '9' for c in str_n):
        return 10 ** length + 1
    mid = length // 2
    left_half = int(str_n[:mid])
    if length % 2 == 0:
        new_left_half = left_half + 1
    else:
        new_left_half = int(str_n[:mid + 1]) + 1
    new_str_n = str(new_left_half) + str(new_left_half)[-2::-1] if length % 2 == 0 else str(new_left_half) + str(new_left_half)[:-1][::-1]
    return int(new_str_n)


def prime_palindrome(n: int) -> int:
    if 8 <= n <= 11:
        return 11
    while True:
        n = next_palindrome(n)
        if is_prime(n):
            return n


Solution = create_solution(prime_palindrome)