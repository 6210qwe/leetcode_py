# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3918
标题: Check Divisibility by Digit Sum and Product
难度: easy
链接: https://leetcode.cn/problems/check-divisibility-by-digit-sum-and-product/
题目类型: 数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3622. 判断整除性 - 给你一个正整数 n。请判断 n 是否可以被以下两值之和 整除： * n 的 数字和（即其各个位数之和）。 * n 的 数字积（即其各个位数之积）。 如果 n 能被该和整除，返回 true；否则，返回 false。 示例 1： 输入： n = 99 输出： true 解释： 因为 99 可以被其数字和 (9 + 9 = 18) 与数字积 (9 * 9 = 81) 之和 (18 + 81 = 99) 整除，因此输出为 true。 示例 2： 输入： n = 23 输出： false 解释： 因为 23 无法被其数字和 (2 + 3 = 5) 与数字积 (2 * 3 = 6) 之和 (5 + 6 = 11) 整除，因此输出为 false。 提示： * 1 <= n <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算 n 的数字和与数字积，然后检查 n 是否能被这两个值的和整除。

算法步骤:
1. 将 n 转换为字符串，以便逐位处理。
2. 初始化数字和 sum_digits 和数字积 product_digits。
3. 遍历 n 的每一位，计算 sum_digits 和 product_digits。
4. 检查 n 是否能被 sum_digits + product_digits 整除。

关键点:
- 使用字符串遍历来处理每一位数字。
- 确保 product_digits 不为零，避免除以零的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(d)，其中 d 是 n 的位数。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(n: int) -> bool:
    """
    函数式接口 - 判断 n 是否可以被其数字和与数字积之和整除。
    """
    # 将 n 转换为字符串
    n_str = str(n)
    
    # 初始化数字和和数字积
    sum_digits = 0
    product_digits = 1
    
    # 遍历 n 的每一位
    for digit in n_str:
        digit = int(digit)
        sum_digits += digit
        if digit != 0:
            product_digits *= digit
    
    # 检查 n 是否能被 sum_digits + product_digits 整除
    return (sum_digits + product_digits) != 0 and n % (sum_digits + product_digits) == 0


Solution = create_solution(solution_function_name)