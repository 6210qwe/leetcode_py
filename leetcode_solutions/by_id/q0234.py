# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 234
标题: Palindrome Linked List
难度: easy
链接: https://leetcode.cn/problems/palindrome-linked-list/
题目类型: 栈、递归、链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
234. 回文链表 - 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。 示例 1： [https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg] 输入：head = [1,2,2,1] 输出：true 示例 2： [https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg] 输入：head = [1,2] 输出：false 提示： * 链表中节点数目在范围[1, 105] 内 * 0 <= Node.val <= 9 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用快慢指针找到中点，反转后半部分，然后比较前后两部分

算法步骤:
1. 使用快慢指针找到链表中点
2. 反转后半部分链表
3. 比较前半部分和反转后的后半部分
4. 恢复链表（可选）

关键点:
- 使用O(1)空间复杂度
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历链表两次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def palindrome_linked_list(head: Optional[ListNode]) -> bool:
    """
    函数式接口 - 回文链表
    
    实现思路:
    使用快慢指针找到中点，反转后半部分，然后比较前后两部分。
    
    Args:
        head: 链表的头节点
        
    Returns:
        是否是回文链表
        
    Example:
        >>> head = ListNode.from_list([1, 2, 2, 1])
        >>> palindrome_linked_list(head)
        True
    """
    if not head or not head.next:
        return True
    
    # 找到中点
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # 反转后半部分
    second_half = slow.next
    slow.next = None
    
    prev = None
    curr = second_half
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    # 比较前后两部分
    first = head
    second = prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    
    return True


# 自动生成Solution类（无需手动编写）
Solution = create_solution(palindrome_linked_list)
