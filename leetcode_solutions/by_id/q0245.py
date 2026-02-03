# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 245
标题: Shortest Word Distance III
难度: medium
链接: https://leetcode.cn/problems/shortest-word-distance-iii/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
245. 最短单词距离 III - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 双指针，记录两个单词的位置，计算最小距离

算法步骤:
1. 遍历数组，记录word1和word2的位置
2. 如果word1和word2相同，需要记录两个不同的位置
3. 计算最小距离

关键点:
- 双指针维护最近的两个位置
- 时间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历数组一次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def shortest_word_distance(wordsDict: List[str], word1: str, word2: str) -> int:
    """
    函数式接口 - 最短单词距离 III
    
    实现思路:
    双指针：记录两个单词的位置，计算最小距离。
    
    Args:
        wordsDict: 单词数组
        word1: 第一个单词
        word2: 第二个单词（可能与word1相同）
        
    Returns:
        最短距离
        
    Example:
        >>> shortest_word_distance(["practice", "makes", "perfect", "coding", "makes"], "makes", "makes")
        3
    """
    min_dist = float('inf')
    idx1 = idx2 = -1
    
    for i, word in enumerate(wordsDict):
        if word == word1:
            idx1 = i
            if idx2 != -1 and idx1 != idx2:
                min_dist = min(min_dist, abs(idx1 - idx2))
        
        if word == word2:
            idx2 = i
            if idx1 != -1 and idx1 != idx2:
                min_dist = min(min_dist, abs(idx1 - idx2))
    
    return min_dist


# 自动生成Solution类（无需手动编写）
Solution = create_solution(shortest_word_distance)
