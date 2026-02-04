# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 730
标题: Count Different Palindromic Subsequences
难度: hard
链接: https://leetcode.cn/problems/count-different-palindromic-subsequences/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
730. 统计不同回文子序列 - 给你一个字符串 s ，返回 s 中不同的非空回文子序列个数 。由于答案可能很大，请返回对 109 + 7 取余 的结果。 字符串的子序列可以经由字符串删除 0 个或多个字符获得。 如果一个序列与它反转后的序列一致，那么它是回文序列。 如果存在某个 i , 满足 ai != bi ，则两个序列 a1, a2, ... 和 b1, b2, ... 不同。 示例 1： 输入：s = 'bccb' 输出：6 解释：6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。 注意：'bcb' 虽然出现两次但仅计数一次。 示例 2： 输入：s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba' 输出：104860361 解释：共有 3104860382 个不同的非空回文子序列，104860361 是对 109 + 7 取余后的值。 提示： * 1 <= s.length <= 1000 * s[i] 仅包含 'a', 'b', 'c' 或 'd'
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i][j] 表示 s[i:j+1] 中的不同回文子序列的数量。通过递归和记忆化搜索来计算每个子区间的结果。

算法步骤:
1. 初始化一个三维数组 dp，其中 dp[i][j][k] 表示在 s[i:j+1] 中以 k 开头和结尾的不同回文子序列的数量。
2. 使用递归和记忆化搜索来填充 dp 数组。
3. 最终结果是 dp[0][n-1][0] 到 dp[0][n-1][3] 的和减去 1（因为要排除空串）。

关键点:
- 使用记忆化搜索来避免重复计算。
- 通过递归处理每个子区间的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^3)，其中 n 是字符串 s 的长度。我们需要计算每个子区间的 dp 值。
空间复杂度: O(n^3)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

MOD = 10**9 + 7

def count_palindromic_subsequences(s: str) -> int:
    n = len(s)
    dp = [[[0] * 4 for _ in range(n)] for _ in range(n)]
    
    def dfs(i: int, j: int, k: int) -> int:
        if i > j:
            return 0
        if dp[i][j][k] != 0:
            return dp[i][j][k]
        
        if i == j:
            dp[i][j][k] = 1 if s[i] == chr(ord('a') + k) else 0
            return dp[i][j][k]
        
        if s[i] == chr(ord('a') + k):
            dp[i][j][k] = (dfs(i, j - 1, k) + dfs(i + 1, j, k) + 1) % MOD
        else:
            dp[i][j][k] = dfs(i + 1, j, k)
        
        return dp[i][j][k]
    
    result = 0
    for k in range(4):
        result = (result + dfs(0, n - 1, k)) % MOD
    
    return (result - 1 + MOD) % MOD

Solution = create_solution(count_palindromic_subsequences)