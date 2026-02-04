# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 770
标题: Couples Holding Hands
难度: hard
链接: https://leetcode.cn/problems/couples-holding-hands/
题目类型: 贪心、深度优先搜索、广度优先搜索、并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
765. 情侣牵手 - n 对情侣坐在连续排列的 2n 个座位上，想要牵到对方的手。 人和座位由一个整数数组 row 表示，其中 row[i] 是坐在第 i 个座位上的人的 ID。情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2n - 2, 2n - 1)。 返回 最少交换座位的次数，以便每对情侣可以并肩坐在一起。 每次交换可选择任意两人，让他们站起来交换座位。 示例 1: 输入: row = [0,2,1,3] 输出: 1 解释: 只需要交换第二个人（row[1]）和第三个人（row[2]）的位置即可。 示例 2: 输入: row = [3,2,0,1] 输出: 0 解释: 无需交换座位，所有的情侣都已经可以手牵手了。 提示: * 2n == row.length * 2 <= n <= 30 * n 是偶数 * 0 <= row[i] < 2n * row 中所有元素均 无重复
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来记录每个情侣的连接情况，并计算需要的最少交换次数。

算法步骤:
1. 初始化并查集，将每对情侣的两个ID合并。
2. 遍历座位数组，检查每对情侣是否已经连接，如果没有连接，则进行合并操作。
3. 计算最终的连通分量数量，最少交换次数为总情侣对数减去连通分量数量。

关键点:
- 使用并查集高效地管理连通性。
- 通过连通分量的数量来计算最少交换次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def min_swaps_couples(row: List[int]) -> int:
    n = len(row) // 2
    uf = UnionFind(n)
    
    for i in range(0, len(row), 2):
        x, y = row[i] // 2, row[i + 1] // 2
        uf.union(x, y)
    
    components = sum(uf.find(i) == i for i in range(n))
    return n - components

Solution = create_solution(min_swaps_couples)