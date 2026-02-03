# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 394
标题: Decode String
难度: medium
链接: https://leetcode.cn/problems/decode-string/
题目类型: 栈、递归、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
394. 字符串解码 - 给定一个经过编码的字符串，返回它解码后的字符串。 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。 测试用例保证输出的长度不会超过 105。 示例 1： 输入：s = "3[a]2[bc]" 输出："aaabcbc" 示例 2： 输入：s = "3[a2[c]]" 输出："accaccacc" 示例 3： 输入：s = "2[abc]3[cd]ef" 输出："abcabccdcdcdef" 示例 4： 输入：s = "abc3[cd]xyz" 输出："abccdcdcdxyz" 提示： * 1 <= s.length <= 30 * s 由小写英文字母、数字和方括号 '[]' 组成 * s 保证是一个 有效 的输入。 * s 中所有整数的取值范围为 [1, 300]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 栈处理嵌套结构

算法步骤:
1. 使用栈存储当前字符串和重复次数
2. 遇到数字时累积数字
3. 遇到'['时，将当前字符串和数字入栈
4. 遇到']'时，弹出栈顶，重复字符串
5. 遇到字母时，追加到当前字符串

关键点:
- 使用栈处理嵌套的括号
- 数字可能有多位，需要累积
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n为字符串长度
空间复杂度: O(n) - 栈空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def decode_string(s: str) -> str:
    """
    函数式接口 - 字符串解码
    
    实现思路:
    使用栈处理嵌套的编码字符串，遇到'['入栈，遇到']'出栈重复。
    
    Args:
        s: 编码字符串
        
    Returns:
        解码后的字符串
        
    Example:
        >>> decode_string("3[a]2[bc]")
        'aaabcbc'
    """
    stack = []
    current_str = ""
    current_num = 0
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char
    
    return current_str


# 自动生成Solution类（无需手动编写）
Solution = create_solution(decode_string)
