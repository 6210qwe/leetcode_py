# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1244
标题: Distinct Echo Substrings
难度: hard
链接: https://leetcode.cn/problems/distinct-echo-substrings/
题目类型: 字典树、字符串、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1316. 不同的循环子字符串 - 给你一个字符串 text ，请你返回满足下述条件的 不同 非空子字符串的数目： * 可以写成某个字符串与其自身相连接的形式（即，可以写为 a + a，其中 a 是某个字符串）。 例如，abcabc 就是 abc 和它自身连接形成的。 示例 1： 输入：text = "abcabcabc" 输出：3 解释：3 个子字符串分别为 "abcabc"，"bcabca" 和 "cabcab" 。 示例 2： 输入：text = "leetcodeleetcode" 输出：2 解释：2 个子字符串为 "ee" 和 "leetcodeleetcode" 。 提示： * 1 <= text.length <= 2000 * text 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滚动哈希来检查所有可能的子字符串是否可以写成某个字符串与其自身相连接的形式。

算法步骤:
1. 初始化一个集合 `seen` 来存储不同的回文子字符串。
2. 遍历所有可能的子字符串长度 `len_a`，从 1 到 `n // 2`。
3. 对于每个 `len_a`，计算滚动哈希值，并检查是否存在相同的哈希值。
4. 如果存在相同的哈希值，则将该子字符串加入 `seen` 集合。
5. 返回 `seen` 集合的大小。

关键点:
- 使用滚动哈希来高效地计算和比较子字符串的哈希值。
- 通过集合来存储不同的回文子字符串，确保唯一性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def distinct_echo_substrings(text: str) -> int:
    """
    函数式接口 - 返回满足条件的不同非空子字符串的数目
    """
    n = len(text)
    if n < 2:
        return 0

    base = 26
    mod = 10**9 + 7
    seen = set()

    for len_a in range(1, n // 2 + 1):
        hash_a = 0
        hash_b = 0
        power = 1

        for i in range(len_a):
            hash_a = (hash_a * base + ord(text[i])) % mod
            hash_b = (hash_b * base + ord(text[len_a + i])) % mod
            if i < len_a - 1:
                power = (power * base) % mod

        for i in range(n - 2 * len_a + 1):
            if hash_a == hash_b and text[i:i+len_a] == text[i+len_a:i+2*len_a]:
                seen.add(text[i:i+2*len_a])

            if i + 2 * len_a < n:
                hash_a = (hash_a * base - ord(text[i]) * power + ord(text[i + len_a])) % mod
                hash_b = (hash_b * base - ord(text[i + len_a]) * power + ord(text[i + 2 * len_a])) % mod
                hash_a = (hash_a + mod) % mod
                hash_b = (hash_b + mod) % mod

    return len(seen)


Solution = create_solution(distinct_echo_substrings)