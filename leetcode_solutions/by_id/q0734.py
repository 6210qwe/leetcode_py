# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 734
标题: Sentence Similarity
难度: easy
链接: https://leetcode.cn/problems/sentence-similarity/
题目类型: 数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
734. 句子相似性 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储单词对，并逐个比较句子中的单词。

算法步骤:
1. 将 pairs 转换为一个哈希表，记录每个单词的相似词。
2. 比较两个句子中的每个单词，如果单词相同则继续比较下一个单词，否则检查它们是否在哈希表中互为相似词。
3. 如果所有单词都匹配，则返回 True，否则返回 False。

关键点:
- 使用哈希表存储相似词对，便于快速查找。
- 逐个比较句子中的单词，确保每个单词都匹配或互为相似词。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 sentence1 和 sentence2 的长度，m 是 pairs 的长度。
空间复杂度: O(m)，用于存储哈希表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def are_sentences_similar(sentence1: List[str], sentence2: List[str], similar_pairs: List[List[str]]) -> bool:
    if len(sentence1) != len(sentence2):
        return False
    
    # 构建相似词哈希表
    similar_dict = {}
    for pair in similar_pairs:
        if pair[0] not in similar_dict:
            similar_dict[pair[0]] = set()
        if pair[1] not in similar_dict:
            similar_dict[pair[1]] = set()
        similar_dict[pair[0]].add(pair[1])
        similar_dict[pair[1]].add(pair[0])
    
    # 比较句子中的每个单词
    for word1, word2 in zip(sentence1, sentence2):
        if word1 != word2 and (word1 not in similar_dict or word2 not in similar_dict[word1]):
            return False
    
    return True

Solution = are_sentences_similar