# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100171
标题: Route Between Nodes LCCI
难度: medium
链接: https://leetcode.cn/problems/route-between-nodes-lcci/
题目类型: 深度优先搜索、广度优先搜索、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 04.01. 节点间通路 - 节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。 示例 1： 输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2 输出：true 示例 2： 输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4 输出：true 提示： 1. 节点数量n在[0, 1e5]范围内。 2. 节点编号大于等于 0 小于 n。 3. 图中可能存在自环和平行边。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来查找从起始节点到目标节点的路径。

算法步骤:
1. 构建图的邻接表表示。
2. 使用队列进行BFS遍历。
3. 如果在遍历过程中找到了目标节点，则返回True。
4. 如果遍历完所有可达节点仍未找到目标节点，则返回False。

关键点:
- 使用队列进行BFS遍历。
- 使用集合记录已访问的节点以避免重复访问。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(V + E)，其中V是节点数，E是边数。
空间复杂度: O(V)，用于存储访问过的节点和队列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(n: int, graph: List[List[int]], start: int, target: int) -> bool:
    """
    函数式接口 - 使用BFS查找从起始节点到目标节点的路径
    """
    # 构建图的邻接表
    adj_list = [[] for _ in range(n)]
    for u, v in graph:
        adj_list[u].append(v)
    
    # 使用队列进行BFS遍历
    from collections import deque
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    return False


Solution = create_solution(solution_function_name)