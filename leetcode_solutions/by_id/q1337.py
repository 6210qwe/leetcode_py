# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1337
标题: Design Skiplist
难度: hard
链接: https://leetcode.cn/problems/design-skiplist/
题目类型: 设计、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1206. 设计跳表 - 不使用任何库函数，设计一个 跳表 。 跳表 是在 O(log(n)) 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想与链表相似。 例如，一个跳表包含 [30, 40, 50, 60, 70, 90] ，然后增加 80、45 到跳表中，以下图的方式操作： [https://pic.leetcode.cn/1702370216-mKQcTt-1506_skiplist.gif] 跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 O(n)。跳表的每一个操作的平均时间复杂度是 O(log(n))，空间复杂度是 O(n)。 了解更多 : https://oi-wiki.org/ds/skiplist/ [https://oi-wiki.org/ds/skiplist/] 在本题中，你的设计应该要包含这些函数： * bool search(int target) : 返回target是否存在于跳表中。 * void add(int num): 插入一个元素到跳表。 * bool erase(int num): 在跳表中删除一个值，如果 num 不存在，直接返回false. 如果存在多个 num ，删除其中任意一个即可。 注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。 示例 1: 输入 ["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"] [[], [1], [2], [3], [0], [4], [1], [0], [1], [1]] 输出 [null, null, null, null, false, null, true, false, true, false] 解释 Skiplist skiplist = new Skiplist(); skiplist.add(1); skiplist.add(2); skiplist.add(3); skiplist.search(0); // 返回 false skiplist.add(4); skiplist.search(1); // 返回 true skiplist.erase(0); // 返回 false，0 不在跳表中 skiplist.erase(1); // 返回 true skiplist.search(1); // 返回 false，1 已被擦除 提示: * 0 <= num, target <= 2 * 104 * 调用search, add, erase操作次数不大于 5 * 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用多层链表来实现跳表，每一层链表的节点数大约是上一层的一半。
- 每个节点包含指向下一节点和下一层节点的指针。

算法步骤:
1. 初始化跳表时，创建头节点和尾节点。
2. 在插入操作时，从最高层开始向下查找，找到合适的位置后插入新节点。
3. 在删除操作时，从最高层开始向下查找，找到目标节点后删除。
4. 在搜索操作时，从最高层开始向下查找，直到找到目标节点或到达最底层。

关键点:
- 使用随机化方法决定新节点的层数，以保持跳表的平衡。
- 通过多层链表实现高效的插入、删除和搜索操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(n)) - 平均情况下，每个操作的时间复杂度为 O(log(n))。
空间复杂度: O(n) - 每个节点的平均层数为 O(log(n))，因此总的空间复杂度为 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

import random

class Node:
    def __init__(self, val, level):
        self.val = val
        self.next = [None] * level

class Skiplist:
    def __init__(self, p=0.5, max_level=32):
        self.p = p
        self.max_level = max_level
        self.head = Node(-1, self.max_level)
        self.level = 0

    def _random_level(self):
        level = 1
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def _update(self, target):
        update = [None] * self.max_level
        current = self.head
        for i in range(self.level - 1, -1, -1):
            while current.next[i] and current.next[i].val < target:
                current = current.next[i]
            update[i] = current
        return update

    def search(self, target):
        current = self.head
        for i in range(self.level - 1, -1, -1):
            while current.next[i] and current.next[i].val < target:
                current = current.next[i]
            if current.next[i] and current.next[i].val == target:
                return True
        return False

    def add(self, num):
        level = self._random_level()
        new_node = Node(num, level)
        if level > self.level:
            for i in range(self.level, level):
                self.head.next[i] = new_node
            self.level = level
        update = self._update(num)
        for i in range(level):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, num):
        update = self._update(num)
        current = update[0].next[0]
        if not current or current.val != num:
            return False
        for i in range(self.level):
            if update[i].next[i] != current:
                break
            update[i].next[i] = current.next[i]
        while self.level > 1 and self.head.next[self.level - 1] is None:
            self.level -= 1
        return True

Solution = create_solution(Skiplist)