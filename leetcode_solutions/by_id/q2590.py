# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2590
标题: Maximum Star Sum of a Graph
难度: medium
链接: https://leetcode.cn/problems/maximum-star-sum-of-a-graph/
题目类型: 贪心、图、数组、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2497. 图中最大星和 - 给你一个 n 个点的无向图，节点从 0 到 n - 1 编号。给你一个长度为 n 下标从 0 开始的整数数组 vals ，其中 vals[i] 表示第 i 个节点的值。 同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条双向边。 星图 是给定图中的一个子图，它包含一个中心节点和 0 个或更多个邻居。换言之，星图是给定图中一个边的子集，且这些边都有一个公共节点。 下图分别展示了有 3 个和 4 个邻居的星图，蓝色节点为中心节点。 [https://assets.leetcode.com/uploads/2022/11/07/max-star-sum-descdrawio.png] 星和 定义为星图中所有节点值的和。 给你一个整数 k ，请你返回 至多 包含 k 条边的星图中的 最大星和 。 示例 1： [https://assets.leetcode.com/uploads/2022/11/07/max-star-sum-example1drawio.png] 输入：vals = [1,2,3,4,10,-10,-20], edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], k = 2 输出：16 解释：上图展示了输入示例。 最大星和对应的星图在上图中用蓝色标出。中心节点是 3 ，星图中还包含邻居 1 和 4 。 无法得到一个和大于 16 且边数不超过 2 的星图。 示例 2： 输入：vals = [-5], edges = [], k = 0 输出：-5 解释：只有一个星图，就是节点 0 自己。 所以我们返回 -5 。 提示： * n == vals.length * 1 <= n <= 105 * -104 <= vals[i] <= 104 * 0 <= edges.length <= min(n * (n - 1) / 2, 105) * edges[i].length == 2 * 0 <= ai, bi <= n - 1 * ai != bi * 0 <= k <= n - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，对于每个节点，选择其最大的 k 个邻居节点值进行累加。

算法步骤:
1. 构建邻接表表示图。
2. 对于每个节点，获取其所有邻居节点的值，并选择最大的 k 个邻居节点值。
3. 计算每个节点的最大星和，并记录全局最大值。

关键点:
- 使用邻接表来存储图的结构。
- 使用堆来选择每个节点的前 k 大邻居节点值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m log k)，其中 n 是节点数，m 是边数，k 是最大邻居数。
空间复杂度: O(n + m)，用于存储邻接表和堆。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import heapq

def solution_function_name(vals: List[int], edges: List[List[int]], k: int) -> int:
    """
    函数式接口 - 返回至多包含 k 条边的星图中的最大星和
    """
    n = len(vals)
    graph = [[] for _ in range(n)]
    
    # 构建邻接表
    for u, v in edges:
        if vals[v] > 0:
            heapq.heappush(graph[u], vals[v])
            if len(graph[u]) > k:
                heapq.heappop(graph[u])
        if vals[u] > 0:
            heapq.heappush(graph[v], vals[u])
            if len(graph[v]) > k:
                heapq.heappop(graph[v])
    
    # 计算最大星和
    max_star_sum = float('-inf')
    for i in range(n):
        star_sum = vals[i] + sum(graph[i])
        max_star_sum = max(max_star_sum, star_sum)
    
    return max_star_sum

Solution = create_solution(solution_function_name)