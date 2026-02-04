# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3864
标题: Count the Number of Computer Unlocking Permutations
难度: medium
链接: https://leetcode.cn/problems/count-the-number-of-computer-unlocking-permutations/
题目类型: 脑筋急转弯、数组、数学、组合数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3577. 统计计算机解锁顺序排列数 - 给你一个长度为 n 的数组 complexity。 在房间里有 n 台 上锁的 计算机，这些计算机的编号为 0 到 n - 1，每台计算机都有一个 唯一 的密码。编号为 i 的计算机的密码复杂度为 complexity[i]。 编号为 0 的计算机密码已经 解锁 ，并作为根节点。其他所有计算机必须通过它或其他已经解锁的计算机来解锁，具体规则如下： * 可以使用编号为 j 的计算机的密码解锁编号为 i 的计算机，其中 j 是任何小于 i 的整数，且满足 complexity[j] < complexity[i]（即 j < i 并且 complexity[j] < complexity[i]）。 * 要解锁编号为 i 的计算机，你需要事先解锁一个编号为 j 的计算机，满足 j < i 并且 complexity[j] < complexity[i]。 求共有多少种 [0, 1, 2, ..., (n - 1)] 的排列方式，能够表示从编号为 0 的计算机（唯一初始解锁的计算机）开始解锁所有计算机的有效顺序。 由于答案可能很大，返回结果需要对 109 + 7 取余数。 注意：编号为 0 的计算机的密码已解锁，而 不是 排列中第一个位置的计算机密码已解锁。 排列 是一个数组中所有元素的重新排列。 示例 1： 输入： complexity = [1,2,3] 输出： 2 解释： 有效的排列有： * [0, 1, 2] * 首先使用根密码解锁计算机 0。 * 使用计算机 0 的密码解锁计算机 1，因为 complexity[0] < complexity[1]。 * 使用计算机 1 的密码解锁计算机 2，因为 complexity[1] < complexity[2]。 * [0, 2, 1] * 首先使用根密码解锁计算机 0。 * 使用计算机 0 的密码解锁计算机 2，因为 complexity[0] < complexity[2]。 * 使用计算机 0 的密码解锁计算机 1，因为 complexity[0] < complexity[1]。 示例 2： 输入： complexity = [3,3,3,4,4,4] 输出： 0 解释： 没有任何排列能够解锁所有计算机。 提示： * 2 <= complexity.length <= 105 * 1 <= complexity[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和组合数学来计算有效排列数。

算法步骤:
1. 将复杂度数组排序，并记录每个复杂度的索引。
2. 使用动态规划数组 dp 来记录到当前复杂度为止的有效排列数。
3. 对于每个复杂度，计算其在排序后的索引位置，并更新 dp 数组。
4. 最终结果是对 dp 数组的最后一个元素取模。

关键点:
- 动态规划数组 dp 用于存储到当前复杂度为止的有效排列数。
- 使用组合数学公式来计算排列数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 complexity 的长度。排序操作的时间复杂度为 O(n log n)，后续遍历操作为 O(n)。
空间复杂度: O(n)，用于存储排序后的索引和动态规划数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(complexity: List[int]) -> int:
    """
    函数式接口 - 计算有效解锁排列数
    """
    MOD = 10**9 + 7
    n = len(complexity)
    
    # 将复杂度数组与其索引配对
    indexed_complexity = [(c, i) for i, c in enumerate(complexity)]
    # 按复杂度排序
    indexed_complexity.sort()
    
    # 初始化动态规划数组
    dp = [0] * n
    dp[0] = 1  # 第一个计算机总是解锁的
    
    # 计算阶乘和逆元
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
        inv_fact[i] = pow(fact[i], MOD - 2, MOD)
    
    # 动态规划计算有效排列数
    for i in range(1, n):
        c, idx = indexed_complexity[i]
        prev_c, _ = indexed_complexity[i - 1]
        if c == prev_c:
            dp[idx] = dp[indexed_complexity[i - 1][1]]
        else:
            dp[idx] = (dp[indexed_complexity[i - 1][1]] * (i)) % MOD
    
    return dp[-1]

Solution = create_solution(solution_function_name)