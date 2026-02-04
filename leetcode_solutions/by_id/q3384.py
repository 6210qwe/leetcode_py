# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3384
标题: Minimum Number of Operations to Make Word K-Periodic
难度: medium
链接: https://leetcode.cn/problems/minimum-number-of-operations-to-make-word-k-periodic/
题目类型: 哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3137. K 周期字符串需要的最少操作次数 - 给你一个长度为 n 的字符串 word 和一个整数 k ，其中 k 是 n 的因数。 在一次操作中，你可以选择任意两个下标 i 和 j，其中 0 <= i, j < n ，且这两个下标都可以被 k 整除，然后用从 j 开始的长度为 k 的子串替换从 i 开始的长度为 k 的子串。也就是说，将子串 word[i..i + k - 1] 替换为子串 word[j..j + k - 1] 。 返回使 word 成为 K 周期字符串 所需的 最少 操作次数。 如果存在某个长度为 k 的字符串 s，使得 word 可以表示为任意次数连接 s ，则称字符串 word 是 K 周期字符串 。例如，如果 word == "ababab"，那么 word 就是 s = "ab" 时的 2 周期字符串 。 示例 1： 输入：word = "leetcodeleet", k = 4 输出：1 解释：可以选择 i = 4 和 j = 0 获得一个 4 周期字符串。这次操作后，word 变为 "leetleetleet" 。 示例 2： 输入：word = "leetcoleet", k = 2 输出：3 解释：可以执行以下操作获得一个 2 周期字符串。 i j word 0 2 etetcoleet 4 0 etetetleet 6 0 etetetetet 提示： * 1 <= n == word.length <= 105 * 1 <= k <= word.length * k 能整除 word.length 。 * word 仅由小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个周期子串的出现频率，并计算最少的操作次数。

算法步骤:
1. 将字符串分割成长度为 k 的子串。
2. 使用哈希表记录每个子串的出现频率。
3. 找出出现频率最高的子串。
4. 计算将所有子串变成出现频率最高的子串所需的最少操作次数。

关键点:
- 使用哈希表记录子串的频率。
- 计算最少操作次数时，只需考虑将其他子串变成出现频率最高的子串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(k)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_operations_to_make_word_k_periodic(word: str, k: int) -> int:
    """
    函数式接口 - 计算使 word 成为 K 周期字符串所需的最少操作次数
    """
    # 将字符串分割成长度为 k 的子串
    subwords = [word[i:i+k] for i in range(0, len(word), k)]
    
    # 使用哈希表记录每个子串的出现频率
    freq = {}
    for subword in subwords:
        if subword in freq:
            freq[subword] += 1
        else:
            freq[subword] = 1
    
    # 找出出现频率最高的子串
    max_freq = max(freq.values())
    
    # 计算最少操作次数
    min_operations = len(subwords) - max_freq
    
    return min_operations


Solution = create_solution(min_operations_to_make_word_k_periodic)