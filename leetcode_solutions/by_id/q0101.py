# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 101
标题: Symmetric Tree
难度: easy
链接: https://leetcode.cn/problems/symmetric-tree/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
101. 对称二叉树 - 给你一个二叉树的根节点 root ， 检查它是否轴对称。 示例 1： [https://pic.leetcode.cn/1698026966-JDYPDU-image.png] 输入：root = [1,2,2,3,4,4,3] 输出：true 示例 2： [https://pic.leetcode.cn/1698027008-nPFLbM-image.png] 输入：root = [1,2,2,null,3,null,3] 输出：false 提示： * 树中节点数目在范围 [1, 1000] 内 * -100 <= Node.val <= 100 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归比较左右子树是否镜像对称

算法步骤:
1. 如果根节点为空，返回True
2. 定义辅助函数，比较两个节点是否镜像
3. 两个节点镜像的条件：
   - 两个节点都为空，返回True
   - 只有一个为空，返回False
   - 两个节点值相等，且左节点的左子树与右节点的右子树镜像，左节点的右子树与右节点的左子树镜像

关键点:
- 递归比较左右子树
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


def symmetric_tree(root: Optional[TreeNode]) -> bool:
    """
    函数式接口 - 递归判断对称二叉树
    
    实现思路:
    递归比较左右子树是否镜像对称，通过辅助函数判断两个节点是否镜像。
    
    Args:
        root: 二叉树的根节点
        
    Returns:
        如果树是对称的返回True，否则返回False
        
    Example:
        >>> root = TreeNode.from_list([1, 2, 2, 3, 4, 4, 3])
        >>> symmetric_tree(root)
        True
    """
    if not root:
        return True
    
    def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """判断两个节点是否镜像"""
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    
    return is_mirror(root.left, root.right)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(symmetric_tree)
