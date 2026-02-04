# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1191
标题: Synonymous Sentences
难度: medium
链接: https://leetcode.cn/problems/synonymous-sentences/
题目类型: 排序、并查集、数组、哈希表、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1258. 近义词句子 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集将同义词归类，然后通过回溯法生成所有可能的句子。

算法步骤:
1. 构建并查集，将同义词对中的单词合并到同一个集合中。
2. 将句子中的每个单词替换为其所在集合的所有可能的同义词。
3. 使用回溯法生成所有可能的句子。

关键点:
- 使用并查集来管理同义词组。
- 使用回溯法生成所有可能的句子。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n * m)，其中 n 是句子中不同单词的数量，m 是每个单词的平均同义词数量。
空间复杂度: O(n + m)，其中 n 是句子中不同单词的数量，m 是所有单词的同义词总数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY

def generate_sentences(synonyms: List[List[str]], text: str) -> List[str]:
    # 构建并查集
    uf = UnionFind()
    for a, b in synonyms:
        uf.union(a, b)
    
    # 构建同义词字典
    synonym_dict = {}
    for word in set([word for pair in synonyms for word in pair]):
        root = uf.find(word)
        if root not in synonym_dict:
            synonym_dict[root] = []
        synonym_dict[root].append(word)
    
    # 分割句子
    words = text.split()
    
    # 回溯生成所有可能的句子
    def backtrack(index, path):
        if index == len(words):
            result.append(' '.join(path))
            return
        if words[index] in uf.parent:
            root = uf.find(words[index])
            for synonym in synonym_dict[root]:
                backtrack(index + 1, path + [synonym])
        else:
            backtrack(index + 1, path + [words[index]])
    
    result = []
    backtrack(0, [])
    return result

Solution = create_solution(generate_sentences)