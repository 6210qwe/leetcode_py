# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100164
标题: Palindrome Linked List LCCI
难度: easy
链接: https://leetcode.cn/problems/palindrome-linked-list-lcci/
题目类型: 栈、递归、链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 02.06. 回文链表 - 编写一个函数，检查输入的链表是否是回文的。 示例 1： 输入： 1->2 输出： false 示例 2： 输入： 1->2->2->1 输出： true 进阶： 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用快慢指针找到链表中点，反转后半部分链表，然后比较前后两部分是否相同。

算法步骤:
1. 使用快慢指针找到链表的中点。
2. 反转后半部分链表。
3. 比较前半部分和反转后的后半部分是否相同。
4. 恢复链表（可选）。

关键点:
- 快慢指针用于找到链表中点。
- 反转链表时需要保存前一个节点。
- 比较前后两部分时注意边界条件。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution

def is_palindrome(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return True

    # 使用快慢指针找到链表中点
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 反转后半部分链表
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # 比较前半部分和反转后的后半部分
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True

Solution = create_solution(is_palindrome)