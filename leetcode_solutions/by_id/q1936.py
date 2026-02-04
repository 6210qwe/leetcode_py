# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1936
标题: Maximize Number of Nice Divisors
难度: hard
链接: https://leetcode.cn/problems/maximize-number-of-nice-divisors/
题目类型: 递归、数学、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1808. 好因子的最大数目 - 给你一个正整数 primeFactors 。你需要构造一个正整数 n ，它满足以下条件： * n 质因数（质因数需要考虑重复的情况）的数目 不超过 primeFactors 个。 * n 好因子的数目最大化。如果 n 的一个因子可以被 n 的每一个质因数整除，我们称这个因子是 好因子 。比方说，如果 n = 12 ，那么它的质因数为 [2,2,3] ，那么 6 和 12 是好因子，但 3 和 4 不是。 请你返回 n 的好因子的数目。由于答案可能会很大，请返回答案对 109 + 7 取余 的结果。 请注意，一个质数的定义是大于 1 ，且不能被分解为两个小于该数的自然数相乘。一个数 n 的质因子是将 n 分解为若干个质因子，且它们的乘积为 n 。 示例 1： 输入：primeFactors = 5 输出：6 解释：200 是一个可行的 n 。 它有 5 个质因子：[2,2,2,5,5] ，且有 6 个好因子：[10,20,40,50,100,200] 。 不存在别的 n 有至多 5 个质因子，且同时有更多的好因子。 示例 2： 输入：primeFactors = 8 输出：18 提示： * 1 <= primeFactors <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用快速幂和贪心算法来最大化好因子的数量。

算法步骤:
1. 将 primeFactors 尽可能多地分解为 3，因为 3 是最优的质因数。
2. 如果剩余的质因数少于 3 个，则直接使用剩余的质因数。
3. 使用快速幂计算结果，并对 10^9 + 7 取模。

关键点:
- 使用 3 作为主要质因数，因为 3 的幂次增长最快。
- 处理剩余的质因数，确保最终结果最大化。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(primeFactors)) - 快速幂的时间复杂度
空间复杂度: O(1) - 常数级额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

MOD = 10**9 + 7

def solution_function_name(prime_factors: int) -> int:
    """
    函数式接口 - 计算最大好因子数量
    """
    def power(x: int, n: int) -> int:
        result = 1
        while n > 0:
            if n % 2 == 1:
                result = (result * x) % MOD
            x = (x * x) % MOD
            n //= 2
        return result

    if prime_factors <= 3:
        return prime_factors

    # 最大化 3 的数量
    quotient, remainder = divmod(prime_factors, 3)
    if remainder == 0:
        return power(3, quotient)
    elif remainder == 1:
        return (power(3, quotient - 1) * 4) % MOD
    else:
        return (power(3, quotient) * 2) % MOD

Solution = create_solution(solution_function_name)