# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 980
标题: Find the Shortest Superstring
难度: hard
链接: https://leetcode.cn/problems/find-the-shortest-superstring/
题目类型: 位运算、数组、字符串、动态规划、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
943. 最短超级串 - 给定一个字符串数组 words，找到以 words 中每个字符串作为子字符串的最短字符串。如果有多个有效最短字符串满足题目条件，返回其中 任意一个 即可。 我们可以假设 words 中没有字符串是 words 中另一个字符串的子字符串。 示例 1： 输入：words = ["alex","loves","leetcode"] 输出："alexlovesleetcode" 解释："alex"，"loves"，"leetcode" 的所有排列都会被接受。 示例 2： 输入：words = ["catg","ctaagt","gcta","ttca","atgcatc"] 输出："gctaagttcatgcatc" 提示： * 1 <= words.length <= 12 * 1 <= words[i].length <= 20 * words[i] 由小写英文字母组成 * words 中的所有字符串 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和状态压缩来解决这个问题。

算法步骤:
1. 计算所有字符串之间的重叠部分。
2. 使用动态规划来记录在某个状态下，最后一个字符串是哪个以及当前的最短长度。
3. 通过回溯找到最终的最短超级串。

关键点:
- 使用状态压缩来表示哪些字符串已经被使用。
- 动态规划表 dp[mask][i] 表示状态 mask 下，最后一个字符串是 words[i] 时的最短长度。
- 重叠部分计算可以帮助减少重复部分。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * 2^n)，其中 n 是 words 的长度。
空间复杂度: O(n * 2^n)，用于存储动态规划表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_shortest_superstring(words: List[str]) -> str:
    n = len(words)
    # 计算所有字符串之间的重叠部分
    overlap = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(1, min(len(words[i]), len(words[j])) + 1):
                    if words[i][-k:] == words[j][:k]:
                        overlap[i][j] = k

    # 动态规划表
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[None] * n for _ in range(1 << n)]

    # 初始化
    for i in range(n):
        dp[1 << i][i] = len(words[i])

    # 动态规划
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

    # 找到最短超级串的最后一个字符串
    last = min(range(n), key=lambda i: dp[(1 << n) - 1][i])
    perm = []
    mask = (1 << n) - 1
    while mask:
        perm.append(last)
        mask, last = mask ^ (1 << last), parent[mask][last]

    # 构建最短超级串
    perm.reverse()
    result = [words[perm[0]]]
    for i in range(1, len(perm)):
        overlap_len = overlap[perm[i - 1]][perm[i]]
        result.append(words[perm[i]][overlap_len:])

    return ''.join(result)


Solution = create_solution(find_shortest_superstring)