# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000270
标题: LRU 缓存
难度: medium
链接: https://leetcode.cn/problems/OrIXps/
题目类型: 设计、哈希表、链表、双向链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 031. LRU 缓存 - 运用所掌握的数据结构，设计和实现一个 LRU (Least Recently Used，最近最少使用) 缓存机制 [https://baike.baidu.com/item/LRU] 。 实现 LRUCache 类： * LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存 * int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。 * void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。 示例： 输入 ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"] [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]] 输出 [null, null, null, 1, null, -1, null, -1, 3, 4] 解释 LRUCache lRUCache = new LRUCache(2); lRUCache.put(1, 1); // 缓存是 {1=1} lRUCache.put(2, 2); // 缓存是 {1=1, 2=2} lRUCache.get(1); // 返回 1 lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3} lRUCache.get(2); // 返回 -1 (未找到) lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3} lRUCache.get(1); // 返回 -1 (未找到) lRUCache.get(3); // 返回 3 lRUCache.get(4); // 返回 4 提示： * 1 <= capacity <= 3000 * 0 <= key <= 10000 * 0 <= value <= 105 * 最多调用 2 * 105 次 get 和 put 进阶：是否可以在 O(1) 时间复杂度内完成这两种操作？ 注意：本题与主站 146 题相同：https://leetcode.cn/problems/lru-cache/ [https://leetcode.cn/problems/lru-cache/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双向链表和哈希表来实现 LRU 缓存。双向链表用于维护访问顺序，哈希表用于快速查找。

算法步骤:
1. 初始化双向链表和哈希表。
2. 在 `get` 方法中，如果键存在于哈希表中，更新其位置到链表头部，并返回其值；否则返回 -1。
3. 在 `put` 方法中，如果键存在于哈希表中，更新其值并移动到链表头部；如果不存在且缓存已满，移除链表尾部的节点，然后将新节点插入链表头部。

关键点:
- 双向链表的头节点和尾节点是虚拟节点，方便插入和删除操作。
- 哈希表存储键到链表节点的映射，保证 O(1) 时间复杂度的查找。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(capacity)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node: ListNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: ListNode):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _move_to_head(self, node: ListNode):
        self._remove_node(node)
        self._add_to_head(node)

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
            if len(self.cache) == self.capacity:
                tail_node = self.tail.prev
                self._remove_node(tail_node)
                del self.cache[tail_node.key]
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)


Solution = create_solution(LRUCache)