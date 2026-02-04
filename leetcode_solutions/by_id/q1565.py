# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1565
标题: Evaluate Boolean Expression
难度: medium
链接: https://leetcode.cn/problems/evaluate-boolean-expression/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1440. 计算布尔表达式的值 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归解析布尔表达式。

算法步骤:
1. 将表达式按照 `&`、`|` 和 `!` 分割成子表达式。
2. 递归解析每个子表达式，直到遇到基本的布尔值或变量。
3. 根据运算符计算子表达式的值。
4. 返回最终的布尔值。

关键点:
- 使用递归处理嵌套的布尔表达式。
- 使用字典存储变量的值，以便快速查找。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是表达式的长度。每个字符最多被访问两次（一次在分割时，一次在递归时）。
空间复杂度: O(n)，递归调用栈和存储变量的字典占用的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def parse_bool_expr(expression: str) -> bool:
    """
    解析布尔表达式并返回其值。
    """
    def evaluate(expr: str) -> bool:
        if expr in {'t', 'f'}:
            return expr == 't'
        if expr[0] == '!':
            return not evaluate(expr[2:-1])
        if expr[0] == '&':
            return all(evaluate(subexpr) for subexpr in split_expr(expr[2:-1]))
        if expr[0] == '|':
            return any(evaluate(subexpr) for subexpr in split_expr(expr[2:-1]))

    def split_expr(expr: str) -> List[str]:
        parts = []
        depth = 0
        start = 0
        for i, char in enumerate(expr):
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            elif char in {',', '&', '|', '!'} and depth == 0:
                if start < i:
                    parts.append(expr[start:i])
                start = i + 1
        if start < len(expr):
            parts.append(expr[start:])
        return parts

    return evaluate(expression)


Solution = create_solution(parse_bool_expr)