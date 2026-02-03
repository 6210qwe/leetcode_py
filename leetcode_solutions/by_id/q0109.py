# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 109
标题: Convert Sorted List to Binary Search Tree
难度: medium
链接: https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/
题目类型: 树、二叉搜索树、链表、分治、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
109. 有序链表转换二叉搜索树 - 给定一个单链表的头节点 head ，其中的元素 按升序排序 ，将其转换为 平衡 二叉搜索树。 示例 1: [https://assets.leetcode.com/uploads/2020/08/17/linked.jpg] 输入: head = [-10,-3,0,5,9] 输出: [0,-3,9,-10,null,5] 解释: 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。 示例 2: 输入: head = [] 输出: [] 提示: * head 中的节点数在[0, 2 * 104] 范围内 * -105 <= Node.val <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用快慢指针找到中间节点，递归构建BST

算法步骤:
1. 如果链表为空，返回None
2. 使用快慢指针找到链表的中间节点
3. 将中间节点作为根节点
4. 递归构建左子树（左半部分）和右子树（右半部分）
5. 返回根节点

关键点:
- 使用快慢指针找中点
- 时间复杂度O(nlogn)，空间复杂度O(logn)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(nlogn) - 每次找中点O(n)，递归logn层
空间复杂度: O(logn) - 递归栈深度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def convert_sorted_list_to_binary_search_tree(head: Optional[ListNode]) -> Optional[TreeNode]:
    """
    函数式接口 - 将有序链表转换为平衡BST
    
    实现思路:
    使用快慢指针找到中间节点，递归构建左右子树。
    
    Args:
        head: 有序链表的头节点
        
    Returns:
        平衡二叉搜索树的根节点
        
    Example:
        >>> # 创建链表 [-10, -3, 0, 5, 9]
        >>> head = ListNode(-10)
        >>> head.next = ListNode(-3)
        >>> head.next.next = ListNode(0)
        >>> head.next.next.next = ListNode(5)
        >>> head.next.next.next.next = ListNode(9)
        >>> root = convert_sorted_list_to_binary_search_tree(head)
        >>> root.val
        0
    """
    if not head:
        return None
    
    if not head.next:
        return TreeNode(head.val)
    
    # 使用快慢指针找到中间节点的前一个节点
    slow = head
    fast = head.next.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # slow.next是中间节点
    mid = slow.next
    slow.next = None  # 断开链表
    
    root = TreeNode(mid.val)
    root.left = convert_sorted_list_to_binary_search_tree(head)
    root.right = convert_sorted_list_to_binary_search_tree(mid.next)
    
    return root


# 自动生成Solution类（无需手动编写）
Solution = create_solution(convert_sorted_list_to_binary_search_tree)
