# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2040
标题: Minimum Cost to Reach Destination in Time
难度: hard
链接: https://leetcode.cn/problems/minimum-cost-to-reach-destination-in-time/
题目类型: 图、数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1928. 规定时间内到达终点的最小花费 - 一个国家有 n 个城市，城市编号为 0 到 n - 1 ，题目保证 所有城市 都由双向道路 连接在一起 。道路由二维整数数组 edges 表示，其中 edges[i] = [xi, yi, timei] 表示城市 xi 和 yi 之间有一条双向道路，耗费时间为 timei 分钟。两个城市之间可能会有多条耗费时间不同的道路，但是不会有道路两头连接着同一座城市。 每次经过一个城市时，你需要付通行费。通行费用一个长度为 n 且下标从 0 开始的整数数组 passingFees 表示，其中 passingFees[j] 是你经过城市 j 需要支付的费用。 一开始，你在城市 0 ，你想要在 maxTime 分钟以内 （包含 maxTime 分钟）到达城市 n - 1 。旅行的 费用 为你经过的所有城市 通行费之和 （包括 起点和终点城市的通行费）。 给你 maxTime，edges 和 passingFees ，请你返回完成旅行的 最小费用 ，如果无法在 maxTime 分钟以内完成旅行，请你返回 -1 。 示例 1： [https://assets.leetcode.com/uploads/2021/06/04/leetgraph1-1.png] 输入：maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3] 输出：11 解释：最优路径为 0 -> 1 -> 2 -> 5 ，总共需要耗费 30 分钟，需要支付 11 的通行费。 示例 2： [https://assets.leetcode.com/uploads/2021/06/04/copy-of-leetgraph1-1.png] 输入：maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3] 输出：48 解释：最优路径为 0 -> 3 -> 4 -> 5 ，总共需要耗费 26 分钟，需要支付 48 的通行费。 你不能选择路径 0 -> 1 -> 2 -> 5 ，因为这条路径耗费的时间太长。 示例 3： 输入：maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3] 输出：-1 解释：无法在 25 分钟以内从城市 0 到达城市 5 。 提示： * 1 <= maxTime <= 1000 * n == passingFees.length * 2 <= n <= 1000 * n - 1 <= edges.length <= 1000 * 0 <= xi, yi <= n - 1 * 1 <= timei <= 1000 * 1 <= passingFees[j] <= 1000 * 图中两个节点之间可能有多条路径。 * 图中不含有自环。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Dijkstra 算法找到在给定时间限制内的最小费用路径。

算法步骤:
1. 构建图的邻接表表示。
2. 使用优先队列（最小堆）来存储当前节点、时间和费用。
3. 初始化优先队列，将起点 (0, 0, 0) 加入队列。
4. 使用一个二维数组 `dist` 来记录从起点到每个节点在特定时间下的最小费用。
5. 从优先队列中取出当前节点，并更新其邻居节点的费用和时间。
6. 如果在规定时间内到达终点，则返回最小费用；否则返回 -1。

关键点:
- 使用优先队列确保每次处理的是当前最小费用的节点。
- 使用二维数组 `dist` 来避免重复计算和优化时间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log E)，其中 E 是边的数量。Dijkstra 算法的时间复杂度主要取决于优先队列的操作。
空间复杂度: O(N * maxTime)，其中 N 是节点数量，maxTime 是最大时间限制。用于存储 `dist` 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

def min_cost_to_reach_destination(maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
    # 构建图的邻接表表示
    graph = [[] for _ in range(len(passingFees))]
    for u, v, time in edges:
        graph[u].append((v, time))
        graph[v].append((u, time))

    # 优先队列，存储 (费用, 时间, 节点)
    pq = [(passingFees[0], 0, 0)]
    # 记录从起点到每个节点在特定时间下的最小费用
    dist = [[float('inf')] * (maxTime + 1) for _ in range(len(passingFees))]
    dist[0][0] = passingFees[0]

    while pq:
        cost, time, node = heapq.heappop(pq)

        if node == len(passingFees) - 1:
            return cost

        for neighbor, travel_time in graph[node]:
            new_time = time + travel_time
            new_cost = cost + passingFees[neighbor]
            if new_time <= maxTime and new_cost < dist[neighbor][new_time]:
                dist[neighbor][new_time] = new_cost
                heapq.heappush(pq, (new_cost, new_time, neighbor))

    return -1

Solution = create_solution(min_cost_to_reach_destination)