# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2209
标题: Number of Equal Count Substrings
难度: medium
链接: https://leetcode.cn/problems/number-of-equal-count-substrings/
题目类型: 哈希表、字符串、计数、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2067. 等计数子串的数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和哈希表来统计子串中每个字符的出现次数，并检查是否所有字符的出现次数相等。

算法步骤:
1. 初始化两个指针 `left` 和 `right`，分别表示滑动窗口的左右边界。
2. 使用一个哈希表 `count` 来记录当前窗口内每个字符的出现次数。
3. 使用一个变量 `unique_chars` 来记录当前窗口内不同字符的数量。
4. 使用一个变量 `equal_count` 来记录当前窗口内每个字符的出现次数是否相等。
5. 移动右指针 `right`，扩展窗口，并更新 `count` 和 `unique_chars`。
6. 检查当前窗口内每个字符的出现次数是否相等，如果相等则增加结果计数。
7. 如果当前窗口内字符的出现次数不相等，移动左指针 `left`，缩小窗口，并更新 `count` 和 `unique_chars`。
8. 重复步骤 5-7，直到遍历完整个字符串。

关键点:
- 使用滑动窗口来动态调整子串的范围。
- 使用哈希表来高效统计字符的出现次数。
- 通过维护 `unique_chars` 和 `equal_count` 来快速判断当前窗口内字符的出现次数是否相等。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度。每个字符最多被处理两次（一次加入窗口，一次移出窗口）。
空间复杂度: O(1)，因为字符集是固定的（假设为 ASCII 字符集），所以哈希表的空间复杂度是常数级别的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_equal_count_substrings(s: str, k: int) -> int:
    """
    函数式接口 - 统计字符串 s 中字符出现次数相等且等于 k 的子串数量
    """
    def is_equal_count(count):
        return all(c == k for c in count.values())

    left = 0
    count = {}
    unique_chars = 0
    result = 0

    for right in range(len(s)):
        if s[right] in count:
            count[s[right]] += 1
        else:
            count[s[right]] = 1
            unique_chars += 1

        while len(s[left:right+1]) * unique_chars > k * unique_chars or not is_equal_count(count):
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
                unique_chars -= 1
            left += 1

        if is_equal_count(count):
            result += 1

    return result


Solution = create_solution(count_equal_count_substrings)