# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 537
标题: Complex Number Multiplication
难度: medium
链接: https://leetcode.cn/problems/complex-number-multiplication/
题目类型: 数学、字符串、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
537. 复数乘法 - 复数 [https://baike.baidu.com/item/%E5%A4%8D%E6%95%B0/254365?fr=aladdin] 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件： * 实部 是一个整数，取值范围是 [-100, 100] * 虚部 也是一个整数，取值范围是 [-100, 100] * i2 == -1 给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。 示例 1： 输入：num1 = "1+1i", num2 = "1+1i" 输出："0+2i" 解释：(1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。 示例 2： 输入：num1 = "1+-1i", num2 = "1+-1i" 输出："0+-2i" 解释：(1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。 提示： * num1 和 num2 都是有效的复数表示。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将复数字符串解析为实部和虚部，然后进行复数乘法运算。

算法步骤:
1. 解析输入字符串，提取实部和虚部。
2. 计算乘积的实部和虚部。
3. 将结果格式化为字符串。

关键点:
- 使用正则表达式解析字符串。
- 复数乘法公式：(a + bi) * (c + di) = (ac - bd) + (ad + bc)i
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 解析字符串和计算乘积的时间复杂度都是常数级。
空间复杂度: O(1) - 仅使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

import re
from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def complex_number_multiply(num1: str, num2: str) -> str:
    """
    函数式接口 - 实现复数乘法
    """
    # 解析输入字符串，提取实部和虚部
    def parse_complex_number(num: str) -> (int, int):
        match = re.match(r"(-?\d+)\+(-?\d+)i", num)
        if not match:
            raise ValueError("Invalid complex number format")
        real, imag = map(int, match.groups())
        return real, imag

    real1, imag1 = parse_complex_number(num1)
    real2, imag2 = parse_complex_number(num2)

    # 计算乘积的实部和虚部
    real_part = real1 * real2 - imag1 * imag2
    imag_part = real1 * imag2 + imag1 * real2

    # 将结果格式化为字符串
    return f"{real_part}+{imag_part}i"


Solution = create_solution(complex_number_multiply)