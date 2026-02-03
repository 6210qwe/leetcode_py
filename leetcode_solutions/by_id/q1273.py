# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1273
标题: Compare Strings by Frequency of the Smallest Character
难度: medium
链接: https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/
题目类型: 数组、哈希表、字符串、二分查找、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1170. 比较字符串最小字母出现频次 - 定义一个函数 f(s)，统计 s 中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。 例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。 现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足 f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。 请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。 示例 1： 输入：queries = ["cbd"], words = ["zaaaz"] 输出：[1] 解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。 示例 2： 输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"] 输出：[1,2] 解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。 提示： * 1 <= queries.length <= 2000 * 1 <= words.length <= 2000 * 1 <= queries[i].length, words[i].length <= 10 * queries[i][j]、words[i][j] 都由小写英文字母组成
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
