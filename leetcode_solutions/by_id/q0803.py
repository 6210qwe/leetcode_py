# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 803
标题: Cheapest Flights Within K Stops
难度: medium
链接: https://leetcode.cn/problems/cheapest-flights-within-k-stops/
题目类型: 深度优先搜索、广度优先搜索、图、动态规划、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
787. K 站中转内最便宜的航班 - 有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。 示例 1： [https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-3drawio.png] 输入: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1 输出: 700 解释: 城市航班图如上 从城市 0 到城市 3 经过最多 1 站的最佳路径用红色标记，费用为 100 + 600 = 700。 请注意，通过城市 [0, 1, 2, 3] 的路径更便宜，但无效，因为它经过了 2 站。 示例 2： [https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-1drawio.png] 输入: n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1 输出: 200 解释: 城市航班图如上 从城市 0 到城市 2 经过最多 1 站的最佳路径标记为红色，费用为 100 + 100 = 200。 示例 3： [https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-2drawio.png] 输入：n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0 输出：500 解释： 城市航班图如上 从城市 0 到城市 2 不经过站点的最佳路径标记为红色，费用为 500。 提示： * 2 <= n <= 100 * 0 <= flights.length <= (n * (n - 1) / 2) * flights[i].length == 3 * 0 <= fromi, toi < n * fromi != toi * 1 <= pricei <= 104 * 航班没有重复，且不存在自环 * 0 <= src, dst, k < n * src != dst
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用带权重的广度优先搜索（BFS）来找到从 src 到 dst 的最便宜路径，同时限制中转次数不超过 k。

算法步骤:
1. 构建邻接表表示图。
2. 使用队列进行 BFS，队列中的每个元素是一个元组 (当前节点, 当前花费, 中转次数)。
3. 使用一个字典 `costs` 来记录到达每个节点的最小花费。
4. 从起点开始，将起点加入队列，并初始化 `costs` 字典。
5. 在 BFS 过程中，如果当前节点是终点且中转次数不超过 k，则更新结果。
6. 如果当前节点的花费大于 `costs` 中记录的最小花费，则跳过。
7. 否则，将当前节点的所有邻居加入队列，并更新 `costs` 字典。

关键点:
- 使用优先队列可以优化搜索过程，但在这里使用普通队列已经足够。
- 通过 `costs` 字典避免重复访问高花费的节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E + V * k)，其中 E 是边的数量，V 是节点的数量，k 是最大中转次数。
空间复杂度: O(V + E)，用于存储图的邻接表和队列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict, deque


def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # 构建邻接表
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))
    
    # 初始化队列和 costs 字典
    queue = deque([(src, 0, 0)])  # (当前节点, 当前花费, 中转次数)
    costs = {src: 0}
    
    while queue:
        current, cost, stops = queue.popleft()
        
        if current == dst:
            return cost
        
        if stops > k:
            continue
        
        for neighbor, price in graph[current]:
            new_cost = cost + price
            if new_cost < costs.get(neighbor, float('inf')):
                costs[neighbor] = new_cost
                queue.append((neighbor, new_cost, stops + 1))
    
    return -1


Solution = create_solution(find_cheapest_price)