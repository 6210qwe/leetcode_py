# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 83
标题: Remove Duplicates from Sorted List
难度: easy
链接: https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
题目类型: 链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
83. 删除排序链表中的重复元素 - 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。 示例 1： [https://assets.leetcode.com/uploads/2021/01/04/list1.jpg] 输入：head = [1,1,2] 输出：[1,2] 示例 2： [https://assets.leetcode.com/uploads/2021/01/04/list2.jpg] 输入：head = [1,1,2,3,3] 输出：[1,2,3] 提示： * 链表中节点数目在范围 [0, 300] 内 * -100 <= Node.val <= 100 * 题目数据保证链表已经按升序 排列
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 遍历链表，如果当前节点与下一个节点值相同，删除下一个节点

算法步骤:
1. 如果链表为空或只有一个节点，直接返回
2. 使用current指向当前节点
3. 遍历链表：
   - 如果current.val == current.next.val，删除current.next
   - 否则，current移动到下一个节点
4. 返回head

关键点:
- 保留第一个出现的节点，删除后续重复的节点
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
    函数式接口 - 遍历删除
    
    实现思路:
    遍历链表，如果当前节点与下一个节点值相同，删除下一个节点。
    
    Args:
        head: 已排序的链表头节点
        
    Returns:
        删除重复元素后的链表头节点
        
    Example:
        >>> head = ListNode.from_list([1,1,2])
        >>> delete_duplicates(head)
        # 返回[1,2]
    """
    if not head or not head.next:
        return head
    
    current = head
    while current and current.next:
        if current.val == current.next.val:
            # 删除下一个节点
            current.next = current.next.next
        else:
            current = current.next
    
    return head


# 自动生成Solution类（无需手动编写）
Solution = create_solution(delete_duplicates)
