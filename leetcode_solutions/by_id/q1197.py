# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1197
标题: Parsing A Boolean Expression
难度: hard
链接: https://leetcode.cn/problems/parsing-a-boolean-expression/
题目类型: 栈、递归、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1106. 解析布尔表达式 - 布尔表达式 是计算结果不是 true 就是 false 的表达式。有效的表达式需遵循以下约定： * 't'，运算结果为 true * 'f'，运算结果为 false * '!(subExpr)'，运算过程为对内部表达式 subExpr 进行 逻辑非（NOT）运算 * '&(subExpr1, subExpr2, ..., subExprn)'，运算过程为对 2 个或以上内部表达式 subExpr1, subExpr2, ..., subExprn 进行 逻辑与（AND）运算 * '|(subExpr1, subExpr2, ..., subExprn)'，运算过程为对 2 个或以上内部表达式 subExpr1, subExpr2, ..., subExprn 进行 逻辑或（OR）运算 给你一个以字符串形式表述的 布尔表达式 [https://baike.baidu.com/item/%E5%B8%83%E5%B0%94%E8%A1%A8%E8%BE%BE%E5%BC%8F/1574380?fr=aladdin] expression，返回该式的运算结果。 题目测试用例所给出的表达式均为有效的布尔表达式，遵循上述约定。 示例 1： 输入：expression = "&(|(f))" 输出：false 解释： 首先，计算 |(f) --> f ，表达式变为 "&(f)" 。 接着，计算 &(f) --> f ，表达式变为 "f" 。 最后，返回 false 。 示例 2： 输入：expression = "|(f,f,f,t)" 输出：true 解释：计算 (false OR false OR false OR true) ，结果为 true 。 示例 3： 输入：expression = "!(&(f,t))" 输出：true 解释： 首先，计算 &(f,t) --> (false AND true) --> false --> f ，表达式变为 "!(f)" 。 接着，计算 !(f) --> NOT false --> true ，返回 true 。 提示： * 1 <= expression.length <= 2 * 104 * expression[i] 为 '('、')'、'&'、'|'、'!'、't'、'f' 和 ',' 之一
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈来解析布尔表达式，并根据操作符进行相应的逻辑运算。

算法步骤:
1. 初始化一个栈，用于存储当前处理的子表达式。
2. 遍历表达式字符串，根据字符的不同进行不同的处理：
   - 如果是 't' 或 'f'，直接压入栈中。
   - 如果是 '!', '&' 或 '|'，将操作符压入栈中。
   - 如果是 ')', 弹出栈中的子表达式并进行相应的逻辑运算，直到遇到对应的 '('。
3. 最终栈中剩下的值即为表达式的计算结果。

关键点:
- 使用栈来处理嵌套的子表达式。
- 根据操作符的不同，进行相应的逻辑运算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是表达式的长度。每个字符只会被处理一次。
空间复杂度: O(n)，最坏情况下栈的大小可能达到 n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def parse_boolean_expression(expression: str) -> bool:
    """
    解析布尔表达式并返回其运算结果。
    """
    stack = []
    for char in expression:
        if char == 't':
            stack.append(True)
        elif char == 'f':
            stack.append(False)
        elif char in ('!', '&', '|'):
            stack.append(char)
        elif char == ')':
            sub_expr = []
            while stack and stack[-1] != '(':
                sub_expr.append(stack.pop())
            stack.pop()  # 弹出 '('
            op = stack.pop()
            if op == '!':
                result = not sub_expr[0]
            elif op == '&':
                result = all(sub_expr)
            elif op == '|':
                result = any(sub_expr)
            stack.append(result)
    
    return stack[0]


Solution = create_solution(parse_boolean_expression)