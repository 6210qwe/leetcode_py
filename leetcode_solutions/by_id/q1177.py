# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1177
标题: Tree Diameter
难度: medium
链接: https://leetcode.cn/problems/tree-diameter/
题目类型: 树、深度优先搜索、广度优先搜索、图、拓扑排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一棵树，树中的节点数为 n。每个节点都有一个唯一的整数编号，范围从 0 到 n-1。
您将获得一个列表 edges，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条边。
返回树的直径，即树中最长路径的长度（不一定经过根节点）。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来计算树的直径。

算法步骤:
1. 构建邻接表表示树。
2. 定义一个递归函数 dfs，用于计算从当前节点出发的最大深度。
3. 在 dfs 函数中，遍历当前节点的所有邻居节点，并递归计算其最大深度。
4. 计算当前节点的最大深度，并更新全局变量 max_diameter。
5. 返回当前节点的最大深度。

关键点:
- 使用邻接表表示树。
- 通过两次 DFS 计算树的直径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是节点数。每个节点和边都只会被访问一次。
空间复杂度: O(n)，存储邻接表和递归调用栈的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def treeDiameter(edges: List[List[int]]) -> int:
    if not edges:
        return 0
    
    # 构建邻接表
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    
    max_diameter = [0]
    
    def dfs(node: int, parent: int) -> int:
        max_depth = 0
        second_max_depth = 0
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            depth = dfs(neighbor, node)
            if depth > max_depth:
                second_max_depth = max_depth
                max_depth = depth
            elif depth > second_max_depth:
                second_max_depth = depth
        
        max_diameter[0] = max(max_diameter[0], max_depth + second_max_depth)
        
        return max_depth + 1
    
    dfs(0, -1)
    
    return max_diameter[0]

Solution = create_solution(treeDiameter)