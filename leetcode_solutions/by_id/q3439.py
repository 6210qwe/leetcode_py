# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3439
标题: Find Minimum Diameter After Merging Two Trees
难度: hard
链接: https://leetcode.cn/problems/find-minimum-diameter-after-merging-two-trees/
题目类型: 树、深度优先搜索、广度优先搜索、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3203. 合并两棵树后的最小直径 - 给你两棵 无向 树，分别有 n 和 m 个节点，节点编号分别为 0 到 n - 1 和 0 到 m - 1 。给你两个二维整数数组 edges1 和 edges2 ，长度分别为 n - 1 和 m - 1 ，其中 edges1[i] = [ai, bi] 表示在第一棵树中节点 ai 和 bi 之间有一条边，edges2[i] = [ui, vi] 表示在第二棵树中节点 ui 和 vi 之间有一条边。 你必须在第一棵树和第二棵树中分别选一个节点，并用一条边连接它们。 请你返回添加边后得到的树中，最小直径 为多少。 一棵树的 直径 指的是树中任意两个节点之间的最长路径长度。 示例 1：[https://assets.leetcode.com/uploads/2024/04/22/example11-transformed.png] 输入：edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]] 输出：3 解释： 将第一棵树中的节点 0 与第二棵树中的任意节点连接，得到一棵直径为 3 的树。 示例 2：[https://assets.leetcode.com/uploads/2024/04/22/example211.png] 输入：edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]] 输出：5 解释： 将第一棵树中的节点 0 和第二棵树中的节点 0 连接，可以得到一棵直径为 5 的树。 提示： * 1 <= n, m <= 105 * edges1.length == n - 1 * edges2.length == m - 1 * edges1[i].length == edges2[i].length == 2 * edges1[i] = [ai, bi] * 0 <= ai, bi < n * edges2[i] = [ui, vi] * 0 <= ui, vi < m * 输入保证 edges1 和 edges2 分别表示一棵合法的树。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 计算每棵树的直径。
2. 计算每棵树的每个节点到最远节点的距离。
3. 通过合并两棵树的任意节点，找到最小的合并后树的直径。

算法步骤:
1. 使用DFS计算每棵树的直径。
2. 使用DFS计算每棵树的每个节点到最远节点的距离。
3. 通过遍历所有可能的节点对，找到最小的合并后树的直径。

关键点:
- 通过两次DFS计算每棵树的直径和每个节点到最远节点的距离。
- 通过合并两棵树的任意节点，找到最小的合并后树的直径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)
空间复杂度: O(n + m)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional

def find_farthest_node(tree, start):
    def dfs(node, parent, depth):
        if depth > farthest_depth[0]:
            farthest_depth[0] = depth
            farthest_node[0] = node
        for neighbor in tree[node]:
            if neighbor != parent:
                dfs(neighbor, node, depth + 1)

    farthest_depth = [0]
    farthest_node = [start]
    dfs(start, -1, 0)
    return farthest_node[0], farthest_depth[0]

def calculate_diameter_and_distances(tree, n):
    # 找到最远的节点
    farthest_node, _ = find_farthest_node(tree, 0)
    # 从最远的节点开始再找一次最远的节点，得到直径
    _, diameter = find_farthest_node(tree, farthest_node)
    
    # 计算每个节点到最远节点的距离
    distances = [0] * n
    def dfs(node, parent, depth):
        distances[node] = depth
        for neighbor in tree[node]:
            if neighbor != parent:
                dfs(neighbor, node, depth + 1)
    
    dfs(farthest_node, -1, 0)
    return diameter, distances

def find_min_diameter(edges1, edges2):
    n = len(edges1) + 1
    m = len(edges2) + 1
    
    # 构建邻接表
    tree1 = [[] for _ in range(n)]
    tree2 = [[] for _ in range(m)]
    
    for u, v in edges1:
        tree1[u].append(v)
        tree1[v].append(u)
    
    for u, v in edges2:
        tree2[u].append(v)
        tree2[v].append(u)
    
    # 计算每棵树的直径和每个节点到最远节点的距离
    diameter1, distances1 = calculate_diameter_and_distances(tree1, n)
    diameter2, distances2 = calculate_diameter_and_distances(tree2, m)
    
    # 通过合并两棵树的任意节点，找到最小的合并后树的直径
    min_diameter = float('inf')
    for i in range(n):
        for j in range(m):
            new_diameter = max(diameter1, diameter2, distances1[i] + distances2[j] + 1)
            min_diameter = min(min_diameter, new_diameter)
    
    return min_diameter

Solution = create_solution(find_min_diameter)