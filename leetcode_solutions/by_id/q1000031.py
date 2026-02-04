# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000031
标题: Boolean Evaluation LCCI
难度: medium
链接: https://leetcode.cn/problems/boolean-evaluation-lcci/
题目类型: 记忆化搜索、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 08.14. 布尔运算 - 给定一个布尔表达式和一个期望的布尔结果 result，布尔表达式由 0 (false)、1 (true)、& (AND)、 | (OR) 和 ^ (XOR) 符号组成。实现一个函数，算出有几种可使该表达式得出 result 值的括号方法。 示例 1： 输入：s = "1^0|0|1", result = 0 输出：2 解释：两种可能的括号方法是 1^(0|(0|1)) 1^((0|0)|1) 示例 2： 输入：s = "0&0&0&1^1|0", result = 1 输出：10 提示： * 运算符的数量不超过 19 个
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用记忆化搜索来解决这个问题。我们可以通过递归地将表达式分成左右两部分，并对每一部分进行计算，然后根据当前操作符来决定最终的结果。

算法步骤:
1. 定义一个递归函数 `count_ways`，它接受四个参数：表达式字符串 `s`，起始索引 `start`，结束索引 `end`，以及期望的结果 `result`。
2. 如果 `start` 等于 `end`，则检查当前字符是否等于 `result`，如果是则返回 1，否则返回 0。
3. 初始化一个变量 `ways` 为 0，用于记录满足条件的括号方法数。
4. 遍历从 `start + 1` 到 `end - 1` 的所有索引，这些索引对应操作符的位置。
5. 对于每个操作符，递归地计算左子表达式和右子表达式的真值和假值的方法数。
6. 根据当前操作符（&、| 或 ^）和期望的结果 `result`，更新 `ways`。
7. 返回 `ways`。

关键点:
- 使用记忆化搜索来避免重复计算。
- 通过递归地将表达式分成左右两部分来解决问题。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^3)，其中 n 是表达式的长度。因为我们需要遍历所有可能的操作符位置，并且每个子问题的大小最多为 n^2。
空间复杂度: O(n^3)，用于存储记忆化搜索的结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def count_ways(s: str, start: int, end: int, result: bool, memo: dict) -> int:
    if (start, end, result) in memo:
        return memo[(start, end, result)]
    
    if start == end:
        return 1 if (s[start] == '1' and result) or (s[start] == '0' and not result) else 0
    
    ways = 0
    for i in range(start + 1, end, 2):
        left_true = count_ways(s, start, i - 1, True, memo)
        left_false = count_ways(s, start, i - 1, False, memo)
        right_true = count_ways(s, i + 1, end, True, memo)
        right_false = count_ways(s, i + 1, end, False, memo)
        
        if s[i] == '&':
            if result:
                ways += left_true * right_true
            else:
                ways += left_true * right_false + left_false * right_true + left_false * right_false
        elif s[i] == '|':
            if result:
                ways += left_true * right_true + left_true * right_false + left_false * right_true
            else:
                ways += left_false * right_false
        elif s[i] == '^':
            if result:
                ways += left_true * right_false + left_false * right_true
            else:
                ways += left_true * right_true + left_false * right_false
    
    memo[(start, end, result)] = ways
    return ways

def solution_function_name(s: str, result: int) -> int:
    """
    函数式接口 - 计算有几种可使该表达式得出 result 值的括号方法
    """
    return count_ways(s, 0, len(s) - 1, result, {})

Solution = create_solution(solution_function_name)