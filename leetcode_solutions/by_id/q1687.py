# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1687
标题: The Most Similar Path in a Graph
难度: hard
链接: https://leetcode.cn/problems/the-most-similar-path-in-a-graph/
题目类型: 图、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1548. 图中最相似的路径 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义一个状态 `dp[i][j]` 表示从节点 `i` 到节点 `j` 的最相似路径的最小编辑距离。通过递归和记忆化搜索来计算每个状态。

算法步骤:
1. 初始化图的邻接表表示。
2. 定义一个递归函数 `dfs(i, j)` 来计算从节点 `i` 到节点 `j` 的最相似路径的最小编辑距离。
3. 使用记忆化搜索来存储已经计算过的状态，避免重复计算。
4. 递归地计算每个状态，并更新最小编辑距离。
5. 返回最终结果。

关键点:
- 使用记忆化搜索来优化递归过程，避免重复计算。
- 通过递归计算每个状态，并更新最小编辑距离。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m * k)，其中 n 是节点数，m 是边数，k 是路径长度。
空间复杂度: O(n * k)，用于存储记忆化搜索的状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def mostSimilar(n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
    # 构建邻接表
    graph = [[] for _ in range(n)]
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    # 记忆化搜索
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if j == len(targetPath):
            return 0, [i]
        min_cost = float('inf')
        best_path = []
        for neighbor in graph[i]:
            cost, path = dfs(neighbor, j + 1)
            if cost < min_cost:
                min_cost = cost
                best_path = path
        min_cost += (names[i] != targetPath[j])
        memo[(i, j)] = (min_cost, [i] + best_path)
        return memo[(i, j)]

    # 找到起点
    min_cost = float('inf')
    best_path = []
    for i in range(n):
        cost, path = dfs(i, 0)
        if cost < min_cost:
            min_cost = cost
            best_path = path
    return best_path

Solution = create_solution(mostSimilar)