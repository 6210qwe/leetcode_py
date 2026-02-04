# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 527
标题: Word Abbreviation
难度: hard
链接: https://leetcode.cn/problems/word-abbreviation/
题目类型: 贪心、字典树、数组、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
527. 单词缩写 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和字典树来生成最短的单词缩写。

算法步骤:
1. 对单词列表进行排序，以确保相同前缀的单词在一起。
2. 初始化一个字典 `abbr` 来存储每个单词的当前缩写。
3. 使用一个循环来不断更新缩写，直到所有单词的缩写都是唯一的。
4. 在每次迭代中，使用字典树来检查当前缩写是否唯一，如果不唯一，则增加缩写的长度。
5. 返回最终的缩写列表。

关键点:
- 使用字典树来高效地检查缩写是否唯一。
- 通过贪心算法逐步增加缩写的长度，直到所有缩写都是唯一的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m^2)，其中 n 是单词的数量，m 是单词的最大长度。
空间复杂度: O(n * m)，用于存储字典树和缩写。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(words: List[str]) -> List[str]:
    """
    函数式接口 - 生成单词缩写
    """
    def is_unique(abbr: str) -> bool:
        return len(abbr_map[abbr]) == 1

    def update_abbr(word: str, index: int) -> None:
        abbr = word[:abbr_len[index]] + str(len(word) - abbr_len[index] - 1) + word[-1]
        if abbr not in abbr_map:
            abbr_map[abbr] = set()
        abbr_map[abbr].add(index)

    n = len(words)
    abbr_len = [1] * n
    abbr_map = {}
    
    for i in range(n):
        update_abbr(words[i], i)
    
    unique = False
    while not unique:
        unique = True
        for i in range(n):
            abbr = words[i][:abbr_len[i]] + str(len(words[i]) - abbr_len[i] - 1) + words[i][-1]
            if not is_unique(abbr):
                unique = False
                abbr_len[i] += 1
                update_abbr(words[i], i)
    
    result = []
    for i in range(n):
        abbr = words[i][:abbr_len[i]] + str(len(words[i]) - abbr_len[i] - 1) + words[i][-1]
        result.append(abbr)
    
    return result


Solution = create_solution(solution_function_name)