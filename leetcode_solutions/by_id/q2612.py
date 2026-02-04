# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2612
标题: Minimum Cost to Buy Apples
难度: medium
链接: https://leetcode.cn/problems/minimum-cost-to-buy-apples/
题目类型: 图、数组、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2473. 购买苹果的最低成本 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Dijkstra 算法找到从起点到所有节点的最短路径，然后计算每个节点购买苹果的成本。

算法步骤:
1. 初始化一个优先队列，将起点加入队列，距离设为 0。
2. 使用一个字典记录每个节点的最短距离。
3. 从优先队列中取出当前距离最小的节点，更新其邻居节点的距离。
4. 重复步骤 3，直到优先队列为空。
5. 计算每个节点购买苹果的成本，返回总成本。

关键点:
- 使用优先队列（最小堆）来高效地获取当前距离最小的节点。
- 使用邻接表表示图结构，方便快速查找邻居节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log V)，其中 E 是边的数量，V 是节点的数量。Dijkstra 算法的时间复杂度主要由优先队列的操作决定。
空间复杂度: O(V + E)，存储图的邻接表和最短路径字典。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def minimum_cost_to_buy_apples(n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
    """
    函数式接口 - 实现购买苹果的最低成本
    """
    # 构建邻接表
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Dijkstra 算法
    def dijkstra(start: int) -> List[int]:
        dist = [float('inf')] * n
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v in graph[u]:
                if dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1
                    heapq.heappush(pq, (dist[v], v))
        return dist

    # 计算每个节点在所有 trip 中的访问次数
    visit_count = [0] * n
    for start, end in trips:
        dist_start = dijkstra(start)
        dist_end = dijkstra(end)
        for i in range(n):
            if dist_start[i] + dist_end[i] == dist_start[end]:
                visit_count[i] += 1

    # 计算总成本
    total_cost = sum(visit_count[i] * price[i] for i in range(n))
    return total_cost

Solution = create_solution(minimum_cost_to_buy_apples)