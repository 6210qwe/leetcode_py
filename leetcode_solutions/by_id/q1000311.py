# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000311
标题: 递增顺序搜索树
难度: easy
链接: https://leetcode.cn/problems/NYBBNL/
题目类型: 栈、树、深度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 052. 递增顺序搜索树 - 给你一棵二叉搜索树，请 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。 示例 1： [https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg] 输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9] 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9] 示例 2： [https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg] 输入：root = [5,1,7] 输出：[1,null,5,null,7] 提示： * 树中节点数的取值范围是 [1, 100] * 0 <= Node.val <= 1000 注意：本题与主站 897 题相同： https://leetcode.cn/problems/increasing-order-search-tree/ [https://leetcode.cn/problems/increasing-order-search-tree/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用中序遍历将二叉搜索树转换为递增顺序搜索树。

算法步骤:
1. 定义一个辅助函数 `inorder_traversal` 进行中序遍历。
2. 在中序遍历过程中，将当前节点的左子节点设为 None，并将其右子节点指向下一个节点。
3. 使用一个指针 `prev` 来记录上一个访问的节点，以便在遍历时更新节点的右子节点。

关键点:
- 中序遍历确保了节点按递增顺序访问。
- 使用 `prev` 指针来连接节点，形成新的递增顺序搜索树。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的空间复杂度为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder_traversal(node: Optional[TreeNode]):
            nonlocal prev
            if not node:
                return
            inorder_traversal(node.left)
            if prev:
                prev.right = node
            else:
                new_root = node
            node.left = None
            prev = node
            inorder_traversal(node.right)

        prev = None
        new_root = None
        inorder_traversal(root)
        return new_root

Solution = create_solution(Solution)