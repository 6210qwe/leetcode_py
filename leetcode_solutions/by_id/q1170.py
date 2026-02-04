# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1170
标题: Shortest Common Supersequence
难度: hard
链接: https://leetcode.cn/problems/shortest-common-supersequence/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1092. 最短公共超序列 - 给你两个字符串 str1 和 str2，返回同时以 str1 和 str2 作为 子序列 的最短字符串。如果答案不止一个，则可以返回满足条件的 任意一个 答案。 如果从字符串 t 中删除一些字符（也可能不删除），可以得到字符串 s ，那么 s 就是 t 的一个子序列。 示例 1： 输入：str1 = "abac", str2 = "cab" 输出："cabac" 解释： str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。 str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。 最终我们给出的答案是满足上述属性的最短字符串。 示例 2： 输入：str1 = "aaaaaaaa", str2 = "aaaaaaaa" 输出："aaaaaaaa" 提示： * 1 <= str1.length, str2.length <= 1000 * str1 和 str2 都由小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划找到最长公共子序列 (LCS)，然后通过 LCS 构造最短公共超序列 (SCS)。

算法步骤:
1. 使用动态规划计算两个字符串的 LCS。
2. 通过 LCS 构造 SCS：
   - 从 LCS 的最后一个字符开始，向前遍历。
   - 如果当前字符在两个字符串中都存在，则将该字符加入结果，并移动两个字符串的指针。
   - 如果当前字符只在一个字符串中存在，则将该字符加入结果，并移动对应的字符串指针。
3. 最后将剩余的字符加入结果。

关键点:
- 动态规划表用于存储 LCS 的长度。
- 通过回溯动态规划表来构造 SCS。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是 str1 和 str2 的长度。
空间复杂度: O(m * n)，用于存储动态规划表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def shortestCommonSupersequence(str1: str, str2: str) -> str:
    """
    函数式接口 - 返回同时以 str1 和 str2 作为子序列的最短字符串
    """
    m, n = len(str1), len(str2)
    
    # 创建动态规划表
    dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]
    
    # 填充动态规划表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
    
    # 回溯构造最短公共超序列
    i, j = m, n
    lcs = dp[m][n]
    scs = []
    k = len(lcs) - 1
    
    while i > 0 and j > 0:
        if k >= 0 and str1[i - 1] == lcs[k] and str2[j - 1] == lcs[k]:
            scs.append(lcs[k])
            i -= 1
            j -= 1
            k -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            scs.append(str1[i - 1])
            i -= 1
        else:
            scs.append(str2[j - 1])
            j -= 1
    
    while i > 0:
        scs.append(str1[i - 1])
        i -= 1
    
    while j > 0:
        scs.append(str2[j - 1])
        j -= 1
    
    return ''.join(reversed(scs))


Solution = create_solution(shortestCommonSupersequence)