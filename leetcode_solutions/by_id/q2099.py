# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2099
标题: Number of Strings That Appear as Substrings in Word
难度: easy
链接: https://leetcode.cn/problems/number-of-strings-that-appear-as-substrings-in-word/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1967. 作为子字符串出现在单词中的字符串数目 - 给你一个字符串数组 patterns 和一个字符串 word ，统计 patterns 中有多少个字符串是 word 的子字符串。返回字符串数目。 子字符串 是字符串中的一个连续字符序列。 示例 1： 输入：patterns = ["a","abc","bc","d"], word = "abc" 输出：3 解释： - "a" 是 "abc" 的子字符串。 - "abc" 是 "abc" 的子字符串。 - "bc" 是 "abc" 的子字符串。 - "d" 不是 "abc" 的子字符串。 patterns 中有 3 个字符串作为子字符串出现在 word 中。 示例 2： 输入：patterns = ["a","b","c"], word = "aaaaabbbbb" 输出：2 解释： - "a" 是 "aaaaabbbbb" 的子字符串。 - "b" 是 "aaaaabbbbb" 的子字符串。 - "c" 不是 "aaaaabbbbb" 的字符串。 patterns 中有 2 个字符串作为子字符串出现在 word 中。 示例 3： 输入：patterns = ["a","a","a"], word = "ab" 输出：3 解释：patterns 中的每个字符串都作为子字符串出现在 word "ab" 中。 提示： * 1 <= patterns.length <= 100 * 1 <= patterns[i].length <= 100 * 1 <= word.length <= 100 * patterns[i] 和 word 由小写英文字母组成
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
