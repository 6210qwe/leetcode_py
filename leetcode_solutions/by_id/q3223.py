# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3223
标题: Count Complete Substrings
难度: hard
链接: https://leetcode.cn/problems/count-complete-substrings/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2953. 统计完全子字符串 - 给你一个字符串 word 和一个整数 k 。 如果 word 的一个子字符串 s 满足以下条件，我们称它是 完全字符串： * s 中每个字符 恰好 出现 k 次。 * 相邻字符在字母表中的顺序 至多 相差 2 。也就是说，s 中两个相邻字符 c1 和 c2 ，它们在字母表中的位置相差 至多 为 2 。 请你返回 word 中 完全 子字符串的数目。 子字符串 指的是一个字符串中一段连续 非空 的字符序列。 示例 1： 输入：word = "igigee", k = 2 输出：3 解释：完全子字符串需要满足每个字符恰好出现 2 次，且相邻字符相差至多为 2 ：igigee, igigee, igigee 。 示例 2： 输入：word = "aaabbbccc", k = 3 输出：6 解释：完全子字符串需要满足每个字符恰好出现 3 次，且相邻字符相差至多为 2 ：aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc 。 提示： * 1 <= word.length <= 105 * word 只包含小写英文字母。 * 1 <= k <= word.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和哈希表来统计符合条件的子字符串。

算法步骤:
1. 将字符串分割成多个子串，每个子串中的相邻字符在字母表中的顺序相差不超过2。
2. 对于每个子串，使用滑动窗口和哈希表来统计每个字符的出现次数。
3. 检查当前窗口内的字符是否都恰好出现k次，如果是，则计数加一。
4. 移动窗口，更新哈希表中的字符计数。

关键点:
- 分割字符串时，确保相邻字符在字母表中的顺序相差不超过2。
- 使用滑动窗口和哈希表来高效统计字符出现次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * 26 * k)，其中n是字符串的长度，26是字母表的大小，k是给定的整数。
空间复杂度: O(26) = O(1)，哈希表的大小最多为26。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def count_complete_substrings(word: str, k: int) -> int:
    def is_valid(a: str, b: str) -> bool:
        return abs(ord(a) - ord(b)) <= 2

    def count_substrings(s: str) -> int:
        n = len(s)
        result = 0
        for unique_chars in range(1, 27):
            if unique_chars * k > n:
                break
            count = [0] * 26
            left = 0
            for right in range(n):
                count[ord(s[right]) - ord('a')] += 1
                while (right - left + 1) > unique_chars * k or \
                      (right - left + 1) < unique_chars * k and min(count) == 0:
                    count[ord(s[left]) - ord('a')] -= 1
                    left += 1
                if (right - left + 1) == unique_chars * k and min(count) >= k:
                    result += 1
        return result

    segments = []
    current_segment = ""
    for i in range(len(word)):
        if i > 0 and not is_valid(word[i - 1], word[i]):
            segments.append(current_segment)
            current_segment = ""
        current_segment += word[i]
    segments.append(current_segment)

    total_count = sum(count_substrings(segment) for segment in segments)
    return total_count

Solution = create_solution(count_complete_substrings)