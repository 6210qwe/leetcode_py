# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2303
标题: Unique Substrings With Equal Digit Frequency
难度: medium
链接: https://leetcode.cn/problems/unique-substrings-with-equal-digit-frequency/
题目类型: 哈希表、字符串、计数、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2168. 每个数字的频率都相同的独特子字符串的数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和计数器来找到所有满足条件的子字符串。

算法步骤:
1. 初始化一个计数器 `counter` 来记录当前窗口内每个数字的频率。
2. 使用两个指针 `left` 和 `right` 来表示滑动窗口的左右边界。
3. 移动右指针 `right` 扩展窗口，更新计数器 `counter`。
4. 如果当前窗口内的所有数字频率相同且不为零，则将该子字符串加入集合 `seen`。
5. 如果当前窗口内的数字频率不再相同或某个数字频率为零，则移动左指针 `left` 缩小窗口，更新计数器 `counter`。
6. 最后返回集合 `seen` 的大小。

关键点:
- 使用滑动窗口和计数器来高效地找到所有满足条件的子字符串。
- 通过集合 `seen` 来去重，确保每个子字符串都是唯一的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - 在最坏情况下，每个子字符串都需要检查其频率。
空间复杂度: O(n) - 计数器和集合 `seen` 的空间开销。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def unique_substrings_with_equal_digit_frequency(s: str) -> int:
    """
    函数式接口 - 返回每个数字的频率都相同的独特子字符串的数量
    """
    def is_valid(counter):
        if not counter:
            return False
        freq = list(counter.values())
        return min(freq) == max(freq)

    n = len(s)
    seen = set()

    for left in range(n):
        counter = {}
        for right in range(left, n):
            digit = s[right]
            counter[digit] = counter.get(digit, 0) + 1
            if is_valid(counter):
                seen.add(s[left:right+1])

    return len(seen)


Solution = create_solution(unique_substrings_with_equal_digit_frequency)