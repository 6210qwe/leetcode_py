# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 984
标题: Most Stones Removed with Same Row or Column
难度: medium
链接: https://leetcode.cn/problems/most-stones-removed-with-same-row-or-column/
题目类型: 深度优先搜索、并查集、图、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
947. 移除最多的同行或同列石头 - n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。 如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。 给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。 示例 1： 输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]] 输出：5 解释：一种移除 5 块石头的方法如下所示： 1. 移除石头 [2,2] ，因为它和 [2,1] 同行。 2. 移除石头 [2,1] ，因为它和 [0,1] 同列。 3. 移除石头 [1,2] ，因为它和 [1,0] 同行。 4. 移除石头 [1,0] ，因为它和 [0,0] 同列。 5. 移除石头 [0,1] ，因为它和 [0,0] 同行。 石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。 示例 2： 输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]] 输出：3 解释：一种移除 3 块石头的方法如下所示： 1. 移除石头 [2,2] ，因为它和 [2,0] 同行。 2. 移除石头 [2,0] ，因为它和 [0,0] 同列。 3. 移除石头 [0,2] ，因为它和 [0,0] 同行。 石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。 示例 3： 输入：stones = [[0,0]] 输出：0 解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。 提示： * 1 <= stones.length <= 1000 * 0 <= xi, yi <= 104 * 不会有两块石头放在同一个坐标点上
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来找到所有连通分量。每个连通分量可以看作是一个独立的图，其中的石头可以通过移除操作使得只剩下一块石头。

算法步骤:
1. 初始化并查集。
2. 遍历每块石头，将同一行或同一列的石头进行合并。
3. 计算连通分量的数量。
4. 最大可移除石头数量为总石头数量减去连通分量的数量。

关键点:
- 并查集用于高效地管理和合并连通分量。
- 通过行和列索引映射到并查集中的节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是石头的数量。并查集的操作均摊时间复杂度接近 O(1)。
空间复杂度: O(n)，并查集需要存储每个节点的父节点和秩。
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


def solution_function_name(stones: List[List[int]]) -> int:
    """
    函数式接口 - 使用并查集计算可以移除的最大石头数量
    """
    n = len(stones)
    if n == 1:
        return 0
    
    uf = UnionFind(20000)  # 0 <= xi, yi <= 10^4，所以使用 20000 个节点
    for x, y in stones:
        uf.union(x, y + 10000)  # 将行和列分别映射到不同的区间
    
    components = set()
    for x, y in stones:
        components.add(uf.find(x))
    
    return n - len(components)


Solution = create_solution(solution_function_name)