# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3615
标题: Convert Doubly Linked List to Array II
难度: medium
链接: https://leetcode.cn/problems/convert-doubly-linked-list-to-array-ii/
题目类型: 数组、链表、双向链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3294. 将双链表转换为数组 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个指针遍历双向链表，并将每个节点的值依次添加到结果数组中。

算法步骤:
1. 初始化一个空的结果数组 `result`。
2. 使用一个指针 `current` 指向双向链表的头节点。
3. 遍历双向链表，直到 `current` 为空：
   - 将 `current.val` 添加到 `result` 中。
   - 将 `current` 移动到下一个节点。
4. 返回结果数组 `result`。

关键点:
- 使用单次遍历即可完成转换，时间复杂度为 O(n)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是双向链表的长度。我们需要遍历整个链表一次。
空间复杂度: O(n)，结果数组需要存储链表中的所有元素。
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
    :param head: 双向链表的头节点
    :return: 转换后的数组
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


Solution = create_solution(convert_doubly_linked_list_to_array)