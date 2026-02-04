# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000272
标题: 分割回文串 II
难度: hard
链接: https://leetcode.cn/problems/omKAoA/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 094. 分割回文串 II - 给定一个字符串 s，请将 s 分割成一些子串，使每个子串都是回文串。 返回符合要求的 最少分割次数 。 示例 1： 输入：s = "aab" 输出：1 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。 示例 2： 输入：s = "a" 输出：0 示例 3： 输入：s = "ab" 输出：1 提示： * 1 <= s.length <= 2000 * s 仅由小写英文字母组成 注意：本题与主站 132 题相同： https://leetcode.cn/problems/palindrome-partitioning-ii/ [https://leetcode.cn/problems/palindrome-partitioning-ii/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。首先预处理出所有子串是否为回文串，然后使用动态规划来计算最少的分割次数。

算法步骤:
1. 预处理所有子串是否为回文串。
2. 使用动态规划数组 dp 来记录到每个位置的最少分割次数。
3. 对于每个位置 i，遍历其之前的所有位置 j，如果 s[j+1:i+1] 是回文串，则更新 dp[i]。

关键点:
- 预处理回文子串可以使用中心扩展法或动态规划。
- 动态规划的状态转移方程为 dp[i] = min(dp[i], dp[j] + 1) if is_palindrome[j+1][i+1]。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是字符串的长度。预处理回文子串和动态规划都需要 O(n^2) 的时间。
空间复杂度: O(n^2)，预处理回文子串需要 O(n^2) 的空间，动态规划数组需要 O(n) 的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_cut(s: str) -> int:
    """
    函数式接口 - 计算将字符串 s 分割成回文子串的最少分割次数
    """
    n = len(s)
    if n == 0:
        return 0

    # 预处理所有子串是否为回文串
    is_palindrome = [[False] * (n + 1) for _ in range(n + 1)]
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if s[start] == s[end] and (length <= 2 or is_palindrome[start + 1][end]):
                is_palindrome[start][end] = True

    # 动态规划数组
    dp = [float('inf')] * n
    for i in range(n):
        if is_palindrome[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if is_palindrome[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

    return dp[n - 1]


Solution = create_solution(min_cut)