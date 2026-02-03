# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 106
标题: Construct Binary Tree from Inorder and Postorder Traversal
难度: medium
链接: https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
题目类型: 树、数组、哈希表、分治、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
106. 从中序与后序遍历序列构造二叉树 - 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。 示例 1: [https://assets.leetcode.com/uploads/2021/02/19/tree.jpg] 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3] 输出：[3,9,20,null,null,15,7] 示例 2: 输入：inorder = [-1], postorder = [-1] 输出：[-1] 提示: * 1 <= inorder.length <= 3000 * postorder.length == inorder.length * -3000 <= inorder[i], postorder[i] <= 3000 * inorder 和 postorder 都由 不同 的值组成 * postorder 中每一个值都在 inorder 中 * inorder 保证是树的中序遍历 * postorder 保证是树的后序遍历
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 利用后序遍历确定根节点，中序遍历确定左右子树范围

算法步骤:
1. 使用哈希表存储中序遍历中每个值的位置
2. 后序遍历的最后一个元素是根节点
3. 在中序遍历中找到根节点的位置，左边是左子树，右边是右子树
4. 递归构建左子树和右子树

关键点:
- 使用哈希表优化查找时间
- 时间复杂度O(n)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要访问每个节点一次
空间复杂度: O(n) - 哈希表和递归栈空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def construct_binary_tree_from_inorder_and_postorder_traversal(
    inorder: List[int], 
    postorder: List[int]
) -> Optional[TreeNode]:
    """
    函数式接口 - 从中序和后序遍历构建二叉树
    
    实现思路:
    利用后序遍历确定根节点，中序遍历确定左右子树范围，递归构建。
    
    Args:
        inorder: 中序遍历序列
        postorder: 后序遍历序列
        
    Returns:
        构建的二叉树根节点
        
    Example:
        >>> root = construct_binary_tree_from_inorder_and_postorder_traversal(
        ...     [9, 3, 15, 20, 7], [9, 15, 7, 20, 3]
        ... )
        >>> root.val
        3
    """
    if not inorder or not postorder:
        return None
    
    # 构建中序遍历的索引映射
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    
    def build(in_start: int, in_end: int, post_start: int, post_end: int) -> Optional[TreeNode]:
        if in_start > in_end or post_start > post_end:
            return None
        
        # 后序遍历的最后一个元素是根节点
        root_val = postorder[post_end]
        root = TreeNode(root_val)
        
        # 在中序遍历中找到根节点的位置
        root_idx = inorder_map[root_val]
        left_size = root_idx - in_start
        
        # 递归构建左子树和右子树
        root.left = build(
            in_start, 
            root_idx - 1, 
            post_start, 
            post_start + left_size - 1
        )
        root.right = build(
            root_idx + 1, 
            in_end, 
            post_start + left_size, 
            post_end - 1
        )
        
        return root
    
    return build(0, len(inorder) - 1, 0, len(postorder) - 1)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(construct_binary_tree_from_inorder_and_postorder_traversal)
