# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3346
标题: Lexicographically Smallest String After Operations With Constraint
难度: medium
链接: https://leetcode.cn/problems/lexicographically-smallest-string-after-operations-with-constraint/
题目类型: 贪心、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3106. 满足距离约束且字典序最小的字符串 - 给你一个字符串 s 和一个整数 k 。 定义函数 distance(s1, s2) ，用于衡量两个长度为 n 的字符串 s1 和 s2 之间的距离，即： * 字符 'a' 到 'z' 按 循环 顺序排列，对于区间 [0, n - 1] 中的 i ，计算所有「 s1[i] 和 s2[i] 之间 最小距离」的 和 。 例如，distance("ab", "cd") == 4 ，且 distance("a", "z") == 1 。 你可以对字符串 s 执行 任意次 操作。在每次操作中，可以将 s 中的一个字母 改变 为 任意 其他小写英文字母。 返回一个字符串，表示在执行一些操作后你可以得到的 字典序最小 的字符串 t ，且满足 distance(s, t) <= k 。 示例 1： 输入：s = "zbbz", k = 3 输出："aaaz" 解释：在这个例子中，可以执行以下操作： 将 s[0] 改为 'a' ，s 变为 "abbz" 。 将 s[1] 改为 'a' ，s 变为 "aabz" 。 将 s[2] 改为 'a' ，s 变为 "aaaz" 。 "zbbz" 和 "aaaz" 之间的距离等于 k = 3 。 可以证明 "aaaz" 是在任意次操作后能够得到的字典序最小的字符串。 因此，答案是 "aaaz" 。 示例 2： 输入：s = "xaxcd", k = 4 输出："aawcd" 解释：在这个例子中，可以执行以下操作： 将 s[0] 改为 'a' ，s 变为 "aaxcd" 。 将 s[2] 改为 'w' ，s 变为 "aawcd" 。 "xaxcd" 和 "aawcd" 之间的距离等于 k = 4 。 可以证明 "aawcd" 是在任意次操作后能够得到的字典序最小的字符串。 因此，答案是 "aawcd" 。 示例 3： 输入：s = "lol", k = 0 输出："lol" 解释：在这个例子中，k = 0，更改任何字符都会使得距离大于 0 。 因此，答案是 "lol" 。 提示： * 1 <= s.length <= 100 * 0 <= k <= 2000 * s 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，尽量将每个字符改为尽可能小的字符，同时保证距离不超过 k。

算法步骤:
1. 遍历字符串 s 的每个字符。
2. 对于每个字符，尝试将其改为从 'a' 到当前字符的前一个字符，选择使距离最小且总距离不超过 k 的字符。
3. 如果当前字符已经是最小字符，则跳过该字符。
4. 更新剩余的 k 值。
5. 返回最终的字符串。

关键点:
- 使用循环字符距离计算。
- 确保每次操作后的总距离不超过 k。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * 26)，其中 n 是字符串 s 的长度。最坏情况下，每个字符都需要遍历 26 个可能的字符。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def smallest_string_with_distance(s: str, k: int) -> str:
    """
    函数式接口 - 返回满足距离约束且字典序最小的字符串
    """
    def char_distance(c1: str, c2: str) -> int:
        """计算两个字符之间的循环距离"""
        return min(abs(ord(c1) - ord(c2)), 26 - abs(ord(c1) - ord(c2)))

    result = list(s)
    for i in range(len(s)):
        for new_char in 'abcdefghijklmnopqrstuvwxyz':
            if new_char >= s[i]:
                break
            dist = char_distance(s[i], new_char)
            if dist <= k:
                result[i] = new_char
                k -= dist
                break
    return ''.join(result)


Solution = create_solution(smallest_string_with_distance)