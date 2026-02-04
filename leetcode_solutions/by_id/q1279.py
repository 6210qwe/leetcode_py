# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1279
标题: Prime Arrangements
难度: easy
链接: https://leetcode.cn/problems/prime-arrangements/
题目类型: 数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1175. 质数排列 - 请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。 让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。 由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。 示例 1： 输入：n = 5 输出：12 解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。 示例 2： 输入：n = 100 输出：682289015 提示： * 1 <= n <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算 1 到 n 中的质数个数，然后计算质数和非质数的排列组合数。

算法步骤:
1. 计算 1 到 n 中的质数个数。
2. 计算质数和非质数的排列组合数。
3. 返回结果模 10^9 + 7。

关键点:
- 使用埃拉托斯特尼筛法来高效计算质数个数。
- 使用阶乘函数来计算排列组合数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log log n) - 埃拉托斯特尼筛法的时间复杂度。
空间复杂度: O(1) - 除了输入输出外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

MOD = 10**9 + 7

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def count_primes(n):
    return sum(is_prime(i) for i in range(1, n + 1))

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % MOD
    return result

def solution_function_name(n: int) -> int:
    """
    函数式接口 - 计算 1 到 n 的质数排列方案数
    """
    prime_count = count_primes(n)
    non_prime_count = n - prime_count
    result = (factorial(prime_count) * factorial(non_prime_count)) % MOD
    return result

Solution = create_solution(solution_function_name)