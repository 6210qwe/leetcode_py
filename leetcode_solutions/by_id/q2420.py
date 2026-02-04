# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2420
标题: Closest Node to Path in Tree
难度: hard
链接: https://leetcode.cn/problems/closest-node-to-path-in-tree/
题目类型: 树、深度优先搜索、广度优先搜索、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2277. 树中最接近路径的节点 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用DFS和LCA（最近公共祖先）来找到最接近路径的节点。

算法步骤:
1. 构建树的父节点映射。
2. 使用DFS找到从根节点到每个目标节点的路径。
3. 找到这些路径的LCA。
4. 计算每个查询节点到LCA的距离，并返回最小距离对应的节点。

关键点:
- 使用DFS构建父节点映射，以便快速查找路径。
- 使用LCA来找到多个路径的最近公共祖先。
- 计算节点到LCA的距离，选择最小距离的节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q * log n)，其中n是节点数，q是查询数。构建父节点映射和路径查找的时间复杂度为O(n)，每次查询的时间复杂度为O(log n)。
空间复杂度: O(n)，存储父节点映射和路径需要O(n)的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_closest_node_to_path(n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
    # 构建树的邻接表
    tree = [[] for _ in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # 构建父节点映射
    parent = [None] * n
    def dfs(node, par):
        parent[node] = par
        for child in tree[node]:
            if child != par:
                dfs(child, node)
    dfs(0, -1)
    
    # 查找从根节点到目标节点的路径
    def get_path(node):
        path = []
        while node != -1:
            path.append(node)
            node = parent[node]
        return path
    
    # 找到两个路径的最近公共祖先
    def lca(path1, path2):
        i, j = len(path1) - 1, len(path2) - 1
        while i >= 0 and j >= 0 and path1[i] == path2[j]:
            i -= 1
            j -= 1
        return path1[i + 1]
    
    # 计算节点到LCA的距离
    def distance_to_lca(node, lca):
        dist = 0
        while node != lca:
            node = parent[node]
            dist += 1
        return dist
    
    result = []
    for start, end, node in query:
        path_start = get_path(start)
        path_end = get_path(end)
        common_ancestor = lca(path_start, path_end)
        dist_start = distance_to_lca(node, common_ancestor)
        dist_end = distance_to_lca(node, common_ancestor)
        if dist_start < dist_end:
            result.append(start)
        else:
            result.append(end)
    
    return result

Solution = create_solution(find_closest_node_to_path)