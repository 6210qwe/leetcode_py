# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2739
标题: Minimize the Total Price of the Trips
难度: hard
链接: https://leetcode.cn/problems/minimize-the-total-price-of-the-trips/
题目类型: 树、深度优先搜索、图、数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2646. 最小化旅行的价格总和 - 现有一棵无向、无根的树，树中有 n 个节点，按从 0 到 n - 1 编号。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条边。 每个节点都关联一个价格。给你一个整数数组 price ，其中 price[i] 是第 i 个节点的价格。 给定路径的 价格总和 是该路径上所有节点的价格之和。 另给你一个二维整数数组 trips ，其中 trips[i] = [starti, endi] 表示您从节点 starti 开始第 i 次旅行，并通过任何你喜欢的路径前往节点 endi 。 在执行第一次旅行之前，你可以选择一些 非相邻节点 并将价格减半。 返回执行所有旅行的最小价格总和。 示例 1： [https://assets.leetcode.com/uploads/2023/03/16/diagram2.png] 输入：n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]] 输出：23 解释： 上图表示将节点 2 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 、2 和 3 并使其价格减半后的树。 第 1 次旅行，选择路径 [0,1,3] 。路径的价格总和为 1 + 2 + 3 = 6 。 第 2 次旅行，选择路径 [2,1] 。路径的价格总和为 2 + 5 = 7 。 第 3 次旅行，选择路径 [2,1,3] 。路径的价格总和为 5 + 2 + 3 = 10 。 所有旅行的价格总和为 6 + 7 + 10 = 23 。可以证明，23 是可以实现的最小答案。 示例 2： [https://assets.leetcode.com/uploads/2023/03/16/diagram3.png] 输入：n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]] 输出：1 解释： 上图表示将节点 0 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 并使其价格减半后的树。 第 1 次旅行，选择路径 [0] 。路径的价格总和为 1 。 所有旅行的价格总和为 1 。可以证明，1 是可以实现的最小答案。 提示： * 1 <= n <= 50 * edges.length == n - 1 * 0 <= ai, bi <= n - 1 * edges 表示一棵有效的树 * price.length == n * price[i] 是一个偶数 * 1 <= price[i] <= 1000 * 1 <= trips.length <= 100 * 0 <= starti, endi <= n - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来找到每条旅行路径上的节点，并计算每个节点的访问次数。然后使用动态规划 (DP) 来决定哪些节点的价格需要减半以最小化总价格。

算法步骤:
1. 构建树的邻接表表示。
2. 对于每条旅行路径，使用 DFS 找到路径上的所有节点，并记录每个节点的访问次数。
3. 计算每个节点的总价格（即访问次数乘以节点价格）。
4. 使用 DP 来决定哪些节点的价格需要减半，以确保非相邻节点的价格减半。
5. 返回最小化后的总价格。

关键点:
- 使用 DFS 找到每条路径上的节点。
- 使用 DP 来决定哪些节点的价格需要减半。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是节点数，m 是旅行路径数。构建邻接表和处理每条旅行路径的时间复杂度是 O(n + m)。
空间复杂度: O(n)，用于存储邻接表、访问次数和 DP 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def find_path(graph, node, end, path, visited):
    if node == end:
        return True
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            path.append(neighbor)
            if find_path(graph, neighbor, end, path, visited):
                return True
            path.pop()
    return False

def dfs(graph, node, parent, count, freq):
    for neighbor in graph[node]:
        if neighbor != parent:
            freq[neighbor] += count
            dfs(graph, neighbor, node, count, freq)

def dp(node, parent, price, freq, memo):
    if (node, parent) in memo:
        return memo[(node, parent)]
    half_price = (price[node] // 2) * freq[node]
    full_price = price[node] * freq[node]
    
    for neighbor in graph[node]:
        if neighbor != parent:
            half_price += dp(neighbor, node, price, freq, memo)[0]
            full_price += min(dp(neighbor, node, price, freq, memo))
    
    memo[(node, parent)] = (half_price, full_price)
    return (half_price, full_price)

def solution_function_name(n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
    # 构建邻接表
    global graph
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # 记录每个节点的访问次数
    freq = [0] * n
    for start, end in trips:
        path = [start]
        visited = {start}
        if find_path(graph, start, end, path, visited):
            for node in path:
                freq[node] += 1
    
    # 动态规划求解
    memo = {}
    root = 0
    total_cost = min(dp(root, -1, price, freq, memo))
    return total_cost

Solution = create_solution(solution_function_name)