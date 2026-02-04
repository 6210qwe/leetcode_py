# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2477
标题: Number of Ways to Reach a Position After Exactly k Steps
难度: medium
链接: https://leetcode.cn/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/
题目类型: 数学、动态规划、组合数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2400. 恰好移动 k 步到达某一位置的方法数目 - 给你两个 正 整数 startPos 和 endPos 。最初，你站在 无限 数轴上位置 startPos 处。在一步移动中，你可以向左或者向右移动一个位置。 给你一个正整数 k ，返回从 startPos 出发、恰好 移动 k 步并到达 endPos 的 不同 方法数目。由于答案可能会很大，返回对 109 + 7 取余 的结果。 如果所执行移动的顺序不完全相同，则认为两种方法不同。 注意：数轴包含负整数。 示例 1： 输入：startPos = 1, endPos = 2, k = 3 输出：3 解释：存在 3 种从 1 到 2 且恰好移动 3 步的方法： - 1 -> 2 -> 3 -> 2. - 1 -> 2 -> 1 -> 2. - 1 -> 0 -> 1 -> 2. 可以证明不存在其他方法，所以返回 3 。 示例 2： 输入：startPos = 2, endPos = 5, k = 10 输出：0 解释：不存在从 2 到 5 且恰好移动 10 步的方法。 提示： * 1 <= startPos, endPos, k <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用组合数学来计算从 startPos 到 endPos 的不同方法数目。

算法步骤:
1. 计算从 startPos 到 endPos 的距离 diff。
2. 如果 diff 和 k 的奇偶性不同，或者 diff > k，则返回 0。
3. 使用组合公式 C(k, (k + diff) // 2) 来计算方法数目，并对 10^9 + 7 取余。

关键点:
- 使用费马小定理和快速幂来计算组合数的逆元。
- 通过预处理阶乘和逆元来优化计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(k)
空间复杂度: O(k)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

MOD = 10**9 + 7

def mod_inverse(x, p):
    """计算 x 在模 p 下的逆元"""
    return pow(x, p - 2, p)

def precompute_factorials_and_inverses(n, p):
    """预计算阶乘和逆元"""
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % p
        inv_fact[i] = mod_inverse(fact[i], p)
    return fact, inv_fact

def combination(n, k, fact, inv_fact, p):
    """计算组合数 C(n, k)"""
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % p * inv_fact[n - k] % p

def solution_function_name(startPos: int, endPos: int, k: int) -> int:
    """
    函数式接口 - 计算从 startPos 到 endPos 的不同方法数目
    """
    diff = abs(endPos - startPos)
    if (diff + k) % 2 != 0 or diff > k:
        return 0
    
    fact, inv_fact = precompute_factorials_and_inverses(k, MOD)
    steps = (k + diff) // 2
    return combination(k, steps, fact, inv_fact, MOD)

Solution = create_solution(solution_function_name)