# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 270
标题: Closest Binary Search Tree Value
难度: easy
链接: https://leetcode.cn/problems/closest-binary-search-tree-value/
题目类型: 树、深度优先搜索、二叉搜索树、二分查找、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
270. 最接近的二叉搜索树值 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: BST遍历，根据target值决定搜索方向

算法步骤:
1. 从根节点开始遍历
2. 如果target<node.val，搜索左子树
3. 如果target>node.val，搜索右子树
4. 更新最接近的值

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


def closest_value(root: Optional[TreeNode], target: float) -> int:
    """
    函数式接口 - 最接近的二叉搜索树值
    
    实现思路:
    BST遍历：根据target值决定搜索方向。
    
    Args:
        root: BST根节点
        target: 目标值
        
    Returns:
        最接近的值
        
    Example:
        >>> root = TreeNode(4)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(5)
        >>> closest_value(root, 3.714286)
        4
    """
    closest = root.val
    node = root
    
    while node:
        if abs(node.val - target) < abs(closest - target):
            closest = node.val
        
        if target < node.val:
            node = node.left
        else:
            node = node.right
    
    return closest


# 自动生成Solution类（无需手动编写）
Solution = create_solution(closest_value)
