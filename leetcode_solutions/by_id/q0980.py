# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 980
标题: Find the Shortest Superstring
难度: hard
链接: https://leetcode.cn/problems/find-the-shortest-superstring/
题目类型: 位运算、数组、字符串、动态规划、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
943. 最短超级串 - 给定一个字符串数组 words，找到以 words 中每个字符串作为子字符串的最短字符串。如果有多个有效最短字符串满足题目条件，返回其中 任意一个 即可。 我们可以假设 words 中没有字符串是 words 中另一个字符串的子字符串。 示例 1： 输入：words = ["alex","loves","leetcode"] 输出："alexlovesleetcode" 解释："alex"，"loves"，"leetcode" 的所有排列都会被接受。 示例 2： 输入：words = ["catg","ctaagt","gcta","ttca","atgcatc"] 输出："gctaagttcatgcatc" 提示： * 1 <= words.length <= 12 * 1 <= words[i].length <= 20 * words[i] 由小写英文字母组成 * words 中的所有字符串 互不相同
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
