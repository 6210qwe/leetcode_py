# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2438
标题: Find Closest Node to Given Two Nodes
难度: medium
链接: https://leetcode.cn/problems/find-closest-node-to-given-two-nodes/
题目类型: 深度优先搜索、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2359. 找到离给定两个节点最近的节点 - 给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，每个节点 至多 有一条出边。 有向图用大小为 n 下标从 0 开始的数组 edges 表示，表示节点 i 有一条有向边指向 edges[i] 。如果节点 i 没有出边，那么 edges[i] == -1 。 同时给你两个节点 node1 和 node2 。 请你返回一个从 node1 和 node2 都能到达节点的编号，使节点 node1 和节点 node2 到这个节点的距离 较大值最小化。如果有多个答案，请返回 最小 的节点编号。如果答案不存在，返回 -1 。 注意 edges 可能包含环。 示例 1： [https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-2.png] 输入：edges = [2,2,3,-1], node1 = 0, node2 = 1 输出：2 解释：从节点 0 到节点 2 的距离为 1 ，从节点 1 到节点 2 的距离为 1 。 两个距离的较大值为 1 。我们无法得到一个比 1 更小的较大值，所以我们返回节点 2 。 示例 2： [https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-4.png] 输入：edges = [1,2,-1], node1 = 0, node2 = 2 输出：2 解释：节点 0 到节点 2 的距离为 2 ，节点 2 到它自己的距离为 0 。 两个距离的较大值为 2 。我们无法得到一个比 2 更小的较大值，所以我们返回节点 2 。 提示： * n == edges.length * 2 <= n <= 105 * -1 <= edges[i] < n * edges[i] != i * 0 <= node1, node2 < n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来计算从 node1 和 node2 出发到其他节点的距离，并找到满足条件的节点。

算法步骤:
1. 使用 DFS 计算从 node1 出发到所有可达节点的距离。
2. 使用 DFS 计算从 node2 出发到所有可达节点的距离。
3. 遍历所有节点，找到同时可从 node1 和 node2 到达的节点，并计算这些节点的最大距离。
4. 返回最大距离最小且节点编号最小的节点。

关键点:
- 使用 DFS 计算距离时，需要记录访问过的节点以避免重复计算。
- 在遍历所有节点时，使用集合操作来快速查找共同可达的节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 每个节点和边最多访问一次。
空间复杂度: O(n) - 需要存储从 node1 和 node2 出发到其他节点的距离。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def dfs(edges: List[int], node: int, dist: List[int]) -> None:
    while node != -1 and dist[node] == -1:
        next_node = edges[node]
        dist[node] = dist[next_node] + 1 if next_node != -1 else 0
        node = next_node

def find_closest_node(edges: List[int], node1: int, node2: int) -> int:
    n = len(edges)
    dist1 = [-1] * n
    dist2 = [-1] * n
    
    # Calculate distances from node1
    dfs(edges, node1, dist1)
    
    # Calculate distances from node2
    dfs(edges, node2, dist2)
    
    min_max_dist = float('inf')
    result_node = -1
    
    for i in range(n):
        if dist1[i] != -1 and dist2[i] != -1:
            max_dist = max(dist1[i], dist2[i])
            if max_dist < min_max_dist or (max_dist == min_max_dist and i < result_node):
                min_max_dist = max_dist
                result_node = i
    
    return result_node

Solution = create_solution(find_closest_node)