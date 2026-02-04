# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1986
标题: Largest Color Value in a Directed Graph
难度: hard
链接: https://leetcode.cn/problems/largest-color-value-in-a-directed-graph/
题目类型: 图、拓扑排序、记忆化搜索、哈希表、动态规划、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1857. 有向图中最大颜色值 - 给你一个 有向图 ，它含有 n 个节点和 m 条边。节点编号从 0 到 n - 1 。 给你一个字符串 colors ，其中 colors[i] 是小写英文字母，表示图中第 i 个节点的 颜色 （下标从 0 开始）。同时给你一个二维数组 edges ，其中 edges[j] = [aj, bj] 表示从节点 aj 到节点 bj 有一条 有向边 。 图中一条有效 路径 是一个点序列 x1 -> x2 -> x3 -> ... -> xk ，对于所有 1 <= i < k ，从 xi 到 xi+1 在图中有一条有向边。路径的 颜色值 是路径中 出现次数最多 颜色的节点数目。 请你返回给定图中有效路径里面的 最大颜色值 。如果图中含有环，请返回 -1 。 示例 1： [https://assets.leetcode.com/uploads/2021/04/21/leet1.png] 输入：colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]] 输出：3 解释：路径 0 -> 2 -> 3 -> 4 含有 3 个颜色为 "a" 的节点（上图中的红色节点）。 示例 2： [https://assets.leetcode.com/uploads/2021/04/21/leet2.png] 输入：colors = "a", edges = [[0,0]] 输出：-1 解释：从 0 到 0 有一个环。 提示： * n == colors.length * m == edges.length * 1 <= n <= 105 * 0 <= m <= 105 * colors 只含有小写英文字母。 * 0 <= aj, bj < n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用拓扑排序和动态规划来解决这个问题。首先通过拓扑排序判断图中是否有环，如果有环则直接返回 -1。然后使用动态规划来计算每个节点的最大颜色值。

算法步骤:
1. 构建图的邻接表表示，并记录每个节点的入度。
2. 使用队列进行拓扑排序，初始化队列为所有入度为 0 的节点。
3. 如果在拓扑排序过程中无法遍历所有节点，则说明图中有环，返回 -1。
4. 使用动态规划计算每个节点的最大颜色值。dp[node][color] 表示从起点到 node 节点路径中颜色 color 的最大出现次数。
5. 更新 dp 数组，并在每次更新时维护全局最大颜色值。

关键点:
- 使用拓扑排序判断图中是否有环。
- 使用动态规划计算每个节点的最大颜色值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是节点数，m 是边数。构建图的邻接表和入度数组的时间复杂度是 O(m)，拓扑排序的时间复杂度是 O(n + m)。
空间复杂度: O(n + m)，存储图的邻接表和入度数组的空间复杂度是 O(m)，存储 dp 数组的空间复杂度是 O(26n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def largest_color_value_in_directed_graph(colors: str, edges: List[List[int]]) -> int:
    n = len(colors)
    graph = [[] for _ in range(n)]
    in_degree = [0] * n
    dp = [[0] * 26 for _ in range(n)]
    
    # 构建图的邻接表和入度数组
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # 初始化队列，包含所有入度为 0 的节点
    queue = [u for u in range(n) if in_degree[u] == 0]
    
    # 拓扑排序
    visited = 0
    while queue:
        u = queue.pop(0)
        visited += 1
        color_idx = ord(colors[u]) - ord('a')
        dp[u][color_idx] = max(dp[u][color_idx], 1)
        
        for v in graph[u]:
            for c in range(26):
                dp[v][c] = max(dp[v][c], dp[u][c])
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # 如果不能遍历所有节点，说明图中有环
    if visited != n:
        return -1
    
    # 计算最大颜色值
    max_color_value = max(max(dp[u]) for u in range(n))
    return max_color_value


Solution = create_solution(largest_color_value_in_directed_graph)