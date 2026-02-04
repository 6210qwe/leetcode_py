# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1774
标题: Add Two Polynomials Represented as Linked Lists
难度: medium
链接: https://leetcode.cn/problems/add-two-polynomials-represented-as-linked-lists/
题目类型: 链表、数学、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定两个表示多项式的链表，每个节点包含一个系数和一个指数。返回表示这两个多项式之和的链表。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针遍历两个链表，根据指数大小合并同类项。

算法步骤:
1. 初始化一个虚拟头节点 `dummy` 和一个指向当前节点的指针 `curr`。
2. 使用两个指针 `p1` 和 `p2` 分别遍历两个链表。
3. 比较 `p1` 和 `p2` 当前节点的指数：
   - 如果 `p1` 的指数大于 `p2` 的指数，将 `p1` 节点添加到结果链表中，并移动 `p1`。
   - 如果 `p1` 的指数小于 `p2` 的指数，将 `p2` 节点添加到结果链表中，并移动 `p2`。
   - 如果 `p1` 和 `p2` 的指数相等，将它们的系数相加，创建一个新的节点并添加到结果链表中，然后同时移动 `p1` 和 `p2`。
4. 如果其中一个链表遍历完，将另一个链表剩余的部分直接连接到结果链表中。
5. 返回 `dummy.next` 作为结果链表的头节点。

关键点:
- 使用虚拟头节点简化链表操作。
- 合并同类项时注意系数相加。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是两个链表的长度。
空间复杂度: O(1)，除了结果链表外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def addPoly(self, poly1: Optional[ListNode], poly2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        
        p1, p2 = poly1, poly2
        
        while p1 and p2:
            if p1.power > p2.power:
                curr.next = p1
                p1 = p1.next
            elif p1.power < p2.power:
                curr.next = p2
                p2 = p2.next
            else:
                new_coeff = p1.coefficient + p2.coefficient
                if new_coeff != 0:
                    curr.next = ListNode(new_coeff, p1.power)
                    curr = curr.next
                p1 = p1.next
                p2 = p2.next
            curr = curr.next
        
        # Append the remaining part of the longer list
        if p1:
            curr.next = p1
        if p2:
            curr.next = p2
        
        return dummy.next

Solution = create_solution(Solution)