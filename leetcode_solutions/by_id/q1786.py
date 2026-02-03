# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1786
标题: Count the Number of Consistent Strings
难度: easy
链接: https://leetcode.cn/problems/count-the-number-of-consistent-strings/
题目类型: 位运算、数组、哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1684. 统计一致字符串的数目 - 给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字符串 。 请你返回 words 数组中 一致字符串 的数目。 示例 1： 输入：allowed = "ab", words = ["ad","bd","aaab","baa","badab"] 输出：2 解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。 示例 2： 输入：allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"] 输出：7 解释：所有字符串都是一致的。 示例 3： 输入：allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"] 输出：4 解释：字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。 提示： * 1 <= words.length <= 104 * 1 <= allowed.length <= 26 * 1 <= words[i].length <= 10 * allowed 中的字符 互不相同 。 * words[i] 和 allowed 只包含小写英文字母。
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
