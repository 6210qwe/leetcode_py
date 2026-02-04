# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1404
标题: Print Immutable Linked List in Reverse
难度: medium
链接: https://leetcode.cn/problems/print-immutable-linked-list-in-reverse/
题目类型: 栈、递归、链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1265. 逆序打印不可变链表 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归来逆序打印链表。

算法步骤:
1. 定义一个递归函数 `print_list_in_reverse`，该函数接受一个链表节点作为参数。
2. 如果当前节点为空，返回空列表。
3. 递归调用 `print_list_in_reverse` 函数处理当前节点的下一个节点。
4. 将当前节点的值添加到递归调用的结果中。
5. 返回结果列表。

关键点:
- 递归调用可以自然地实现逆序打印。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是链表的长度。每个节点只被访问一次。
空间复杂度: O(n)，递归调用栈的深度为链表的长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def print_linked_list_in_reverse(head: Optional[ListNode]) -> List[int]:
    """
    函数式接口 - 逆序打印不可变链表
    """
    def print_list_in_reverse(node: Optional[ListNode]) -> List[int]:
        if not node:
            return []
        # 递归调用处理下一个节点
        next_values = print_list_in_reverse(node.next)
        # 将当前节点的值添加到结果中
        return next_values + [node.val]

    return print_list_in_reverse(head)


Solution = create_solution(print_linked_list_in_reverse)