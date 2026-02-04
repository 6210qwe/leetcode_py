# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2517
标题: Choose Edges to Maximize Score in a Tree
难度: medium
链接: https://leetcode.cn/problems/choose-edges-to-maximize-score-in-a-tree/
题目类型: 树、深度优先搜索、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一棵有 n 个节点的树，每个节点有一个权值。你需要选择一些边，使得选择的边形成一个连通子图，并且这个连通子图的权值和最大。返回这个最大权值和。

输入:
- n: 节点数
- edges: 边列表
- values: 每个节点的权值

输出:
- 最大权值和
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）结合动态规划（DP）来解决这个问题。对于每个节点，我们有两个选择：要么选择它并将其所有子节点的权值加起来，要么不选择它并递归地处理其子节点。

算法步骤:
1. 构建树的邻接表表示。
2. 定义一个 DFS 函数，该函数返回两个值：选择当前节点的最大权值和，以及不选择当前节点的最大权值和。
3. 在 DFS 函数中，对于每个子节点，递归调用 DFS 函数，计算选择和不选择该子节点的最大权值和。
4. 更新当前节点的选择和不选择的最大权值和。
5. 返回根节点的选择最大权值和。

关键点:
- 使用 DP 数组来存储中间结果，避免重复计算。
- 通过 DFS 递归地处理每个节点及其子节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是节点数。每个节点和每条边都只会被访问一次。
空间复杂度: O(n)，递归栈的深度最多为 n，同时使用了额外的 DP 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def maxScoreAfterOperations(n: int, edges: List[List[int]], values: List[int]) -> int:
    # 构建树的邻接表表示
    tree = [[] for _ in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    def dfs(node: int, parent: int) -> (int, int):
        # 选择当前节点的最大权值和
        choose = values[node]
        # 不选择当前节点的最大权值和
        not_choose = 0

        for child in tree[node]:
            if child == parent:
                continue
            child_choose, child_not_choose = dfs(child, node)
            choose += child_not_choose
            not_choose += max(child_choose, child_not_choose)

        return choose, not_choose

    # 从根节点开始 DFS
    root_choose, root_not_choose = dfs(0, -1)
    return max(root_choose, root_not_choose)

Solution = create_solution(maxScoreAfterOperations)