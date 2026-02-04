# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3949
标题: Minimum Number of Primes to Sum to Target
难度: medium
链接: https://leetcode.cn/problems/minimum-number-of-primes-to-sum-to-target/
题目类型: 数组、数学、动态规划、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3610. 目标和所需的最小质数个数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义一个数组 dp，其中 dp[i] 表示和为 i 的最小质数个数。通过遍历所有可能的质数，更新 dp 数组。

算法步骤:
1. 生成所有小于等于目标值 target 的质数。
2. 初始化 dp 数组，长度为 target + 1，初始值为无穷大，dp[0] = 0。
3. 遍历每个质数 p，对于每个质数 p，更新 dp 数组中的每一个值 dp[j] (j >= p)，使其等于 min(dp[j], dp[j - p] + 1)。
4. 返回 dp[target]，如果 dp[target] 仍为无穷大，则返回 -1。

关键点:
- 生成质数时可以使用埃拉托斯特尼筛法。
- 动态规划的状态转移方程为 dp[j] = min(dp[j], dp[j - p] + 1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log log n + n * sqrt(n))，其中 n 是目标值 target。生成质数的时间复杂度为 O(n log log n)，动态规划的时间复杂度为 O(n * sqrt(n))。
空间复杂度: O(n)，需要一个长度为 n + 1 的 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(target: int) -> int:
    """
    函数式接口 - 实现
    """
    def sieve_of_eratosthenes(n: int) -> List[int]:
        """生成所有小于等于 n 的质数"""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return [i for i in range(n + 1) if is_prime[i]]

    primes = sieve_of_eratosthenes(target)
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for p in primes:
        for j in range(p, target + 1):
            dp[j] = min(dp[j], dp[j - p] + 1)

    return dp[target] if dp[target] != float('inf') else -1


Solution = create_solution(solution_function_name)