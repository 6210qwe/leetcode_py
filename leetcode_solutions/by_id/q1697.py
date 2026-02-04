# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1697
标题: Strings Differ by One Character
难度: medium
链接: https://leetcode.cn/problems/strings-differ-by-one-character/
题目类型: 哈希表、字符串、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1554. 只有一个不同字符的字符串 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滚动哈希来检查每对字符串是否只有一个字符不同。

算法步骤:
1. 计算每个字符串的滚动哈希值。
2. 对于每个字符串，生成其所有可能的一个字符替换后的哈希值，并存储在哈希表中。
3. 检查哈希表中是否存在相同的哈希值，如果存在则说明有字符串只差一个字符。

关键点:
- 使用滚动哈希可以高效地计算和比较字符串的哈希值。
- 通过替换每个字符并生成新的哈希值，可以检查所有可能的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m^2)，其中 n 是字符串的数量，m 是字符串的长度。
空间复杂度: O(n * m)，用于存储哈希值。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(strings: List[str]) -> bool:
    """
    函数式接口 - 检查字符串列表中是否有两个字符串只差一个字符
    """
    if not strings:
        return False

    n = len(strings)
    m = len(strings[0])
    base = 26
    mod = 10**9 + 7
    hash_values = [0] * n
    power = [1] * (m + 1)

    # 计算每个字符串的初始哈希值
    for i in range(n):
        for j in range(m):
            hash_values[i] = (hash_values[i] * base + (ord(strings[i][j]) - ord('a'))) % mod
        power[j + 1] = (power[j] * base) % mod

    # 生成所有可能的一个字符替换后的哈希值
    for i in range(n):
        for j in range(m):
            for k in range(base):
                new_char = (ord(strings[i][j]) - ord('a') + k) % base
                if new_char == (ord(strings[i][j]) - ord('a')):
                    continue
                new_hash = (hash_values[i] - (ord(strings[i][j]) - ord('a')) * power[m - j - 1] + new_char * power[m - j - 1]) % mod
                if new_hash in hash_values[:i]:
                    return True
            hash_values[i] = (hash_values[i] - (ord(strings[i][j]) - ord('a')) * power[m - j - 1]) % mod

    return False


Solution = create_solution(solution_function_name)