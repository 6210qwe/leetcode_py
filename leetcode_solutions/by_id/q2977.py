# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2977
标题: Check if a String Is an Acronym of Words
难度: easy
链接: https://leetcode.cn/problems/check-if-a-string-is-an-acronym-of-words/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2828. 判别首字母缩略词 - 给你一个字符串数组 words 和一个字符串 s ，请你判断 s 是不是 words 的 首字母缩略词 。 如果可以按顺序串联 words 中每个字符串的第一个字符形成字符串 s ，则认为 s 是 words 的首字母缩略词。例如，"ab" 可以由 ["apple", "banana"] 形成，但是无法从 ["bear", "aardvark"] 形成。 如果 s 是 words 的首字母缩略词，返回 true ；否则，返回 false 。 示例 1： 输入：words = ["alice","bob","charlie"], s = "abc" 输出：true 解释：words 中 "alice"、"bob" 和 "charlie" 的第一个字符分别是 'a'、'b' 和 'c'。因此，s = "abc" 是首字母缩略词。 示例 2： 输入：words = ["an","apple"], s = "a" 输出：false 解释：words 中 "an" 和 "apple" 的第一个字符分别是 'a' 和 'a'。 串联这些字符形成的首字母缩略词是 "aa" 。 因此，s = "a" 不是首字母缩略词。 示例 3： 输入：words = ["never","gonna","give","up","on","you"], s = "ngguoy" 输出：true 解释：串联数组 words 中每个字符串的第一个字符，得到字符串 "ngguoy" 。 因此，s = "ngguoy" 是首字母缩略词。 提示： * 1 <= words.length <= 100 * 1 <= words[i].length <= 10 * 1 <= s.length <= 100 * words[i] 和 s 由小写英文字母组成
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
