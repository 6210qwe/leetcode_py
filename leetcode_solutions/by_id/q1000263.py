# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000263
标题: 回文链表
难度: easy
链接: https://leetcode.cn/problems/aMhZSa/
题目类型: 栈、递归、链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 027. 回文链表 - 给定一个链表的 头节点 head ，请判断其是否为回文链表。 如果一个链表是回文，那么链表节点序列从前往后看和从后往前看是相同的。 示例 1： [https://pic.leetcode.cn/1626421737-LjXceN-image.png] 输入: head = [1,2,3,3,2,1] 输出: true 示例 2： [https://pic.leetcode.cn/1626422231-wgvnWh-image.png] 输入: head = [1,2] 输出: false 提示： * 链表 L 的长度范围为 [1, 105] * 0 <= node.val <= 9 进阶：能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 注意：本题与主站 234 题相同：https://leetcode.cn/problems/palindrome-linked-list/ [https://leetcode.cn/problems/palindrome-linked-list/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用快慢指针找到链表中点，反转后半部分链表，然后比较前半部分和反转后的后半部分。

算法步骤:
1. 使用快慢指针找到链表的中点。
2. 反转链表的后半部分。
3. 比较前半部分和反转后的后半部分是否相等。
4. 恢复链表（可选）。

关键点:
- 快慢指针用于找到链表中点。
- 反转链表的后半部分以进行比较。
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
    """
    判断给定链表是否为回文链表。
    
    :param head: 链表的头节点
    :return: 是否为回文链表
    """
    if not head or not head.next:
        return True

    # 使用快慢指针找到链表的中点
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 反转链表的后半部分
    second_half = reverse_linked_list(slow)
    first_half = head

    # 比较前半部分和反转后的后半部分
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True

def reverse_linked_list(head: ListNode) -> ListNode:
    """
    反转链表。
    
    :param head: 链表的头节点
    :return: 反转后的链表头节点
    """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

Solution = create_solution(is_palindrome)