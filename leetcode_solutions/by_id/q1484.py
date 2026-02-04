# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1484
标题: Linked List in Binary Tree
难度: medium
链接: https://leetcode.cn/problems/linked-list-in-binary-tree/
题目类型: 树、深度优先搜索、链表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1367. 二叉树中的链表 - 给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。 如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 head 为首的链表中每个节点的值，那么请你返回 True ，否则返回 False 。 一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/29/sample_1_1720.png] 输入：head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3] 输出：true 解释：树中蓝色的节点构成了与链表对应的子路径。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/29/sample_2_1720.png] 输入：head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3] 输出：true 示例 3： 输入：head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3] 输出：false 解释：二叉树中不存在一一对应链表的路径。 提示： * 二叉树和链表中的每个节点的值都满足 1 <= node.val <= 100 。 * 链表包含的节点数目在 1 到 100 之间。 * 二叉树包含的节点数目在 1 到 2500 之间。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来检查二叉树中是否存在一条路径，该路径上的节点值与链表中的节点值一一对应。

算法步骤:
1. 定义一个辅助函数 `is_sub_path`，用于检查从当前节点开始是否能找到链表的路径。
2. 在主函数 `is_sub_path_in_tree` 中，对二叉树进行遍历，对于每个节点调用 `is_sub_path` 函数。
3. 如果找到匹配的路径，返回 `True`；否则，继续遍历其他节点。
4. 如果遍历完整棵树都没有找到匹配的路径，返回 `False`。

关键点:
- 使用递归进行深度优先搜索。
- 在每次递归调用中，同时检查当前节点及其左右子节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是二叉树的节点数，m 是链表的节点数。最坏情况下，我们需要对每个二叉树节点进行一次链表的匹配。
空间复杂度: O(h)，其中 h 是二叉树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def is_sub_path(head: ListNode, root: TreeNode) -> bool:
    if not head:
        return True
    if not root:
        return False
    if head.val == root.val:
        if is_sub_path(head.next, root.left) or is_sub_path(head.next, root.right):
            return True
    return is_sub_path(head, root.left) or is_sub_path(head, root.right)

def is_sub_path_in_tree(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
    if not head:
        return True
    if not root:
        return False
    if is_sub_path(head, root):
        return True
    return is_sub_path_in_tree(head, root.left) or is_sub_path_in_tree(head, root.right)

Solution = create_solution(is_sub_path_in_tree)