# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 19
标题: Remove Nth Node From End of List
难度: medium
链接: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
题目类型: 链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
19. 删除链表的倒数第 N 个结点 - 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。 示例 1： [https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg] 输入：head = [1,2,3,4,5], n = 2 输出：[1,2,3,5] 示例 2： 输入：head = [1], n = 1 输出：[] 示例 3： 输入：head = [1,2], n = 1 输出：[1] 提示： * 链表中结点的数目为 sz * 1 <= sz <= 30 * 0 <= Node.val <= 100 * 1 <= n <= sz 进阶：你能尝试使用一趟扫描实现吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 双指针法，快指针先走n步，然后快慢指针同时移动

算法步骤:
1. 创建虚拟头节点dummy，简化边界处理
2. 快指针先走n步
3. 快慢指针同时移动，直到快指针到达链表末尾
4. 此时慢指针指向要删除节点的前一个节点
5. 删除节点：slow.next = slow.next.next
6. 返回dummy.next

关键点:
- 使用虚拟头节点可以简化删除头节点的特殊情况
- 快指针先走n步，确保快慢指针之间距离为n
- 时间复杂度O(L)，L为链表长度，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(L) - 只需遍历链表一次，L为链表长度
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    函数式接口 - 双指针法实现
    
    实现思路:
    使用双指针，快指针先走n步，然后快慢指针同时移动，找到要删除节点的前一个节点。
    
    Args:
        head: 链表头节点
        n: 要删除的倒数第n个节点
        
    Returns:
        删除节点后的链表头节点
        
    Example:
        >>> head = ListNode.from_list([1,2,3,4,5])
        >>> result = remove_nth_from_end(head, 2)
        >>> result.to_list()
        [1, 2, 3, 5]
    """
    # 创建虚拟头节点，简化边界处理
    dummy = ListNode(0)
    dummy.next = head
    
    # 快指针先走n步
    fast = dummy
    for _ in range(n + 1):
        fast = fast.next
    
    # 快慢指针同时移动
    slow = dummy
    while fast:
        fast = fast.next
        slow = slow.next
    
    # 删除节点
    slow.next = slow.next.next
    
    return dummy.next


# 自动生成Solution类（无需手动编写）
Solution = create_solution(remove_nth_from_end)
