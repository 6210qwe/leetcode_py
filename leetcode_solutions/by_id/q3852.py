# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3852
标题: Path Existence Queries in a Graph II
难度: hard
链接: https://leetcode.cn/problems/path-existence-queries-in-a-graph-ii/
题目类型: 贪心、位运算、图、数组、双指针、二分查找、动态规划、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3534. 针对图的路径存在性查询 II - 给你一个整数 n，表示图中的节点数量，这些节点按从 0 到 n - 1 编号。 同时给你一个长度为 n 的整数数组 nums，以及一个整数 maxDiff。 如果满足 |nums[i] - nums[j]| <= maxDiff（即 nums[i] 和 nums[j] 的 绝对差 至多为 maxDiff），则节点 i 和节点 j 之间存在一条 无向边 。 此外，给你一个二维整数数组 queries。对于每个 queries[i] = [ui, vi]，找到节点 ui 和节点 vi 之间的 最短距离 。如果两节点之间不存在路径，则返回 -1。 返回一个数组 answer，其中 answer[i] 是第 i 个查询的结果。 注意：节点之间的边是无权重（unweighted）的。 示例 1： 输入: n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]] 输出: [1,1] 解释: 生成的图如下： [https://pic.leetcode.cn/1745660620-PauXMH-4149example1drawio.png] 查询 最短路径 最短距离 [0, 3] 0 → 3 1 [2, 4] 2 → 4 1 因此，输出为 [1, 1]。 示例 2： 输入: n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]] 输出: [1,2,-1,1] 解释: 生成的图如下： [https://pic.leetcode.cn/1745660627-mSVsDs-4149example2drawio.png] 查询 最短路径 最短距离 [0, 1] 0 → 1 1 [0, 2] 0 → 1 → 2 2 [2, 3] 无 -1 [4, 3] 3 → 4 1 因此，输出为 [1, 2, -1, 1]。 示例 3： 输入: n = 3, nums = [3,6,1], maxDiff = 1, queries = [[0,0],[0,1],[1,2]] 输出: [0,-1,-1] 解释: 由于以下原因，任意两个节点之间都不存在边： * 节点 0 和节点 1：|nums[0] - nums[1]| = |3 - 6| = 3 > 1 * 节点 0 和节点 2：|nums[0] - nums[2]| = |3 - 1| = 2 > 1 * 节点 1 和节点 2：|nums[1] - nums[2]| = |6 - 1| = 5 > 1 因此，不存在任何可以到达其他节点的节点，输出为 [0, -1, -1]。 提示： * 1 <= n == nums.length <= 105 * 0 <= nums[i] <= 105 * 0 <= maxDiff <= 105 * 1 <= queries.length <= 105 * queries[i] == [ui, vi] * 0 <= ui, vi < n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来处理连通性问题，并使用广度优先搜索 (BFS) 来计算最短路径。

算法步骤:
1. 初始化并查集。
2. 遍历所有节点，将满足条件的节点进行合并。
3. 对于每个查询，使用 BFS 计算最短路径。

关键点:
- 并查集用于高效地处理连通性问题。
- BFS 用于计算无权图中的最短路径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n + q * (n + m))，其中 n 是节点数，q 是查询数，m 是边数。
空间复杂度: O(n)，并查集和 BFS 所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict, deque

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

def bfs(graph, start, end):
    if start == end:
        return 0
    queue = deque([(start, 0)])
    visited = set([start])
    while queue:
        node, dist = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                if neighbor == end:
                    return dist + 1
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1

def solution_function_name(n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
    """
    函数式接口 - 实现最优解法
    """
    # Step 1: Initialize Union-Find
    uf = UnionFind(n)
    
    # Step 2: Merge nodes that satisfy the condition
    for i in range(n):
        for j in range(i + 1, n):
            if abs(nums[i] - nums[j]) <= maxDiff:
                uf.union(i, j)
    
    # Step 3: Build the graph
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            if uf.find(i) == uf.find(j):
                graph[i].append(j)
                graph[j].append(i)
    
    # Step 4: Process each query using BFS
    result = []
    for u, v in queries:
        if uf.find(u) != uf.find(v):
            result.append(-1)
        else:
            result.append(bfs(graph, u, v))
    
    return result

Solution = create_solution(solution_function_name)