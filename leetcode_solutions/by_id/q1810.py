# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1810
标题: Change the Root of a Binary Tree
难度: medium
链接: https://leetcode.cn/problems/change-the-root-of-a-binary-tree/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1666. 改变二叉树的根节点 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 找到目标节点，并重新构建树结构。

算法步骤:
1. 定义一个递归函数 `dfs` 来遍历树，找到目标节点并记录路径。
2. 如果找到目标节点，记录其父节点和子节点。
3. 重新构建树结构，将目标节点作为新的根节点。
4. 返回新的根节点。

关键点:
- 使用递归遍历树，找到目标节点并记录路径。
- 重新构建树结构时，需要处理好新根节点的左右子树。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。我们需要遍历整个树来找到目标节点。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def change_root(root: Optional[TreeNode], new_root_val: int) -> Optional[TreeNode]:
    """
    改变二叉树的根节点，使指定值的新节点成为新的根节点。
    """
    if not root:
        return None

    # 用于存储目标节点及其父节点
    target_node = None
    parent_node = None

    def dfs(node: Optional[TreeNode], parent: Optional[TreeNode]):
        nonlocal target_node, parent_node
        if not node:
            return
        if node.val == new_root_val:
            target_node = node
            parent_node = parent
            return
        dfs(node.left, node)
        dfs(node.right, node)

    # 找到目标节点
    dfs(root, None)

    if not target_node:
        return root  # 如果没有找到目标节点，返回原树

    # 重新构建树结构
    if parent_node:
        if parent_node.left == target_node:
            parent_node.left = None
        else:
            parent_node.right = None

    target_node.left = root if target_node != root else target_node.left
    target_node.right = None

    return target_node

Solution = create_solution(change_root)