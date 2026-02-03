# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 226
标题: Invert Binary Tree
难度: easy
链接: https://leetcode.cn/problems/invert-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
226. 翻转二叉树 - 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。 示例 1： [https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg] 输入：root = [4,2,7,1,3,6,9] 输出：[4,7,2,9,6,3,1] 示例 2： [https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg] 输入：root = [2,1,3] 输出：[2,3,1] 示例 3： 输入：root = [] 输出：[] 提示： * 树中节点数目范围在 [0, 100] 内 * -100 <= Node.val <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归交换左右子树

算法步骤:
1. 如果根节点为空，返回None
2. 递归翻转左子树和右子树
3. 交换左右子树
4. 返回根节点

关键点:
- 递归交换左右子树
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


def invert_binary_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    函数式接口 - 翻转二叉树
    
    实现思路:
    递归交换左右子树。
    
    Args:
        root: 二叉树的根节点
        
    Returns:
        翻转后的二叉树根节点
        
    Example:
        >>> root = TreeNode.from_list([4, 2, 7, 1, 3, 6, 9])
        >>> result = invert_binary_tree(root)
    """
    if not root:
        return None
    
    # 递归翻转左右子树
    left = invert_binary_tree(root.left)
    right = invert_binary_tree(root.right)
    
    # 交换左右子树
    root.left = right
    root.right = left
    
    return root


# 自动生成Solution类（无需手动编写）
Solution = create_solution(invert_binary_tree)
