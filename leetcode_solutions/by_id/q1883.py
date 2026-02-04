# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1883
标题: Find Distance in a Binary Tree
难度: medium
链接: https://leetcode.cn/problems/find-distance-in-a-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、哈希表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1740. 找到二叉树中的距离 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来找到两个节点的最近公共祖先 (LCA)，然后计算从 LCA 到两个节点的距离。

算法步骤:
1. 定义一个辅助函数 `find_lca`，使用 DFS 来找到两个节点的最近公共祖先 (LCA)。
2. 定义一个辅助函数 `find_distance`，使用 DFS 来计算从某个节点到目标节点的距离。
3. 计算从 LCA 到两个节点的距离之和。

关键点:
- 使用 DFS 来找到 LCA 和计算距离。
- 通过递归调用来遍历树。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点最多被访问两次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_lca(root: TreeNode, p: int, q: int) -> TreeNode:
    if not root or root.val == p or root.val == q:
        return root
    left = find_lca(root.left, p, q)
    right = find_lca(root.right, p, q)
    if left and right:
        return root
    return left if left else right

def find_distance(node: TreeNode, target: int, distance: int) -> int:
    if not node:
        return -1
    if node.val == target:
        return distance
    left_dist = find_distance(node.left, target, distance + 1)
    if left_dist != -1:
        return left_dist
    return find_distance(node.right, target, distance + 1)

def solution_function_name(root: TreeNode, p: int, q: int) -> int:
    """
    函数式接口 - 找到二叉树中两个节点之间的距离
    """
    lca = find_lca(root, p, q)
    dist_p = find_distance(lca, p, 0)
    dist_q = find_distance(lca, q, 0)
    return dist_p + dist_q

Solution = create_solution(solution_function_name)