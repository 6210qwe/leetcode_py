# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2627
标题: Difference Between Maximum and Minimum Price Sum
难度: hard
链接: https://leetcode.cn/problems/difference-between-maximum-and-minimum-price-sum/
题目类型: 树、深度优先搜索、数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2538. 最大价值和与最小价值和的差值 - 给你一个 n 个节点的无向无根图，节点编号为 0 到 n - 1 。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间有一条边。 每个节点都有一个价值。给你一个整数数组 price ，其中 price[i] 是第 i 个节点的价值。 一条路径的 价值和 是这条路径上所有节点的价值之和。 你可以选择树中任意一个节点作为根节点 root 。选择 root 为根的 开销 是以 root 为起点的所有路径中，价值和 最大的一条路径与最小的一条路径的差值。 请你返回所有节点作为根节点的选择中，最大 的 开销 为多少。 示例 1： [https://assets.leetcode.com/uploads/2022/12/01/example14.png] 输入：n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5] 输出：24 解释：上图展示了以节点 2 为根的树。左图（红色的节点）是最大价值和路径，右图（蓝色的节点）是最小价值和路径。 - 第一条路径节点为 [2,1,3,4]：价值为 [7,8,6,10] ，价值和为 31 。 - 第二条路径节点为 [2] ，价值为 [7] 。 最大路径和与最小路径和的差值为 24 。24 是所有方案中的最大开销。 示例 2： [https://assets.leetcode.com/uploads/2022/11/24/p1_example2.png] 输入：n = 3, edges = [[0,1],[1,2]], price = [1,1,1] 输出：2 解释：上图展示了以节点 0 为根的树。左图（红色的节点）是最大价值和路径，右图（蓝色的节点）是最小价值和路径。 - 第一条路径包含节点 [0,1,2]：价值为 [1,1,1] ，价值和为 3 。 - 第二条路径节点为 [0] ，价值为 [1] 。 最大路径和与最小路径和的差值为 2 。2 是所有方案中的最大开销。 提示： * 1 <= n <= 105 * edges.length == n - 1 * 0 <= ai, bi <= n - 1 * edges 表示一棵符合题面要求的树。 * price.length == n * 1 <= price[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两次深度优先搜索 (DFS) 来计算每个节点的最大路径和和最小路径和。

算法步骤:
1. 构建邻接表表示树。
2. 第一次 DFS 计算每个节点的最大路径和。
3. 第二次 DFS 计算每个节点的最小路径和。
4. 遍历所有节点，计算每个节点作为根节点时的最大开销，并返回最大值。

关键点:
- 使用两次 DFS 分别计算最大路径和和最小路径和。
- 通过维护父节点信息来避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def max_min_price_sum(n: int, edges: List[List[int]], price: List[int]) -> int:
    # 构建邻接表
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # 第一次 DFS 计算每个节点的最大路径和
    def dfs_max(node: int, parent: int) -> int:
        max_sum = price[node]
        for neighbor in adj_list[node]:
            if neighbor != parent:
                max_sum = max(max_sum, price[node] + dfs_max(neighbor, node))
        return max_sum

    # 第二次 DFS 计算每个节点的最小路径和
    def dfs_min(node: int, parent: int) -> int:
        min_sum = price[node]
        for neighbor in adj_list[node]:
            if neighbor != parent:
                min_sum = min(min_sum, price[node] + dfs_min(neighbor, node))
        return min_sum

    # 计算每个节点作为根节点时的最大开销
    max_cost = 0
    for i in range(n):
        max_path_sum = dfs_max(i, -1)
        min_path_sum = dfs_min(i, -1)
        max_cost = max(max_cost, max_path_sum - min_path_sum)

    return max_cost

Solution = create_solution(max_min_price_sum)