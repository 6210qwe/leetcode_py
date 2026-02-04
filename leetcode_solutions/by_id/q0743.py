# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 743
标题: Closest Leaf in a Binary Tree
难度: medium
链接: https://leetcode.cn/problems/closest-leaf-in-a-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一个二叉树，找到距离目标节点最近的叶节点。返回该叶节点的值。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）将树转换为无向图，然后使用广度优先搜索（BFS）从目标节点开始寻找最近的叶节点。

算法步骤:
1. 使用 DFS 将树转换为无向图，并记录每个节点的父节点。
2. 使用 BFS 从目标节点开始，逐层扩展，直到找到第一个叶节点。

关键点:
- 使用字典记录每个节点的邻接节点。
- 在 BFS 中，使用队列存储当前层的节点，并使用集合记录已访问的节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。DFS 和 BFS 的时间复杂度均为 O(n)。
空间复杂度: O(n)，需要额外的空间存储图和队列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_closest_leaf(root: TreeNode, target: int) -> int:
    # 构建无向图
    graph = {}
    def dfs(node, parent=None):
        if node is None:
            return
        if node not in graph:
            graph[node] = []
        if parent is not None:
            graph[node].append(parent)
            graph[parent].append(node)
        dfs(node.left, node)
        dfs(node.right, node)
    
    dfs(root)
    
    # 使用 BFS 寻找最近的叶节点
    from collections import deque
    queue = deque([target])
    visited = set([target])
    
    while queue:
        node = queue.popleft()
        if len(graph[node]) <= 1 and node != root:
            return node.val
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

Solution = create_solution(find_closest_leaf)