# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3514
标题: Shortest Distance After Road Addition Queries II
难度: hard
链接: https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-ii/
题目类型: 贪心、图、数组、有序集合
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3244. 新增道路查询后的最短距离 II - 给你一个整数 n 和一个二维整数数组 queries。 有 n 个城市，编号从 0 到 n - 1。初始时，每个城市 i 都有一条单向道路通往城市 i + 1（ 0 <= i < n - 1）。 queries[i] = [ui, vi] 表示新建一条从城市 ui 到城市 vi 的单向道路。每次查询后，你需要找到从城市 0 到城市 n - 1 的最短路径的长度。 所有查询中不会存在两个查询都满足 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]。 返回一个数组 answer，对于范围 [0, queries.length - 1] 中的每个 i，answer[i] 是处理完前 i + 1 个查询后，从城市 0 到城市 n - 1 的最短路径的长度。 示例 1： 输入： n = 5, queries = [[2, 4], [0, 2], [0, 4]] 输出： [3, 2, 1] 解释： [https://assets.leetcode.com/uploads/2024/06/28/image8.jpg] 新增一条从 2 到 4 的道路后，从 0 到 4 的最短路径长度为 3。 [https://assets.leetcode.com/uploads/2024/06/28/image9.jpg] 新增一条从 0 到 2 的道路后，从 0 到 4 的最短路径长度为 2。 [https://assets.leetcode.com/uploads/2024/06/28/image10.jpg] 新增一条从 0 到 4 的道路后，从 0 到 4 的最短路径长度为 1。 示例 2： 输入： n = 4, queries = [[0, 3], [0, 2]] 输出： [1, 1] 解释： [https://assets.leetcode.com/uploads/2024/06/28/image11.jpg] 新增一条从 0 到 3 的道路后，从 0 到 3 的最短路径长度为 1。 [https://assets.leetcode.com/uploads/2024/06/28/image12.jpg] 新增一条从 0 到 2 的道路后，从 0 到 3 的最短路径长度仍为 1。 提示: * 3 <= n <= 105 * 1 <= queries.length <= 105 * queries[i].length == 2 * 0 <= queries[i][0] < queries[i][1] < n * 1 < queries[i][1] - queries[i][0] * 查询中不存在重复的道路。 * 不存在两个查询都满足 i != j 且 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和有序集合来维护当前最短路径。

算法步骤:
1. 初始化一个数组 dp，其中 dp[i] 表示从城市 0 到城市 i 的最短路径长度。
2. 使用一个有序集合来存储当前可以到达的城市及其最短路径长度。
3. 对于每个查询，更新 dp 数组，并更新有序集合。
4. 每次查询后，返回 dp[n-1] 作为结果。

关键点:
- 使用有序集合来高效地更新和查询最短路径。
- 动态规划数组 dp 用于存储从城市 0 到每个城市的最短路径长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m log m)，其中 n 是城市的数量，m 是查询的数量。
空间复杂度: O(n + m)，其中 n 是城市的数量，m 是查询的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import bisect

def shortest_distance_after_queries(n: int, queries: List[List[int]]) -> List[int]:
    """
    函数式接口 - 实现新增道路查询后的最短距离
    """
    # 初始化 dp 数组
    dp = list(range(n))
    
    # 有序集合，存储 (距离, 城市) 对
    reachable = [(0, 0)]
    
    result = []
    
    for u, v in queries:
        # 更新 dp 数组
        if dp[v] > dp[u] + 1:
            dp[v] = dp[u] + 1
            # 在有序集合中插入新的 (距离, 城市) 对
            bisect.insort(reachable, (dp[v], v))
        
        # 更新从城市 0 到城市 n-1 的最短路径
        while reachable and reachable[0][1] < n - 1:
            dist, city = reachable.pop(0)
            if dp[city + 1] > dist + 1:
                dp[city + 1] = dist + 1
                bisect.insort(reachable, (dp[city + 1], city + 1))
        
        result.append(dp[-1])
    
    return result

Solution = create_solution(shortest_distance_after_queries)