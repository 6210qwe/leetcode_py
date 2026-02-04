# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2065
标题: Check for Contradictions in Equations
难度: hard
链接: https://leetcode.cn/problems/check-for-contradictions-in-equations/
题目类型: 深度优先搜索、并查集、图、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2307. 检查方程中的矛盾之处 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来检查方程中的矛盾。

算法步骤:
1. 初始化并查集，用于存储变量及其对应的值。
2. 遍历所有等式，将变量和其值加入并查集中。
3. 对于每个不等式，检查其是否与已有的等式矛盾。
4. 如果发现矛盾，返回 True；否则，遍历完所有方程后返回 False。

关键点:
- 使用并查集来管理变量及其值。
- 在处理不等式时，检查并查集中是否存在矛盾。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * α(n))，其中 n 是方程的数量，α 是反阿克曼函数。
空间复杂度: O(m)，其中 m 是变量的数量。
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
        self.value = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.value[x] = 1.0
            return x
        if x != self.parent[x]:
            origin = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.value[x] *= self.value[origin]
        return self.parent[x]

    def union(self, x, y, val):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.value[root_x] = val * self.value[y] / self.value[x]

    def is_connected(self, x, y):
        if x not in self.parent or y not in self.parent:
            return False
        return self.find(x) == self.find(y)

    def get_value(self, x):
        self.find(x)
        return self.value[x]


def solution_function_name(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    """
    函数式接口 - 检查方程中的矛盾之处
    """
    uf = UnionFind()
    
    # 处理等式
    for (a, b), val in zip(equations, values):
        uf.union(a, b, val)
    
    # 检查不等式
    for a, b in queries:
        if uf.is_connected(a, b):
            if uf.get_value(a) / uf.get_value(b) == 1.0:
                return True
        else:
            continue
    
    return False


Solution = create_solution(solution_function_name)