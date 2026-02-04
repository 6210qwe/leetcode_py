# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2141
标题: Smallest Greater Multiple Made of Two Digits
难度: medium
链接: https://leetcode.cn/problems/smallest-greater-multiple-made-of-two-digits/
题目类型: 数学、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1999. 最小的仅由两个数组成的倍数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过枚举所有可能的数字组合，找到第一个大于给定整数 n 的仅由两个不同数字组成的最小倍数。

算法步骤:
1. 枚举所有可能的两位数字组合（0-9）。
2. 对于每个组合，生成从该组合构成的最小整数开始的所有可能的整数。
3. 检查这些整数是否是 n 的倍数，并且大于 n。
4. 返回找到的第一个满足条件的整数。

关键点:
- 使用字符串操作来生成由两个数字组成的整数。
- 通过循环和条件判断来找到满足条件的最小整数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 因为枚举的组合数量是固定的（100种），生成的整数范围也是有限的。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(n: int) -> int:
    """
    函数式接口 - 找到第一个大于给定整数 n 的仅由两个不同数字组成的最小倍数
    """
    def generate_numbers(digit1: str, digit2: str) -> int:
        for length in range(1, 11):  # 限制长度以避免无限循环
            for i in range(10 ** (length - 1), 10 ** length):
                num_str = f"{digit1}{digit2}" * (length // 2)
                if length % 2 == 1:
                    num_str += digit1
                num = int(num_str[:length])
                if num > n and num % n == 0:
                    return num
        return -1  # 理论上不会到达这里

    for d1 in range(10):
        for d2 in range(d1 + 1, 10):
            result = generate_numbers(str(d1), str(d2))
            if result != -1:
                return result
    return -1  # 如果没有找到符合条件的数，返回-1

Solution = create_solution(solution_function_name)