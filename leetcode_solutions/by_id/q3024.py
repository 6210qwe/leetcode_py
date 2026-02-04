# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3024
标题: String Transformation
难度: hard
链接: https://leetcode.cn/problems/string-transformation/
题目类型: 数学、字符串、动态规划、字符串匹配
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2851. 字符串转换 - 给你两个长度都为 n 的字符串 s 和 t 。你可以对字符串 s 执行以下操作： * 将 s 长度为 l （0 < l < n）的 后缀字符串 删除，并将它添加在 s 的开头。 比方说，s = 'abcd' ，那么一次操作中，你可以删除后缀 'cd' ，并将它添加到 s 的开头，得到 s = 'cdab' 。 给你一个整数 k ，请你返回 恰好 k 次操作将 s 变为 t 的方案数。 由于答案可能很大，返回答案对 109 + 7 取余 后的结果。 示例 1： 输入：s = "abcd", t = "cdab", k = 2 输出：2 解释： 第一种方案： 第一次操作，选择 index = 3 开始的后缀，得到 s = "dabc" 。 第二次操作，选择 index = 3 开始的后缀，得到 s = "cdab" 。 第二种方案： 第一次操作，选择 index = 1 开始的后缀，得到 s = "bcda" 。 第二次操作，选择 index = 1 开始的后缀，得到 s = "cdab" 。 示例 2： 输入：s = "ababab", t = "ababab", k = 1 输出：2 解释： 第一种方案： 选择 index = 2 开始的后缀，得到 s = "ababab" 。 第二种方案： 选择 index = 4 开始的后缀，得到 s = "ababab" 。 提示： * 2 <= s.length <= 5 * 105 * 1 <= k <= 1015 * s.length == t.length * s 和 t 都只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用矩阵快速幂来计算 k 次操作后的状态转移矩阵。

算法步骤:
1. 构建初始的状态转移矩阵和初始状态向量。
2. 使用矩阵快速幂计算 k 次操作后的状态转移矩阵。
3. 计算最终状态向量，并提取结果。

关键点:
- 使用矩阵快速幂来高效计算大指数次幂。
- 状态转移矩阵的构建和初始化。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log k)
空间复杂度: O(n^2)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import numpy as np

MOD = 10**9 + 7

def matrix_mult(A, B):
    return (A @ B) % MOD

def matrix_pow(matrix, power):
    result = np.eye(len(matrix), dtype=int)
    base = matrix
    while power > 0:
        if power & 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        power >>= 1
    return result

def solution_function_name(s: str, t: str, k: int) -> int:
    n = len(s)
    
    # 构建状态转移矩阵
    transition_matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if s[i:] + s[:i] == t[j:] + t[:j]:
                transition_matrix[i][j] = 1
    
    # 初始状态向量
    initial_state = np.zeros(n, dtype=int)
    for i in range(n):
        if s[i:] + s[:i] == t:
            initial_state[i] = 1
    
    # 计算 k 次操作后的状态转移矩阵
    final_transition_matrix = matrix_pow(transition_matrix, k)
    
    # 计算最终状态向量
    final_state = matrix_mult(final_transition_matrix, initial_state)
    
    # 返回结果
    return sum(final_state) % MOD

Solution = create_solution(solution_function_name)