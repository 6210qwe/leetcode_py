# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000027
标题: Calculator LCCI
难度: medium
链接: https://leetcode.cn/problems/calculator-lcci/
题目类型: 栈、数学、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 16.26. 计算器 - 给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。 表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格 。 整数除法仅保留整数部分。 示例 1： 输入："3+2*2" 输出：7 示例 2： 输入：" 3/2 " 输出：1 示例 3： 输入：" 3+5 / 2 " 输出：5 说明： * 你可以假设所给定的表达式都是有效的。 * 请不要使用内置的库函数 eval。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈来处理表达式中的运算符和操作数，并根据运算符的优先级进行计算。

算法步骤:
1. 初始化两个栈：一个用于存储数字，另一个用于存储运算符。
2. 遍历表达式，将数字和运算符分别压入对应的栈中。
3. 当遇到运算符时，比较当前运算符与栈顶运算符的优先级：
   - 如果当前运算符优先级更高，则直接压入运算符栈。
   - 否则，弹出运算符栈顶运算符及其对应的操作数，进行计算，并将结果压入数字栈。
4. 最后，处理剩余的运算符和操作数，直到所有运算符都被处理完。

关键点:
- 使用栈来处理运算符和操作数。
- 根据运算符的优先级进行计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是表达式的长度。
空间复杂度: O(n)，最坏情况下需要存储所有的数字和运算符。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(s: str) -> int:
    """
    函数式接口 - 计算表达式的值
    """
    def calculate(num1: int, num2: int, operator: str) -> int:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 // num2

    def precedence(op: str) -> int:
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def apply_operator(operators: List[str], values: List[int]) -> None:
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        values.append(calculate(left, right, operator))

    values = []
    operators = []
    i = 0
    while i < len(s):
        if s[i] == ' ':
            i += 1
            continue
        if s[i].isdigit():
            val = 0
            while i < len(s) and s[i].isdigit():
                val = (val * 10) + int(s[i])
                i += 1
            values.append(val)
            i -= 1
        else:
            while (operators and precedence(operators[-1]) >= precedence(s[i])):
                apply_operator(operators, values)
            operators.append(s[i])
        i += 1

    while operators:
        apply_operator(operators, values)

    return values[0]


Solution = create_solution(solution_function_name)