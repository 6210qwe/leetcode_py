# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1050
标题: Construct Binary Search Tree from Preorder Traversal
难度: medium
链接: https://leetcode.cn/problems/construct-binary-search-tree-from-preorder-traversal/
题目类型: 栈、树、二叉搜索树、数组、二叉树、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1008. 前序遍历构造二叉搜索树 - 给定一个整数数组，它表示BST(即 二叉搜索树 )的 先序遍历 ，构造树并返回其根。 保证 对于给定的测试用例，总是有可能找到具有给定需求的二叉搜索树。 二叉搜索树 是一棵二叉树，其中每个节点， Node.left 的任何后代的值 严格小于 Node.val , Node.right 的任何后代的值 严格大于 Node.val。 二叉树的 前序遍历 首先显示节点的值，然后遍历Node.left，最后遍历Node.right。 示例 1： [https://assets.leetcode.com/uploads/2019/03/06/1266.png] 输入：preorder = [8,5,1,7,10,12] 输出：[8,5,10,1,7,null,12] 示例 2: 输入: preorder = [1,3] 输出: [1,null,3] 提示： * 1 <= preorder.length <= 100 * 1 <= preorder[i] <= 10^8 * preorder 中的值 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归方法构建二叉搜索树。通过前序遍历的特点，可以确定根节点和左右子树的范围。

算法步骤:
1. 从 preorder 数组中取出第一个元素作为根节点。
2. 找到第一个大于根节点值的位置，将数组分成左子树和右子树。
3. 递归地构建左子树和右子树。

关键点:
- 利用二叉搜索树的性质，通过比较当前节点值与根节点值来划分左右子树。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 每个元素只处理一次。
空间复杂度: O(h) - 递归调用栈的深度为树的高度 h。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def bst_from_preorder(preorder: List[int]) -> Optional[TreeNode]:
    """
    通过前序遍历构造二叉搜索树
    """
    if not preorder:
        return None

    def build_tree(start, end):
        if start > end:
            return None

        # 当前子树的根节点
        root_val = preorder[start]
        root = TreeNode(root_val)

        # 找到第一个大于根节点值的位置
        i = start + 1
        while i <= end and preorder[i] < root_val:
            i += 1

        # 递归构建左子树和右子树
        root.left = build_tree(start + 1, i - 1)
        root.right = build_tree(i, end)

        return root

    return build_tree(0, len(preorder) - 1)


Solution = create_solution(bst_from_preorder)