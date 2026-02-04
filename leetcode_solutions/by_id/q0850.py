# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 850
标题: Insert into a Sorted Circular Linked List
难度: medium
链接: https://leetcode.cn/problems/insert-into-a-sorted-circular-linked-list/
题目类型: 链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
708. 循环有序列表的插入 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针法找到插入位置，并将新节点插入到循环链表中。

算法步骤:
1. 初始化两个指针 `prev` 和 `curr`，都指向链表头节点。
2. 遍历链表，找到第一个大于等于新节点值的位置。
3. 将新节点插入到 `prev` 和 `curr` 之间。
4. 如果遍历完链表没有找到合适的位置，则将新节点插入到链表尾部。

关键点:
- 双指针法可以有效地找到插入位置。
- 注意处理空链表和只有一个节点的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是链表的长度。最坏情况下需要遍历整个链表。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def insert(self, head: 'Optional[ListNode]', insertVal: int) -> 'ListNode':
        if not head:
            # 如果链表为空，创建一个新节点并指向自己
            new_node = ListNode(insertVal)
            new_node.next = new_node
            return new_node
        
        prev, curr = head, head.next
        to_insert = False
        
        while True:
            # 找到插入位置
            if prev.val <= insertVal <= curr.val:
                to_insert = True
            elif prev.val > curr.val:
                # 处理循环链表的边界情况
                if insertVal >= prev.val or insertVal <= curr.val:
                    to_insert = True
            
            if to_insert:
                # 插入新节点
                prev.next = ListNode(insertVal, curr)
                return head
            
            prev, curr = curr, curr.next
            if prev == head:
                # 遍历完一圈，直接插入到链表尾部
                break
        
        # 插入到链表尾部
        prev.next = ListNode(insertVal, curr)
        return head

Solution = create_solution(Solution)