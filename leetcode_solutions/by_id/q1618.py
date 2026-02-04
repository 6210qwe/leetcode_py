# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1618
标题: Delete N Nodes After M Nodes of a Linked List
难度: easy
链接: https://leetcode.cn/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/
题目类型: 链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1474. 删除链表 M 个节点之后的 N 个节点 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针遍历链表，跳过 M 个节点后删除 N 个节点。

算法步骤:
1. 初始化两个指针 `prev` 和 `current`，都指向链表头。
2. 遍历链表，每次移动 `current` 指针 M 个节点。
3. 将 `prev` 指针的 `next` 指向 `current` 的下一个节点，跳过 N 个节点。
4. 更新 `prev` 指针为 `current`，继续遍历直到链表结束。

关键点:
- 使用双指针可以有效地遍历和删除节点。
- 注意处理边界情况，如链表为空或 M、N 为 0 的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是链表的长度。每个节点最多被访问两次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution

def delete_nodes(head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
    """
    删除链表中每 M 个节点后的 N 个节点。
    
    :param head: 链表头节点
    :param m: 保留的节点数
    :param n: 删除的节点数
    :return: 修改后的链表头节点
    """
    if not head or m == 0:
        return None
    
    dummy = ListNode(0)
    dummy.next = head
    prev, current = dummy, head
    
    while current:
        # 保留 M 个节点
        for _ in range(m):
            if not current:
                break
            prev, current = current, current.next
        
        # 删除 N 个节点
        for _ in range(n):
            if not current:
                break
            current = current.next
        
        # 连接剩余的链表
        prev.next = current
    
    return dummy.next

Solution = create_solution(delete_nodes)