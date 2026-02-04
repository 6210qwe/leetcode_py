# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000305
标题: 除法求值
难度: medium
链接: https://leetcode.cn/problems/vlzXQL/
题目类型: 深度优先搜索、广度优先搜索、并查集、图、数组、最短路
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 111. 除法求值 - 给定一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。 注意：输入总是有效的。可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。 示例 1： 输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]] 输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000] 解释： 条件：a / b = 2.0, b / c = 3.0 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 结果：[6.0, 0.5, -1.0, 1.0, -1.0 ] 示例 2： 输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]] 输出：[3.75000,0.40000,5.00000,0.20000] 示例 3： 输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]] 输出：[0.50000,2.00000,-1.00000,-1.00000] 提示： * 1 <= equations.length <= 20 * equations[i].length == 2 * 1 <= Ai.length, Bi.length <= 5 * values.length == equations.length * 0.0 < values[i] <= 20.0 * 1 <= queries.length <= 20 * queries[i].length == 2 * 1 <= Cj.length, Dj.length <= 5 * Ai, Bi, Cj, Dj 由小写英文字母与数字组成 注意：本题与主站 399 题相同： https://leetcode.cn/problems/evaluate-division/ [https://leetcode.cn/problems/evaluate-division/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用图的深度优先搜索（DFS）来解决这个问题。

算法步骤:
1. 构建图：使用字典存储每个节点及其邻居节点和对应的权重。
2. 对于每个查询，使用DFS来查找从起点到终点的路径，并计算路径上的权重乘积。
3. 如果找到路径，则返回路径上的权重乘积；否则返回-1.0。

关键点:
- 使用字典构建有向加权图。
- 使用DFS进行路径查找和权重计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E + Q * (V + E))，其中E是边的数量，Q是查询的数量，V是顶点的数量。每个查询需要遍历所有顶点和边。
空间复杂度: O(V + E)，用于存储图的结构。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    def build_graph(equations, values):
        graph = {}
        for (dividend, divisor), value in zip(equations, values):
            if dividend not in graph:
                graph[dividend] = {}
            if divisor not in graph:
                graph[divisor] = {}
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value
        return graph

    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                weight = dfs(neighbor, end, visited)
                if weight != -1.0:
                    return graph[start][neighbor] * weight
        return -1.0

    graph = build_graph(equations, values)
    results = []
    for query in queries:
        start, end = query
        result = dfs(start, end, set())
        results.append(result)
    return results

Solution = create_solution(calcEquation)