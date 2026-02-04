# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 781
标题: Basic Calculator IV
难度: hard
链接: https://leetcode.cn/problems/basic-calculator-iv/
题目类型: 栈、递归、哈希表、数学、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
770. 基本计算器 IV - 给定一个表达式如 expression = "e + 8 - a + 5" 和一个求值映射，如 {"e": 1}（给定的形式为 evalvars = ["e"] 和 evalints = [1]），返回表示简化表达式的标记列表，例如 ["-1*a","14"] * 表达式交替使用块和符号，每个块和符号之间有一个空格。 * 块要么是括号中的表达式，要么是变量，要么是非负整数。 * 变量是一个由小写字母组成的字符串（不包括数字）。请注意，变量可以是多个字母，并注意变量从不具有像 "2x" 或 "-x" 这样的前导系数或一元运算符 。 表达式按通常顺序进行求值：先是括号，然后求乘法，再计算加法和减法。 * 例如，expression = "1 + 2 * 3" 的答案是 ["7"]。 输出格式如下： * 对于系数非零的每个自变量项，我们按字典排序的顺序将自变量写在一个项中。 * 例如，我们永远不会写像 “b*a*c” 这样的项，只写 “a*b*c”。 * 项的次数等于被乘的自变量的数目，并计算重复项。我们先写出答案的最大次数项，用字典顺序打破关系，此时忽略词的前导系数。 * 例如，"a*a*b*c" 的次数为 4。 * 项的前导系数直接放在左边，用星号将它与变量分隔开(如果存在的话)。前导系数 1 仍然要打印出来。 * 格式良好的一个示例答案是 ["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"] 。 * 系数为 0 的项（包括常数项）不包括在内。 * 例如，“0” 的表达式输出为 [] 。 注意：你可以假设给定的表达式均有效。所有中间结果都在区间 [-231, 231 - 1] 内。 示例 1： 输入：expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1] 输出：["-1*a","14"] 示例 2： 输入：expression = "e - 8 + temperature - pressure", evalvars = ["e", "temperature"], evalints = [1, 12] 输出：["-1*pressure","5"] 示例 3： 输入：expression = "(e + 8) * (e - 8)", evalvars = [], evalints = [] 输出：["1*e*e","-64"] 提示： * 1 <= expression.length <= 250 * expression 由小写英文字母，数字 '+', '-', '*', '(', ')', ' ' 组成 * expression 不包含任何前空格或后空格 * expression 中的所有符号都用一个空格隔开 * 0 <= evalvars.length <= 100 * 1 <= evalvars[i].length <= 20 * evalvars[i] 由小写英文字母组成 * evalints.length == evalvars.length * -100 <= evalints[i] <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归解析表达式，并使用字典存储多项式。

算法步骤:
1. 将 evalvars 和 evalints 转换为字典。
2. 定义一个辅助函数 `parse`，用于递归解析表达式。
3. 在 `parse` 函数中，处理括号、乘法、加法和减法。
4. 合并同类项，生成最终结果。

关键点:
- 使用递归解析括号内的表达式。
- 使用字典存储多项式，并合并同类项。
- 按照字典序和次数对结果进行排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是表达式的长度。最坏情况下，每个字符都需要处理多次。
空间复杂度: O(n)，递归调用栈和存储多项式的字典。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict
import re

def basic_calculator_iv(expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
    def parse(expr):
        stack = []
        sign = '+'
        num = ''
        for i, c in enumerate(expr):
            if c.isdigit() or c.isalpha():
                num += c
            if (c in '+-*/()' and i > 0 and expr[i-1] != ' ') or i == len(expr) - 1:
                if num:
                    if num in var_map:
                        num = var_map[num]
                    else:
                        num = int(num)
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                elif sign == '/':
                    stack[-1] //= num
                sign = c
                num = ''
            if c == '(':
                j = i
                balance = 1
                while balance > 0:
                    j += 1
                    if expr[j] == '(':
                        balance += 1
                    elif expr[j] == ')':
                        balance -= 1
                num = parse(expr[i+1:j])
                i = j
        return sum(stack)

    def merge_terms(terms):
        merged = defaultdict(int)
        for term, coeff in terms.items():
            merged[term] += coeff
        return {k: v for k, v in merged.items() if v != 0}

    def format_terms(terms):
        result = []
        for term, coeff in sorted(terms.items(), key=lambda x: (-len(x[0]), x[0])):
            if coeff == 1:
                result.append(term)
            else:
                result.append(f"{coeff}*{term}")
        return result

    var_map = dict(zip(evalvars, evalints))
    tokens = re.findall(r'\d+|\w+|[()+\-*/]', expression)
    terms = defaultdict(int)
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token.isalpha():
            stack.append(token)
        elif token in '+-*/':
            op = token
        elif token == '(':
            stack.append('(')
        elif token == ')':
            sub_expr = []
            while stack and stack[-1] != '(':
                sub_expr.append(stack.pop())
            stack.pop()
            sub_result = parse(' '.join(sub_expr[::-1]))
            stack.append(sub_result)
    
    # 合并同类项
    terms = merge_terms(terms)
    # 格式化结果
    return format_terms(terms)

Solution = create_solution(basic_calculator_iv)