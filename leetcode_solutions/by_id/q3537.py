# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3537
标题: Number of Subsequences with Odd Sum
难度: medium
链接: https://leetcode.cn/problems/number-of-subsequences-with-odd-sum/
题目类型: 数组、数学、动态规划、组合数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3247. 奇数和子序列的数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用组合数学的方法来计算奇数和子序列的数量。

算法步骤:
1. 统计数组中奇数和偶数的数量。
2. 计算所有可能的奇数和子序列的数量。一个奇数和子序列必须包含至少一个奇数，可以包含任意数量的偶数。
3. 使用组合数学公式计算结果，并对结果取模。

关键点:
- 奇数和子序列的数量可以通过组合数学公式计算。
- 使用快速幂算法来计算大数的幂次。
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

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def mod_pow(x: int, n: int, mod: int) -> int:
    """快速幂算法"""
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * x) % mod
        x = (x * x) % mod
        n //= 2
    return result

def solution_function_name(arr: List[int]) -> int:
    """
    函数式接口 - 计算奇数和子序列的数量
    """
    MOD = 10**9 + 7
    odd_count = sum(1 for num in arr if num % 2 == 1)
    even_count = len(arr) - odd_count
    
    # 计算所有可能的奇数和子序列的数量
    total_subsequences = mod_pow(2, even_count, MOD) * (mod_pow(2, odd_count, MOD) - 1) % MOD
    return total_subsequences

Solution = create_solution(solution_function_name)