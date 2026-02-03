# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 166
标题: Fraction to Recurring Decimal
难度: medium
链接: https://leetcode.cn/problems/fraction-to-recurring-decimal/
题目类型: 哈希表、数学、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
166. 分数到小数 - 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。 如果小数部分为循环小数，则将循环的部分括在括号内。 如果存在多个答案，只需返回 任意一个 。 对于所有给定的输入，保证 答案字符串的长度小于 104 。 注意，如果分数可以表示为有限长度的字符串，则 必须 返回它。 示例 1： 输入：numerator = 1, denominator = 2 输出："0.5" 示例 2： 输入：numerator = 2, denominator = 1 输出："2" 示例 3： 输入：numerator = 4, denominator = 333 输出："0.(012)" 提示： * -231 <= numerator, denominator <= 231 - 1 * denominator != 0
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 模拟长除法，使用哈希表记录余数出现的位置以检测循环

算法步骤:
1. 处理符号和整数部分
2. 计算小数部分，使用长除法
3. 使用哈希表记录余数，如果余数重复出现，说明有循环
4. 在循环开始位置插入括号

关键点:
- 使用哈希表检测循环小数
- 时间复杂度O(denominator)，空间复杂度O(denominator)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(denominator) - 最坏情况下需要遍历所有余数
空间复杂度: O(denominator) - 哈希表存储余数
"""

# ============================================================================
# 代码实现
# ============================================================================

from leetcode_solutions.utils.solution import create_solution


def fraction_to_recurring_decimal(numerator: int, denominator: int) -> str:
    """
    函数式接口 - 分数到小数
    
    实现思路:
    模拟长除法，使用哈希表记录余数出现的位置以检测循环。
    
    Args:
        numerator: 分子
        denominator: 分母
        
    Returns:
        小数字符串，循环部分用括号括起来
        
    Example:
        >>> fraction_to_recurring_decimal(4, 333)
        '0.(012)'
    """
    if numerator == 0:
        return "0"
    
    result = []
    
    # 处理符号
    if (numerator < 0) ^ (denominator < 0):
        result.append('-')
    
    numerator = abs(numerator)
    denominator = abs(denominator)
    
    # 整数部分
    result.append(str(numerator // denominator))
    remainder = numerator % denominator
    
    if remainder == 0:
        return ''.join(result)
    
    result.append('.')
    
    # 小数部分
    remainder_map = {}
    
    while remainder != 0:
        if remainder in remainder_map:
            # 发现循环
            result.insert(remainder_map[remainder], '(')
            result.append(')')
            break
        
        remainder_map[remainder] = len(result)
        remainder *= 10
        result.append(str(remainder // denominator))
        remainder %= denominator
    
    return ''.join(result)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(fraction_to_recurring_decimal)
