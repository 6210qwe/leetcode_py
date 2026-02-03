# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 111
标题: Minimum Depth of Binary Tree
难度: easy
链接: https://leetcode.cn/problems/minimum-depth-of-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
111. 二叉树的最小深度 - 给定一个二叉树，找出其最小深度。 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。 说明：叶子节点是指没有子节点的节点。 示例 1： [https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg] 输入：root = [3,9,20,null,null,15,7] 输出：2 示例 2： 输入：root = [2,null,3,null,4,null,5,null,6] 输出：5 提示： * 树中节点数的范围在 [0, 105] 内 * -1000 <= Node.val <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归计算最小深度，注意只有叶子节点才算深度

算法步骤:
1. 如果根节点为空，返回0
2. 如果左右子树都为空，返回1
3. 如果左子树为空，递归计算右子树的最小深度
4. 如果右子树为空，递归计算左子树的最小深度
5. 否则返回左右子树最小深度的较小值加1

关键点:
- 只有叶子节点才算深度，单边子树需要特殊处理
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


def minimum_depth_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 计算二叉树最小深度
    
    实现思路:
    递归计算最小深度，注意只有叶子节点才算深度，单边子树需要特殊处理。
    
    Args:
        root: 二叉树的根节点
        
    Returns:
        二叉树的最小深度
        
    Example:
        >>> root = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
        >>> minimum_depth_of_binary_tree(root)
        2
    """
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 1
    
    if not root.left:
        return minimum_depth_of_binary_tree(root.right) + 1
    
    if not root.right:
        return minimum_depth_of_binary_tree(root.left) + 1
    
    return min(
        minimum_depth_of_binary_tree(root.left),
        minimum_depth_of_binary_tree(root.right)
    ) + 1


# 自动生成Solution类（无需手动编写）
Solution = create_solution(minimum_depth_of_binary_tree)
