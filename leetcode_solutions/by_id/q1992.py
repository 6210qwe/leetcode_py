# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1992
标题: Sort Linked List Already Sorted Using Absolute Values
难度: medium
链接: https://leetcode.cn/problems/sort-linked-list-already-sorted-using-absolute-values/
题目类型: 链表、双指针、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一个链表，其中的节点已经按照绝对值大小进行了排序。现在需要将链表重新排序，使得节点按照实际值进行排序。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针法，一个指针遍历链表，另一个指针用于插入负数节点。

算法步骤:
1. 初始化两个指针：`dummy` 作为新链表的头节点，`cur` 用于遍历原链表。
2. 遍历链表，如果当前节点的值为负数，则将其插入到 `dummy` 链表中适当的位置。
3. 如果当前节点的值为非负数，则直接连接到 `dummy` 链表的末尾。
4. 最后返回 `dummy` 链表的下一个节点作为新的链表头。

关键点:
- 使用双指针法，一个指针遍历链表，另一个指针用于插入负数节点。
- 通过比较和插入操作，确保链表按实际值排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是链表的长度。最坏情况下，每次插入操作的时间复杂度为 O(n)。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def sortLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    将按照绝对值排序的链表重新排序，使得节点按照实际值进行排序。
    """
    dummy = ListNode(0)
    cur = head
    prev = dummy

    while cur:
        if cur.val < 0:
            # 找到插入位置
            insert_pos = dummy
            while insert_pos.next and insert_pos.next.val < cur.val:
                insert_pos = insert_pos.next
            # 插入节点
            next_node = cur.next
            cur.next = insert_pos.next
            insert_pos.next = cur
            cur = next_node
        else:
            # 直接连接到新链表末尾
            prev.next = cur
            prev = cur
            cur = cur.next

    return dummy.next


Solution = create_solution(sortLinkedList)