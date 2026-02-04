# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3486
标题: Count the Number of Good Nodes
难度: medium
链接: https://leetcode.cn/problems/count-the-number-of-good-nodes/
题目类型: 树、深度优先搜索
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3249. 统计好节点的数目 - 现有一棵 无向 树，树中包含 n 个节点，按从 0 到 n - 1 标记。树的根节点是节点 0 。给你一个长度为 n - 1 的二维整数数组 edges，其中 edges[i] = [ai, bi] 表示树中节点 ai 与节点 bi 之间存在一条边。 如果一个节点的所有子节点为根的 子树 包含的节点数相同，则认为该节点是一个 好节点。 返回给定树中 好节点 的数量。 子树 指的是一个节点以及它所有后代节点构成的一棵树。 示例 1： 输入：edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]] 输出：7 说明： [https://assets.leetcode.com/uploads/2024/05/26/tree1.png] 树的所有节点都是好节点。 示例 2： 输入：edges = [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]] 输出：6 说明： [https://assets.leetcode.com/uploads/2024/06/03/screenshot-2024-06-03-193552.png] 树中有 6 个好节点。上图中已将这些节点着色。 示例 3： 输入：edges = [[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]] 输出：12 解释： [https://assets.leetcode.com/uploads/2024/08/08/rob.jpg] 除了节点 9 以外其他所有节点都是好节点。 提示： * 2 <= n <= 105 * edges.length == n - 1 * edges[i].length == 2 * 0 <= ai, bi < n * 输入确保 edges 总表示一棵有效的树。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来计算每个节点的子树大小，并检查每个节点是否是好节点。

算法步骤:
1. 构建树的邻接表表示。
2. 使用 DFS 计算每个节点的子树大小。
3. 在回溯过程中，检查当前节点是否是好节点。
4. 返回好节点的数量。

关键点:
- 使用邻接表表示树结构。
- 通过 DFS 计算子树大小并检查好节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是节点数。每个节点和边都只访问一次。
空间复杂度: O(n)，用于存储邻接表和递归调用栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def count_good_nodes(edges: List[List[int]]) -> int:
    """
    函数式接口 - 统计给定树中的好节点数量
    """
    def dfs(node: int, parent: int) -> int:
        subtree_size = 1  # 当前节点自身
        subtree_sizes = []
        
        for neighbor in adj_list[node]:
            if neighbor != parent:
                subtree_size += dfs(neighbor, node)
                subtree_sizes.append(subtree_size - 1)
        
        if all(size == subtree_sizes[0] for size in subtree_sizes) or not subtree_sizes:
            good_nodes[0] += 1
        
        return subtree_size
    
    n = len(edges) + 1
    adj_list = [[] for _ in range(n)]
    
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    good_nodes = [0]
    dfs(0, -1)
    
    return good_nodes[0]

Solution = create_solution(count_good_nodes)