# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000277
标题: 交错字符串
难度: medium
链接: https://leetcode.cn/problems/IY6buf/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 096. 交错字符串 - 给定三个字符串 s1、s2、s3，请判断 s3 能不能由 s1 和 s2 交织（交错） 组成。 两个字符串 s 和 t 交织 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串： * s = s1 + s2 + ... + sn * t = t1 + t2 + ... + tm * |n - m| <= 1 * 交织 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ... 提示：a + b 意味着字符串 a 和 b 连接。 示例 1： [https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg] 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac" 输出：true 示例 2： 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc" 输出：false 示例 3： 输入：s1 = "", s2 = "", s3 = "" 输出：true 提示： * 0 <= s1.length, s2.length <= 100 * 0 <= s3.length <= 200 * s1、s2、和 s3 都由小写英文字母组成 注意：本题与主站 97 题相同： https://leetcode.cn/problems/interleaving-string/ [https://leetcode.cn/problems/interleaving-string/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义一个二维布尔数组 dp，其中 dp[i][j] 表示 s1 的前 i 个字符和 s2 的前 j 个字符是否可以交织成 s3 的前 i+j 个字符。

算法步骤:
1. 初始化 dp 数组，dp[0][0] = True。
2. 填充 dp 数组的第一行和第一列，表示 s1 或 s2 为空的情况。
3. 通过双重循环填充 dp 数组的其余部分，根据 s1 和 s2 的字符是否匹配 s3 的字符来更新 dp 数组。
4. 最终返回 dp[len(s1)][len(s2)] 的值。

关键点:
- 动态规划的状态转移方程为 dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
- 边界条件需要特别处理，例如当 s1 或 s2 为空时的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是 s1 和 s2 的长度。
空间复杂度: O(m * n)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    """
    判断 s3 是否可以由 s1 和 s2 交织而成。
    """
    len1, len2, len3 = len(s1), len(s2), len(s3)
    
    if len1 + len2 != len3:
        return False
    
    # 初始化 dp 数组
    dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
    dp[0][0] = True
    
    # 填充 dp 数组的第一行
    for j in range(1, len2 + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
    
    # 填充 dp 数组的第一列
    for i in range(1, len1 + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
    
    # 填充 dp 数组的其余部分
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
    
    return dp[len1][len2]


Solution = create_solution(isInterleave)