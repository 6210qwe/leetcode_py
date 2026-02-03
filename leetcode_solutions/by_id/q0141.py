# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 141
标题: Linked List Cycle
难度: easy
链接: https://leetcode.cn/problems/linked-list-cycle/
题目类型: 哈希表、链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
141. 环形链表 - 给你一个链表的头节点 head ，判断链表中是否有环。 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。 如果链表中存在环 ，则返回 true 。 否则，返回 false 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png] 输入：head = [3,2,0,-4], pos = 1 输出：true 解释：链表中有一个环，其尾部连接到第二个节点。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png] 输入：head = [1,2], pos = 0 输出：true 解释：链表中有一个环，其尾部连接到第一个节点。 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png] 输入：head = [1], pos = -1 输出：false 解释：链表中没有环。 提示： * 链表中节点的数目范围是 [0, 104] * -105 <= Node.val <= 105 * pos 为 -1 或者链表中的一个 有效索引 。 进阶：你能用 O(1)（即，常量）内存解决此问题吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用快慢指针，如果有环快指针会追上慢指针

算法步骤:
1. 使用两个指针，慢指针每次走一步，快指针每次走两步
2. 如果链表有环，快指针最终会追上慢指针
3. 如果快指针到达末尾，说明没有环

关键点:
- 快慢指针法（Floyd判圈算法）
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 最多遍历链表一次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def linked_list_cycle(head: Optional[ListNode]) -> bool:
    """
    函数式接口 - 判断链表是否有环
    
    实现思路:
    使用快慢指针，如果有环快指针会追上慢指针。
    
    Args:
        head: 链表的头节点
        
    Returns:
        如果有环返回True，否则返回False
        
    Example:
        >>> # 创建有环的链表
        >>> head = ListNode(3)
        >>> head.next = ListNode(2)
        >>> head.next.next = ListNode(0)
        >>> head.next.next.next = ListNode(-4)
        >>> head.next.next.next.next = head.next  # 形成环
        >>> linked_list_cycle(head)
        True
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False


# 自动生成Solution类（无需手动编写）
Solution = create_solution(linked_list_cycle)
