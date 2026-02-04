# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4070
标题: Maximum Distance Between Unequal Words in Array II
难度: medium
链接: https://leetcode.cn/problems/maximum-distance-between-unequal-words-in-array-ii/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3706. 不同单词间的最大距离 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个单词的首次出现和最后一次出现的位置，然后遍历哈希表计算最大距离。

算法步骤:
1. 初始化一个字典 `word_indices`，用于存储每个单词的首次出现和最后一次出现的索引。
2. 遍历数组，更新每个单词的首次出现和最后一次出现的索引。
3. 遍历字典 `word_indices`，计算每个单词的最大距离，并更新全局最大距离。

关键点:
- 使用字典记录每个单词的索引，避免重复计算。
- 通过遍历字典来计算最大距离，确保时间复杂度最优。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。我们只需要遍历数组一次。
空间复杂度: O(m)，其中 m 是数组中不同单词的数量。我们需要存储每个单词的索引。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(words: List[str]) -> int:
    """
    函数式接口 - 计算不同单词间的最大距离
    """
    word_indices = {}
    max_distance = 0

    # 记录每个单词的首次出现和最后一次出现的索引
    for i, word in enumerate(words):
        if word not in word_indices:
            word_indices[word] = [i, i]
        else:
            word_indices[word][1] = i

    # 计算每个单词的最大距离
    for indices in word_indices.values():
        max_distance = max(max_distance, indices[1] - indices[0])

    return max_distance


Solution = create_solution(solution_function_name)