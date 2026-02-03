# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 838
标题: Design Linked List
难度: medium
链接: https://leetcode.cn/problems/design-linked-list/
题目类型: 设计、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
707. 设计链表 - 你可以选择使用单链表或者双链表，设计并实现自己的链表。 单链表中的节点应该具备两个属性：val 和 next 。val 是当前节点的值，next 是指向下一个节点的指针/引用。 如果是双向链表，则还需要属性 prev 以指示链表中的上一个节点。假设链表中的所有节点下标从 0 开始。 实现 MyLinkedList 类： * MyLinkedList() 初始化 MyLinkedList 对象。 * int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。 * void addAtHead(int val) 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。 * void addAtTail(int val) 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。 * void addAtIndex(int index, int val) 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。 * void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点。 示例： 输入 ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"] [[], [1], [3], [1, 2], [1], [1], [1]] 输出 [null, null, null, null, 2, null, 3] 解释 MyLinkedList myLinkedList = new MyLinkedList(); myLinkedList.addAtHead(1); myLinkedList.addAtTail(3); myLinkedList.addAtIndex(1, 2); // 链表变为 1->2->3 myLinkedList.get(1); // 返回 2 myLinkedList.deleteAtIndex(1); // 现在，链表变为 1->3 myLinkedList.get(1); // 返回 3 提示： * 0 <= index, val <= 1000 * 请不要使用内置的 LinkedList 库。 * 调用 get、addAtHead、addAtTail、addAtIndex 和 deleteAtIndex 的次数不超过 2000 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
