# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1816
标题: Lowest Common Ancestor of a Binary Tree IV
难度: medium
链接: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iv/
题目类型: 树、深度优先搜索、哈希表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1676. 二叉树的最近公共祖先 IV - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）找到所有目标节点，并记录每个节点的父节点。然后从目标节点向上回溯，找到第一个共同的祖先。

算法步骤:
1. 使用 DFS 遍历树，记录每个节点的父节点。
2. 从目标节点开始向上回溯，找到第一个共同的祖先。

关键点:
- 使用字典记录每个节点的父节点。
- 从目标节点向上回溯，找到第一个共同的祖先。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。我们需要遍历整棵树来记录每个节点的父节点，并且在最坏情况下需要遍历所有节点来找到最近公共祖先。
空间复杂度: O(n)，存储每个节点的父节点关系需要 O(n) 的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_lowest_common_ancestor(root: 'TreeNode', nodes: 'List[TreeNode]') -> 'Optional[TreeNode]':
    if not root or not nodes:
        return None

    # 记录每个节点的父节点
    parent = {root: None}
    stack = [root]
    target_nodes = set(nodes)

    while stack:
        node = stack.pop()
        if node in target_nodes:
            target_nodes.remove(node)
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
        if not target_nodes:
            break

    # 从目标节点开始向上回溯，找到第一个共同的祖先
    ancestors = set()
    for node in nodes:
        while node:
            if node in ancestors:
                return node
            ancestors.add(node)
            node = parent[node]

    return None

Solution = create_solution(find_lowest_common_ancestor)