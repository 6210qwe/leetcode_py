# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1229
标题: Shortest Path with Alternating Colors
难度: medium
链接: https://leetcode.cn/problems/shortest-path-with-alternating-colors/
题目类型: 广度优先搜索、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1129. 颜色交替的最短路径 - 给定一个整数 n，即有向图中的节点数，其中节点标记为 0 到 n - 1。图中的每条边为红色或者蓝色，并且可能存在自环或平行边。 给定两个数组 redEdges 和 blueEdges，其中： * redEdges[i] = [ai, bi] 表示图中存在一条从节点 ai 到节点 bi 的红色有向边， * blueEdges[j] = [uj, vj] 表示图中存在一条从节点 uj 到节点 vj 的蓝色有向边。 返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 answer[x] = -1。 示例 1： 输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = [] 输出：[0,1,-1] 示例 2： 输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]] 输出：[0,1,-1] 提示： * 1 <= n <= 100 * 0 <= redEdges.length, blueEdges.length <= 400 * redEdges[i].length == blueEdges[j].length == 2 * 0 <= ai, bi, uj, vj < n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来找到从节点 0 到其他节点的最短路径，并确保路径上的边颜色交替。

算法步骤:
1. 构建图的邻接表表示。
2. 初始化队列，将起点 (0, 'red') 和 (0, 'blue') 放入队列。
3. 使用 BFS 进行遍历，同时记录每个节点在两种颜色路径下的最短距离。
4. 如果当前节点的颜色与上一个节点的颜色不同，则继续遍历。
5. 更新结果数组，记录每个节点的最短路径长度。

关键点:
- 使用队列进行 BFS 遍历。
- 通过颜色交替来确保路径的有效性。
- 使用两个字典分别记录红色和蓝色路径的最短距离。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + E)，其中 n 是节点数，E 是边数。
空间复杂度: O(n + E)，用于存储图的邻接表和队列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import deque, defaultdict

def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    # 构建图的邻接表表示
    graph = defaultdict(lambda: {'red': [], 'blue': []})
    for u, v in redEdges:
        graph[u]['red'].append(v)
    for u, v in blueEdges:
        graph[u]['blue'].append(v)

    # 初始化结果数组
    result = [-1] * n
    result[0] = 0

    # 初始化队列
    queue = deque([(0, 'red', 0), (0, 'blue', 0)])
    visited = set([(0, 'red'), (0, 'blue')])

    while queue:
        node, color, distance = queue.popleft()

        # 更新结果数组
        if result[node] == -1 or result[node] > distance:
            result[node] = distance

        # 获取下一个颜色
        next_color = 'blue' if color == 'red' else 'red'

        # 遍历相邻节点
        for neighbor in graph[node][color]:
            if (neighbor, next_color) not in visited:
                visited.add((neighbor, next_color))
                queue.append((neighbor, next_color, distance + 1))

    return result

Solution = create_solution(shortestAlternatingPaths)