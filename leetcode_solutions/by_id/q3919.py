# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3919
标题: Network Recovery Pathways
难度: hard
链接: https://leetcode.cn/problems/network-recovery-pathways/
题目类型: 图、拓扑排序、数组、二分查找、动态规划、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3620. 恢复网络路径 - 给你一个包含 n 个节点（编号从 0 到 n - 1）的有向无环图。图由长度为 m 的二维数组 edges 表示，其中 edges[i] = [ui, vi, costi] 表示从节点 ui 到节点 vi 的单向通信，恢复成本为 costi。 一些节点可能处于离线状态。给定一个布尔数组 online，其中 online[i] = true 表示节点 i 在线。节点 0 和 n - 1 始终在线。 从 0 到 n - 1 的路径如果满足以下条件，那么它是 有效 的： * 路径上的所有中间节点都在线。 * 路径上所有边的总恢复成本不超过 k。 对于每条有效路径，其 分数 定义为该路径上的最小边成本。 返回所有有效路径中的 最大 路径分数（即最大 最小 边成本）。如果没有有效路径，则返回 -1。 示例 1: 输入: edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], online = [true,true,true,true], k = 10 输出: 3 解释: [https://assets.leetcode.com/uploads/2025/06/06/graph-10.png] * 图中有两条从节点 0 到节点 3 的可能路线： 1. 路径 0 → 1 → 3 * 总成本 = 5 + 10 = 15，超过了 k (15 > 10)，因此此路径无效。 2. 路径 0 → 2 → 3 * 总成本 = 3 + 4 = 7 <= k，因此此路径有效。 * 此路径上的最小边成本为 min(3, 4) = 3。 * 没有其他有效路径。因此，所有有效路径分数中的最大值为 3。 示例 2: 输入: edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [true,true,true,false,true], k = 12 输出: 6 解释: [https://assets.leetcode.com/uploads/2025/06/06/graph-11.png] * 节点 3 离线，因此任何通过 3 的路径都是无效的。 * 考虑从 0 到 4 的其余路线： 1. 路径 0 → 1 → 4 * 总成本 = 7 + 5 = 12 <= k，因此此路径有效。 * 此路径上的最小边成本为 min(7, 5) = 5。 2. 路径 0 → 2 → 3 → 4 * 节点 3 离线，因此无论成本多少，此路径无效。 3. 路径 0 → 2 → 4 * 总成本 = 6 + 6 = 12 <= k，因此此路径有效。 * 此路径上的最小边成本为 min(6, 6) = 6。 * 在两条有效路径中，它们的分数分别为 5 和 6。因此，答案是 6。 提示: * n == online.length * 2 <= n <= 5 * 104 * 0 <= m == edges.length <= min(105, n * (n - 1) / 2) * edges[i] = [ui, vi, costi] * 0 <= ui, vi < n * ui != vi * 0 <= costi <= 109 * 0 <= k <= 5 * 1013 * online[i] 是 true 或 false，且 online[0] 和 online[n - 1] 均为 true。 * 给定的图是一个有向无环图。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找和 Dijkstra 算法来找到满足条件的最大路径分数。

算法步骤:
1. 构建图的邻接表表示。
2. 使用二分查找来确定最大路径分数的范围。
3. 对于每个二分查找的中间值，使用 Dijkstra 算法来检查是否存在一条路径满足条件。
4. 如果存在满足条件的路径，则更新二分查找的下界；否则，更新上界。
5. 最终返回二分查找的结果。

关键点:
- 使用二分查找来缩小最大路径分数的范围。
- 使用 Dijkstra 算法来检查路径的有效性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((m + n) log C)，其中 m 是边的数量，n 是节点的数量，C 是边的成本范围。
空间复杂度: O(m + n)，用于存储图的邻接表和 Dijkstra 算法的辅助数据结构。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import heapq

def solution_function_name(edges: List[List[int]], online: List[bool], k: int) -> int:
    def dijkstra(max_cost: int) -> bool:
        # Dijkstra's algorithm to check if there is a valid path with minimum edge cost >= max_cost
        n = len(online)
        graph = [[] for _ in range(n)]
        for u, v, cost in edges:
            if online[u] and online[v] and cost >= max_cost:
                graph[u].append((v, cost))
        
        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]  # (cost, node)
        
        while pq:
            current_cost, u = heapq.heappop(pq)
            if u == n - 1:
                return True
            if current_cost > k:
                continue
            for v, cost in graph[u]:
                new_cost = current_cost + cost
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
        
        return False
    
    low, high = 0, 10**9
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if dijkstra(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return result

Solution = create_solution(solution_function_name)