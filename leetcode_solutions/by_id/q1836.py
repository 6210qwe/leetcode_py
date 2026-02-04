# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1836
标题: Count Ways to Make Array With Product
难度: hard
链接: https://leetcode.cn/problems/count-ways-to-make-array-with-product/
题目类型: 数组、数学、动态规划、组合数学、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1735. 生成乘积数组的方案数 - 给你一个二维整数数组 queries ，其中 queries[i] = [ni, ki] 。第 i 个查询 queries[i] 要求构造长度为 ni 、每个元素都是正整数的数组，且满足所有元素的乘积为 ki ，请你找出有多少种可行的方案。由于答案可能会很大，方案数需要对 109 + 7 取余 。 请你返回一个整数数组 answer，满足 answer.length == queries.length ，其中 answer[i]是第 i 个查询的结果。 示例 1： 输入：queries = [[2,6],[5,1],[73,660]] 输出：[4,1,50734910] 解释：每个查询之间彼此独立。 [2,6]：总共有 4 种方案得到长度为 2 且乘积为 6 的数组：[1,6]，[2,3]，[3,2]，[6,1]。 [5,1]：总共有 1 种方案得到长度为 5 且乘积为 1 的数组：[1,1,1,1,1]。 [73,660]：总共有 1050734917 种方案得到长度为 73 且乘积为 660 的数组。1050734917 对 109 + 7 取余得到 50734910 。 示例 2 ： 输入：queries = [[1,1],[2,2],[3,3],[4,4],[5,5]] 输出：[1,2,3,10,5] 提示： * 1 <= queries.length <= 104 * 1 <= ni, ki <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用组合数学和动态规划来计算方案数。

算法步骤:
1. 预处理质因数分解和组合数。
2. 对于每个查询，计算所有可能的方案数。

关键点:
- 使用预处理的质因数分解和组合数来加速计算。
- 动态规划用于计算每个质因数的分配方案。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log(k) + q * n * log(n))
空间复杂度: O(n * log(k) + n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import math

MOD = 10**9 + 7

def precompute_factorials_and_inverses(max_n: int):
    factorials = [1] * (max_n + 1)
    inverses = [1] * (max_n + 1)
    
    for i in range(2, max_n + 1):
        factorials[i] = factorials[i - 1] * i % MOD
        inverses[i] = pow(factorials[i], -1, MOD)
    
    return factorials, inverses

def comb(n: int, k: int, factorials, inverses):
    if k > n:
        return 0
    return factorials[n] * inverses[k] * inverses[n - k] % MOD

def solution_function_name(queries: List[List[int]]) -> List[int]:
    """
    函数式接口 - 计算生成乘积数组的方案数
    """
    max_n = max(ni for ni, _ in queries)
    max_k = max(ki for _, ki in queries)
    
    # 预处理阶乘和逆元
    factorials, inverses = precompute_factorials_and_inverses(max_n)
    
    def count_ways(n: int, k: int) -> int:
        if k == 1:
            return 1
        
        factors = []
        for i in range(2, int(math.sqrt(k)) + 1):
            count = 0
            while k % i == 0:
                k //= i
                count += 1
            if count > 0:
                factors.append(count)
        
        if k > 1:
            factors.append(1)
        
        dp = [1]
        for f in factors:
            new_dp = [0] * (n + 1)
            for j in range(n + 1):
                for x in range(f + 1):
                    if j - x >= 0:
                        new_dp[j] = (new_dp[j] + dp[j - x] * comb(j, x, factorials, inverses)) % MOD
            dp = new_dp
        
        return dp[n]
    
    return [count_ways(ni, ki) for ni, ki in queries]

Solution = create_solution(solution_function_name)