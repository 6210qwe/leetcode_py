# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3245
标题: Find Beautiful Indices in the Given Array I
难度: medium
链接: https://leetcode.cn/problems/find-beautiful-indices-in-the-given-array-i/
题目类型: 双指针、字符串、二分查找、字符串匹配、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3006. 找出数组中的美丽下标 I - 给你一个下标从 0 开始的字符串 s 、字符串 a 、字符串 b 和一个整数 k 。 如果下标 i 满足以下条件，则认为它是一个 美丽下标： * 0 <= i <= s.length - a.length * s[i..(i + a.length - 1)] == a * 存在下标 j 使得： * 0 <= j <= s.length - b.length * s[j..(j + b.length - 1)] == b * |j - i| <= k 以数组形式按 从小到大排序 返回美丽下标。 示例 1： 输入：s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15 输出：[16,33] 解释：存在 2 个美丽下标：[16,33]。 - 下标 16 是美丽下标，因为 s[16..17] == "my" ，且存在下标 4 ，满足 s[4..11] == "squirrel" 且 |16 - 4| <= 15 。 - 下标 33 是美丽下标，因为 s[33..34] == "my" ，且存在下标 18 ，满足 s[18..25] == "squirrel" 且 |33 - 18| <= 15 。 因此返回 [16,33] 作为结果。 示例 2： 输入：s = "abcd", a = "a", b = "a", k = 4 输出：[0] 解释：存在 1 个美丽下标：[0]。 - 下标 0 是美丽下标，因为 s[0..0] == "a" ，且存在下标 0 ，满足 s[0..0] == "a" 且 |0 - 0| <= 4 。 因此返回 [0] 作为结果。 提示： * 1 <= k <= s.length <= 105 * 1 <= a.length, b.length <= 10 * s、a、和 b 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 KMP 算法找到所有匹配 a 和 b 的子串位置，然后通过双指针方法找到满足条件的美丽下标。

算法步骤:
1. 使用 KMP 算法找到字符串 s 中所有匹配 a 和 b 的子串位置。
2. 使用双指针方法遍历这些位置，找到满足 |j - i| <= k 的美丽下标。

关键点:
- 使用 KMP 算法进行高效的字符串匹配。
- 使用双指针方法高效地找到满足条件的美丽下标。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m + p)，其中 n 是字符串 s 的长度，m 是字符串 a 的长度，p 是字符串 b 的长度。
空间复杂度: O(m + p)，用于存储 KMP 算法的前缀函数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def compute_kmp_table(pattern: str) -> List[int]:
    """
    计算 KMP 算法的前缀函数表。
    """
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        table[i] = j
    return table

def find_substring_indices(s: str, pattern: str) -> List[int]:
    """
    使用 KMP 算法找到所有匹配 pattern 的子串位置。
    """
    table = compute_kmp_table(pattern)
    indices = []
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = table[j - 1]
        if s[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            indices.append(i - j + 1)
            j = table[j - 1]
    return indices

def solution_function_name(s: str, a: str, b: str, k: int) -> List[int]:
    """
    函数式接口 - 找出数组中的美丽下标 I
    """
    # 使用 KMP 算法找到所有匹配 a 和 b 的子串位置
    a_indices = find_substring_indices(s, a)
    b_indices = find_substring_indices(s, b)

    beautiful_indices = []
    j = 0
    for i in a_indices:
        # 使用双指针方法找到满足 |j - i| <= k 的美丽下标
        while j < len(b_indices) and b_indices[j] < i - k:
            j += 1
        if j < len(b_indices) and abs(b_indices[j] - i) <= k:
            beautiful_indices.append(i)

    return beautiful_indices

Solution = create_solution(solution_function_name)