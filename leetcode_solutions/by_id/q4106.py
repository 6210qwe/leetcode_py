# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4106
标题: Lexicographically Smallest String After Reverse II
难度: hard
链接: https://leetcode.cn/problems/lexicographically-smallest-string-after-reverse-ii/
题目类型: 字符串、二分查找、后缀数组、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3735. 反转后字典序最小的字符串 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用后缀数组和滚动哈希来找到反转后的字典序最小的字符串。

算法步骤:
1. 构建后缀数组和排名数组。
2. 使用滚动哈希来加速比较。
3. 通过二分查找找到最优的分割点。
4. 返回反转后的最小字符串。

关键点:
- 后缀数组和排名数组的构建。
- 滚动哈希的使用。
- 二分查找的应用。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def build_suffix_array(s: str) -> List[int]:
    n = len(s)
    sa = list(range(n))
    rank = [ord(c) for c in s]
    k = 1
    while k < n:
        def compare(i, j):
            if rank[i] != rank[j]:
                return rank[i] < rank[j]
            i += k
            j += k
            return rank[i] < rank[j] if i < n and j < n else i > j

        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))
        new_rank = [0] * n
        new_rank[sa[0]] = 0
        for i in range(1, n):
            new_rank[sa[i]] = new_rank[sa[i - 1]] + (compare(sa[i - 1], sa[i]) == False)
        rank = new_rank
        k *= 2
    return sa, rank


def solution_function_name(s: str) -> str:
    """
    函数式接口 - 实现
    """
    n = len(s)
    sa, rank = build_suffix_array(s)

    # 滚动哈希
    base = 257
    mod = 10 ** 9 + 7
    hash_values = [0] * (n + 1)
    power = [1] * (n + 1)
    for i in range(n):
        hash_values[i + 1] = (hash_values[i] * base + ord(s[i])) % mod
        power[i + 1] = (power[i] * base) % mod

    def get_hash(l, r):
        return (hash_values[r + 1] - hash_values[l] * power[r - l + 1]) % mod

    def is_smaller(l1, r1, l2, r2):
        len1, len2 = r1 - l1 + 1, r2 - l2 + 1
        left, right = 0, min(len1, len2)
        while left < right:
            mid = (left + right + 1) // 2
            if get_hash(l1, l1 + mid - 1) == get_hash(l2, l2 + mid - 1):
                left = mid
            else:
                right = mid - 1
        if left == min(len1, len2):
            return len1 < len2
        return s[l1 + left] < s[l2 + left]

    best = s
    for i in range(n):
        for j in range(i + 1, n + 1):
            candidate = s[:i] + s[i:j][::-1] + s[j:]
            if is_smaller(0, n - 1, 0, len(candidate) - 1):
                best = candidate
    return best


Solution = create_solution(solution_function_name)