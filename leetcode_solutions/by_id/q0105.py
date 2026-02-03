# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 105
标题: Construct Binary Tree from Preorder and Inorder Traversal
难度: medium
链接: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
题目类型: 树、数组、哈希表、分治、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
105. 从前序与中序遍历序列构造二叉树 - 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。 示例 1: [https://assets.leetcode.com/uploads/2021/02/19/tree.jpg] 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] 输出: [3,9,20,null,null,15,7] 示例 2: 输入: preorder = [-1], inorder = [-1] 输出: [-1] 提示: * 1 <= preorder.length <= 3000 * inorder.length == preorder.length * -3000 <= preorder[i], inorder[i] <= 3000 * preorder 和 inorder 均 无重复 元素 * inorder 均出现在 preorder * preorder 保证 为二叉树的前序遍历序列 * inorder 保证 为二叉树的中序遍历序列
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 利用前序遍历确定根节点，中序遍历确定左右子树范围

算法步骤:
1. 使用哈希表存储中序遍历中每个值的位置
2. 前序遍历的第一个元素是根节点
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


def construct_binary_tree_from_preorder_and_inorder_traversal(
    preorder: List[int], 
    inorder: List[int]
) -> Optional[TreeNode]:
    """
    函数式接口 - 从前序和中序遍历构建二叉树
    
    实现思路:
    利用前序遍历确定根节点，中序遍历确定左右子树范围，递归构建。
    
    Args:
        preorder: 前序遍历序列
        inorder: 中序遍历序列
        
    Returns:
        构建的二叉树根节点
        
    Example:
        >>> root = construct_binary_tree_from_preorder_and_inorder_traversal(
        ...     [3, 9, 20, 15, 7], [9, 3, 15, 20, 7]
        ... )
        >>> root.val
        3
    """
    if not preorder or not inorder:
        return None
    
    # 构建中序遍历的索引映射
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    
    def build(pre_start: int, pre_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
        if pre_start > pre_end or in_start > in_end:
            return None
        
        # 前序遍历的第一个元素是根节点
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        
        # 在中序遍历中找到根节点的位置
        root_idx = inorder_map[root_val]
        left_size = root_idx - in_start
        
        # 递归构建左子树和右子树
        root.left = build(
            pre_start + 1, 
            pre_start + left_size, 
            in_start, 
            root_idx - 1
        )
        root.right = build(
            pre_start + left_size + 1, 
            pre_end, 
            root_idx + 1, 
            in_end
        )
        
        return root
    
    return build(0, len(preorder) - 1, 0, len(inorder) - 1)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(construct_binary_tree_from_preorder_and_inorder_traversal)
