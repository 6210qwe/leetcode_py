# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1456
标题: Find the City With the Smallest Number of Neighbors at a Threshold Distance
难度: medium
链接: https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
题目类型: 图、动态规划、最短路
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1334. 阈值距离内邻居最少的城市 - 有 n 个城市，按从 0 到 n-1 编号。给你一个边数组 edges，其中 edges[i] = [fromi, toi, weighti] 代表 fromi 和 toi 两个城市之间的双向加权边，距离阈值是一个整数 distanceThreshold。 返回在路径距离限制为 distanceThreshold 以内可到达城市最少的城市。如果有多个这样的城市，则返回编号最大的城市。 注意，连接城市 i 和 j 的路径的距离等于沿该路径的所有边的权重之和。 示例 1： [https://assets.leetcode.com/uploads/2024/08/23/problem1334example1.png] 输入：n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4 输出：3 解释：城市分布图如上。 每个城市阈值距离 distanceThreshold = 4 内的邻居城市分别是： 城市 0 -> [城市 1, 城市 2] 城市 1 -> [城市 0, 城市 2, 城市 3] 城市 2 -> [城市 0, 城市 1, 城市 3] 城市 3 -> [城市 1, 城市 2] 城市 0 和 3 在阈值距离 4 以内都有 2 个邻居城市，但是我们必须返回城市 3，因为它的编号最大。 示例 2： [https://assets.leetcode.com/uploads/2024/08/23/problem1334example0.png] 输入：n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2 输出：0 解释：城市分布图如上。 每个城市阈值距离 distanceThreshold = 2 内的邻居城市分别是： 城市 0 -> [城市 1] 城市 1 -> [城市 0, 城市 4] 城市 2 -> [城市 3, 城市 4] 城市 3 -> [城市 2, 城市 4] 城市 4 -> [城市 1, 城市 2, 城市 3] 城市 0 在阈值距离 2 以内只有 1 个邻居城市。 提示： * 2 <= n <= 100 * 1 <= edges.length <= n * (n - 1) / 2 * edges[i].length == 3 * 0 <= fromi < toi < n * 1 <= weighti, distanceThreshold <= 10^4 * 所有 (fromi, toi) 都是不同的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Floyd-Warshall 算法计算所有节点对之间的最短路径，然后统计每个城市的邻居数量。

算法步骤:
1. 初始化邻接矩阵 `dist`，初始值为无穷大。
2. 根据 `edges` 更新 `dist` 矩阵。
3. 使用 Floyd-Warshall 算法更新 `dist` 矩阵，计算所有节点对之间的最短路径。
4. 统计每个城市在阈值距离内的邻居数量。
5. 找到邻居数量最少且编号最大的城市。

关键点:
- 使用 Floyd-Warshall 算法计算所有节点对之间的最短路径。
- 统计每个城市的邻居数量，并找到符合条件的城市。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^3)，Floyd-Warshall 算法的时间复杂度为 O(n^3)。
空间复杂度: O(n^2)，存储邻接矩阵的空间复杂度为 O(n^2)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_the_city(n: int, edges: List[List[int]], distance_threshold: int) -> int:
    """
    函数式接口 - 找到在路径距离限制为 distanceThreshold 以内可到达城市最少的城市。
    """
    # 初始化邻接矩阵
    dist = [[float('inf')] * n for _ in range(n)]
    
    # 根据 edges 更新 dist 矩阵
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w
    
    # 使用 Floyd-Warshall 算法更新 dist 矩阵
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # 统计每个城市在阈值距离内的邻居数量
    neighbors_count = [sum(dist[i][j] <= distance_threshold for j in range(n) if i != j) for i in range(n)]
    
    # 找到邻居数量最少且编号最大的城市
    min_neighbors = min(neighbors_count)
    result = max(i for i, count in enumerate(neighbors_count) if count == min_neighbors)
    
    return result


Solution = create_solution(find_the_city)