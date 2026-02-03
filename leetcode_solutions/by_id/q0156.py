# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 156
标题: Binary Tree Upside Down
难度: medium
链接: https://leetcode.cn/problems/binary-tree-upside-down/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
156. 上下翻转二叉树 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归翻转，左子节点成为新的根，原根成为右子节点

算法步骤:
1. 如果根节点为空或没有左子节点，返回根节点
2. 递归处理左子树
3. 将原根节点作为新右子节点，原右子节点作为新左子节点
4. 返回新的根节点

关键点:
- 递归翻转二叉树结构
- 时间复杂度O(n)，空间复杂度O(h)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要访问每个节点一次
空间复杂度: O(h) - 递归栈深度，h为树的高度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def binary_tree_upside_down(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    函数式接口 - 上下翻转二叉树
    
    实现思路:
    递归翻转，左子节点成为新的根，原根成为右子节点。
    
    Args:
        root: 二叉树的根节点
        
    Returns:
        翻转后的二叉树根节点
        
    Example:
        >>> root = TreeNode.from_list([1, 2, 3, 4, 5])
        >>> result = binary_tree_upside_down(root)
    """
    if not root or not root.left:
        return root
    
    new_root = binary_tree_upside_down(root.left)
    
    root.left.left = root.right
    root.left.right = root
    root.left = None
    root.right = None
    
    return new_root


# 自动生成Solution类（无需手动编写）
Solution = create_solution(binary_tree_upside_down)
