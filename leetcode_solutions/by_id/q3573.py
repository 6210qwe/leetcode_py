# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3573
标题: Count Substrings That Can Be Rearranged to Contain a String I
难度: medium
链接: https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3297. 统计重新排列后包含另一个字符串的子字符串数目 I - 给你两个字符串 word1 和 word2 。 如果一个字符串 x 重新排列后，word2 是重排字符串的 前缀 ，那么我们称字符串 x 是 合法的 。 请你返回 word1 中 合法 子字符串 的数目。 示例 1： 输入：word1 = "bcca", word2 = "abc" 输出：1 解释： 唯一合法的子字符串是 "bcca" ，可以重新排列得到 "abcc" ，"abc" 是它的前缀。 示例 2： 输入：word1 = "abcabc", word2 = "abc" 输出：10 解释： 除了长度为 1 和 2 的所有子字符串都是合法的。 示例 3： 输入：word1 = "abcabc", word2 = "aaabc" 输出：0 解释： * 1 <= word1.length <= 105 * 1 <= word2.length <= 104 * word1 和 word2 都只包含小写英文字母。
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
