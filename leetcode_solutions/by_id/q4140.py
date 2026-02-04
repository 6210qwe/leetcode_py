# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4140
标题: Evaluate Valid Expressions
难度: hard
链接: https://leetcode.cn/problems/evaluate-valid-expressions/
题目类型: 栈、哈希表、数学、字符串、分治
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3749. 计算有效表达式 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈来处理括号匹配和计算表达式的值。

算法步骤:
1. 初始化一个栈，用于存储当前的表达式结果和变量映射。
2. 遍历输入字符串，根据字符类型进行不同的操作：
   - 如果是字母或数字，将其加入当前表达式。
   - 如果是左括号，将当前表达式和变量映射压入栈，并重置当前表达式和变量映射。
   - 如果是右括号，计算当前表达式的值，并将其与栈顶的表达式和变量映射合并。
   - 如果是运算符（如 `+`, `-`, `*`, `/`），将其加入当前表达式。
3. 最后返回计算结果。

关键点:
- 使用栈来处理嵌套的括号。
- 使用字典来存储变量及其对应的值。
- 通过递归解析表达式中的子表达式。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是输入字符串的长度。每个字符最多被处理两次（一次进栈，一次出栈）。
空间复杂度: O(n)，栈的最大深度为输入字符串的长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(expression: str) -> int:
    """
    函数式接口 - 计算有效表达式的值
    """
    def evaluate(expr: str, var_map: dict) -> int:
        # 计算表达式的值
        if expr.isdigit():
            return int(expr)
        if expr in var_map:
            return var_map[expr]
        
        # 处理括号内的表达式
        stack = []
        current_expr = ""
        for char in expr:
            if char == '(':
                stack.append(current_expr)
                current_expr = ""
            elif char == ')':
                result = evaluate(current_expr, var_map)
                current_expr = stack.pop() + str(result)
            else:
                current_expr += char
        
        # 计算最终表达式的值
        return eval(current_expr, {}, var_map)

    # 主函数逻辑
    stack = []
    current_expr = ""
    var_map = {}
    
    for char in expression:
        if char == '(':
            stack.append((current_expr, var_map))
            current_expr = ""
            var_map = {}
        elif char == ')':
            result = evaluate(current_expr, var_map)
            current_expr, var_map = stack.pop()
            current_expr += str(result)
        else:
            current_expr += char
    
    return evaluate(current_expr, var_map)


Solution = create_solution(solution_function_name)