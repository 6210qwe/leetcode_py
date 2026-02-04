# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1768
标题: Design an Expression Tree With Evaluate Function
难度: medium
链接: https://leetcode.cn/problems/design-an-expression-tree-with-evaluate-function/
题目类型: 栈、树、设计、数组、数学、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1628. 设计带解析函数的表达式树 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二叉树来表示表达式，并递归地计算表达式的值。

算法步骤:
1. 定义一个 Node 类来表示表达式树的节点，包含操作符或数值。
2. 定义一个 TreeBuilder 类来构建表达式树，使用栈来处理操作数和操作符。
3. 在 TreeBuilder 类中实现 build 方法，将后缀表达式转换为表达式树。
4. 在 Node 类中实现 evaluate 方法，递归地计算表达式树的值。

关键点:
- 使用栈来处理后缀表达式，确保操作数和操作符的正确顺序。
- 递归地计算表达式树的值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是后缀表达式的长度。每个节点只会被访问一次。
空间复杂度: O(n)，存储表达式树的空间。
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

    def evaluate(self) -> int:
        if self.val.isdigit():
            return int(self.val)
        else:
            left_val = self.left.evaluate()
            right_val = self.right.evaluate()
            if self.val == '+':
                return left_val + right_val
            elif self.val == '-':
                return left_val - right_val
            elif self.val == '*':
                return left_val * right_val
            elif self.val == '/':
                return left_val // right_val


class TreeBuilder:
    def build(self, postfix: List[str]) -> 'Node':
        stack = []
        for token in postfix:
            if token.isdigit():
                node = Node(token)
            else:
                right = stack.pop()
                left = stack.pop()
                node = Node(token)
                node.left = left
                node.right = right
            stack.append(node)
        return stack[0]


def solution_function_name(postfix: List[str]) -> int:
    """
    函数式接口 - 构建表达式树并计算其值
    """
    tree_builder = TreeBuilder()
    root = tree_builder.build(postfix)
    return root.evaluate()


Solution = create_solution(solution_function_name)