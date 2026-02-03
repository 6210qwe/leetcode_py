# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000258
标题: 环形链表 II
难度: medium
链接: https://leetcode.cn/problems/c32eOV/
题目类型: 哈希表、链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 022. 环形链表 II - 给定一个链表，返回链表开始入环的第一个节点。 从链表的头节点开始沿着 next 指针进入环的第一个节点为环的入口节点。如果链表无环，则返回 null。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。 说明：不允许修改给定的链表。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png] 输入：head = [3,2,0,-4], pos = 1 输出：返回索引为 1 的链表节点 解释：链表中有一个环，其尾部连接到第二个节点。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png] 输入：head = [1,2], pos = 0 输出：返回索引为 0 的链表节点 解释：链表中有一个环，其尾部连接到第一个节点。 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png] 输入：head = [1], pos = -1 输出：返回 null 解释：链表中没有环。 提示： * 链表中节点的数目范围在范围 [0, 104] 内 * -105 <= Node.val <= 105 * pos 的值为 -1 或者链表中的一个有效索引 进阶：是否可以使用 O(1) 空间解决此题？ 注意：本题与主站 142 题相同： https://leetcode.cn/problems/linked-list-cycle-ii/ [https://leetcode.cn/problems/linked-list-cycle-ii/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: Floyd 判圈算法（快慢指针）定位入环点

算法步骤:
1. 使用快慢指针 fast、slow：
   - slow 每次走 1 步，fast 每次走 2 步
2. 若 fast 或 fast.next 为 None，说明无环，返回 None
3. 若 fast 与 slow 相遇，说明有环：
   - 将一个指针 ptr 从 head 出发，另一个指针保持在相遇点
   - 两指针每次都走 1 步，再次相遇的位置即为入环点

关键点:
- 快慢指针相遇后，从头节点与相遇点同步前进会在入环点相遇（经典结论）
- 不允许修改链表且需 O(1) 额外空间
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(L) - L 为链表节点数（含环前长度 + 环长度）
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    函数式接口 - 环形链表 II
    """
    if head is None:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            ptr = head
            while ptr != slow:
                ptr = ptr.next
                slow = slow.next
            return ptr
    return None


Solution = create_solution(detect_cycle)
