# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 142
标题: Linked List Cycle II
难度: medium
链接: https://leetcode.cn/problems/linked-list-cycle-ii/
题目类型: 哈希表、链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
142. 环形链表 II - 给定一个链表的头节点 head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。 不允许修改 链表。 示例 1： [https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png] 输入：head = [3,2,0,-4], pos = 1 输出：返回索引为 1 的链表节点 解释：链表中有一个环，其尾部连接到第二个节点。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png] 输入：head = [1,2], pos = 0 输出：返回索引为 0 的链表节点 解释：链表中有一个环，其尾部连接到第一个节点。 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png] 输入：head = [1], pos = -1 输出：返回 null 解释：链表中没有环。 提示： * 链表中节点的数目范围在范围 [0, 104] 内 * -105 <= Node.val <= 105 * pos 的值为 -1 或者链表中的一个有效索引 进阶：你是否可以使用 O(1) 空间解决此题？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 快慢指针，找到相遇点后，一个指针从头开始，另一个从相遇点开始，同时移动

算法步骤:
1. 使用快慢指针找到相遇点
2. 一个指针从头开始，另一个从相遇点开始，同时移动
3. 相遇点即为环的入口

关键点:
- 快慢指针+数学证明
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历链表
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def linked_list_cycle_ii(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    函数式接口 - 环形链表II
    
    实现思路:
    快慢指针，找到相遇点后，一个指针从头开始，另一个从相遇点开始，同时移动。
    
    Args:
        head: 链表的头节点
        
    Returns:
        链表开始入环的第一个节点，如果无环返回None
        
    Example:
        >>> head = ListNode.from_list([3,2,0,-4])
        >>> linked_list_cycle_ii(head)
    """
    if not head or not head.next:
        return None
    
    slow = fast = head
    
    # 找到相遇点
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    
    # 一个指针从头开始，另一个从相遇点开始
    ptr1 = head
    ptr2 = slow
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return ptr1


# 自动生成Solution类（无需手动编写）
Solution = create_solution(linked_list_cycle_ii)
