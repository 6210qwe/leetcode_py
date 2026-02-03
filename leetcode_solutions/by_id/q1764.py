# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1764
标题: Maximum Repeating Substring
难度: easy
链接: https://leetcode.cn/problems/maximum-repeating-substring/
题目类型: 字符串、动态规划、字符串匹配
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1668. 最大重复子字符串 - 给你一个字符串 sequence ，如果字符串 word 连续重复 k 次形成的字符串是 sequence 的一个子字符串，那么单词 word 的 重复值为 k 。单词 word 的 最大重复值 是单词 word 在 sequence 中最大的重复值。如果 word 不是 sequence 的子串，那么重复值 k 为 0 。 给你一个字符串 sequence 和 word ，请你返回 最大重复值 k 。 示例 1： 输入：sequence = "ababc", word = "ab" 输出：2 解释："abab" 是 "ababc" 的子字符串。 示例 2： 输入：sequence = "ababc", word = "ba" 输出：1 解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。 示例 3： 输入：sequence = "ababc", word = "ac" 输出：0 解释："ac" 不是 "ababc" 的子字符串。 提示： * 1 <= sequence.length <= 100 * 1 <= word.length <= 100 * sequence 和 word 都只包含小写英文字母。
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
