# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 147
标题: Insertion Sort List
难度: medium
链接: https://leetcode.cn/problems/insertion-sort-list/
题目类型: 链表、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
147. 对链表进行插入排序 - 给定单个链表的头 head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。 插入排序 算法的步骤: 1. 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。 2. 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。 3. 重复直到所有输入数据插入完为止。 下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。 对链表进行插入排序。 [https://pic.leetcode.cn/1724130387-qxfMwx-Insertion-sort-example-300px.gif] 示例 1： [https://pic.leetcode.cn/1724130414-QbPAjl-image.png] 输入: head = [4,2,1,3] 输出: [1,2,3,4] 示例 2： [https://pic.leetcode.cn/1724130432-zoOvdI-image.png] 输入: head = [-1,5,3,4,0] 输出: [-1,0,3,4,5] 提示： * 列表中的节点数在 [1, 5000]范围内 * -5000 <= Node.val <= 5000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 插入排序，维护一个已排序的链表，逐个插入新节点

算法步骤:
1. 创建虚拟头节点
2. 遍历原链表，对于每个节点，在已排序链表中找到合适位置插入

关键点:
- 插入排序，维护已排序链表
- 时间复杂度O(n^2)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - 插入排序的时间复杂度
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def insertion_sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    函数式接口 - 对链表进行插入排序
    
    实现思路:
    插入排序，维护一个已排序的链表，逐个插入新节点。
    
    Args:
        head: 链表的头节点
        
    Returns:
        排序后链表的头节点
        
    Example:
        >>> head = ListNode.from_list([4,2,1,3])
        >>> insertion_sort_list(head)
    """
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    current = head
    
    while current:
        prev = dummy
        # 在已排序链表中找到插入位置
        while prev.next and prev.next.val < current.val:
            prev = prev.next
        
        # 插入节点
        next_node = current.next
        current.next = prev.next
        prev.next = current
        current = next_node
    
    return dummy.next


# 自动生成Solution类（无需手动编写）
Solution = create_solution(insertion_sort_list)
