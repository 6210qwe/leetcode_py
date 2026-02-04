# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1132
标题: Before and After Puzzle
难度: medium
链接: https://leetcode.cn/problems/before-and-after-puzzle/
题目类型: 数组、哈希表、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1181. 前后拼接 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储每个句子的前缀和后缀，然后通过拼接前缀和后缀生成结果。

算法步骤:
1. 遍历所有句子，提取每个句子的前缀和后缀，并存储在哈希表中。
2. 遍历哈希表中的后缀，检查是否存在对应的前缀，如果存在则拼接成新的句子。
3. 对结果进行去重并排序。

关键点:
- 提取句子的前缀和后缀时需要考虑空格和标点符号。
- 使用哈希表存储前缀和后缀可以快速查找和拼接。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m + n * log n)，其中 n 是句子的数量，m 是句子的平均长度。遍历句子和拼接操作的时间复杂度是 O(n * m)，排序操作的时间复杂度是 O(n * log n)。
空间复杂度: O(n * m)，用于存储前缀和后缀。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def beforeAndAfterPuzzles(phrases: List[str]) -> List[str]:
    """
    函数式接口 - 实现前后拼接
    """
    # 哈希表存储后缀和前缀
    suffix_map = {}
    prefix_map = {}
    
    for phrase in phrases:
        words = phrase.split()
        prefix = words[0]
        suffix = words[-1]
        
        if suffix not in suffix_map:
            suffix_map[suffix] = []
        suffix_map[suffix].append(phrase)
        
        if prefix not in prefix_map:
            prefix_map[prefix] = []
        prefix_map[prefix].append(phrase)
    
    result = set()
    
    for suffix, phrases_with_suffix in suffix_map.items():
        if suffix in prefix_map:
            for phrase1 in phrases_with_suffix:
                for phrase2 in prefix_map[suffix]:
                    if phrase1 != phrase2:
                        result.add(phrase1 + phrase2[len(suffix):])
    
    return sorted(result)


Solution = create_solution(beforeAndAfterPuzzles)