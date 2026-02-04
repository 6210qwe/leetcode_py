# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2880
标题: Find the Closest Marked Node
难度: medium
链接: https://leetcode.cn/problems/find-the-closest-marked-node/
题目类型: 图、数组、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2737. 找到最近的标记节点 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）从每个节点开始，找到最近的标记节点。

算法步骤:
1. 初始化一个队列，将所有标记节点加入队列。
2. 使用一个字典记录每个节点到最近标记节点的距离。
3. 从队列中取出节点，更新其邻居节点的距离，并将未访问过的邻居节点加入队列。
4. 重复步骤3直到队列为空。
5. 返回距离字典。

关键点:
- 使用BFS可以确保找到的路径是最短的。
- 使用字典记录距离可以避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中n是节点数，m是边数。每个节点和每条边最多访问一次。
空间复杂度: O(n + m)，队列和距离字典的空间开销。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_closest_marked_node(n: int, edges: List[List[int]], marked: List[int]) -> List[int]:
    """
    函数式接口 - 找到每个节点到最近标记节点的距离
    """
    from collections import deque, defaultdict

    # 构建图
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 初始化队列和距离字典
    queue = deque(marked)
    distances = {i: float('inf') for i in range(n)}
    for node in marked:
        distances[node] = 0

    # BFS
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return [distances[i] for i in range(n)]


Solution = create_solution(find_closest_marked_node)