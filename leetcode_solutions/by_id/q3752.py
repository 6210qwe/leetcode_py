# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3752
标题: Unit Conversion II
难度: medium
链接: https://leetcode.cn/problems/unit-conversion-ii/
题目类型: 深度优先搜索、广度优先搜索、图、数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3535. 单位转换 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用图的深度优先搜索（DFS）或广度优先搜索（BFS）来找到从一个单位到另一个单位的转换路径。

算法步骤:
1. 构建单位转换图。
2. 使用DFS或BFS找到从起始单位到目标单位的路径。
3. 根据路径计算转换值。

关键点:
- 使用邻接表表示单位转换图。
- 使用DFS或BFS遍历图，找到从起始单位到目标单位的路径。
- 计算路径上的转换值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(V + E)，其中V是单位的数量，E是单位转换关系的数量。在最坏情况下，我们需要遍历所有节点和边。
空间复杂度: O(V + E)，存储图的邻接表和递归调用栈的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(start: str, end: str, units: List[List[str]], values: List[float]) -> float:
    """
    函数式接口 - 实现单位转换
    """
    # 构建单位转换图
    graph = {}
    for i in range(len(units)):
        u, v = units[i]
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, values[i]))
        graph[v].append((u, 1 / values[i]))

    # 使用DFS查找从start到end的路径
    def dfs(node, target, visited, value):
        if node == target:
            return value
        visited.add(node)
        for neighbor, conversion in graph.get(node, []):
            if neighbor not in visited:
                result = dfs(neighbor, target, visited, value * conversion)
                if result is not None:
                    return result
        return None

    visited = set()
    result = dfs(start, end, visited, 1.0)
    return result if result is not None else -1.0

Solution = create_solution(solution_function_name)