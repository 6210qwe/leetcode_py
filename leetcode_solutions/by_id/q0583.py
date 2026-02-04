# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 583
标题: Delete Operation for Two Strings
难度: medium
链接: https://leetcode.cn/problems/delete-operation-for-two-strings/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
583. 两个字符串的删除操作 - 给定两个单词 word1 和 word2 ，返回使得 word1 和 word2 相同所需的最小步数。 每步 可以删除任意一个字符串中的一个字符。 示例 1： 输入: word1 = "sea", word2 = "eat" 输出: 2 解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea" 示例 2: 输入：word1 = "leetcode", word2 = "etco" 输出：4 提示： * 1 <= word1.length, word2.length <= 500 * word1 和 word2 只包含小写英文字母
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i][j] 表示 word1 的前 i 个字符和 word2 的前 j 个字符的最小删除次数。

算法步骤:
1. 初始化一个 (m+1) x (n+1) 的二维数组 dp，其中 m 和 n 分别是 word1 和 word2 的长度。
2. 如果 word1 的前 i 个字符和 word2 的前 j 个字符相同，则 dp[i][j] = dp[i-1][j-1]。
3. 否则，dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1，表示删除一个字符。
4. 最终结果保存在 dp[m][n] 中。

关键点:
- 动态规划的状态转移方程
- 边界条件的处理
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是 word1 和 word2 的长度。
空间复杂度: O(m * n)，使用了一个 (m+1) x (n+1) 的二维数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(word1: str, word2: str) -> int:
    """
    函数式接口 - 计算使两个字符串相同的最小删除次数
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化边界条件
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # 填充 dp 数组
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]


Solution = create_solution(solution_function_name)