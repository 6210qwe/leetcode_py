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
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
