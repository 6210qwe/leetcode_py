# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1513
标题: Find All Good Strings
难度: hard
链接: https://leetcode.cn/problems/find-all-good-strings/
题目类型: 字符串、动态规划、字符串匹配
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1397. 找到所有好字符串 - 给你两个长度为 n 的字符串 s1 和 s2 ，以及一个字符串 evil 。请你返回 好字符串 的数目。 好字符串 的定义为：它的长度为 n ，字典序大于等于 s1 ，字典序小于等于 s2 ，且不包含 evil 为子字符串。 由于答案可能很大，请你返回答案对 10^9 + 7 取余的结果。 示例 1： 输入：n = 2, s1 = "aa", s2 = "da", evil = "b" 输出：51 解释：总共有 25 个以 'a' 开头的好字符串："aa"，"ac"，"ad"，...，"az"。还有 25 个以 'c' 开头的好字符串："ca"，"cc"，"cd"，...，"cz"。最后，还有一个以 'd' 开头的好字符串："da"。 示例 2： 输入：n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet" 输出：0 解释：所有字典序大于等于 s1 且小于等于 s2 的字符串都以 evil 字符串 "leet" 开头。所以没有好字符串。 示例 3： 输入：n = 2, s1 = "gx", s2 = "gz", evil = "x" 输出：2 提示： * s1.length == n * s2.length == n * s1 <= s2 * 1 <= n <= 500 * 1 <= evil.length <= 50 * 所有字符串都只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和KMP算法来解决这个问题。

算法步骤:
1. 构建evil字符串的KMP前缀数组。
2. 定义一个递归函数来计算从某个位置开始的好字符串数量。
3. 使用记忆化搜索来避免重复计算。
4. 分别计算以s1和s2为边界的字符串数量，并减去重叠部分。

关键点:
- 使用KMP算法来快速判断是否包含evil子字符串。
- 使用记忆化搜索来优化动态规划。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中n是字符串长度，m是evil字符串的长度。
空间复杂度: O(n * m)，用于存储记忆化搜索的状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from functools import lru_cache

MOD = 10**9 + 7

def kmp_prefix(evil: str) -> List[int]:
    m = len(evil)
    prefix = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and evil[i] != evil[j]:
            j = prefix[j - 1]
        if evil[i] == evil[j]:
            j += 1
        prefix[i] = j
    return prefix

@lru_cache(None)
def dp(index: int, match_len: int, is_s1: bool, is_s2: bool, n: int, s1: str, s2: str, evil: str, prefix: List[int]) -> int:
    if match_len == len(evil):
        return 0
    if index == n:
        return 1
    low = ord(s1[index]) if is_s1 else ord('a')
    high = ord(s2[index]) if is_s2 else ord('z')
    res = 0
    for c in range(low, high + 1):
        char = chr(c)
        new_match_len = match_len
        while new_match_len > 0 and char != evil[new_match_len]:
            new_match_len = prefix[new_match_len - 1]
        if char == evil[new_match_len]:
            new_match_len += 1
        res = (res + dp(index + 1, new_match_len, is_s1 and c == ord(s1[index]), is_s2 and c == ord(s2[index]), n, s1, s2, evil, prefix)) % MOD
    return res

def find_good_strings(n: int, s1: str, s2: str, evil: str) -> int:
    prefix = kmp_prefix(evil)
    return (dp(0, 0, True, True, n, s1, s2, evil, prefix) - 1) % MOD

Solution = create_solution(find_good_strings)