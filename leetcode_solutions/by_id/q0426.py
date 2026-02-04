# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 426
标题: 将二叉搜索树转换为排序的双向链表
难度: 中等
链接: https://leetcode.cn/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
题目类型: 二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一棵二叉搜索树，将其就地转换为一个排序的循环双向链表。对于双向链表，要求节点的左指针指向其前驱节点，右指针指向其后继节点。特别地，我们希望第一个节点的左指针指向最后一个节点，最后一个节点的右指针指向第一个节点。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用中序遍历将二叉搜索树转换为排序的双向链表

算法步骤:
1. 定义两个指针 `prev` 和 `head`，分别用于记录当前节点的前驱节点和双向链表的头节点。
2. 使用递归进行中序遍历：
   - 递归遍历左子树
   - 处理当前节点：将当前节点与前驱节点连接，并更新前驱节点
   - 递归遍历右子树
3. 最后，将头节点和尾节点连接起来，形成循环双向链表。

关键点:
- 注意边界条件，特别是处理空树的情况
- 优化时间和空间复杂度，使用 O(1) 的额外空间
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历每个节点一次
空间复杂度: O(h) - 递归调用栈的空间复杂度，h 为树的高度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def __init__(self):
        self.prev = None
        self.head = None

    def treeToDoublyList(self, root: 'Optional[TreeNode]') -> 'Optional[TreeNode]':
        """
        函数式接口 - 将二叉搜索树转换为排序的双向链表
        
        实现思路:
        使用中序遍历将二叉搜索树转换为排序的双向链表，并将头节点和尾节点连接起来，形成循环双向链表。
        
        Args:
            root: 二叉搜索树的根节点
            
        Returns:
            排序的循环双向链表的头节点
            
        Example:
            >>> root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
            >>> solution = Solution()
            >>> head = solution.treeToDoublyList(root)
            >>> # 检查结果
        """
        if not root:
            return None

        def inorder(node: 'Optional[TreeNode]'):
            if not node:
                return
            inorder(node.left)
            if self.prev:
                self.prev.right = node
                node.left = self.prev
            else:
                self.head = node
            self.prev = node
            inorder(node.right)

        inorder(root)
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head

# 自动生成Solution类（无需手动编写）
Solution = create_solution(Solution.treeToDoublyList)