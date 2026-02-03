# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 131
标题: Palindrome Partitioning
难度: medium
链接: https://leetcode.cn/problems/palindrome-partitioning/
题目类型: 字符串、动态规划、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
131. 分割回文串 - 给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。 示例 1： 输入：s = "aab" 输出：[["a","a","b"],["aa","b"]] 示例 2： 输入：s = "a" 输出：[["a"]] 提示： * 1 <= s.length <= 16 * s 仅由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯算法，使用动态规划预处理回文串

算法步骤:
1. 使用DP预处理，判断所有子串是否为回文串
2. 使用回溯，尝试所有可能的分割方式
3. 如果当前子串是回文串，继续递归

关键点:
- 回溯+DP预处理
- 时间复杂度O(2^n)，空间复杂度O(n^2)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n) - 所有可能的分割方式
空间复杂度: O(n^2) - DP数组空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def palindrome_partitioning(s: str) -> List[List[str]]:
    """
    函数式接口 - 分割回文串
    
    实现思路:
    回溯算法，使用动态规划预处理回文串。
    
    Args:
        s: 字符串
        
    Returns:
        所有可能的分割方案
        
    Example:
        >>> palindrome_partitioning("aab")
        [['a', 'a', 'b'], ['aa', 'b']]
    """
    n = len(s)
    # DP预处理，判断子串是否为回文串
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
    
    result = []
    
    def backtrack(start: int, path: List[str]):
        """回溯函数"""
        if start == n:
            result.append(path[:])
            return
        
        for end in range(start, n):
            if dp[start][end]:
                path.append(s[start:end + 1])
                backtrack(end + 1, path)
                path.pop()
    
    backtrack(0, [])
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(palindrome_partitioning)
