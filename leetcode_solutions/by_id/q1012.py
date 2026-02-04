# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1012
标题: Equal Rational Numbers
难度: hard
链接: https://leetcode.cn/problems/equal-rational-numbers/
题目类型: 数学、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
972. 相等的有理数 - 给定两个字符串 s 和 t ，每个字符串代表一个非负有理数，只有当它们表示相同的数字时才返回 true 。字符串中可以使用括号来表示有理数的重复部分。 有理数 最多可以用三个部分来表示：整数部分 <IntegerPart>、小数非重复部分 <NonRepeatingPart> 和小数重复部分 <(><RepeatingPart><)>。数字可以用以下三种方法之一来表示： * <IntegerPart> * 例： 0 ,12 和 123 * <IntegerPart><.><NonRepeatingPart> * 例： 0.5 , 1. , 2.12 和 123.0001 * <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)> * 例： 0.1(6) ， 1.(9)， 123.00(1212) 十进制展开的重复部分通常在一对圆括号内表示。例如： * 1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66) 示例 1： 输入：s = "0.(52)", t = "0.5(25)" 输出：true 解释：因为 "0.(52)" 代表 0.52525252...，而 "0.5(25)" 代表 0.52525252525.....，则这两个字符串表示相同的数字。 示例 2： 输入：s = "0.1666(6)", t = "0.166(66)" 输出：true 示例 3： 输入：s = "0.9(9)", t = "1." 输出：true 解释："0.9(9)" 代表 0.999999999... 永远重复，等于 1 。[有关说明，请参阅此链接https://baike.baidu.com/item/0.999…/5615429?fr=aladdin] "1." 表示数字 1，其格式正确：(IntegerPart) = "1" 且 (NonRepeatingPart) = "" 。 提示： * 每个部分仅由数字组成。 * 整数部分 <IntegerPart> 不会以零开头。（零本身除外） * 1 <= <IntegerPart>.length <= 4 * 0 <= <NonRepeatingPart>.length <= 4 * 1 <= <RepeatingPart>.length <= 4
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将字符串表示的有理数转换为分数形式，然后比较两个分数是否相等。

算法步骤:
1. 解析字符串，提取整数部分、小数非重复部分和小数重复部分。
2. 将这些部分转换为分数形式。
3. 比较两个分数是否相等。

关键点:
- 使用数学公式将有理数转换为分数。
- 使用最大公约数简化分数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Tuple
import math

def parse_rational_number(s: str) -> Tuple[int, int]:
    """
    解析有理数字符串，返回分子和分母。
    """
    if '.' not in s:
        return int(s), 1
    
    integer_part, fractional_part = s.split('.')
    non_repeating, repeating = '', ''
    
    if '(' in fractional_part:
        non_repeating, repeating = fractional_part.split('(')
        repeating = repeating.rstrip(')')
    else:
        non_repeating = fractional_part
    
    numerator = int(integer_part + non_repeating + repeating) - int(integer_part + non_repeating)
    denominator = 10 ** (len(non_repeating) + len(repeating)) - 10 ** len(non_repeating)
    
    if non_repeating:
        numerator += int(integer_part + non_repeating) * denominator
        denominator *= 10 ** len(non_repeating)
    
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd

def is_rational_equal(s: str, t: str) -> bool:
    """
    判断两个有理数字符串是否表示相同的数值。
    """
    s_num, s_den = parse_rational_number(s)
    t_num, t_den = parse_rational_number(t)
    
    return s_num * t_den == t_num * s_den

Solution = create_solution(is_rational_equal)