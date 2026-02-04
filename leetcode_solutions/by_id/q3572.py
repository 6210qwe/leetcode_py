# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3572
标题: Count Substrings That Can Be Rearranged to Contain a String II
难度: hard
链接: https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3298. 统计重新排列后包含另一个字符串的子字符串数目 II - 给你两个字符串 word1 和 word2 。 如果一个字符串 x 重新排列后，word2 是重排字符串的 前缀 ，那么我们称字符串 x 是 合法的 。 请你返回 word1 中 合法 子字符串 的数目。 注意 ，这个问题中的内存限制比其他题目要 小 ，所以你 必须 实现一个线性复杂度的解法。 示例 1： 输入：word1 = "bcca", word2 = "abc" 输出：1 解释： 唯一合法的子字符串是 "bcca" ，可以重新排列得到 "abcc" ，"abc" 是它的前缀。 示例 2： 输入：word1 = "abcabc", word2 = "abc" 输出：10 解释： 除了长度为 1 和 2 的所有子字符串都是合法的。 示例 3： 输入：word1 = "abcabc", word2 = "aaabc" 输出：0 解释： * 1 <= word1.length <= 106 * 1 <= word2.length <= 104 * word1 和 word2 都只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和哈希表来统计子字符串中字符的频率，并检查是否满足条件。

算法步骤:
1. 初始化两个哈希表，一个用于记录 word2 中每个字符的频率，另一个用于记录当前窗口中字符的频率。
2. 使用滑动窗口遍历 word1，维护一个窗口大小为 word2 长度的子字符串。
3. 在每次滑动时，更新窗口中字符的频率，并检查当前窗口是否满足条件。
4. 如果满足条件，则增加计数器。

关键点:
- 使用滑动窗口和哈希表来高效地统计和检查字符频率。
- 确保窗口大小始终为 word2 的长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)（因为字母表大小固定为 26）
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_valid_substrings(word1: str, word2: str) -> int:
    """
    函数式接口 - 计算 word1 中合法子字符串的数目
    """
    n, m = len(word1), len(word2)
    if m > n:
        return 0

    # 记录 word2 中每个字符的频率
    target_freq = [0] * 26
    for char in word2:
        target_freq[ord(char) - ord('a')] += 1

    # 初始化窗口
    window_freq = [0] * 26
    for i in range(m):
        window_freq[ord(word1[i]) - ord('a')] += 1

    count = 1 if window_freq == target_freq else 0

    # 滑动窗口
    for i in range(m, n):
        window_freq[ord(word1[i]) - ord('a')] += 1
        window_freq[ord(word1[i - m]) - ord('a')] -= 1
        if window_freq == target_freq:
            count += 1

    return count


Solution = create_solution(count_valid_substrings)