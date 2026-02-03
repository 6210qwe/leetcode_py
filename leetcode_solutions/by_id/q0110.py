# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 110
标题: Balanced Binary Tree
难度: easy
链接: https://leetcode.cn/problems/balanced-binary-tree/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
110. 平衡二叉树 - 给定一个二叉树，判断它是否是 平衡二叉树 示例 1： [https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg] 输入：root = [3,9,20,null,null,15,7] 输出：true 示例 2： [https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg] 输入：root = [1,2,2,3,3,null,null,4,4] 输出：false 示例 3： 输入：root = [] 输出：true 提示： * 树中的节点数在范围 [0, 5000] 内 * -104 <= Node.val <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归计算每个节点的深度，同时检查是否平衡

算法步骤:
1. 定义辅助函数计算节点高度并检查平衡
2. 如果节点为空，返回0（高度）和True（平衡）
3. 递归计算左右子树的高度
4. 如果左右子树高度差大于1，返回-1表示不平衡
5. 否则返回较大高度加1

关键点:
- 自底向上检查，避免重复计算
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


def balanced_binary_tree(root: Optional[TreeNode]) -> bool:
    """
    函数式接口 - 判断是否为平衡二叉树
    
    实现思路:
    递归计算每个节点的高度，同时检查是否平衡。如果高度差大于1，返回-1表示不平衡。
    
    Args:
        root: 二叉树的根节点
        
    Returns:
        如果是平衡二叉树返回True，否则返回False
        
    Example:
        >>> root = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
        >>> balanced_binary_tree(root)
        True
    """
    def height(node: Optional[TreeNode]) -> int:
        """计算节点高度，如果不平衡返回-1"""
        if not node:
            return 0
        
        left_height = height(node.left)
        if left_height == -1:
            return -1
        
        right_height = height(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
    
    return height(root) != -1


# 自动生成Solution类（无需手动编写）
Solution = create_solution(balanced_binary_tree)
