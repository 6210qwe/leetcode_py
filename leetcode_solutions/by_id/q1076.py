# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1076
标题: Brace Expansion
难度: medium
链接: https://leetcode.cn/problems/brace-expansion/
题目类型: 栈、广度优先搜索、字符串、回溯、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1087. 花括号展开 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归和栈来处理花括号的展开

算法步骤:
1. 定义一个递归函数 `expand` 来处理花括号内的字符串。
2. 使用栈来存储当前处理的字符串片段。
3. 遍历输入字符串，遇到 `{` 时开始一个新的子串处理，遇到 `}` 时结束当前子串处理。
4. 对于每个子串，递归调用 `expand` 函数进行处理。
5. 最后将所有结果进行拼接并去重。

关键点:
- 使用递归和栈来处理嵌套的花括号。
- 对结果进行去重以确保唯一性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * 2^m)，其中 n 是输入字符串的长度，m 是花括号的最大嵌套深度。
空间复杂度: O(n * 2^m)，用于存储所有的可能结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def expand(expression: str) -> List[str]:
    if not expression:
        return [""]
    
    result = []
    i = 0
    while i < len(expression):
        if expression[i] == '{':
            start = i + 1
            end = start
            while expression[end] != '}':
                end += 1
            sub_expressions = expression[start:end].split(',')
            left = expand(expression[:i])
            right = expand(expression[end + 1:])
            for l in left:
                for s in sub_expressions:
                    for r in right:
                        result.append(l + s + r)
            i = end + 1
        else:
            i += 1
            result = [expression[:i]]
    
    return list(set(result))


def solution_function_name(s: str) -> List[str]:
    """
    函数式接口 - 实现花括号展开
    """
    return sorted(expand(s))


Solution = create_solution(solution_function_name)