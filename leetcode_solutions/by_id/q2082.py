# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2082
标题: Minimum Cost to Separate Sentence Into Rows
难度: medium
链接: https://leetcode.cn/problems/minimum-cost-to-separate-sentence-into-rows/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2052. 将句子分隔成行的最低成本 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i] 表示将前 i 个单词分隔成若干行的最小成本。对于每个 dp[i]，我们需要考虑从 j 到 i 的所有可能的子句，并计算它们的成本。

算法步骤:
1. 初始化 dp 数组，dp[0] = 0，因为没有单词时成本为 0。
2. 对于每个 i，从 0 到 i-1 遍历 j，计算将从 j+1 到 i 的单词放在一行的成本。
3. 更新 dp[i] 为当前最小成本。
4. 最终结果是 dp[n]，其中 n 是单词的数量。

关键点:
- 计算每行的成本时，需要考虑单词长度和空格数。
- 动态规划的状态转移方程：dp[i] = min(dp[j] + cost(j+1, i))，其中 cost(j+1, i) 是将从 j+1 到 i 的单词放在一行的成本。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是单词的数量。我们需要遍历每个单词对。
空间复杂度: O(n)，dp 数组的大小为 n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def minimum_cost_to_separate_sentence_into_rows(sentence: str, k: int) -> int:
    """
    函数式接口 - 将句子分隔成行的最低成本
    """
    words = sentence.split()
    n = len(words)
    
    # 预处理每个单词的长度
    word_lengths = [len(word) for word in words]
    
    # 初始化 dp 数组
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # 动态规划
    for i in range(1, n + 1):
        total_length = 0
        for j in range(i - 1, -1, -1):
            total_length += word_lengths[j]
            if total_length + (i - j - 1) > k:  # 加上空格数
                break
            cost = (k - total_length - (i - j - 1)) ** 2 if i < n else 0
            dp[i] = min(dp[i], dp[j] + cost)
    
    return dp[n]

Solution = create_solution(minimum_cost_to_separate_sentence_into_rows)