# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 82
标题: Remove Duplicates from Sorted List II
难度: medium
链接: https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/
题目类型: 链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
82. 删除排序链表中的重复元素 II - 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。 示例 1： [https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg] 输入：head = [1,2,3,3,4,4,5] 输出：[1,2,5] 示例 2： [https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg] 输入：head = [1,1,1,2,3] 输出：[2,3] 提示： * 链表中节点数目在范围 [0, 300] 内 * -100 <= Node.val <= 100 * 题目数据保证链表已经按升序 排列
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用虚拟头节点，遍历链表，删除所有重复的节点

算法步骤:
1. 创建虚拟头节点dummy，指向head
2. 使用prev指向当前不重复节点的最后一个节点
3. 遍历链表：
   - 如果当前节点与下一个节点值相同，记录这个值
   - 删除所有值等于该值的节点
   - 否则，prev移动到下一个节点
4. 返回dummy.next

关键点:
- 使用虚拟头节点简化边界处理
- 需要删除所有重复的节点，包括第一个出现的
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 只需一次遍历
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    函数式接口 - 虚拟头节点
    
    实现思路:
    使用虚拟头节点，遍历链表，删除所有重复的节点。
    
    Args:
        head: 已排序的链表头节点
        
    Returns:
        删除重复节点后的链表头节点
        
    Example:
        >>> head = ListNode.from_list([1,2,3,3,4,4,5])
        >>> delete_duplicates(head)
        # 返回[1,2,5]
    """
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while prev.next and prev.next.next:
        if prev.next.val == prev.next.next.val:
            # 记录重复的值
            val = prev.next.val
            # 删除所有值等于val的节点
            while prev.next and prev.next.val == val:
                prev.next = prev.next.next
        else:
            prev = prev.next
    
    return dummy.next


# 自动生成Solution类（无需手动编写）
Solution = create_solution(delete_duplicates)
