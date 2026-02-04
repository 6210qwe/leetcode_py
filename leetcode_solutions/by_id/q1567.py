# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1567
标题: Maximum Number of Vowels in a Substring of Given Length
难度: medium
链接: https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
题目类型: 字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1456. 定长子串中元音的最大数目 - 给你字符串 s 和整数 k 。 请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。 英文中的 元音字母 为（a, e, i, o, u）。 示例 1： 输入：s = "abciiidef", k = 3 输出：3 解释：子字符串 "iii" 包含 3 个元音字母。 示例 2： 输入：s = "aeiou", k = 2 输出：2 解释：任意长度为 2 的子字符串都包含 2 个元音字母。 示例 3： 输入：s = "leetcode", k = 3 输出：2 解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。 示例 4： 输入：s = "rhythms", k = 4 输出：0 解释：字符串 s 中不含任何元音字母。 示例 5： 输入：s = "tryhard", k = 4 输出：1 提示： * 1 <= s.length <= 10^5 * s 由小写英文字母组成 * 1 <= k <= s.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来计算每个长度为 k 的子字符串中的元音字母数量。

算法步骤:
1. 初始化一个集合，包含所有元音字母。
2. 初始化两个指针 left 和 right，以及一个计数器 count 来记录当前窗口中的元音字母数量。
3. 遍历字符串 s，右指针 right 从 0 到 n-1：
   - 如果右指针指向的字符是元音字母，则增加计数器 count。
   - 如果右指针和左指针之间的距离大于等于 k，则移动左指针，并根据左指针指向的字符是否是元音字母来更新计数器 count。
   - 更新最大元音字母数量 max_vowels。
4. 返回最大元音字母数量 max_vowels。

关键点:
- 使用滑动窗口来保持窗口大小为 k。
- 通过移动左右指针来更新窗口内的元音字母数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。每个字符最多被访问两次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_vowels_in_substring(s: str, k: int) -> int:
    """
    函数式接口 - 计算字符串 s 中长度为 k 的子字符串中可能包含的最大元音字母数。
    """
    vowels = set("aeiou")
    max_vowels = 0
    count = 0
    left = 0

    for right in range(len(s)):
        if s[right] in vowels:
            count += 1
        if right - left + 1 > k:
            if s[left] in vowels:
                count -= 1
            left += 1
        max_vowels = max(max_vowels, count)

    return max_vowels


Solution = create_solution(max_vowels_in_substring)