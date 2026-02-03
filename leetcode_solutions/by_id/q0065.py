# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 65
标题: Valid Number
难度: hard
链接: https://leetcode.cn/problems/valid-number/
题目类型: 字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
65. 有效数字 - 给定一个字符串 s ，返回 s 是否是一个 有效数字。 例如，下面的都是有效数字："2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"，而接下来的不是："abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"。 一般的，一个 有效数字 可以用以下的规则之一定义： 1. 一个 整数 后面跟着一个 可选指数。 2. 一个 十进制数 后面跟着一个 可选指数。 一个 整数 定义为一个 可选符号 '-' 或 '+' 后面跟着 数字。 一个 十进制数 定义为一个 可选符号 '-' 或 '+' 后面跟着下述规则： 1. 数字 后跟着一个 小数点 .。 2. 数字 后跟着一个 小数点 . 再跟着 数位。 3. 一个 小数点 . 后跟着 数位。 指数 定义为指数符号 'e' 或 'E'，后面跟着一个 整数。 数字 定义为一个或多个数位。 示例 1： 输入：s = "0" 输出：true 示例 2： 输入：s = "e" 输出：false 示例 3： 输入：s = "." 输出：false 提示： * 1 <= s.length <= 20 * s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 有限状态自动机（DFA），根据当前状态和输入字符转换状态

算法步骤:
1. 定义状态：开始、符号、整数部分、小数点、小数部分、指数符号、指数符号、指数整数
2. 定义接受状态：整数部分、小数部分、指数整数
3. 遍历字符串，根据当前状态和字符转换状态
4. 如果最终状态是接受状态，返回True，否则返回False

关键点:
- 使用状态机可以清晰地处理各种边界情况
- 需要处理：符号、小数点、指数、数字
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 只需遍历字符串一次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from leetcode_solutions.utils.solution import create_solution


def is_number(s: str) -> bool:
    """
    函数式接口 - 有限状态自动机
    
    实现思路:
    使用有限状态自动机判断字符串是否为有效数字。
    
    Args:
        s: 待判断的字符串
        
    Returns:
        如果是有效数字返回True，否则返回False
        
    Example:
        >>> is_number("0")
        True
        >>> is_number("e")
        False
    """
    # 定义状态
    STATE_START = 0
    STATE_SIGN = 1
    STATE_INTEGER = 2
    STATE_POINT = 3
    STATE_DECIMAL = 4
    STATE_EXP = 5
    STATE_EXP_SIGN = 6
    STATE_EXP_INTEGER = 7
    
    # 接受状态
    ACCEPT_STATES = {STATE_INTEGER, STATE_DECIMAL, STATE_EXP_INTEGER}
    
    state = STATE_START
    
    for char in s:
        if state == STATE_START:
            if char in '+-':
                state = STATE_SIGN
            elif char.isdigit():
                state = STATE_INTEGER
            elif char == '.':
                state = STATE_POINT
            else:
                return False
        elif state == STATE_SIGN:
            if char.isdigit():
                state = STATE_INTEGER
            elif char == '.':
                state = STATE_POINT
            else:
                return False
        elif state == STATE_INTEGER:
            if char.isdigit():
                state = STATE_INTEGER
            elif char == '.':
                state = STATE_DECIMAL
            elif char in 'eE':
                state = STATE_EXP
            else:
                return False
        elif state == STATE_POINT:
            if char.isdigit():
                state = STATE_DECIMAL
            else:
                return False
        elif state == STATE_DECIMAL:
            if char.isdigit():
                state = STATE_DECIMAL
            elif char in 'eE':
                state = STATE_EXP
            else:
                return False
        elif state == STATE_EXP:
            if char in '+-':
                state = STATE_EXP_SIGN
            elif char.isdigit():
                state = STATE_EXP_INTEGER
            else:
                return False
        elif state == STATE_EXP_SIGN:
            if char.isdigit():
                state = STATE_EXP_INTEGER
            else:
                return False
        elif state == STATE_EXP_INTEGER:
            if char.isdigit():
                state = STATE_EXP_INTEGER
            else:
                return False
    
    return state in ACCEPT_STATES


# 自动生成Solution类（无需手动编写）
Solution = create_solution(is_number)
