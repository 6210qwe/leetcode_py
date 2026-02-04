# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 817
标题: Design HashMap
难度: easy
链接: https://leetcode.cn/problems/design-hashmap/
题目类型: 设计、数组、哈希表、链表、哈希函数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
706. 设计哈希映射 - 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。 实现 MyHashMap 类： * MyHashMap() 用空映射初始化对象 * void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。 * int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。 * void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。 示例： 输入： ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"] [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]] 输出： [null, null, null, 1, -1, null, 1, null, -1] 解释： MyHashMap myHashMap = new MyHashMap(); myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]] myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]] myHashMap.get(1); // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]] myHashMap.get(3); // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]] myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值） myHashMap.get(2); // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]] myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]] myHashMap.get(2); // 返回 -1（未找到），myHashMap 现在为 [[1,1]] 提示： * 0 <= key, value <= 106 * 最多调用 104 次 put、get 和 remove 方法
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用链地址法解决哈希冲突。通过一个固定大小的数组存储链表头节点，每个链表用于存储哈希到同一位置的键值对。

算法步骤:
1. 初始化一个固定大小的数组，每个元素是一个链表头节点。
2. 在 put 操作中，计算 key 的哈希值，找到对应的链表，遍历链表检查是否存在 key，如果存在则更新 value，否则插入新的键值对。
3. 在 get 操作中，计算 key 的哈希值，找到对应的链表，遍历链表查找 key，如果找到则返回对应的 value，否则返回 -1。
4. 在 remove 操作中，计算 key 的哈希值，找到对应的链表，遍历链表查找 key，如果找到则删除该节点。

关键点:
- 使用链地址法处理哈希冲突。
- 数组大小选择合适的质数以减少冲突。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) 平均情况，O(n) 最坏情况（n 为哈希表中的元素个数）
空间复杂度: O(m + n)，其中 m 是数组的大小，n 是存储的键值对数量
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional

class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1009  # 选择一个质数作为数组大小
        self.buckets = [None] * self.size  # 初始化桶数组

    def _hash(self, key: int) -> int:
        return key % self.size  # 计算哈希值

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = ListNode(-1, -1)  # 虚拟头节点
        prev = self.buckets[index]
        while prev.next:
            if prev.next.key == key:
                prev.next.value = value  # 更新值
                return
            prev = prev.next
        prev.next = ListNode(key, value)  # 插入新节点

    def get(self, key: int) -> int:
        index = self._hash(key)
        curr = self.buckets[index]
        while curr and curr.next:
            if curr.next.key == key:
                return curr.next.value  # 返回值
            curr = curr.next
        return -1  # 未找到

    def remove(self, key: int) -> None:
        index = self._hash(key)
        curr = self.buckets[index]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next  # 删除节点
                return
            curr = curr.next

# 测试用例
if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))  # 输出 1
    print(obj.get(3))  # 输出 -1
    obj.put(2, 1)
    print(obj.get(2))  # 输出 1
    obj.remove(2)
    print(obj.get(2))  # 输出 -1