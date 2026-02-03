# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 143
标题: Reorder List
难度: medium
链接: https://leetcode.cn/problems/reorder-list/
题目类型: 栈、递归、链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
143. 重排链表 - 给定一个单链表 L 的头节点 head ，单链表 L 表示为： L0 → L1 → … → Ln - 1 → Ln 请将其重新排列后变为： L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → … 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 示例 1： [https://pic.leetcode.cn/1626420311-PkUiGI-image.png] 输入：head = [1,2,3,4] 输出：[1,4,2,3] 示例 2： [https://pic.leetcode.cn/1626420320-YUiulT-image.png] 输入：head = [1,2,3,4,5] 输出：[1,5,2,4,3] 提示： * 链表的长度范围为 [1, 5 * 104] * 1 <= node.val <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 找到中点，反转后半部分，然后合并两个链表

算法步骤:
1. 使用快慢指针找到中点
2. 反转后半部分链表
3. 合并前半部分和反转后的后半部分

关键点:
- 快慢指针+反转链表+合并
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


def reorder_list(head: Optional[ListNode]) -> None:
    """
    函数式接口 - 重排链表
    
    实现思路:
    找到中点，反转后半部分，然后合并两个链表。
    
    Args:
        head: 链表的头节点（原地修改）
        
    Returns:
        None（直接修改链表）
        
    Example:
        >>> head = ListNode.from_list([1,2,3,4])
        >>> reorder_list(head)
    """
    if not head or not head.next:
        return
    
    # 找到中点
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # 反转后半部分
    prev = None
    current = slow.next
    slow.next = None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    # 合并两个链表
    first = head
    second = prev
    while second:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2


# 自动生成Solution类（无需手动编写）
Solution = create_solution(reorder_list)
