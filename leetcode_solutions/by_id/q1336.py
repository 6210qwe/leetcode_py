# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1336
标题: Maximum Product of the Length of Two Palindromic Substrings
难度: hard
链接: https://leetcode.cn/problems/maximum-product-of-the-length-of-two-palindromic-substrings/
题目类型: 字符串、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1960. 两个回文子字符串长度的最大乘积 - 给你一个下标从 0 开始的字符串 s ，你需要找到两个 不重叠的回文 子字符串，它们的长度都必须为 奇数 ，使得它们长度的乘积最大。 更正式地，你想要选择四个整数 i ，j ，k ，l ，使得 0 <= i <= j < k <= l < s.length ，且子字符串 s[i...j] 和 s[k...l] 都是回文串且长度为奇数。s[i...j] 表示下标从 i 到 j 且 包含 两端下标的子字符串。 请你返回两个不重叠回文子字符串长度的 最大 乘积。 回文字符串 指的是一个从前往后读和从后往前读一模一样的字符串。子字符串 指的是一个字符串中一段连续字符。 示例 1： 输入：s = "ababbb" 输出：9 解释：子字符串 "aba" 和 "bbb" 为奇数长度的回文串。乘积为 3 * 3 = 9 。 示例 2： 输入：s = "zaaaxbbby" 输出：9 解释：子字符串 "aaa" 和 "bbb" 为奇数长度的回文串。乘积为 3 * 3 = 9 。 提示： * 2 <= s.length <= 105 * s 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用马拉车算法（Manacher's Algorithm）来找到所有奇数长度的回文子串，并记录每个位置的最长回文子串长度。然后使用动态规划来计算两个不重叠回文子串的最大乘积。

算法步骤:
1. 使用马拉车算法预处理字符串，得到每个位置的最长奇数长度回文子串半径。
2. 通过预处理结果，构建前缀最大值数组和后缀最大值数组，分别记录每个位置之前和之后的最长奇数长度回文子串长度。
3. 使用动态规划计算两个不重叠回文子串的最大乘积。

关键点:
- 马拉车算法可以在 O(n) 时间内找到所有奇数长度的回文子串。
- 动态规划用于计算两个不重叠回文子串的最大乘积。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def manacher(s: str) -> List[int]:
    n = len(s)
    s = '#' + '#'.join(s) + '#'
    p = [0] * (2 * n + 1)
    center, right = 0, 0
    for i in range(2 * n + 1):
        if i < right:
            p[i] = min(right - i, p[2 * center - i])
        while i - p[i] - 1 >= 0 and i + p[i] + 1 < 2 * n + 1 and s[i - p[i] - 1] == s[i + p[i] + 1]:
            p[i] += 1
        if i + p[i] > right:
            center, right = i, i + p[i]
    return p


def max_product_of_palindromic_substrings(s: str) -> int:
    n = len(s)
    p = manacher(s)
    max_len_left = [0] * n
    max_len_right = [0] * n

    # 构建前缀最大值数组
    for i in range(n):
        max_len_left[i] = max(max_len_left[i - 1], p[2 * i + 1]) if i > 0 else p[1]

    # 构建后缀最大值数组
    for i in range(n - 1, -1, -1):
        max_len_right[i] = max(max_len_right[i + 1], p[2 * i + 1]) if i < n - 1 else p[2 * n - 1]

    # 计算最大乘积
    max_product = 0
    for i in range(n - 1):
        max_product = max(max_product, max_len_left[i] * max_len_right[i + 1])

    return max_product


Solution = create_solution(max_product_of_palindromic_substrings)