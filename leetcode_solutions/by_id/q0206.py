# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 206
标题: Reverse Linked List
难度: easy
链接: https://leetcode.cn/problems/reverse-linked-list/
题目类型: 递归、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
206. 反转链表 - 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。 示例 1： [https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg] 输入：head = [1,2,3,4,5] 输出：[5,4,3,2,1] 示例 2： [https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg] 输入：head = [1,2] 输出：[2,1] 示例 3： 输入：head = [] 输出：[] 提示： * 链表中节点的数目范围是 [0, 5000] * -5000 <= Node.val <= 5000 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用迭代方法，维护前一个节点和当前节点，逐个反转

算法步骤:
1. 初始化prev为None，curr为head
2. 遍历链表：
   - 保存下一个节点
   - 将当前节点的next指向前一个节点
   - 更新prev和curr
3. 返回prev（新的头节点）

关键点:
- 迭代反转，需要保存下一个节点
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历链表一次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    函数式接口 - 反转链表
    
    实现思路:
    使用迭代方法，维护前一个节点和当前节点，逐个反转。
    
    Args:
        head: 链表的头节点
        
    Returns:
        反转后的链表头节点
        
    Example:
        >>> head = ListNode.from_list([1, 2, 3, 4, 5])
        >>> reversed_head = reverse_linked_list(head)
        >>> reversed_head.to_list()
        [5, 4, 3, 2, 1]
    """
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev


# 自动生成Solution类（无需手动编写）
Solution = create_solution(reverse_linked_list)
