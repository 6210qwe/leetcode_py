# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1736
标题: Build Binary Expression Tree From Infix Expression
难度: hard
链接: https://leetcode.cn/problems/build-binary-expression-tree-from-infix-expression/
题目类型: 栈、树、字符串、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1597. 根据中缀表达式构造二叉表达式树 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈来构建二叉表达式树。首先将中缀表达式转换为后缀表达式（逆波兰表示法），然后使用栈来构建二叉树。

算法步骤:
1. 将中缀表达式转换为后缀表达式。
2. 使用栈来构建二叉表达式树。

关键点:
- 优先级处理：在转换为后缀表达式时，需要处理运算符的优先级。
- 栈的使用：在构建二叉树时，使用栈来存储节点，并根据后缀表达式的顺序进行连接。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是表达式的长度。
空间复杂度: O(n)，用于存储后缀表达式和栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional

class Node:
    def __init__(self, val: str):
        self.val = val
        self.left = None
        self.right = None

def infix_to_postfix(expression: str) -> List[str]:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        if expression[i].isalnum():
            j = i
            while j < len(expression) and (expression[j].isalnum() or expression[j] == '.'):
                j += 1
            output.append(expression[i:j])
            i = j
        elif expression[i] in precedence:
            while (stack and stack[-1] != '(' and
                   precedence[expression[i]] <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(expression[i])
            i += 1
        elif expression[i] == '(':
            stack.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
            i += 1
    while stack:
        output.append(stack.pop())
    return output

def build_expression_tree(postfix: List[str]) -> Optional[Node]:
    stack = []
    for token in postfix:
        if token.isalnum():
            node = Node(token)
            stack.append(node)
        else:
            right = stack.pop()
            left = stack.pop()
            node = Node(token)
            node.left = left
            node.right = right
            stack.append(node)
    return stack[0] if stack else None

def solution_function_name(expression: str) -> Optional[Node]:
    """
    函数式接口 - 根据中缀表达式构造二叉表达式树
    """
    postfix = infix_to_postfix(expression)
    return build_expression_tree(postfix)

Solution = create_solution(solution_function_name)