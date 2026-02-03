# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 244
标题: Shortest Word Distance II
难度: medium
链接: https://leetcode.cn/problems/shortest-word-distance-ii/
题目类型: 设计、数组、哈希表、双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
244. 最短单词距离 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储每个单词的所有位置，查询时使用双指针计算最短距离

算法步骤:
1. 初始化时，用哈希表存储每个单词的所有位置
2. 查询时，获取两个单词的位置列表，使用双指针计算最短距离

关键点:
- 预处理存储位置，查询时O(m+n)时间
- 时间复杂度：初始化O(n)，查询O(m+n)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 初始化O(n)，查询O(m+n) - m和n为两个单词的出现次数
空间复杂度: O(n) - 哈希表空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict
from leetcode_solutions.utils.solution import create_solution


class WordDistance:
    """
    最短单词距离II
    """
    def __init__(self, wordsDict: List[str]):
        self.word_indices = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.word_indices[word].append(i)
    
    def shortest(self, word1: str, word2: str) -> int:
        """返回两个单词之间的最短距离"""
        indices1 = self.word_indices[word1]
        indices2 = self.word_indices[word2]
        
        min_distance = float('inf')
        i = j = 0
        
        while i < len(indices1) and j < len(indices2):
            min_distance = min(min_distance, abs(indices1[i] - indices2[j]))
            if indices1[i] < indices2[j]:
                i += 1
            else:
                j += 1
        
        return min_distance


def shortest_word_distance_ii(wordsDict: List[str]) -> WordDistance:
    """
    函数式接口 - 创建最短单词距离II对象
    
    实现思路:
    使用哈希表存储每个单词的所有位置，查询时使用双指针计算最短距离。
    
    Args:
        wordsDict: 单词数组
        
    Returns:
        WordDistance实例
        
    Example:
        >>> wordDistance = shortest_word_distance_ii(["practice", "makes", "perfect", "coding", "makes"])
        >>> wordDistance.shortest("coding", "practice")
        3
    """
    return WordDistance(wordsDict)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(shortest_word_distance_ii)
