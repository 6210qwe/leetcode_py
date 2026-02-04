# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2582
标题: Minimum Score of a Path Between Two Cities
难度: medium
链接: https://leetcode.cn/problems/minimum-score-of-a-path-between-two-cities/
题目类型: 深度优先搜索、广度优先搜索、并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2492. 两个城市间路径的最小分数 - 给你一个正整数 n ，表示总共有 n 个城市，城市从 1 到 n 编号。给你一个二维数组 roads ，其中 roads[i] = [ai, bi, distancei] 表示城市 ai 和 bi 之间有一条 双向 道路，道路距离为 distancei 。城市构成的图不一定是连通的。 两个城市之间一条路径的 分数 定义为这条路径中道路的 最小 距离。 返回城市 1 和城市 n 之间的所有路径的 最小 分数。 注意： * 一条路径指的是两个城市之间的道路序列。 * 一条路径可以 多次 包含同一条道路，你也可以沿着路径多次到达城市 1 和城市 n 。 * 测试数据保证城市 1 和城市n 之间 至少 有一条路径。 示例 1： [https://assets.leetcode.com/uploads/2022/10/12/graph11.png] 输入：n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]] 输出：5 解释：城市 1 到城市 4 的路径中，分数最小的一条为：1 -> 2 -> 4 。这条路径的分数是 min(9,5) = 5 。 不存在分数更小的路径。 示例 2： [https://assets.leetcode.com/uploads/2022/10/12/graph22.png] 输入：n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]] 输出：2 解释：城市 1 到城市 4 分数最小的路径是：1 -> 2 -> 1 -> 3 -> 4 。这条路径的分数是 min(2,2,4,7) = 2 。 提示： * 2 <= n <= 105 * 1 <= roads.length <= 105 * roads[i].length == 3 * 1 <= ai, bi <= n * ai != bi * 1 <= distancei <= 104 * 不会有重复的边。 * 城市 1 和城市 n 之间至少有一条路径。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来找到城市 1 和城市 n 之间的所有路径，并在过程中记录每条路径的最小分数。

算法步骤:
1. 初始化并查集，用于连接城市。
2. 遍历所有道路，将城市连接起来，并记录每条道路的距离。
3. 使用并查集找到城市 1 和城市 n 之间的所有路径。
4. 在遍历过程中记录每条路径的最小分数。
5. 返回所有路径中的最小分数。

关键点:
- 使用并查集来高效地连接和查找城市。
- 在连接城市时记录每条道路的距离。
- 在查找路径时记录每条路径的最小分数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是城市的数量，m 是道路的数量。
空间复杂度: O(n + m)，存储并查集和道路信息。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

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

def min_score(n: int, roads: List[List[int]]) -> int:
    uf = UnionFind(n + 1)
    min_distances = [float('inf')] * (n + 1)
    
    for a, b, distance in roads:
        uf.union(a, b)
        min_distances[a] = min(min_distances[a], distance)
        min_distances[b] = min(min_distances[b], distance)
    
    root_1 = uf.find(1)
    root_n = uf.find(n)
    
    if root_1 != root_n:
        return -1  # 如果城市 1 和城市 n 不连通，返回 -1
    
    min_score = float('inf')
    for i in range(1, n + 1):
        if uf.find(i) == root_1:
            min_score = min(min_score, min_distances[i])
    
    return min_score

Solution = create_solution(min_score)