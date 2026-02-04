# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 640
标题: Solve the Equation
难度: medium
链接: https://leetcode.cn/problems/solve-the-equation/
题目类型: 数学、字符串、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
640. 求解方程 - 求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。 如果方程没有解或存在的解不为整数，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。 题目保证，如果方程中只有一个解，则 'x' 的值是一个整数。 示例 1： 输入: equation = "x+5-3+x=6+x-2" 输出: "x=2" 示例 2: 输入: equation = "x=x" 输出: "Infinite solutions" 示例 3: 输入: equation = "2x=x" 输出: "x=0" 提示: * 3 <= equation.length <= 1000 * equation 只有一个 '='. * 方程由绝对值在 [0, 100] 范围内且无任何前导零的整数和变量 'x' 组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将方程分成左右两部分，分别解析出 x 的系数和常数项，然后通过简单的数学运算求解。

算法步骤:
1. 将方程按 '=' 分割成左右两部分。
2. 定义一个辅助函数 `parse_expression` 来解析表达式，计算 x 的系数和常数项。
3. 对左右两部分分别调用 `parse_expression`，得到各自的 x 系数和常数项。
4. 通过简单的数学运算求解 x 的值：
   - 如果左右两边 x 的系数相同且常数项也相同，则方程有无限解。
   - 如果左右两边 x 的系数相同但常数项不同，则方程无解。
   - 否则，通过 (右边常数项 - 左边常数项) / (左边 x 系数 - 右边 x 系数) 求解 x 的值。

关键点:
- 使用正则表达式来解析表达式中的 x 系数和常数项。
- 处理特殊情况，如 x 系数为 0 或常数项为 0 的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是方程的长度。我们需要遍历整个方程一次来解析 x 的系数和常数项。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Tuple
import re

def parse_expression(expression: str) -> Tuple[int, int]:
    # 默认系数和常数项
    coeff_x, constant = 0, 0
    
    # 匹配所有项
    for term in re.split(r'(\+|-)', expression):
        if 'x' in term:
            # 去掉 'x' 并转换为整数
            coeff = int(term.replace('x', '') or '1')
            coeff_x += coeff
        else:
            # 转换为整数
            constant += int(term)
    
    return coeff_x, constant

def solve_equation(equation: str) -> str:
    # 将方程按 '=' 分割成左右两部分
    left, right = equation.split('=')
    
    # 解析左右两部分
    left_coeff_x, left_constant = parse_expression(left)
    right_coeff_x, right_constant = parse_expression(right)
    
    # 计算最终的 x 系数和常数项
    final_coeff_x = left_coeff_x - right_coeff_x
    final_constant = right_constant - left_constant
    
    # 判断解的情况
    if final_coeff_x == 0:
        if final_constant == 0:
            return "Infinite solutions"
        else:
            return "No solution"
    else:
        return f"x={final_constant // final_coeff_x}"

# 测试
print(solve_equation("x+5-3+x=6+x-2"))  # 输出: "x=2"
print(solve_equation("x=x"))  # 输出: "Infinite solutions"
print(solve_equation("2x=x"))  # 输出: "x=0"

Solution = create_solution(solve_equation)