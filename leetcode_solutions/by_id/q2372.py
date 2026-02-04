# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2372
标题: Rearrange Characters to Make Target String
难度: easy
链接: https://leetcode.cn/problems/rearrange-characters-to-make-target-string/
题目类型: 哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2287. 重排字符形成目标字符串 - 给你两个下标从 0 开始的字符串 s 和 target 。你可以从 s 取出一些字符并将其重排，得到若干新的字符串。 从 s 中取出字符并重新排列，返回可以形成 target 的 最大 副本数。 示例 1： 输入：s = "ilovecodingonleetcode", target = "code" 输出：2 解释： 对于 "code" 的第 1 个副本，选取下标为 4 、5 、6 和 7 的字符。 对于 "code" 的第 2 个副本，选取下标为 17 、18 、19 和 20 的字符。 形成的字符串分别是 "ecod" 和 "code" ，都可以重排为 "code" 。 可以形成最多 2 个 "code" 的副本，所以返回 2 。 示例 2： 输入：s = "abcba", target = "abc" 输出：1 解释： 选取下标为 0 、1 和 2 的字符，可以形成 "abc" 的 1 个副本。 可以形成最多 1 个 "abc" 的副本，所以返回 1 。 注意，尽管下标 3 和 4 分别有额外的 'a' 和 'b' ，但不能重用下标 2 处的 'c' ，所以无法形成 "abc" 的第 2 个副本。 示例 3： 输入：s = "abbaccaddaeea", target = "aaaaa" 输出：1 解释： 选取下标为 0 、3 、6 、9 和 12 的字符，可以形成 "aaaaa" 的 1 个副本。 可以形成最多 1 个 "aaaaa" 的副本，所以返回 1 。 提示： * 1 <= s.length <= 100 * 1 <= target.length <= 10 * s 和 target 由小写英文字母组成 注意：本题与 1189. “气球” 的最大数量 [https://leetcode.cn/problems/maximum-number-of-balloons/] 相同。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表统计 `s` 和 `target` 中每个字符的出现次数，然后计算 `s` 中的字符能组成 `target` 的最大副本数。

算法步骤:
1. 统计 `s` 和 `target` 中每个字符的出现次数。
2. 计算 `s` 中的字符能组成 `target` 的最大副本数，即 `s` 中每个字符的出现次数除以 `target` 中该字符的出现次数，取最小值。

关键点:
- 使用 `collections.Counter` 来统计字符出现次数。
- 计算最大副本数时，需要考虑 `target` 中每个字符的出现次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 `s` 的长度，m 是 `target` 的长度。
空间复杂度: O(1)，因为字符集是固定的（26 个小写字母）。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from collections import Counter


def rearrange_characters(s: str, target: str) -> int:
    """
    函数式接口 - 返回可以形成 target 的最大副本数
    """
    # 统计 s 和 target 中每个字符的出现次数
    s_count = Counter(s)
    target_count = Counter(target)

    # 计算 s 中的字符能组成 target 的最大副本数
    max_copies = float('inf')
    for char in target_count:
        if char in s_count:
            max_copies = min(max_copies, s_count[char] // target_count[char])
        else:
            return 0

    return max_copies


Solution = create_solution(rearrange_characters)