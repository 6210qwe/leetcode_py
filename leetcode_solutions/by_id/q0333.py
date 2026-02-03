# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 333
标题: Largest BST Subtree
难度: medium
链接: https://leetcode.cn/problems/largest-bst-subtree/
题目类型: 树、深度优先搜索、二叉搜索树、动态规划、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
333. 最大二叉搜索子树 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: DFS后序遍历，判断子树是否为BST

算法步骤:
1. 后序遍历，先处理左右子树
2. 如果左右子树都是BST，且当前节点满足BST条件，则当前子树是BST
3. 记录最大BST子树的大小

关键点:
- DFS后序遍历
- BST判断
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历所有节点
空间复杂度: O(h) - 递归栈空间，h为树高
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def largest_bst_subtree(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 最大二叉搜索子树
    
    实现思路:
    DFS后序遍历：判断子树是否为BST。
    
    Args:
        root: 二叉树根节点
        
    Returns:
        最大BST子树的节点数
        
    Example:
        >>> root = TreeNode(10)
        >>> root.left = TreeNode(5)
        >>> root.right = TreeNode(15)
        >>> largest_bst_subtree(root)
        3
    """
    max_size = 0
    
    def dfs(node: Optional[TreeNode]) -> tuple:
        """返回(is_bst, min_val, max_val, size)"""
        nonlocal max_size
        
        if not node:
            return (True, float('inf'), float('-inf'), 0)
        
        left_bst, left_min, left_max, left_size = dfs(node.left)
        right_bst, right_min, right_max, right_size = dfs(node.right)
        
        if left_bst and right_bst and left_max < node.val < right_min:
            size = left_size + right_size + 1
            max_size = max(max_size, size)
            return (True, min(left_min, node.val), max(right_max, node.val), size)
        
        return (False, 0, 0, 0)
    
    dfs(root)
    return max_size


# 自动生成Solution类（无需手动编写）
Solution = create_solution(largest_bst_subtree)
