# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3266
标题: Find Longest Special Substring That Occurs Thrice II
难度: medium
链接: https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii/
题目类型: 哈希表、字符串、二分查找、计数、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2982. 找出出现至少三次的最长特殊子字符串 II - 给你一个仅由小写英文字母组成的字符串 s 。 如果一个字符串仅由单一字符组成，那么它被称为 特殊 字符串。例如，字符串 "abc" 不是特殊字符串，而字符串 "ddd"、"zz" 和 "f" 是特殊字符串。 返回在 s 中出现 至少三次 的 最长特殊子字符串 的长度，如果不存在出现至少三次的特殊子字符串，则返回 -1 。 子字符串 是字符串中的一个连续 非空 字符序列。 示例 1： 输入：s = "aaaa" 输出：2 解释：出现三次的最长特殊子字符串是 "aa" ：子字符串 "aaaa"、"aaaa" 和 "aaaa"。 可以证明最大长度是 2 。 示例 2： 输入：s = "abcdef" 输出：-1 解释：不存在出现至少三次的特殊子字符串。因此返回 -1 。 示例 3： 输入：s = "abcaba" 输出：1 解释：出现三次的最长特殊子字符串是 "a" ：子字符串 "abcaba"、"abcaba" 和 "abcaba"。 可以证明最大长度是 1 。 提示： * 3 <= s.length <= 5 * 105 * s 仅由小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找和滑动窗口来找到最长的特殊子字符串。

算法步骤:
1. 使用二分查找来确定最长的特殊子字符串的长度。
2. 对于每个长度，使用滑动窗口来检查是否存在至少三个这样的子字符串。
3. 如果存在，更新结果；否则，减少长度继续查找。

关键点:
- 二分查找用于快速确定可能的最长长度。
- 滑动窗口用于高效地检查子字符串的存在性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是字符串 s 的长度。二分查找的时间复杂度是 O(log n)，每次检查的时间复杂度是 O(n)。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_longest_special_substring(s: str) -> int:
    def is_valid(length: int) -> bool:
        count = defaultdict(int)
        left = 0
        for right in range(len(s)):
            if right - left + 1 == length:
                if s[left:right + 1] == s[left] * length:
                    count[s[left]] += 1
                left += 1
        return any(c >= 3 for c in count.values())

    left, right = 1, len(s) // 3
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


Solution = create_solution(find_longest_special_substring)