# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1325
标题: Path with Maximum Probability
难度: medium
链接: https://leetcode.cn/problems/path-with-maximum-probability/
题目类型: 图、数组、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1514. 概率最大的路径 - 给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，其中 edges[i] = [a, b] 表示连接节点 a 和 b 的一条无向边，且该边遍历成功的概率为 succProb[i] 。 指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。 如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/07/12/1558_ex1.png] 输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2 输出：0.25000 解释：从起点到终点有两条路径，其中一条的成功概率为 0.2 ，而另一条为 0.5 * 0.5 = 0.25 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/07/12/1558_ex2.png] 输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2 输出：0.30000 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/07/12/1558_ex3.png] 输入：n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2 输出：0.00000 解释：节点 0 和 节点 2 之间不存在路径 提示： * 2 <= n <= 10^4 * 0 <= start, end < n * start != end * 0 <= a, b < n * a != b * 0 <= succProb.length == edges.length <= 2*10^4 * 0 <= succProb[i] <= 1 * 每两个节点之间最多有一条边
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Dijkstra 算法来找到从起点到终点的最大概率路径。我们将边的概率取负对数，这样可以将最大概率路径问题转化为最小路径和问题。

算法步骤:
1. 构建图的邻接表表示。
2. 初始化距离数组 `dist`，所有节点的距离初始化为负无穷，起点的距离初始化为 0。
3. 使用优先队列（最小堆）进行 Dijkstra 算法，每次从堆中取出当前距离最小的节点，并更新其邻居节点的距离。
4. 最后返回终点的距离，如果终点的距离仍为负无穷，则说明没有路径，返回 0。

关键点:
- 将概率取负对数，将最大概率路径问题转化为最小路径和问题。
- 使用优先队列优化 Dijkstra 算法。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log V)，其中 E 是边的数量，V 是节点的数量。优先队列的插入和删除操作的时间复杂度是 O(log V)。
空间复杂度: O(V + E)，存储图的邻接表和距离数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq
import math

def max_probability(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    # 构建图的邻接表表示
    graph = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        prob = -math.log(succProb[i])  # 取负对数
        graph[u].append((v, prob))
        graph[v].append((u, prob))

    # 初始化距离数组
    dist = [float('inf')] * n
    dist[start] = 0

    # 优先队列
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    # 返回结果
    return math.exp(-dist[end]) if dist[end] != float('inf') else 0

Solution = create_solution(max_probability)