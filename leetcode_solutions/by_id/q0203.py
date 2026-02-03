# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 203
标题: Remove Linked List Elements
难度: easy
链接: https://leetcode.cn/problems/remove-linked-list-elements/
题目类型: 递归、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
203. 移除链表元素 - 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。 示例 1： [https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg] 输入：head = [1,2,6,3,4,5,6], val = 6 输出：[1,2,3,4,5] 示例 2： 输入：head = [], val = 1 输出：[] 示例 3： 输入：head = [7,7,7,7], val = 7 输出：[] 提示： * 列表中的节点数目在范围 [0, 104] 内 * 1 <= Node.val <= 50 * 0 <= val <= 50
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 遍历链表，删除值等于val的节点

算法步骤:
1. 使用虚拟头节点简化边界处理
2. 遍历链表，如果下一个节点的值等于val，则删除
3. 返回虚拟头节点的下一个节点

关键点:
- 使用虚拟头节点简化删除操作
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历链表一次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def remove_linked_list_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """
    函数式接口 - 移除链表元素
    
    实现思路:
    遍历链表，删除值等于val的节点。
    
    Args:
        head: 链表头节点
        val: 要删除的值
        
    Returns:
        删除后的链表头节点
        
    Example:
        >>> head = ListNode.from_list([1, 2, 6, 3, 4, 5, 6])
        >>> remove_linked_list_elements(head, 6)
        ListNode.from_list([1, 2, 3, 4, 5])
    """
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next


# 自动生成Solution类（无需手动编写）
Solution = create_solution(remove_linked_list_elements)
