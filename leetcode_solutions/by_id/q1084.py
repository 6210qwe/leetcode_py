# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1084
标题: Find K-Length Substrings With No Repeated Characters
难度: medium
链接: https://leetcode.cn/problems/find-k-length-substrings-with-no-repeated-characters/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1100. 长度为 K 的无重复字符子串 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和哈希表来检查长度为 K 的子串是否有重复字符。

算法步骤:
1. 初始化一个哈希表 `char_count` 来记录当前窗口内每个字符的出现次数。
2. 使用两个指针 `left` 和 `right` 来表示滑动窗口的左右边界。
3. 移动 `right` 指针扩展窗口，并更新 `char_count`。
4. 如果窗口内的字符数超过 K 或者某个字符出现多次，则移动 `left` 指针缩小窗口，直到窗口内的字符数不超过 K 且没有重复字符。
5. 如果窗口大小正好为 K 且没有重复字符，则计数器加一。
6. 重复步骤 3-5 直到 `right` 指针到达字符串末尾。

关键点:
- 使用滑动窗口和哈希表来高效地检查子串是否有重复字符。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度。每个字符最多被访问两次（一次通过 `right` 指针，一次通过 `left` 指针）。
空间复杂度: O(min(n, k))，哈希表的空间复杂度取决于窗口大小 K 和字符集的大小。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(s: str, k: int) -> int:
    """
    函数式接口 - 计算字符串 s 中长度为 K 的无重复字符子串的数量
    """
    if k > len(s):
        return 0

    char_count = {}
    left = 0
    count = 0

    for right in range(len(s)):
        if s[right] in char_count:
            char_count[s[right]] += 1
        else:
            char_count[s[right]] = 1

        while char_count[s[right]] > 1 or (right - left + 1) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        if (right - left + 1) == k:
            count += 1

    return count


Solution = create_solution(solution_function_name)