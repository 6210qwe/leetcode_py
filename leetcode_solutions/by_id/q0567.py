# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 567
标题: Permutation in String
难度: medium
链接: https://leetcode.cn/problems/permutation-in-string/
题目类型: 哈希表、双指针、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
567. 字符串的排列 - 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的 排列。如果是，返回 true ；否则，返回 false 。 换句话说，s1 的排列之一是 s2 的 子串 。 示例 1： 输入：s1 = "ab" s2 = "eidbaooo" 输出：true 解释：s2 包含 s1 的排列之一 ("ba"). 示例 2： 输入：s1= "ab" s2 = "eidboaoo" 输出：false 提示： * 1 <= s1.length, s2.length <= 104 * s1 和 s2 仅包含小写字母
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和哈希表来检查 s2 中是否存在 s1 的排列。

算法步骤:
1. 初始化两个哈希表 `count_s1` 和 `count_window` 分别记录 s1 和当前窗口的字符频率。
2. 初始化窗口的左右边界 `left` 和 `right`。
3. 移动右边界 `right`，扩展窗口，并更新 `count_window`。
4. 如果窗口大小等于 s1 的长度，比较 `count_s1` 和 `count_window`，如果相等则返回 True。
5. 移动左边界 `left`，收缩窗口，并更新 `count_window`。
6. 重复步骤 3-5 直到右边界到达 s2 的末尾。

关键点:
- 使用滑动窗口技术，保持窗口大小为 s1 的长度。
- 使用哈希表记录字符频率，快速比较两个字符串的字符频率是否相同。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 s2 的长度。每个字符最多被处理两次（一次加入窗口，一次移出窗口）。
空间复杂度: O(1)，因为字母表的大小是固定的（26 个小写字母），所以哈希表的空间复杂度是常数级别的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def check_inclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    count_s1 = [0] * 26
    count_window = [0] * 26

    for char in s1:
        count_s1[ord(char) - ord('a')] += 1

    left, right = 0, 0
    while right < len(s2):
        count_window[ord(s2[right]) - ord('a')] += 1

        if right - left + 1 == len(s1):
            if count_s1 == count_window:
                return True

            count_window[ord(s2[left]) - ord('a')] -= 1
            left += 1

        right += 1

    return False


Solution = create_solution(check_inclusion)