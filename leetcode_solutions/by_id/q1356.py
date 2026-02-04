# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1356
标题: Minimum Number of Moves to Make Palindrome
难度: hard
链接: https://leetcode.cn/problems/minimum-number-of-moves-to-make-palindrome/
题目类型: 贪心、树状数组、双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2193. 得到回文串的最少操作次数 - 给你一个只包含小写英文字母的字符串 s 。 每一次 操作 ，你可以选择 s 中两个 相邻 的字符，并将它们交换。 请你返回将 s 变成回文串的 最少操作次数 。 注意 ，输入数据会确保 s 一定能变成一个回文串。 示例 1： 输入：s = "aabb" 输出：2 解释： 我们可以将 s 变成 2 个回文串，"abba" 和 "baab" 。 - 我们可以通过 2 次操作得到 "abba" ："aabb" -> "abab" -> "abba" 。 - 我们可以通过 2 次操作得到 "baab" ："aabb" -> "abab" -> "baab" 。 因此，得到回文串的最少总操作次数为 2 。 示例 2： 输入：s = "letelt" 输出：2 解释： 通过 2 次操作从 s 能得到回文串 "lettel" 。 其中一种方法是："letelt" -> "letetl" -> "lettel" 。 其他回文串比方说 "tleelt" 也可以通过 2 次操作得到。 可以证明少于 2 次操作，无法得到回文串。 提示： * 1 <= s.length <= 2000 * s 只包含小写英文字母。 * s 可以通过有限次操作得到一个回文串。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和双指针来找到需要移动的字符，并计算最少的操作次数。

算法步骤:
1. 初始化左右指针 `left` 和 `right`，分别指向字符串的开头和结尾。
2. 找到 `left` 和 `right` 指向的字符相同的位置，如果找不到，则将 `right` 指向的字符移到合适的位置。
3. 计算移动次数并更新指针位置。
4. 重复上述步骤直到 `left` 和 `right` 相遇。

关键点:
- 通过双指针找到需要移动的字符，并计算最少的操作次数。
- 使用贪心算法确保每次移动都是最优的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是字符串的长度。最坏情况下，每次移动都需要遍历剩余的字符。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_moves_to_palindrome(s: str) -> int:
    """
    函数式接口 - 返回将 s 变成回文串的最少操作次数
    """
    def find_next_char(s: str, start: int, end: int, char: str) -> int:
        for i in range(end, start - 1, -1):
            if s[i] == char:
                return i
        return -1

    n = len(s)
    moves = 0
    left, right = 0, n - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            next_right = find_next_char(s, left, right, s[left])
            if next_right == -1:
                # 如果找不到相同的字符，说明已经处理完所有字符
                break
            else:
                # 将 right 指向的字符移到合适的位置
                for j in range(next_right, right):
                    s = s[:j] + s[j + 1] + s[j] + s[j + 2:]
                    moves += 1
                right -= 1

    return moves


Solution = create_solution(min_moves_to_palindrome)