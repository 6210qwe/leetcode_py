# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3911
标题: Find the Shortest Superstring II
难度: easy
链接: https://leetcode.cn/problems/find-the-shortest-superstring-ii/
题目类型: 字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3571. 最短超级串 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和动态规划来找到最短的超级串。

算法步骤:
1. 计算所有字符串之间的重叠部分。
2. 使用动态规划来找到最短的超级串。
3. 通过回溯路径来构建最终的超级串。

关键点:
- 计算重叠部分时，使用双重循环。
- 动态规划状态转移方程：dp[mask][i] 表示当前状态为 mask 且最后一个字符串为 i 的最短超级串长度。
- 回溯路径时，从 dp[final_mask][best_last] 开始，逐步构建最终的超级串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * 2^n)，其中 n 是字符串的数量。
空间复杂度: O(n * 2^n)，用于存储动态规划表和路径。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_shortest_superstring(words: List[str]) -> str:
    """
    函数式接口 - 找到最短的超级串
    """
    n = len(words)
    overlap = [[0] * n for _ in range(n)]
    
    # 计算所有字符串之间的重叠部分
    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(1, min(len(words[i]), len(words[j])) + 1):
                    if words[i][-k:] == words[j][:k]:
                        overlap[i][j] = k
    
    # 动态规划初始化
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
    
    # 初始状态
    for i in range(n):
        dp[1 << i][i] = len(words[i])
    
    # 动态规划状态转移
    for mask in range(1, 1 << n):
        for bit in range(n):
            if (mask >> bit) & 1:
                pmask = mask ^ (1 << bit)
                if pmask:
                    for i in range(n):
                        if (pmask >> i) & 1:
                            value = dp[pmask][i] + len(words[bit]) - overlap[i][bit]
                            if value < dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i
    
    # 找到最优解
    final_mask = (1 << n) - 1
    best_last = min(range(n), key=lambda i: dp[final_mask][i])
    perm = []
    mask = final_mask
    while mask:
        perm.append(best_last)
        mask, best_last = mask ^ (1 << best_last), parent[mask][best_last]
    
    perm.reverse()
    ans = [words[perm[0]]]
    for i in range(1, len(perm)):
        overlap_len = overlap[perm[i-1]][perm[i]]
        ans.append(words[perm[i]][overlap_len:])
    
    return ''.join(ans)


Solution = create_solution(find_shortest_superstring)