# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3557
标题: Minimum Number of Valid Strings to Form Target II
难度: hard
链接: https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/
题目类型: 线段树、数组、字符串、二分查找、动态规划、字符串匹配、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3292. 形成目标字符串需要的最少字符串数 II - 给你一个字符串数组 words 和一个字符串 target。 如果字符串 x 是 words 中 任意 字符串的 前缀，则认为 x 是一个 有效 字符串。 现计划通过 连接 有效字符串形成 target ，请你计算并返回需要连接的 最少 字符串数量。如果无法通过这种方式形成 target，则返回 -1。 示例 1： 输入： words = ["abc","aaaaa","bcdef"], target = "aabcdabc" 输出： 3 解释： target 字符串可以通过连接以下有效字符串形成： * words[1] 的长度为 2 的前缀，即 "aa"。 * words[2] 的长度为 3 的前缀，即 "bcd"。 * words[0] 的长度为 3 的前缀，即 "abc"。 示例 2： 输入： words = ["abababab","ab"], target = "ababaababa" 输出： 2 解释： target 字符串可以通过连接以下有效字符串形成： * words[0] 的长度为 5 的前缀，即 "ababa"。 * words[0] 的长度为 5 的前缀，即 "ababa"。 示例 3： 输入： words = ["abcdef"], target = "xyz" 输出： -1 提示： * 1 <= words.length <= 100 * 1 <= words[i].length <= 5 * 104 * 输入确保 sum(words[i].length) <= 105. * words[i] 只包含小写英文字母。 * 1 <= target.length <= 5 * 104 * target 只包含小写英文字母。
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
