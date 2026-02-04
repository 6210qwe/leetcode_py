# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1903
标题: Design Most Recently Used Queue
难度: medium
链接: https://leetcode.cn/problems/design-most-recently-used-queue/
题目类型: 设计、数组、链表、分治、双向链表、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1756. 设计最近使用（MRU）队列 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双向链表来维护最近使用的元素顺序，并使用哈希表来实现 O(1) 时间复杂度的插入和删除操作。

算法步骤:
1. 初始化一个双向链表和一个哈希表。
2. 在 `moveToHead` 方法中，将指定节点移动到双向链表的头部。
3. 在 `removeNode` 方法中，从双向链表中移除指定节点。
4. 在 `insertAtHead` 方法中，将新节点插入到双向链表的头部。
5. 在 `get` 方法中，如果键存在，则将对应的节点移动到头部并返回其值；否则返回 -1。
6. 在 `put` 方法中，如果键存在，则更新其值并将其移动到头部；否则插入新节点，并在超出容量时移除最旧的节点。
7. 在 `mostRecentlyUsed` 方法中，返回当前最常使用的键。

关键点:
- 使用双向链表来维护最近使用的元素顺序。
- 使用哈希表来实现 O(1) 时间复杂度的插入和删除操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 所有操作（get, put, mostRecentlyUsed）的时间复杂度均为 O(1)。
空间复杂度: O(capacity) - 双向链表和哈希表的空间复杂度均为 O(capacity)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: Node):
        # Always add the new node right after head.
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node):
        # Remove an existing node from the linked list.
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node: Node):
        # Move certain node in between to the head.
        self._remove_node(node)
        self._add_node(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            if len(self.cache) > self.capacity:
                # Pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]

    def _pop_tail(self) -> Node:
        res = self.tail.prev
        self._remove_node(res)
        return res

    def mostRecentlyUsed(self) -> int:
        return self.head.next.key


# 示例用法
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # 返回 1
    cache.put(3, 3)      # 该操作会使得密钥 2 作废
    print(cache.get(2))  # 返回 -1 (未找到)
    cache.put(4, 4)      # 该操作会使得密钥 1 作废
    print(cache.get(1))  # 返回 -1 (未找到)
    print(cache.get(3))  # 返回 3
    print(cache.get(4))  # 返回 4
    print(cache.mostRecentlyUsed())  # 返回 4