# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 432
标题: All O`one Data Structure
难度: hard
链接: https://leetcode.cn/problems/all-oone-data-structure/
题目类型: 设计、哈希表、链表、双向链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
432. 全 O(1) 的数据结构 - 请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。 实现 AllOne 类： * AllOne() 初始化数据结构的对象。 * inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。 * dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。测试用例保证：在减少计数前，key 存在于数据结构中。 * getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。 * getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。 注意：每个函数都应当满足 O(1) 平均时间复杂度。 示例： 输入 ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"] [[], ["hello"], ["hello"], [], [], ["leet"], [], []] 输出 [null, null, null, "hello", "hello", null, "hello", "leet"] 解释 AllOne allOne = new AllOne(); allOne.inc("hello"); allOne.inc("hello"); allOne.getMaxKey(); // 返回 "hello" allOne.getMinKey(); // 返回 "hello" allOne.inc("leet"); allOne.getMaxKey(); // 返回 "hello" allOne.getMinKey(); // 返回 "leet" 提示： * 1 <= key.length <= 10 * key 由小写英文字母组成 * 测试用例保证：在每次调用 dec 时，数据结构中总存在 key * 最多调用 inc、dec、getMaxKey 和 getMinKey 方法 5 * 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双向链表和哈希表来实现 O(1) 时间复杂度的操作。

算法步骤:
1. 使用双向链表来维护不同计数的节点。
2. 使用哈希表来快速查找每个键对应的节点。
3. 在 `inc` 和 `dec` 操作中，更新键的计数并调整其在链表中的位置。
4. `getMaxKey` 和 `getMinKey` 操作直接返回链表头尾节点的键。

关键点:
- 使用双向链表来维护计数节点的顺序。
- 使用哈希表来快速查找键对应的节点。
- 在 `inc` 和 `dec` 操作中，通过调整节点的位置来保持链表的有序性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 所有操作都在 O(1) 时间内完成。
空间复杂度: O(n) - 使用了哈希表和双向链表来存储数据，其中 n 是键的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Dict, Optional


class Node:
    def __init__(self, count: int):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.key_to_node = {}
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_if_empty(self, node: Node):
        if not node.keys:
            self._remove_node(node)

    def _remove_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_after(self, prev_node: Node, new_node: Node):
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def inc(self, key: str) -> None:
        if key in self.key_to_node:
            current_node = self.key_to_node[key]
            current_node.keys.remove(key)
            self._remove_if_empty(current_node)
            new_count = current_node.count + 1
        else:
            new_count = 1

        if current_node.next.count > new_count:
            new_node = Node(new_count)
            self._insert_after(current_node, new_node)
        else:
            new_node = current_node.next

        new_node.keys.add(key)
        self.key_to_node[key] = new_node

    def dec(self, key: str) -> None:
        if key in self.key_to_node:
            current_node = self.key_to_node[key]
            current_node.keys.remove(key)
            self._remove_if_empty(current_node)
            new_count = current_node.count - 1

            if new_count > 0:
                if current_node.prev.count < new_count:
                    new_node = Node(new_count)
                    self._insert_after(current_node.prev, new_node)
                else:
                    new_node = current_node.prev

                new_node.keys.add(key)
                self.key_to_node[key] = new_node
            else:
                del self.key_to_node[key]

    def getMaxKey(self) -> str:
        if self.tail.prev.count == float('inf'):
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next.count == float('-inf'):
            return ""
        return next(iter(self.head.next.keys))


# 自动生成Solution类（无需手动编写）
Solution = create_solution(AllOne)