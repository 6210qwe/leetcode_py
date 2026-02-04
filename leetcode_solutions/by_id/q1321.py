# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1321
标题: Get Equal Substrings Within Budget
难度: medium
链接: https://leetcode.cn/problems/get-equal-substrings-within-budget/
题目类型: 字符串、二分查找、前缀和、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1208. 尽可能使字符串相等 - 给你两个长度相同的字符串，s 和 t。 将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。 用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。 如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。 如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。 示例 1： 输入：s = "abcd", t = "bcdf", maxCost = 3 输出：3 解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。 示例 2： 输入：s = "abcd", t = "cdef", maxCost = 3 输出：1 解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。 示例 3： 输入：s = "abcd", t = "acde", maxCost = 0 输出：1 解释：a -> a, cost = 0，字符串未发生变化，所以最大长度为 1。 提示： * 1 <= s.length, t.length <= 10^5 * 0 <= maxCost <= 10^6 * s 和 t 都只含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到最长的子字符串，使得转换成本不超过 maxCost。

算法步骤:
1. 初始化两个指针 left 和 right 以及当前的成本 current_cost。
2. 使用 right 指针扩展窗口，计算当前字符的转换成本并累加到 current_cost。
3. 如果 current_cost 超过 maxCost，移动 left 指针缩小窗口，直到 current_cost 不超过 maxCost。
4. 在每次调整窗口后，更新最大长度。

关键点:
- 使用滑动窗口技术，确保时间复杂度为 O(n)。
- 通过维护当前窗口的成本，动态调整窗口大小。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def equal_substring(s: str, t: str, maxCost: int) -> int:
    """
    函数式接口 - 返回可以转化的最大长度
    """
    n = len(s)
    left, right, current_cost, max_length = 0, 0, 0, 0
    
    while right < n:
        current_cost += abs(ord(s[right]) - ord(t[right]))
        
        while current_cost > maxCost:
            current_cost -= abs(ord(s[left]) - ord(t[left]))
            left += 1
        
        max_length = max(max_length, right - left + 1)
        right += 1
    
    return max_length


Solution = create_solution(equal_substring)