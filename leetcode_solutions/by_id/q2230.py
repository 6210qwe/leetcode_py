# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2230
标题: Minimum Cost to Reach City With Discounts
难度: medium
链接: https://leetcode.cn/problems/minimum-cost-to-reach-city-with-discounts/
题目类型: 图、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2093. 前往目标城市的最小费用 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Dijkstra 算法求解带折扣的最短路径问题。

算法步骤:
1. 初始化一个优先队列，将起点 (0, 0, 0) 加入队列，表示从起点出发，花费为 0，使用了 0 次折扣。
2. 初始化一个距离数组 `dist`，用于记录从起点到每个城市在不同折扣次数下的最小花费。
3. 从优先队列中取出当前花费最小的城市，并更新其邻居城市的花费。
4. 如果当前城市可以使用折扣，则更新使用折扣后的邻居城市的花费。
5. 重复步骤 3 和 4，直到优先队列为空或到达终点城市。

关键点:
- 使用优先队列来保证每次处理的都是当前最小花费的城市。
- 维护一个三维数组 `dist` 来记录不同折扣次数下的最小花费。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((n + m) log n)，其中 n 是城市数量，m 是道路数量。Dijkstra 算法的时间复杂度是 O((V + E) log V)，这里 V = n，E = m。
空间复杂度: O(n * k)，其中 n 是城市数量，k 是最大折扣次数。需要维护一个三维数组 `dist`。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

def minimumCost(n: int, highways: List[List[int]], discounts: int) -> int:
    # 构建图
    graph = [[] for _ in range(n)]
    for u, v, cost in highways:
        graph[u].append((v, cost))
        graph[v].append((u, cost))

    # 初始化距离数组
    dist = [[float('inf')] * (discounts + 1) for _ in range(n)]
    dist[0][0] = 0

    # 优先队列
    pq = [(0, 0, 0)]  # (cost, city, discount_count)

    while pq:
        cost, city, discount_count = heapq.heappop(pq)

        if cost > dist[city][discount_count]:
            continue

        for next_city, edge_cost in graph[city]:
            new_cost = cost + edge_cost
            if new_cost < dist[next_city][discount_count]:
                dist[next_city][discount_count] = new_cost
                heapq.heappush(pq, (new_cost, next_city, discount_count))

            if discount_count < discounts and cost + edge_cost // 2 < dist[next_city][discount_count + 1]:
                dist[next_city][discount_count + 1] = cost + edge_cost // 2
                heapq.heappush(pq, (cost + edge_cost // 2, next_city, discount_count + 1))

    return min(dist[n - 1])

Solution = create_solution(minimumCost)