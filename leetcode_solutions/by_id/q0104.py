# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 104
标题: Maximum Depth of Binary Tree
难度: easy
链接: https://leetcode.cn/problems/maximum-depth-of-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
104. 二叉树的最大深度 - 给定一个二叉树 root ，返回其最大深度。 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。 示例 1： [https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg] 输入：root = [3,9,20,null,null,15,7] 输出：3 示例 2： 输入：root = [1,null,2] 输出：2 提示： * 树中节点的数量在 [0, 104] 区间内。 * -100 <= Node.val <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归计算左右子树的最大深度

算法步骤:
1. 如果根节点为空，返回0
2. 递归计算左子树的最大深度
3. 递归计算右子树的最大深度
4. 返回左右子树最大深度的较大值加1

关键点:
- 递归实现简洁
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


def maximum_depth_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 递归计算最大深度
    
    实现思路:
    递归计算左右子树的最大深度，返回较大值加1。
    
    Args:
        root: 二叉树的根节点
        
    Returns:
        二叉树的最大深度
        
    Example:
        >>> root = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
        >>> maximum_depth_of_binary_tree(root)
        3
    """
    if not root:
        return 0
    
    left_depth = maximum_depth_of_binary_tree(root.left)
    right_depth = maximum_depth_of_binary_tree(root.right)
    
    return max(left_depth, right_depth) + 1


# 自动生成Solution类（无需手动编写）
Solution = create_solution(maximum_depth_of_binary_tree)
