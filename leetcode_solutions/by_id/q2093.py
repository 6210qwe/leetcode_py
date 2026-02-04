# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2093
标题: Check If String Is a Prefix of Array
难度: easy
链接: https://leetcode.cn/problems/check-if-string-is-a-prefix-of-array/
题目类型: 数组、双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1961. 检查字符串是否为数组前缀 - 给你一个字符串 s 和一个字符串数组 words ，请你判断 s 是否为 words 的 前缀字符串 。 字符串 s 要成为 words 的 前缀字符串 ，需要满足：s 可以由 words 中的前 k（k 为 正数 ）个字符串按顺序相连得到，且 k 不超过 words.length 。 如果 s 是 words 的 前缀字符串 ，返回 true ；否则，返回 false 。 示例 1： 输入：s = "iloveleetcode", words = ["i","love","leetcode","apples"] 输出：true 解释： s 可以由 "i"、"love" 和 "leetcode" 相连得到。 示例 2： 输入：s = "iloveleetcode", words = ["apples","i","love","leetcode"] 输出：false 解释： 数组的前缀相连无法得到 s 。 提示： * 1 <= words.length <= 100 * 1 <= words[i].length <= 20 * 1 <= s.length <= 1000 * words[i] 和 s 仅由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针方法，逐个字符比较字符串 s 和 words 中的字符。

算法步骤:
1. 初始化两个指针 i 和 j，分别指向 s 和 words 的起始位置。
2. 遍历 words 中的每个字符串，逐个字符与 s 进行比较。
3. 如果在遍历过程中发现不匹配的字符，返回 False。
4. 如果遍历完 s 或者 words，检查是否已经完全匹配 s。

关键点:
- 使用双指针方法逐个字符比较，确保时间复杂度最优。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 s 的长度。最坏情况下需要遍历 s 的所有字符。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_prefix_of_array(s: str, words: List[str]) -> bool:
    """
    函数式接口 - 检查字符串 s 是否为 words 的前缀字符串
    """
    i = 0  # 指向 s 的指针
    for word in words:
        for char in word:
            if i < len(s) and s[i] == char:
                i += 1
            else:
                return False
        if i == len(s):
            return True
    return i == len(s)


Solution = create_solution(is_prefix_of_array)