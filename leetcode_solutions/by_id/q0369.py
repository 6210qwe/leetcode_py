# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 369
标题: Plus One Linked List
难度: medium
链接: https://leetcode.cn/problems/plus-one-linked-list/
题目类型: 链表、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
369. 给单链表加一 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 从链表尾部往前找到第一个不为 9 的节点加一，其后的所有节点清零；若不存在，则在头部新建 1。

算法步骤:
1. 使用哑节点 dummy 指向 head，遍历链表，用指针 `last_not_nine` 记录「最后一个值不为 9 的节点」，初始指向 dummy。
2. 完成遍历后：
   - 将 `last_not_nine.val += 1`。
   - 将 `last_not_nine` 之后的所有节点值设为 0。
3. 若 dummy.val 仍为 0，则说明没有进位到新头，返回 dummy.next；否则返回 dummy 作为新表头。

关键点:
- 不需要反转链表或用栈，单次遍历即可完成。
- 通过哑节点自然处理「所有位都为 9」的情况，例如 9->9 变为 1->0->0。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，n 为链表长度，两次线性扫描：一次确定 `last_not_nine`，一次把其后节点清零。
空间复杂度: O(1) 额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def plus_one_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    单链表表示非负整数，在其基础上加一并返回新表头。

    先找到从尾部起第一个不是 9 的节点，加一并将之后所有节点置为 0，如不存在则在头部插入 1。
    """
    dummy = ListNode(0, head)
    last_not_nine = dummy
    cur = head
    while cur:
        if cur.val != 9:
            last_not_nine = cur
        cur = cur.next

    # last_not_nine 之后全部变为 0
    last_not_nine.val += 1
    cur = last_not_nine.next
    while cur:
        cur.val = 0
        cur = cur.next

    return dummy if dummy.val else dummy.next


# 自动生成Solution类（无需手动编写）
Solution = create_solution(plus_one_linked_list)
