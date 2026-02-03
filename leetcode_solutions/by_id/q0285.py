# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 285
标题: Inorder Successor in BST
难度: medium
链接: https://leetcode.cn/problems/inorder-successor-in-bst/
题目类型: 树、深度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
285. 二叉搜索树中的中序后继 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: BST特性，中序后继是右子树的最左节点或最近的祖先

算法步骤:
1. 如果p有右子树，后继是右子树的最左节点
2. 否则，后继是最近的祖先，且p在其左子树中

关键点:
- BST特性
- 时间复杂度O(h)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(h) - h为树高
空间复杂度: O(1) - 迭代实现
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def inorder_successor(root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    """
    函数式接口 - 二叉搜索树中的中序后继
    
    实现思路:
    BST特性：中序后继是右子树的最左节点或最近的祖先。
    
    Args:
        root: BST根节点
        p: 目标节点
        
    Returns:
        中序后继节点
        
    Example:
        >>> # 示例用法
    """
    # 如果p有右子树，后继是右子树的最左节点
    if p.right:
        node = p.right
        while node.left:
            node = node.left
        return node
    
    # 否则，后继是最近的祖先，且p在其左子树中
    successor = None
    node = root
    
    while node:
        if node.val > p.val:
            successor = node
            node = node.left
        else:
            node = node.right
    
    return successor


# 自动生成Solution类（无需手动编写）
Solution = create_solution(inorder_successor)
