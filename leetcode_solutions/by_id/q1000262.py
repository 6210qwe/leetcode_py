# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000262
标题: 重排链表
难度: medium
链接: https://leetcode.cn/problems/LGjMqU/
题目类型: 栈、递归、链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 026. 重排链表 - 给定一个单链表 L 的头节点 head ，单链表 L 表示为： L0 → L1 → … → Ln-1 → Ln 请将其重新排列后变为： L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → … 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 示例 1： [https://pic.leetcode.cn/1626420311-PkUiGi-image.png] 输入: head = [1,2,3,4] 输出: [1,4,2,3] 示例 2： [https://pic.leetcode.cn/1626420320-YUiulT-image.png] 输入: head = [1,2,3,4,5] 输出: [1,5,2,4,3] 提示： * 链表的长度范围为 [1, 5 * 104] * 1 <= node.val <= 1000 注意：本题与主站 143 题相同：https://leetcode.cn/problems/reorder-list/ [https://leetcode.cn/problems/reorder-list/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用快慢指针找到链表中点，然后反转后半部分链表，最后将前半部分和反转后的后半部分交替合并。

算法步骤:
1. 使用快慢指针找到链表的中点。
2. 反转链表的后半部分。
3. 将前半部分和反转后的后半部分交替合并。

关键点:
- 快慢指针用于找到链表中点。
- 反转链表的后半部分。
- 交替合并两个链表。
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

def reorderList(head: Optional[ListNode]) -> None:
    if not head or not head.next:
        return

    # 找到链表中点
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 反转后半部分链表
    prev, curr = None, slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # 交替合并两个链表
    first, second = head, prev
    while second.next:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

Solution = create_solution(reorderList)