# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 243
标题: Shortest Word Distance
难度: easy
链接: https://leetcode.cn/problems/shortest-word-distance/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
243. 最短单词距离 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 遍历数组，记录两个单词的最新位置，计算距离的最小值

算法步骤:
1. 遍历数组，找到word1和word2的所有位置
2. 使用双指针，分别指向两个单词的位置列表
3. 计算所有位置对的距离，取最小值

关键点:
- 使用双指针优化，一次遍历
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历数组一次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def shortest_word_distance(wordsDict: List[str], word1: str, word2: str) -> int:
    """
    函数式接口 - 最短单词距离
    
    实现思路:
    遍历数组，记录两个单词的最新位置，计算距离的最小值。
    
    Args:
        wordsDict: 单词数组
        word1: 单词1
        word2: 单词2
        
    Returns:
        两个单词之间的最短距离
        
    Example:
        >>> shortest_word_distance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")
        3
    """
    min_distance = float('inf')
    index1 = index2 = -1
    
    for i, word in enumerate(wordsDict):
        if word == word1:
            index1 = i
            if index2 != -1:
                min_distance = min(min_distance, abs(index1 - index2))
        elif word == word2:
            index2 = i
            if index1 != -1:
                min_distance = min(min_distance, abs(index1 - index2))
    
    return min_distance


# 自动生成Solution类（无需手动编写）
Solution = create_solution(shortest_word_distance)
