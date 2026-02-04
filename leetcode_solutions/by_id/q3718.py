# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3718
标题: Minimum Runes to Add to Cast Spell
难度: hard
链接: https://leetcode.cn/problems/minimum-runes-to-add-to-cast-spell/
题目类型: 深度优先搜索、广度优先搜索、并查集、图、拓扑排序、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3383. 施法所需最低符文数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用拓扑排序和动态规划来计算每个节点的最小符文需求。

算法步骤:
1. 构建图和入度表。
2. 初始化队列，将所有入度为0的节点加入队列。
3. 使用动态规划计算每个节点的最小符文需求。
4. 返回目标节点的最小符文需求。

关键点:
- 使用拓扑排序确保节点按依赖顺序处理。
- 动态规划状态转移方程：dp[node] = max(dp[node], dp[prev] + runes[node])
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(V + E)，其中 V 是节点数，E 是边数。
空间复杂度: O(V + E)，用于存储图和动态规划数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict, deque

def solution_function_name(n: int, connections: List[List[int]], runes: List[int]) -> int:
    """
    函数式接口 - 计算施法所需最低符文数量
    """
    # 构建图和入度表
    graph = defaultdict(list)
    in_degree = [0] * n
    for u, v in connections:
        graph[u].append(v)
        in_degree[v] += 1
    
    # 初始化队列，将所有入度为0的节点加入队列
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    
    # 动态规划数组
    dp = runes[:]
    
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            dp[next_node] = max(dp[next_node], dp[node] + runes[next_node])
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                queue.append(next_node)
    
    return dp[n - 1]

Solution = create_solution(solution_function_name)