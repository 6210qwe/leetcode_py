# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 148
标题: Sort List
难度: medium
链接: https://leetcode.cn/problems/sort-list/
题目类型: 链表、双指针、分治、排序、归并排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
148. 排序链表 - 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 示例 1： [https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg] 输入：head = [4,2,1,3] 输出：[1,2,3,4] 示例 2： [https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg] 输入：head = [-1,5,3,4,0] 输出：[-1,0,3,4,5] 示例 3： 输入：head = [] 输出：[] 提示： * 链表中节点的数目在范围 [0, 5 * 104] 内 * -105 <= Node.val <= 105 进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 归并排序，使用快慢指针找到中点，递归排序左右两部分，然后合并

算法步骤:
1. 使用快慢指针找到中点
2. 递归排序左半部分和右半部分
3. 合并两个有序链表

关键点:
- 归并排序，O(nlogn)时间复杂度
- 时间复杂度O(nlogn)，空间复杂度O(logn)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(nlogn) - 归并排序的时间复杂度
空间复杂度: O(logn) - 递归栈深度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    函数式接口 - 排序链表
    
    实现思路:
    归并排序，使用快慢指针找到中点，递归排序左右两部分，然后合并。
    
    Args:
        head: 链表的头节点
        
    Returns:
        排序后链表的头节点
        
    Example:
        >>> head = ListNode.from_list([4,2,1,3])
        >>> sort_list(head)
    """
    if not head or not head.next:
        return head
    
    # 找到中点
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # 分割链表
    mid = slow.next
    slow.next = None
    
    # 递归排序
    left = sort_list(head)
    right = sort_list(mid)
    
    # 合并两个有序链表
    dummy = ListNode(0)
    current = dummy
    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
    
    current.next = left or right
    return dummy.next


# 自动生成Solution类（无需手动编写）
Solution = create_solution(sort_list)
