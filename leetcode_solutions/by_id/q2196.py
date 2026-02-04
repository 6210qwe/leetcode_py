# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2196
标题: Reverse Nodes in Even Length Groups
难度: medium
链接: https://leetcode.cn/problems/reverse-nodes-in-even-length-groups/
题目类型: 链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2074. 反转偶数长度组的节点 - 给你一个链表的头节点 head 。 链表中的节点 按顺序 划分成若干 非空 组，这些非空组的长度构成一个自然数序列（1, 2, 3, 4, ...）。一个组的 长度 就是组中分配到的节点数目。换句话说： * 节点 1 分配给第一组 * 节点 2 和 3 分配给第二组 * 节点 4、5 和 6 分配给第三组，以此类推 注意，最后一组的长度可能小于或者等于 1 + 倒数第二组的长度 。 反转 每个 偶数 长度组中的节点，并返回修改后链表的头节点 head 。 示例 1： [https://assets.leetcode.com/uploads/2021/10/25/eg1.png] 输入：head = [5,2,6,3,9,1,7,3,8,4] 输出：[5,6,2,3,9,1,4,8,3,7] 解释： - 第一组长度为 1 ，奇数，没有发生反转。 - 第二组长度为 2 ，偶数，节点反转。 - 第三组长度为 3 ，奇数，没有发生反转。 - 最后一组长度为 4 ，偶数，节点反转。 示例 2： [https://assets.leetcode.com/uploads/2021/10/25/eg2.png] 输入：head = [1,1,0,6] 输出：[1,0,1,6] 解释： - 第一组长度为 1 ，没有发生反转。 - 第二组长度为 2 ，节点反转。 - 最后一组长度为 1 ，没有发生反转。 示例 3： [https://assets.leetcode.com/uploads/2021/10/28/eg3.png] 输入：head = [2,1] 输出：[2,1] 解释： - 第一组长度为 1 ，没有发生反转。 - 最后一组长度为 1 ，没有发生反转。 提示： * 链表中节点数目范围是 [1, 105] * 0 <= Node.val <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个指针来遍历链表并反转偶数长度的组。

算法步骤:
1. 初始化一个虚拟头节点 `dummy`，指向链表的头节点 `head`。
2. 使用两个指针 `prev` 和 `curr` 来遍历链表。
3. 对于每个组，计算该组的长度 `group_length`。
4. 如果 `group_length` 是偶数，则反转该组的节点。
5. 更新 `prev` 和 `curr` 指针，继续处理下一个组。
6. 返回修改后的链表头节点。

关键点:
- 使用辅助函数 `reverse_group` 来反转指定长度的节点。
- 通过 `prev` 和 `curr` 指针来管理当前组和下一个组的连接。
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

def reverse_group(head: ListNode, length: int) -> ListNode:
    """反转链表中的前 length 个节点"""
    prev, curr = None, head
    for _ in range(length):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev, head

def solution_function_name(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    函数式接口 - 反转偶数长度组的节点
    """
    if not head:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev, curr = dummy, head
    group_length = 1

    while curr:
        # 计算当前组的实际长度
        actual_length = 0
        temp = curr
        while temp and actual_length < group_length:
            temp = temp.next
            actual_length += 1

        if actual_length % 2 == 0:
            # 反转当前组
            new_head, new_tail = reverse_group(curr, actual_length)
            prev.next = new_head
            new_tail.next = temp
            prev = new_tail
            curr = temp
        else:
            # 不反转，直接移动指针
            for _ in range(actual_length):
                prev = curr
                curr = curr.next

        group_length += 1

    return dummy.next

Solution = create_solution(solution_function_name)