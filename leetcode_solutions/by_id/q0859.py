# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 859
标题: Design Circular Deque
难度: medium
链接: https://leetcode.cn/problems/design-circular-deque/
题目类型: 设计、队列、数组、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
641. 设计循环双端队列 - 设计实现双端队列。 实现 MyCircularDeque 类: * MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。 * boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。 * boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。 * boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。 * boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。 * int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。 * int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。 * boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false 。 * boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。 示例 1： 输入 ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"] [[3], [1], [2], [3], [4], [], [], [], [4], []] 输出 [null, true, true, true, false, 2, true, true, true, 4] 解释 MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3 circularDeque.insertLast(1); // 返回 true circularDeque.insertLast(2); // 返回 true circularDeque.insertFront(3); // 返回 true circularDeque.insertFront(4); // 已经满了，返回 false circularDeque.getRear(); // 返回 2 circularDeque.isFull(); // 返回 true circularDeque.deleteLast(); // 返回 true circularDeque.insertFront(4); // 返回 true circularDeque.getFront(); // 返回 4 提示： * 1 <= k <= 1000 * 0 <= value <= 1000 * insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull 调用次数不大于 2000 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用数组来实现循环双端队列，并使用两个指针 head 和 tail 来标记队列的头和尾。

算法步骤:
1. 初始化时，分配一个大小为 k+1 的数组，以避免在插入和删除时进行额外的检查。
2. 使用两个指针 head 和 tail 分别指向队列的头和尾。
3. 在插入和删除操作中，更新 head 和 tail 指针的位置。
4. 使用模运算来处理循环。

关键点:
- 数组大小为 k+1，以避免在插入和删除时进行额外的检查。
- 使用模运算来处理循环。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(k)，其中 k 是队列的最大容量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional


class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k + 1
        self.data = [0] * self.capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head - 1 + self.capacity) % self.capacity
        self.data[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.tail - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity - 1


# 测试用例
if __name__ == "__main__":
    circularDeque = MyCircularDeque(3)
    print(circularDeque.insertLast(1))  # 返回 true
    print(circularDeque.insertLast(2))  # 返回 true
    print(circularDeque.insertFront(3))  # 返回 true
    print(circularDeque.insertFront(4))  # 返回 false
    print(circularDeque.getRear())  # 返回 2
    print(circularDeque.isFull())  # 返回 true
    print(circularDeque.deleteLast())  # 返回 true
    print(circularDeque.insertFront(4))  # 返回 true
    print(circularDeque.getFront())  # 返回 4