# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1085
标题: The Earliest Moment When Everyone Become Friends
难度: medium
链接: https://leetcode.cn/problems/the-earliest-moment-when-everyone-become-friends/
题目类型: 并查集、数组、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1101. 彼此熟识的最早时间 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来跟踪每个人的朋友关系，并在每次合并时检查是否所有人都已经彼此熟识。

算法步骤:
1. 初始化并查集，将每个人的父节点设为自己。
2. 对所有事件按时间排序。
3. 遍历每个事件，合并两个朋友的关系，并更新集合大小。
4. 如果在某个时刻，所有人的父节点都指向同一个根节点，则返回该时刻。
5. 如果遍历完所有事件后仍未找到这样的时刻，则返回 -1。

关键点:
- 使用路径压缩和按秩合并优化并查集操作。
- 在每次合并时检查是否所有人都已经彼此熟识。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 logs 的长度。主要由排序操作决定。
空间复杂度: O(n)，用于存储并查集的数据结构。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
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
            self.count -= 1

def earliest_acq(logs: List[List[int]], n: int) -> int:
    """
    函数式接口 - 返回所有人成为朋友的最早时间
    """
    # 按时间排序
    logs.sort(key=lambda x: x[0])
    
    uf = UnionFind(n)
    
    for timestamp, x, y in logs:
        uf.union(x, y)
        if uf.count == 1:
            return timestamp
    
    return -1

Solution = create_solution(earliest_acq)