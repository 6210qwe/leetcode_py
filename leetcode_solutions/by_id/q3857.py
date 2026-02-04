# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3857
标题: Find Maximum Number of Non Intersecting Substrings
难度: medium
链接: https://leetcode.cn/problems/find-maximum-number-of-non-intersecting-substrings/
题目类型: 贪心、哈希表、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3557. 不相交子字符串的最大数量 - 给你一个字符串 word。 返回以 首尾字母相同 且 长度至少为 4 的 不相交子字符串 的最大数量。 子字符串 是字符串中连续的 非空 字符序列。 示例 1： 输入： word = "abcdeafdef" 输出： 2 解释： 两个子字符串是 "abcdea" 和 "fdef"。 示例 2： 输入： word = "bcdaaaab" 输出： 1 解释： 唯一的子字符串是 "aaaa"。注意我们 不能 同时选择 "bcdaaaab"，因为它和另一个子字符串有重叠。 提示： * 1 <= word.length <= 2 * 105 * word 仅由小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和双指针来找到所有符合条件的子字符串，并使用动态规划来记录每个位置的最大不相交子字符串数量。

算法步骤:
1. 初始化两个数组 `left` 和 `right`，分别记录每个字符从左到右和从右到左的第一个和最后一个出现位置。
2. 遍历字符串，填充 `left` 和 `right` 数组。
3. 使用动态规划数组 `dp` 来记录每个位置的最大不相交子字符串数量。
4. 遍历字符串，对于每个字符，检查其左侧和右侧的相同字符位置，更新 `dp` 数组。
5. 最终结果为 `dp` 数组中的最大值。

关键点:
- 使用 `left` 和 `right` 数组快速找到每个字符的边界位置。
- 使用动态规划来记录每个位置的最大不相交子字符串数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度。我们需要遍历字符串几次，但每次都是线性时间。
空间复杂度: O(n)，用于存储 `left`、`right` 和 `dp` 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_non_intersecting_substrings(word: str) -> int:
    """
    函数式接口 - 返回以首尾字母相同且长度至少为4的不相交子字符串的最大数量
    """
    n = len(word)
    if n < 4:
        return 0

    # 初始化 left 和 right 数组
    left = [-1] * 26
    right = [-1] * 26
    for i in range(n):
        char_idx = ord(word[i]) - ord('a')
        if left[char_idx] == -1:
            left[char_idx] = i
        right[char_idx] = i

    # 初始化 dp 数组
    dp = [0] * (n + 1)

    # 遍历字符串，更新 dp 数组
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        char_idx = ord(word[i - 1]) - ord('a')
        if i - left[char_idx] >= 4:
            dp[i] = max(dp[i], dp[left[char_idx]] + 1)
        if right[char_idx] - i + 1 >= 4:
            dp[i] = max(dp[i], dp[i - 1] + 1)

    return dp[n]


Solution = create_solution(max_non_intersecting_substrings)