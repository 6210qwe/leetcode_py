# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 301
标题: Remove Invalid Parentheses
难度: hard
链接: https://leetcode.cn/problems/remove-invalid-parentheses/
题目类型: 广度优先搜索、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
301. 删除无效的括号 - 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。 返回所有可能的结果。答案可以按 任意顺序 返回。 示例 1： 输入：s = "()())()" 输出：["(())()","()()()"] 示例 2： 输入：s = "(a)())()" 输出：["(a())()","(a)()()"] 示例 3： 输入：s = ")(" 输出：[""] 提示： * 1 <= s.length <= 25 * s 由小写英文字母以及括号 '(' 和 ')' 组成 * s 中至多含 20 个括号
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 先计算需要删除的左右括号数量，然后使用回溯+剪枝删除

算法步骤:
1. 计算需要删除的左右括号数量
2. 使用回溯尝试删除每个括号
3. 验证删除后的字符串是否有效
4. 使用集合去重，避免重复结果

关键点:
- 回溯+剪枝优化
- 时间复杂度O(2^n)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n) - n为括号数量
空间复杂度: O(n) - 递归栈深度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Set
from leetcode_solutions.utils.solution import create_solution


def remove_invalid_parentheses(s: str) -> List[str]:
    """
    函数式接口 - 删除无效的括号
    
    实现思路:
    先计算需要删除的左右括号数量，然后使用回溯+剪枝删除。
    
    Args:
        s: 由括号和字母组成的字符串
        
    Returns:
        所有可能的结果列表
        
    Example:
        >>> remove_invalid_parentheses("()())()")
        ['(())()', '()()()']
    """
    def is_valid(t: str) -> bool:
        """判断字符串是否有效"""
        count = 0
        for char in t:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0
    
    def backtrack(index: int, left_remove: int, right_remove: int, 
                  left_count: int, right_count: int, expr: List[str], result: Set[str]):
        """回溯函数"""
        if index == len(s):
            if left_remove == 0 and right_remove == 0 and is_valid(''.join(expr)):
                result.add(''.join(expr))
            return
        
        char = s[index]
        
        # 尝试删除当前字符（如果是括号）
        if (char == '(' and left_remove > 0) or (char == ')' and right_remove > 0):
            backtrack(
                index + 1,
                left_remove - (1 if char == '(' else 0),
                right_remove - (1 if char == ')' else 0),
                left_count,
                right_count,
                expr,
                result
            )
        
        # 保留当前字符
        expr.append(char)
        
        if char != '(' and char != ')':
            backtrack(index + 1, left_remove, right_remove, left_count, right_count, expr, result)
        elif char == '(':
            backtrack(index + 1, left_remove, right_remove, left_count + 1, right_count, expr, result)
        elif char == ')' and left_count > right_count:
            backtrack(index + 1, left_remove, right_remove, left_count, right_count + 1, expr, result)
        
        expr.pop()
    
    # 计算需要删除的左右括号数量
    left_remove = right_remove = 0
    for char in s:
        if char == '(':
            left_remove += 1
        elif char == ')':
            if left_remove == 0:
                right_remove += 1
            else:
                left_remove -= 1
    
    result = set()
    backtrack(0, left_remove, right_remove, 0, 0, [], result)
    return list(result)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(remove_invalid_parentheses)
