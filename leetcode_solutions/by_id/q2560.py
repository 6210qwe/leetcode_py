# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2560
标题: Closest Fair Integer
难度: medium
链接: https://leetcode.cn/problems/closest-fair-integer/
题目类型: 数学、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2417. 最近的公平整数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过枚举所有可能的公平整数，并找到最接近给定整数 n 的那个。

算法步骤:
1. 定义一个函数 `is_fair` 来判断一个整数是否是公平整数。
2. 从给定整数 n 开始，向两边扩展，找到第一个公平整数。

关键点:
- 公平整数的定义：奇数位和偶数位的数字之和相等。
- 通过枚举的方式，从 n 向两边扩展，找到最近的公平整数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 因为数字的范围是有限的，最多需要检查 9999999999 个数字。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def is_fair(num: int) -> bool:
    """判断一个整数是否是公平整数"""
    digits = [int(d) for d in str(num)]
    even_sum = sum(digits[i] for i in range(0, len(digits), 2))
    odd_sum = sum(digits[i] for i in range(1, len(digits), 2))
    return even_sum == odd_sum

def closest_fair_integer(n: int) -> int:
    """
    找到最接近给定整数 n 的公平整数
    """
    step = 1
    while True:
        if n - step >= 0 and is_fair(n - step):
            return n - step
        if is_fair(n + step):
            return n + step
        step += 1

Solution = create_solution(closest_fair_integer)