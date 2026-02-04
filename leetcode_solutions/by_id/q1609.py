# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1609
标题: Find All The Lonely Nodes
难度: easy
链接: https://leetcode.cn/problems/find-all-the-lonely-nodes/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1469. 寻找所有的独生节点 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 遍历二叉树，找到所有只有一个子节点的节点，并记录这些节点的唯一子节点。

算法步骤:
1. 定义一个递归函数 `dfs` 来遍历二叉树。
2. 在每个节点上检查其左右子节点：
   - 如果该节点只有一个子节点，则将该子节点加入结果列表。
   - 递归调用 `dfs` 函数遍历左子树和右子树。
3. 返回结果列表。

关键点:
- 使用递归进行深度优先搜索。
- 只有当一个节点只有一个子节点时，才将其子节点加入结果列表。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数。每个节点只被访问一次。
空间复杂度: O(h)，其中 h 是二叉树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_lonely_nodes(root: Optional[TreeNode]) -> List[int]:
    """
    找到所有的独生节点
    """
    def dfs(node: Optional[TreeNode], lonely_nodes: List[int]):
        if not node:
            return
        # 检查当前节点是否只有一个子节点
        if (node.left and not node.right) or (not node.left and node.right):
            if node.left:
                lonely_nodes.append(node.left.val)
            if node.right:
                lonely_nodes.append(node.right.val)
        # 递归遍历左子树和右子树
        dfs(node.left, lonely_nodes)
        dfs(node.right, lonely_nodes)

    lonely_nodes = []
    dfs(root, lonely_nodes)
    return lonely_nodes

Solution = create_solution(find_lonely_nodes)