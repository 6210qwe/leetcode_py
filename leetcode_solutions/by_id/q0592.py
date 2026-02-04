# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 592
标题: Fraction Addition and Subtraction
难度: medium
链接: https://leetcode.cn/problems/fraction-addition-and-subtraction/
题目类型: 数学、字符串、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
592. 分数加减运算 - 给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。 这个结果应该是不可约分的分数，即 最简分数 [https://baike.baidu.com/item/%E6%9C%80%E7%AE%80%E5%88%86%E6%95%B0]。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。 示例 1: 输入: expression = "-1/2+1/2" 输出: "0/1" 示例 2: 输入: expression = "-1/2+1/2+1/3" 输出: "1/3" 示例 3: 输入: expression = "1/3-1/2" 输出: "-1/6" 提示: * 输入和输出字符串只包含 '0' 到 '9' 的数字，以及 '/', '+' 和 '-'。 * 输入和输出分数格式均为 ±分子/分母。如果输入的第一个分数或者输出的分数是正数，则 '+' 会被省略掉。 * 输入只包含合法的 最简分数，每个分数的分子与分母的范围是 [1,10]。 如果分母是 1，意味着这个分数实际上是一个整数。 * 输入的分数个数范围是 [1,10]。 * 最终结果 的分子与分母保证是 32 位整数范围内的有效整数。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将字符串解析为分数列表，然后逐个进行加减运算，并在最后约分结果。

算法步骤:
1. 解析输入字符串，提取出所有的分数。
2. 初始化结果分数为 (0, 1)。
3. 对于每个分数，计算其与当前结果的和或差。
4. 在每次计算后，更新结果分数。
5. 最后，对结果分数进行约分。
6. 返回结果分数的字符串表示。

关键点:
- 使用最大公约数 (GCD) 来约分结果分数。
- 处理负数和多个分数的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log(max_denominator))，其中 n 是分数的数量，max_denominator 是所有分数的最大分母。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution_function_name(expression: str) -> str:
    """
    函数式接口 - 实现分数加减运算
    """
    def parse_expression(expression: str) -> List[List[int]]:
        fractions = []
        i = 0
        while i < len(expression):
            if expression[i] == '-' or expression[i] == '+':
                sign = -1 if expression[i] == '-' else 1
                i += 1
            else:
                sign = 1
            numerator = 0
            while i < len(expression) and expression[i].isdigit():
                numerator = numerator * 10 + int(expression[i])
                i += 1
            i += 1  # skip '/'
            denominator = 0
            while i < len(expression) and expression[i].isdigit():
                denominator = denominator * 10 + int(expression[i])
                i += 1
            fractions.append([sign * numerator, denominator])
        return fractions

    def add_fractions(frac1, frac2):
        num1, den1 = frac1
        num2, den2 = frac2
        new_num = num1 * den2 + num2 * den1
        new_den = den1 * den2
        common_divisor = gcd(new_num, new_den)
        return [new_num // common_divisor, new_den // common_divisor]

    fractions = parse_expression(expression)
    result = [0, 1]
    for fraction in fractions:
        result = add_fractions(result, fraction)

    return f"{result[0]}/{result[1]}"

Solution = create_solution(solution_function_name)