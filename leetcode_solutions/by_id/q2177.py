# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2177
标题: Check Whether Two Strings are Almost Equivalent
难度: easy
链接: https://leetcode.cn/problems/check-whether-two-strings-are-almost-equivalent/
题目类型: 哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2068. 检查两个字符串是否几乎相等 - 如果两个字符串 word1 和 word2 中从 'a' 到 'z' 每一个字母出现频率之差都 不超过 3 ，那么我们称这两个字符串 word1 和 word2 几乎相等 。 给你两个长度都为 n 的字符串 word1 和 word2 ，如果 word1 和 word2 几乎相等 ，请你返回 true ，否则返回 false 。 一个字母 x 的出现 频率 指的是它在字符串中出现的次数。 示例 1： 输入：word1 = "aaaa", word2 = "bccb" 输出：false 解释：字符串 "aaaa" 中有 4 个 'a' ，但是 "bccb" 中有 0 个 'a' 。 两者之差为 4 ，大于上限 3 。 示例 2： 输入：word1 = "abcdeef", word2 = "abaaacc" 输出：true 解释：word1 和 word2 中每个字母出现频率之差至多为 3 ： - 'a' 在 word1 中出现了 1 次，在 word2 中出现了 4 次，差为 3 。 - 'b' 在 word1 中出现了 1 次，在 word2 中出现了 1 次，差为 0 。 - 'c' 在 word1 中出现了 1 次，在 word2 中出现了 2 次，差为 1 。 - 'd' 在 word1 中出现了 1 次，在 word2 中出现了 0 次，差为 1 。 - 'e' 在 word1 中出现了 2 次，在 word2 中出现了 0 次，差为 2 。 - 'f' 在 word1 中出现了 1 次，在 word2 中出现了 0 次，差为 1 。 示例 3： 输入：word1 = "cccddabba", word2 = "babababab" 输出：true 解释：word1 和 word2 中每个字母出现频率之差至多为 3 ： - 'a' 在 word1 中出现了 2 次，在 word2 中出现了 4 次，差为 2 。 - 'b' 在 word1 中出现了 2 次，在 word2 中出现了 5 次，差为 3 。 - 'c' 在 word1 中出现了 3 次，在 word2 中出现了 0 次，差为 3 。 - 'd' 在 word1 中出现了 2 次，在 word2 中出现了 0 次，差为 2 。 提示： * n == word1.length == word2.length * 1 <= n <= 100 * word1 和 word2 都只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个字母的频率差，检查频率差是否不超过 3。

算法步骤:
1. 初始化一个长度为 26 的数组，用于记录每个字母的频率差。
2. 遍历 word1 和 word2，更新频率差数组。
3. 检查频率差数组中的每个值是否都不超过 3。

关键点:
- 使用固定大小的数组来记录频率差，避免了动态分配和查找操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度。我们需要遍历每个字符一次。
空间复杂度: O(1)，因为频率差数组的大小是固定的 26。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def check_almost_equivalent(word1: str, word2: str) -> bool:
    """
    检查两个字符串是否几乎相等。
    """
    # 初始化频率差数组
    freq_diff = [0] * 26

    # 更新频率差数组
    for char in word1:
        freq_diff[ord(char) - ord('a')] += 1
    for char in word2:
        freq_diff[ord(char) - ord('a')] -= 1

    # 检查频率差是否不超过 3
    for diff in freq_diff:
        if abs(diff) > 3:
            return False

    return True


Solution = create_solution(check_almost_equivalent)