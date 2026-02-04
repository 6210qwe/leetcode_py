# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2328
标题: Minimize Result by Adding Parentheses to Expression
难度: medium
链接: https://leetcode.cn/problems/minimize-result-by-adding-parentheses-to-expression/
题目类型: 字符串、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2232. 向表达式添加括号后的最小结果 - 给你一个下标从 0 开始的字符串 expression ，格式为 "<num1>+<num2>" ，其中 <num1> 和 <num2> 表示正整数。 请你向 expression 中添加一对括号，使得在添加之后， expression 仍然是一个有效的数学表达式，并且计算后可以得到 最小 可能值。左括号 必须 添加在 '+' 的左侧，而右括号必须添加在 '+' 的右侧。 返回添加一对括号后形成的表达式 expression ，且满足 expression 计算得到 最小 可能值。如果存在多个答案都能产生相同结果，返回任意一个答案。 生成的输入满足：expression 的原始值和添加满足要求的任一对括号之后 expression 的值，都符合 32-bit 带符号整数范围。 示例 1： 输入：expression = "247+38" 输出："2(47+38)" 解释：表达式计算得到 2 * (47 + 38) = 2 * 85 = 170 。 注意 "2(4)7+38" 不是有效的结果，因为右括号必须添加在 '+' 的右侧。 可以证明 170 是最小可能值。 示例 2： 输入：expression = "12+34" 输出："1(2+3)4" 解释：表达式计算得到 1 * (2 + 3) * 4 = 1 * 5 * 4 = 20 。 示例 3： 输入：expression = "999+999" 输出："(999+999)" 解释：表达式计算得到 999 + 999 = 1998 。 提示： * 3 <= expression.length <= 10 * expression 仅由数字 '1' 到 '9' 和 '+' 组成 * expression 由数字开始和结束 * expression 恰好仅含有一个 '+'. * expression 的原始值和添加满足要求的任一对括号之后 expression 的值，都符合 32-bit 带符号整数范围
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 枚举所有可能的括号位置，计算每个位置的结果，选择最小的结果。

算法步骤:
1. 找到 '+' 的位置。
2. 枚举所有可能的左括号位置（从 0 到 '+' 的前一个位置）。
3. 枚举所有可能的右括号位置（从 '+' 的后一个位置到字符串末尾）。
4. 对于每种括号位置组合，计算表达式的值。
5. 选择最小值对应的括号位置，构造最终表达式。

关键点:
- 使用嵌套循环枚举所有可能的括号位置。
- 通过字符串切片和转换来计算表达式的值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是 expression 的长度。需要枚举所有可能的括号位置。
空间复杂度: O(1)，只需要常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(expression: str) -> str:
    """
    函数式接口 - 实现
    """
    plus_index = expression.index('+')
    min_value = float('inf')
    best_expression = ""

    for i in range(plus_index):
        for j in range(plus_index + 1, len(expression)):
            left_part = expression[:i] if i > 0 else ""
            mid_part = expression[i:plus_index] + "+" + expression[plus_index + 1:j + 1]
            right_part = expression[j + 1:] if j < len(expression) - 1 else ""
            value = int(left_part or "1") * (int(mid_part.split('+')[0]) + int(mid_part.split('+')[1])) * int(right_part or "1")
            if value < min_value:
                min_value = value
                best_expression = f"{left_part}({mid_part}){right_part}"

    return best_expression


Solution = create_solution(solution_function_name)