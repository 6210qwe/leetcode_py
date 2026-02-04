# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3352
标题: Find Pattern in Infinite Stream II
难度: hard
链接: https://leetcode.cn/problems/find-pattern-in-infinite-stream-ii/
题目类型: 数组、字符串匹配、滑动窗口、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3037. 在无限流中寻找模式 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滚动哈希（Rabin-Karp 算法）来在无限流中查找模式。

算法步骤:
1. 计算模式串的哈希值。
2. 使用滑动窗口在无限流中计算子串的哈希值，并与模式串的哈希值进行比较。
3. 如果哈希值匹配，则进一步验证子串是否与模式串完全相同。
4. 如果找到匹配的子串，返回其起始位置；否则继续滑动窗口。

关键点:
- 使用滚动哈希可以高效地计算子串的哈希值。
- 滑动窗口技术可以在无限流中逐步检查每个子串。
- 通过哈希值初步匹配，再进行精确匹配，可以减少不必要的比较。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m) 其中 n 是无限流的长度，m 是模式串的长度。实际操作中，我们只需要处理有限长度的流。
空间复杂度: O(1) 除了固定的几个变量外，不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_pattern_in_stream(stream: str, pattern: str) -> int:
    """
    在无限流中查找模式串的位置。

    :param stream: 无限流字符串
    :param pattern: 模式串
    :return: 模式串在无限流中的起始位置，如果不存在则返回 -1
    """
    if not pattern:
        return -1

    base = 256  # 基数
    prime = 101  # 一个大素数
    m = len(pattern)
    n = len(stream)
    p_hash = 0  # 模式串的哈希值
    s_hash = 0  # 当前窗口的哈希值
    h = 1  # 最高位的权重

    # 计算最高位的权重
    for i in range(m - 1):
        h = (h * base) % prime

    # 计算模式串和第一个窗口的哈希值
    for i in range(m):
        p_hash = (base * p_hash + ord(pattern[i])) % prime
        s_hash = (base * s_hash + ord(stream[i])) % prime

    # 滑动窗口
    for i in range(n - m + 1):
        # 如果哈希值匹配，进一步验证
        if p_hash == s_hash:
            if stream[i:i + m] == pattern:
                return i

        # 计算下一个窗口的哈希值
        if i < n - m:
            s_hash = (base * (s_hash - ord(stream[i]) * h) + ord(stream[i + m])) % prime
            if s_hash < 0:
                s_hash += prime

    return -1


Solution = create_solution(find_pattern_in_stream)