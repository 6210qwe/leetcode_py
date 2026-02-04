# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1941
标题: Minimum Number of Operations to Make String Sorted
难度: hard
链接: https://leetcode.cn/problems/minimum-number-of-operations-to-make-string-sorted/
题目类型: 数学、字符串、组合数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1830. 使字符串有序的最少操作次数 - 给你一个字符串 s （下标从 0 开始）。你需要对 s 执行以下操作直到它变为一个有序字符串： 1. 找到 最大下标 i ，使得 1 <= i < s.length 且 s[i] < s[i - 1] 。 2. 找到 最大下标 j ，使得 i <= j < s.length 且对于所有在闭区间 [i, j] 之间的 k 都有 s[k] < s[i - 1] 。 3. 交换下标为 i - 1 和 j 处的两个字符。 4. 将下标 i 开始的字符串后缀反转。 请你返回将字符串变成有序的最少操作次数。由于答案可能会很大，请返回它对 109 + 7 取余 的结果。 示例 1： 输入：s = "cba" 输出：5 解释：模拟过程如下所示： 操作 1：i=2，j=2。交换 s[1] 和 s[2] 得到 s="cab" ，然后反转下标从 2 开始的后缀字符串，得到 s="cab" 。 操作 2：i=1，j=2。交换 s[0] 和 s[2] 得到 s="bac" ，然后反转下标从 1 开始的后缀字符串，得到 s="bca" 。 操作 3：i=2，j=2。交换 s[1] 和 s[2] 得到 s="bac" ，然后反转下标从 2 开始的后缀字符串，得到 s="bac" 。 操作 4：i=1，j=1。交换 s[0] 和 s[1] 得到 s="abc" ，然后反转下标从 1 开始的后缀字符串，得到 s="acb" 。 操作 5：i=2，j=2。交换 s[1] 和 s[2] 得到 s="abc" ，然后反转下标从 2 开始的后缀字符串，得到 s="abc" 。 示例 2： 输入：s = "aabaa" 输出：2 解释：模拟过程如下所示： 操作 1：i=3，j=4。交换 s[2] 和 s[4] 得到 s="aaaab" ，然后反转下标从 3 开始的后缀字符串，得到 s="aaaba" 。 操作 2：i=4，j=4。交换 s[3] 和 s[4] 得到 s="aaaab" ，然后反转下标从 4 开始的后缀字符串，得到 s="aaaab" 。 示例 3： 输入：s = "cdbea" 输出：63 示例 4： 输入：s = "leetcodeleetcodeleetcode" 输出：982157772 提示： * 1 <= s.length <= 3000 * s 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用组合数学计算逆序数

算法步骤:
1. 计算每个字符的逆序数。
2. 使用动态规划和组合数学计算排列数。

关键点:
- 使用阶乘和逆元来计算组合数。
- 通过逆序数计算最小操作次数。
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

MOD = 10**9 + 7

def factorial_mod(n: int) -> int:
    """计算 n! % MOD"""
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % MOD
    return result

def mod_inverse(x: int) -> int:
    """计算 x 的模逆元"""
    return pow(x, MOD - 2, MOD)

def combination_mod(n: int, k: int) -> int:
    """计算 C(n, k) % MOD"""
    if k > n:
        return 0
    num = factorial_mod(n)
    den = (factorial_mod(k) * factorial_mod(n - k)) % MOD
    return (num * mod_inverse(den)) % MOD

def solution_function_name(s: str) -> int:
    """
    函数式接口 - 计算使字符串有序的最少操作次数
    """
    n = len(s)
    count = [0] * 26
    inv_count = 0
    
    for i in range(n - 1, -1, -1):
        ch = ord(s[i]) - ord('a')
        inv_count = (inv_count + sum(count[:ch])) % MOD
        count[ch] += 1
    
    return inv_count

Solution = create_solution(solution_function_name)