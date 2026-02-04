# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 933
标题: Increasing Order Search Tree
难度: easy
链接: https://leetcode.cn/problems/increasing-order-search-tree/
题目类型: 栈、树、深度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
897. 递增顺序搜索树 - 给你一棵二叉搜索树的 root ，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。 示例 1： [https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg] 输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9] 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9] 示例 2： [https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg] 输入：root = [5,1,7] 输出：[1,null,5,null,7] 提示： * 树中节点数的取值范围是 [1, 100] * 0 <= Node.val <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用中序遍历将二叉搜索树转换为递增顺序搜索树。

算法步骤:
1. 定义一个全局变量 `prev` 用于记录上一个访问的节点。
2. 定义一个辅助函数 `inorder` 进行中序遍历。
3. 在中序遍历过程中，将当前节点的左子节点设为 `None`，并将 `prev` 的右子节点设为当前节点。
4. 更新 `prev` 为当前节点。
5. 最后返回新的根节点。

关键点:
- 使用中序遍历确保节点按递增顺序排列。
- 通过修改节点的左右子节点来构建新的树结构。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的空间复杂度为 O(h)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal prev, new_root
            if node is None:
                return
            inorder(node.left)
            if prev is None:
                new_root = node  # 第一个访问的节点是新的根节点
            else:
                prev.right = node  # 将上一个节点的右子节点设为当前节点
                node.left = None  # 当前节点的左子节点设为 None
            prev = node  # 更新 prev 为当前节点
            inorder(node.right)

        prev = None
        new_root = None
        inorder(root)
        return new_root

Solution = create_solution(Solution)