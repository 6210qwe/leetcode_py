# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1838
标题: Number of Distinct Substrings in a String
难度: medium
链接: https://leetcode.cn/problems/number-of-distinct-substrings-in-a-string/
题目类型: 字典树、字符串、后缀数组、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1698. 字符串的不同子字符串个数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用后缀数组和高度数组来计算不同子字符串的数量。

算法步骤:
1. 构建后缀数组 (suffix array) 和排名数组 (rank array)。
2. 构建高度数组 (height array)。
3. 使用高度数组来计算不同子字符串的数量。

关键点:
- 后缀数组用于对所有后缀进行排序。
- 排名数组用于记录每个后缀的排名。
- 高度数组用于记录相邻后缀的最长公共前缀长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是字符串的长度。构建后缀数组的时间复杂度为 O(n log n)。
空间复杂度: O(n)，需要额外的空间来存储后缀数组、排名数组和高度数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def build_suffix_array(s: str) -> List[int]:
    """
    构建后缀数组
    """
    n = len(s)
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort()
    return [suffix[1] for suffix in suffixes]

def build_rank_array(suffix_array: List[int]) -> List[int]:
    """
    构建排名数组
    """
    n = len(suffix_array)
    rank_array = [0] * n
    for i, suffix in enumerate(suffix_array):
        rank_array[suffix] = i
    return rank_array

def build_height_array(s: str, suffix_array: List[int], rank_array: List[int]) -> List[int]:
    """
    构建高度数组
    """
    n = len(s)
    height_array = [0] * n
    h = 0
    for i in range(n):
        if rank_array[i] > 0:
            j = suffix_array[rank_array[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            height_array[rank_array[i]] = h
            if h > 0:
                h -= 1
    return height_array

def count_distinct_substrings(s: str) -> int:
    """
    计算不同子字符串的数量
    """
    suffix_array = build_suffix_array(s)
    rank_array = build_rank_array(suffix_array)
    height_array = build_height_array(s, suffix_array, rank_array)
    
    n = len(s)
    distinct_count = sum(n - suffix_array[i] - height_array[i] for i in range(n))
    return distinct_count

Solution = create_solution(count_distinct_substrings)