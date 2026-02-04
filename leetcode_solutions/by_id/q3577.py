# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3577
标题: Convert Doubly Linked List to Array I
难度: easy
链接: https://leetcode.cn/problems/convert-doubly-linked-list-to-array-i/
题目类型: 数组、链表、双向链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3263. 将双链表转换为数组 I - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 遍历双向链表并将节点值存储到数组中。

算法步骤:
1. 初始化一个空数组 `result`。
2. 使用一个指针遍历双向链表，将每个节点的值添加到 `result` 中。
3. 返回 `result`。

关键点:
- 使用指针遍历双向链表，确保所有节点都被访问到。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是双向链表的长度。我们需要遍历整个链表一次。
空间复杂度: O(n)，需要一个数组来存储双向链表的所有节点值。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def convert_doubly_linked_list_to_array(head: Optional[ListNode]) -> List[int]:
    """
    将双向链表转换为数组
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


Solution = create_solution(convert_doubly_linked_list_to_array)