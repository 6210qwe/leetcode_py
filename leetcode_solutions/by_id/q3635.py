# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3635
标题: Smallest Divisible Digit Product II
难度: hard
链接: https://leetcode.cn/problems/smallest-divisible-digit-product-ii/
题目类型: 贪心、数学、字符串、回溯、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3348. 最小可整除数位乘积 II - 给你一个字符串 num ，表示一个 正 整数，同时给你一个整数 t 。 如果一个整数 没有 任何数位是 0 ，那么我们称这个整数是 无零 数字。 请你返回一个字符串，这个字符串对应的整数是大于等于 num 的 最小无零 整数，且 各数位之积 能被 t 整除。如果不存在这样的数字，请你返回 "-1" 。 示例 1： 输入：num = "1234", t = 256 输出："1488" 解释： 大于等于 1234 且能被 256 整除的最小无零整数是 1488 ，它的数位乘积为 256 。 示例 2： 输入：num = "12355", t = 50 输出："12355" 解释： 12355 已经是无零且数位乘积能被 50 整除的整数，它的数位乘积为 150 。 示例 3： 输入：num = "11111", t = 26 输出："-1" 解释： 不存在大于等于 11111 且数位乘积能被 26 整除的整数。 提示： * 2 <= num.length <= 2 * 105 * num 只包含 ['0', '9'] 之间的数字。 * num 不包含前导 0 。 * 1 <= t <= 1014
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心和回溯的方法，从给定的数字开始逐步增加，直到找到满足条件的最小无零整数。

算法步骤:
1. 定义一个辅助函数 `is_valid` 来检查一个数字是否满足条件。
2. 从给定的数字 `num` 开始，逐步增加，直到找到满足条件的数字。
3. 在每次增加时，使用回溯方法生成下一个可能的无零整数。
4. 如果找到满足条件的数字，返回该数字；否则返回 "-1"。

关键点:
- 使用贪心策略，从当前数字开始逐步增加。
- 使用回溯方法生成下一个可能的无零整数。
- 检查每个生成的数字是否满足条件。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(9^n)，其中 n 是 num 的长度。最坏情况下，需要遍历所有可能的无零整数。
空间复杂度: O(n)，递归调用栈的深度最多为 n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def is_valid(num: str, t: int) -> bool:
    product = 1
    for digit in num:
        product *= int(digit)
        if product % t == 0:
            return True
    return False

def find_next_number(num: str) -> str:
    n = len(num)
    digits = list(num)
    
    for i in range(n - 1, -1, -1):
        if digits[i] < '9':
            digits[i] = chr(ord(digits[i]) + 1)
            for j in range(i + 1, n):
                digits[j] = '1'
            return ''.join(digits)
    
    return '1' + '1' * n

def solution_function_name(num: str, t: int) -> str:
    """
    函数式接口 - 返回大于等于 num 的最小无零整数，且各数位之积能被 t 整除。
    """
    current_num = num
    while True:
        if is_valid(current_num, t):
            return current_num
        current_num = find_next_number(current_num)
        if len(current_num) > len(num) * 2:
            return "-1"

Solution = create_solution(solution_function_name)