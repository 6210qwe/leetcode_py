# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100168
标题: Linked List Cycle LCCI
难度: medium
链接: https://leetcode.cn/problems/linked-list-cycle-lcci/
题目类型: 哈希表、链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 02.08. 环路检测 - 给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。若环不存在，请返回 null。 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png] 输入：head = [3,2,0,-4], pos = 1 输出：tail connects to node index 1 解释：链表中有一个环，其尾部连接到第二个节点。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png] 输入：head = [1,2], pos = 0 输出：tail connects to node index 0 解释：链表中有一个环，其尾部连接到第一个节点。 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png] 输入：head = [1], pos = -1 输出：no cycle 解释：链表中没有环。 进阶： * 你是否可以不用额外空间解决此题？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用快慢指针法来检测链表中的环，并找到环的起始节点。

算法步骤:
1. 初始化两个指针 slow 和 fast，都指向链表的头节点。
2. 快指针每次移动两步，慢指针每次移动一步。如果链表中存在环，快指针和慢指针最终会在环内相遇。
3. 当快指针和慢指针相遇时，将其中一个指针重新指向链表头节点，另一个指针保持在相遇点。
4. 两个指针每次都移动一步，它们会在环的起始节点相遇。

关键点:
- 使用快慢指针法可以在 O(1) 的空间复杂度下检测环并找到环的起始节点。
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

def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    检测链表中的环，并返回环的起始节点。如果没有环，返回 None。
    """
    if not head or not head.next:
        return None

    # 初始化快慢指针
    slow = head
    fast = head

    # 快指针每次移动两步，慢指针每次移动一步
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # 快慢指针相遇，说明存在环
        if slow == fast:
            break

    # 如果快指针或快指针的下一个节点为空，说明没有环
    if not fast or not fast.next:
        return None

    # 将慢指针重新指向链表头节点
    slow = head

    # 两个指针每次都移动一步，直到相遇
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

Solution = create_solution(detect_cycle)