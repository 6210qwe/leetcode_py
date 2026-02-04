# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 737
标题: Sentence Similarity II
难度: medium
链接: https://leetcode.cn/problems/sentence-similarity-ii/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
737. 句子相似性 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来处理单词之间的相似关系。

算法步骤:
1. 初始化并查集，将每个单词初始化为其自身的根节点。
2. 遍历所有相似对，将每对单词合并到同一个集合中。
3. 遍历两个句子中的单词，检查它们是否属于同一个集合。如果有一个单词不在同一个集合中，则返回 False。
4. 如果所有单词都属于同一个集合，则返回 True。

关键点:
- 使用并查集来高效地处理单词之间的相似关系。
- 并查集的路径压缩和按秩合并优化可以保证操作的时间复杂度接近 O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是相似对的数量，m 是句子的长度。
空间复杂度: O(w)，其中 w 是不同单词的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def are_sentences_similar_two(sentence1: List[str], sentence2: List[str], similar_pairs: List[List[str]]) -> bool:
    if len(sentence1) != len(sentence2):
        return False

    # 将单词映射到索引
    word_to_index = {}
    index = 0
    for pair in similar_pairs:
        for word in pair:
            if word not in word_to_index:
                word_to_index[word] = index
                index += 1

    # 初始化并查集
    uf = UnionFind(len(word_to_index))

    # 合并相似对
    for word1, word2 in similar_pairs:
        uf.union(word_to_index[word1], word_to_index[word2])

    # 检查句子中的单词是否属于同一个集合
    for word1, word2 in zip(sentence1, sentence2):
        if word1 == word2:
            continue
        if word1 not in word_to_index or word2 not in word_to_index or uf.find(word_to_index[word1]) != uf.find(word_to_index[word2]):
            return False

    return True

Solution = are_sentences_similar_two