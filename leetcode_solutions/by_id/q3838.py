# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3838
标题: Path Existence Queries in a Graph I
难度: medium
链接: https://leetcode.cn/problems/path-existence-queries-in-a-graph-i/
题目类型: 并查集、图、数组、哈希表、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3532. 针对图的路径存在性查询 I - 给你一个整数 n，表示图中的节点数量，这些节点按从 0 到 n - 1 编号。 同时给你一个长度为 n 的整数数组 nums，该数组按 非递减 顺序排序，以及一个整数 maxDiff。 如果满足 |nums[i] - nums[j]| <= maxDiff（即 nums[i] 和 nums[j] 的 绝对差 至多为 maxDiff），则节点 i 和节点 j 之间存在一条 无向边 。 此外，给你一个二维整数数组 queries。对于每个 queries[i] = [ui, vi]，需要判断节点 ui 和 vi 之间是否存在路径。 返回一个布尔数组 answer，其中 answer[i] 等于 true 表示在第 i 个查询中节点 ui 和 vi 之间存在路径，否则为 false。 示例 1： 输入: n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]] 输出: [true,false] 解释: * 查询 [0,0]：节点 0 有一条到自己的显然路径。 * 查询 [0,1]：节点 0 和节点 1 之间没有边，因为 |nums[0] - nums[1]| = |1 - 3| = 2，大于 maxDiff。 * 因此，在处理完所有查询后，最终答案为 [true, false]。 示例 2： 输入: n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]] 输出: [false,false,true,true] 解释: 生成的图如下： [https://pic.leetcode.cn/1745660506-eNVQtC-screenshot-2025-03-26-at-122249.png] * 查询 [0,1]：节点 0 和节点 1 之间没有边，因为 |nums[0] - nums[1]| = |2 - 5| = 3，大于 maxDiff。 * 查询 [0,2]：节点 0 和节点 2 之间没有边，因为 |nums[0] - nums[2]| = |2 - 6| = 4，大于 maxDiff。 * 查询 [1,3]：节点 1 和节点 3 之间存在路径通过节点 2，因为 |nums[1] - nums[2]| = |5 - 6| = 1 和 |nums[2] - nums[3]| = |6 - 8| = 2，都小于等于 maxDiff。 * 查询 [2,3]：节点 2 和节点 3 之间有一条边，因为 |nums[2] - nums[3]| = |6 - 8| = 2，等于 maxDiff。 * 因此，在处理完所有查询后，最终答案为 [false, false, true, true]。 提示： * 1 <= n == nums.length <= 105 * 0 <= nums[i] <= 105 * nums 按 非递减 顺序排序。 * 0 <= maxDiff <= 105 * 1 <= queries.length <= 105 * queries[i] == [ui, vi] * 0 <= ui, vi < n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来管理节点之间的连通性，并通过遍历 nums 数组来构建图。

算法步骤:
1. 初始化并查集。
2. 遍历 nums 数组，将满足条件的节点进行合并。
3. 对于每个查询，使用并查集判断两个节点是否连通。

关键点:
- 使用并查集来高效地管理连通性。
- 由于 nums 数组是有序的，可以利用这一点来优化合并操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m * α(n))，其中 n 是节点数，m 是查询数，α 是反阿克曼函数。
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

def path_existence_queries(n: int, nums: List[int], max_diff: int, queries: List[List[int]]) -> List[bool]:
    uf = UnionFind(n)
    
    # 构建图
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] - nums[i] <= max_diff:
                uf.union(i, j)
            else:
                break
    
    # 处理查询
    result = []
    for u, v in queries:
        result.append(uf.find(u) == uf.find(v))
    
    return result

Solution = create_solution(path_existence_queries)