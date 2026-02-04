# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 424
标题: Longest Repeating Character Replacement
难度: medium
链接: https://leetcode.cn/problems/longest-repeating-character-replacement/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
424. 替换后的最长重复字符 - 给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。 在执行上述操作后，返回 包含相同字母的最长子字符串的长度。 示例 1： 输入：s = "ABAB", k = 2 输出：4 解释：用两个'A'替换为两个'B',反之亦然。 示例 2： 输入：s = "AABABBA", k = 1 输出：4 解释： 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。 子串 "BBBB" 有最长重复字母, 答案为 4。 可能存在其他的方法来得到同样的结果。 提示： * 1 <= s.length <= 105 * s 仅由大写英文字母组成 * 0 <= k <= s.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和哈希表来解决问题

算法步骤:
1. 初始化左右指针 l 和 r，以及一个计数器 count 用于记录当前窗口内每个字符的出现次数。
2. 扩展右指针 r，同时更新计数器 count。
3. 如果当前窗口的长度减去窗口内出现次数最多的字符的数量大于 k，则收缩左指针 l。
4. 更新最大长度 res。

关键点:
- 使用滑动窗口技术，确保在 O(n) 时间复杂度内解决问题。
- 使用哈希表记录字符出现次数，方便快速查找和更新。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 每个字符最多被处理两次（一次通过右指针，一次通过左指针）。
空间复杂度: O(1) - 计数器 count 的大小固定为 26（大写字母的数量），因此是常数级别的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_repeating_character_replacement(s: str, k: int) -> int:
    """
    函数式接口 - 返回包含相同字母的最长子字符串的长度

    实现思路:
    使用滑动窗口和哈希表来解决问题

    Args:
        s (str): 输入字符串
        k (int): 最多可以进行的替换次数

    Returns:
        int: 包含相同字母的最长子字符串的长度

    Example:
        >>> longest_repeating_character_replacement("ABAB", 2)
        4
        >>> longest_repeating_character_replacement("AABABBA", 1)
        4
    """
    count = {}
    l = 0
    max_count = 0
    res = 0
    
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        max_count = max(max_count, count[s[r]])
        
        if (r - l + 1) - max_count > k:
            count[s[l]] -= 1
            l += 1
        
        res = max(res, r - l + 1)
    
    return res


# 自动生成Solution类（无需手动编写）
Solution = create_solution(longest_repeating_character_replacement)