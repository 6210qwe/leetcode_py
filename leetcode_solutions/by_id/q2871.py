# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2871
标题: Double a Number Represented as a Linked List
难度: medium
链接: https://leetcode.cn/problems/double-a-number-represented-as-a-linked-list/
题目类型: 栈、链表、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2816. 翻倍以链表形式表示的数字 - 给你一个 非空 链表的头节点 head ，表示一个不含前导零的非负数整数。 将链表 翻倍 后，返回头节点 head 。 示例 1： [https://assets.leetcode.com/uploads/2023/05/28/example.png] 输入：head = [1,8,9] 输出：[3,7,8] 解释：上图中给出的链表，表示数字 189 。返回的链表表示数字 189 * 2 = 378 。 示例 2： [https://assets.leetcode.com/uploads/2023/05/28/example2.png] 输入：head = [9,9,9] 输出：[1,9,9,8] 解释：上图中给出的链表，表示数字 999 。返回的链表表示数字 999 * 2 = 1998 。 提示： * 链表中节点的数目在范围 [1, 104] 内 * 0 <= Node.val <= 9 * 生成的输入满足：链表表示一个不含前导零的数字，除了数字 0 本身。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈来存储链表节点的值，然后从栈顶开始处理每个节点，进行翻倍操作，并处理进位。

算法步骤:
1. 使用栈存储链表节点的值。
2. 从栈顶开始处理每个节点，进行翻倍操作，并处理进位。
3. 如果最后有进位，则在链表头部添加一个新的节点。

关键点:
- 使用栈来逆序处理链表节点。
- 处理进位时，需要考虑是否需要在链表头部添加新的节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是链表的长度。我们需要遍历链表一次将节点值存入栈中，再遍历栈一次进行翻倍和进位处理。
空间复杂度: O(n)，我们使用了一个栈来存储链表节点的值。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution

def double_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    # 使用栈存储链表节点的值
    stack = []
    current = head
    while current:
        stack.append(current.val)
        current = current.next

    carry = 0
    new_head = None
    while stack:
        val = stack.pop()
        doubled_val = val * 2 + carry
        node_val = doubled_val % 10
        carry = doubled_val // 10

        new_node = ListNode(node_val)
        new_node.next = new_head
        new_head = new_node

    if carry:
        new_node = ListNode(carry)
        new_node.next = new_head
        new_head = new_node

    return new_head

Solution = create_solution(double_linked_list)