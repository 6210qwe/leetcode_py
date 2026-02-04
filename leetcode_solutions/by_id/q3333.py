# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3333
标题: Find Pattern in Infinite Stream I
难度: medium
链接: https://leetcode.cn/problems/find-pattern-in-infinite-stream-i/
题目类型: 数组、字符串匹配、滑动窗口、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3023. 在无限流中寻找模式 I - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Rabin-Karp 算法进行字符串匹配。通过滚动哈希来实现高效的模式匹配。

算法步骤:
1. 计算模式串的哈希值。
2. 初始化一个滑动窗口，计算初始窗口的哈希值。
3. 滑动窗口逐个字符移动，更新哈希值，并与模式串的哈希值进行比较。
4. 如果哈希值相等且字符串匹配成功，则返回匹配位置；否则继续滑动。

关键点:
- 使用滚动哈希来减少重复计算，提高效率。
- 选择合适的哈希函数和模数以避免哈希冲突。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是流的长度，m 是模式串的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def rabin_karp_search(stream: str, pattern: str) -> int:
    """
    使用 Rabin-Karp 算法在无限流中寻找模式串。
    
    :param stream: 无限流（假设为一个很长的字符串）
    :param pattern: 模式串
    :return: 模式串在流中的起始位置，如果不存在则返回 -1
    """
    if not pattern or not stream:
        return -1

    base = 256  # 基数
    prime = 101  # 模数
    pattern_len = len(pattern)
    stream_len = len(stream)
    pattern_hash = 0
    window_hash = 0
    h = 1

    # 计算模式串的哈希值和 h 的值
    for i in range(pattern_len):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        h = (h * base) % prime

    # 计算初始窗口的哈希值
    for i in range(pattern_len):
        window_hash = (base * window_hash + ord(stream[i])) % prime

    # 滑动窗口逐个字符移动
    for i in range(stream_len - pattern_len + 1):
        if pattern_hash == window_hash:
            # 检查字符串是否真的匹配
            if stream[i:i+pattern_len] == pattern:
                return i
        if i < stream_len - pattern_len:
            # 更新窗口哈希值
            window_hash = (base * (window_hash - ord(stream[i]) * h) + ord(stream[i + pattern_len])) % prime
            if window_hash < 0:
                window_hash += prime

    return -1

Solution = create_solution(rabin_karp_search)