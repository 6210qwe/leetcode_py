# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1201
标题: Delete Tree Nodes
难度: medium
链接: https://leetcode.cn/problems/delete-tree-nodes/
题目类型: 树、深度优先搜索、广度优先搜索、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1273. 删除树节点 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用后序遍历（DFS）来计算每个子树的节点值之和，并根据条件删除节点。

算法步骤:
1. 定义一个递归函数 `dfs` 来进行后序遍历。
2. 在递归函数中，首先递归处理当前节点的所有子节点。
3. 计算当前子树的节点值之和。
4. 如果当前子树的节点值之和为 0，则删除该子树。
5. 返回当前子树的节点数和节点值之和。

关键点:
- 使用后序遍历可以确保在处理当前节点之前已经处理了所有子节点。
- 通过递归函数返回子树的节点数和节点值之和，方便判断是否需要删除子树。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只被访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def delete_tree_nodes(nodes: int, parent: List[int], value: List[int]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    # 构建树
    tree = [TreeNode(i) for i in range(nodes)]
    for i in range(1, nodes):
        tree[parent[i]].children.append(tree[i])
    
    def dfs(node: TreeNode) -> (int, int):
        total_nodes = 0
        total_value = node.val
        for child in node.children:
            child_nodes, child_value = dfs(child)
            total_nodes += child_nodes
            total_value += child_value
        if total_value == 0:
            return 0, 0
        return total_nodes + 1, total_value
    
    root = tree[0]
    remaining_nodes, _ = dfs(root)
    return remaining_nodes

Solution = create_solution(delete_tree_nodes)