# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2025
标题: Redistribute Characters to Make All Strings Equal
难度: easy
链接: https://leetcode.cn/problems/redistribute-characters-to-make-all-strings-equal/
题目类型: 哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1897. 重新分配字符使所有字符串都相等 - 给你一个字符串数组 words（下标 从 0 开始 计数）。 在一步操作中，需先选出两个 不同 下标 i 和 j，其中 words[i] 是一个非空字符串，接着将 words[i] 中的 任一 字符移动到 words[j] 中的 任一 位置上。 如果执行任意步操作可以使 words 中的每个字符串都相等，返回 true ；否则，返回 false 。 示例 1： 输入：words = ["abc","aabc","bc"] 输出：true 解释：将 words[1] 中的第一个 'a' 移动到 words[2] 的最前面。 使 words[1] = "abc" 且 words[2] = "abc" 。 所有字符串都等于 "abc" ，所以返回 true 。 示例 2： 输入：words = ["ab","a"] 输出：false 解释：执行操作无法使所有字符串都相等。 提示： * 1 <= words.length <= 100 * 1 <= words[i].length <= 100 * words[i] 由小写英文字母组成
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
