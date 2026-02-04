# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 785
标题: Basic Calculator III
难度: hard
链接: https://leetcode.cn/problems/basic-calculator-iii/
题目类型: 栈、递归、数学、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
772. 基本计算器 III - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈和递归来处理表达式中的括号和运算符。

算法步骤:
1. 初始化一个栈来存储数字和运算符。
2. 从左到右遍历表达式：
   - 如果遇到数字，将其加入当前数字。
   - 如果遇到运算符，将当前数字压入栈，并更新当前运算符。
   - 如果遇到左括号，递归处理子表达式。
   - 如果遇到右括号，返回子表达式的结果。
3. 计算栈中的结果。

关键点:
- 使用栈来处理运算符的优先级。
- 递归处理括号内的子表达式。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是表达式的长度。每个字符只被处理一次。
空间复杂度: O(n)，栈的深度最多为表达式的长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def calculate(s: str) -> int:
    def helper(s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign = s[i]
                num = 0
            if s[i] == '(':
                j = i
                cnt = 0
                while i < len(s):
                    if s[i] == '(':
                        cnt += 1
                    elif s[i] == ')':
                        cnt -= 1
                    if cnt == 0:
                        break
                    i += 1
                num = helper(s[j+1:i])
            i += 1
        return sum(stack)

    return helper(s.strip())

Solution = create_solution(calculate)