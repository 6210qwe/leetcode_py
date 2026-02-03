# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 952
标题: Word Subsets
难度: medium
链接: https://leetcode.cn/problems/word-subsets/
题目类型: 数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
916. 单词子集 - 给你两个字符串数组 words1 和 words2。 现在，如果 b 中的每个字母都出现在 a 中，包括重复出现的字母，那么称字符串 b 是字符串 a 的 子集 。 * 例如，"wrr" 是 "warrior" 的子集，但不是 "world" 的子集。 如果对 words2 中的每一个单词 b，b 都是 a 的子集，那么我们称 words1 中的单词 a 是 通用单词 。 以数组形式返回 words1 中所有的 通用 单词。你可以按 任意顺序 返回答案。 示例 1： 输入：words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"] 输出：["facebook","google","leetcode"] 示例 2： 输入：words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"] 输出：["leetcode"] 示例 3： 输入：words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"] 输出：["cccbb"] 提示： * 1 <= words1.length, words2.length <= 104 * 1 <= words1[i].length, words2[i].length <= 10 * words1[i] 和 words2[i] 仅由小写英文字母组成 * words1 中的所有字符串 互不相同
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
