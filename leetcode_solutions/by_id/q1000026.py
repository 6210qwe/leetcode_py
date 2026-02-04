# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000026
标题: LRU Cache LCCI
难度: medium
链接: https://leetcode.cn/problems/lru-cache-lcci/
题目类型: 设计、哈希表、链表、双向链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 16.25. LRU 缓存 - 设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。当缓存被填满时，它应该删除最近最少使用的项目。 它应该支持以下操作： 获取数据 get 和 写入数据 put 。 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。 示例： LRUCache cache = new LRUCache( 2 /* 缓存容量 */ ); cache.put(1, 1); cache.put(2, 2); cache.get(1); // 返回 1 cache.put(3, 3); // 该操作会使得密钥 2 作废 cache.get(2); // 返回 -1 (未找到) cache.put(4, 4); // 该操作会使得密钥 1 作废 cache.get(1); // 返回 -1 (未找到) cache.get(3); // 返回 3 cache.get(4); // 返回 4
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双向链表和哈希表来实现 LRU 缓存。双向链表用于维护元素的顺序，哈希表用于快速查找。

算法步骤:
1. 初始化缓存，设置最大容量，并创建一个双向链表和一个哈希表。
2. 在 `get` 操作中，如果键存在，则将对应的节点移到链表头部，并返回节点的值；否则返回 -1。
3. 在 `put` 操作中，如果键已存在，则更新节点的值并将其移到链表头部；如果键不存在且缓存已满，则移除链表尾部的节点，然后在链表头部插入新节点。

关键点:
- 双向链表用于维护元素的顺序，最近使用的元素在头部，最久未使用的元素在尾部。
- 哈希表用于快速查找节点。
- `get` 和 `put` 操作的时间复杂度均为 O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 所有操作（get 和 put）的时间复杂度均为 O(1)。
空间复杂度: O(capacity) - 空间复杂度取决于缓存的最大容量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional


class DLinkedNode:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev: Optional[DLinkedNode] = None
        self.next: Optional[DLinkedNode] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, DLinkedNode] = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_to_head(self, node: DLinkedNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DLinkedNode):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _move_to_head(self, node: DLinkedNode):
        self._remove_node(node)
        self._add_node_to_head(node)

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
            if len(self.cache) >= self.capacity:
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_node_to_head(new_node)


def create_solution():
    """
    工厂函数 - 创建并返回 LRUCache 类的实例
    """
    def solution_function_name(params):
        capacity = params['capacity']
        return LRUCache(capacity)

    return solution_function_name


Solution = create_solution()