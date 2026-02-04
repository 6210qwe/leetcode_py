# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1383
标题: Number of Single Divisor Triplets
难度: medium
链接: https://leetcode.cn/problems/number-of-single-divisor-triplets/
题目类型: 数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一个整数 n，返回满足以下条件的三元组 (i, j, k) 的数量：
1. 1 <= i < j < k <= n
2. i * j * k 恰好有三个不同的质因数。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过预处理质数和它们的倍数来快速计算满足条件的三元组。

算法步骤:
1. 找出所有小于等于 n 的质数。
2. 对于每个质数 p，计算其在 [1, n] 范围内的倍数。
3. 使用三个嵌套循环遍历所有可能的三元组 (i, j, k)，检查它们是否满足条件。

关键点:
- 通过预处理质数及其倍数，可以快速判断一个数是否为质数的倍数。
- 使用集合来存储质数及其倍数，以便快速查找。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def sieve_of_eratosthenes(n: int) -> List[bool]:
    """埃拉托斯特尼筛法，返回一个布尔数组，表示每个数是否为质数。"""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def count_single_divisor_triplets(n: int) -> int:
    """
    计算满足条件的三元组 (i, j, k) 的数量。
    """
    # 预处理质数
    is_prime = sieve_of_eratosthenes(n)
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    
    # 计算每个质数的倍数
    multiples = {p: set(range(p, n + 1, p)) for p in primes}
    
    count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                factors = set()
                for p in primes:
                    if i in multiples[p] or j in multiples[p] or k in multiples[p]:
                        factors.add(p)
                if len(factors) == 3:
                    count += 1
    return count

Solution = create_solution(count_single_divisor_triplets)