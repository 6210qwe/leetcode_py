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
核心思想: 使用单链表实现，并通过虚拟头节点简化操作。

算法步骤:
1. 初始化链表时，创建一个虚拟头节点 dummy_head。
2. get 方法：遍历链表，找到指定索引的节点并返回其值。
3. addAtHead 方法：在虚拟头节点后插入新节点。
4. addAtTail 方法：遍历链表到最后一个节点，然后插入新节点。
5. addAtIndex 方法：遍历链表到指定索引前一个节点，然后插入新节点。
6. deleteAtIndex 方法：遍历链表到指定索引前一个节点，然后删除下一个节点。

关键点:
- 使用虚拟头节点简化插入和删除操作。
- 注意边界条件处理，如索引越界等。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 最坏情况下需要遍历整个链表。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.dummy_head.next
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        self.size += 1
        pred = self.dummy_head
        for _ in range(index):
            pred = pred.next
        to_add = ListNode(val, pred.next)
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.dummy_head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next

# 示例测试
if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    print(obj.get(1))  # 输出 2
    obj.deleteAtIndex(1)
    print(obj.get(1))  # 输出 3