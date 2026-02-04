# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 860
标题: Design Circular Queue
难度: medium
链接: https://leetcode.cn/problems/design-circular-queue/
题目类型: 设计、队列、数组、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
622. 设计循环队列 - 设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。 循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。 你的实现应该支持如下操作： * MyCircularQueue(k): 构造器，设置队列长度为 k 。 * Front: 从队首获取元素。如果队列为空，返回 -1 。 * Rear: 获取队尾元素。如果队列为空，返回 -1 。 * enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。 * deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。 * isEmpty(): 检查循环队列是否为空。 * isFull(): 检查循环队列是否已满。 示例： MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3 circularQueue.enQueue(1); // 返回 true circularQueue.enQueue(2); // 返回 true circularQueue.enQueue(3); // 返回 true circularQueue.enQueue(4); // 返回 false，队列已满 circularQueue.Rear(); // 返回 3 circularQueue.isFull(); // 返回 true circularQueue.deQueue(); // 返回 true circularQueue.enQueue(4); // 返回 true circularQueue.Rear(); // 返回 4 提示： * 所有的值都在 0 至 1000 的范围内； * 操作数将在 1 至 1000 的范围内； * 请不要使用内置的队列库。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用固定大小的数组来实现循环队列，并使用两个指针 front 和 rear 来跟踪队列的头部和尾部。

算法步骤:
1. 初始化队列时，分配一个固定大小的数组，并初始化 front 和 rear 指针。
2. enQueue 时，检查队列是否已满，未满则将元素插入到 rear 指针位置，并更新 rear 指针。
3. deQueue 时，检查队列是否为空，非空则移除 front 指针位置的元素，并更新 front 指针。
4. Front 和 Rear 方法分别返回 front 和 rear 指针位置的元素。
5. isEmpty 和 isFull 方法分别检查队列是否为空或已满。

关键点:
- 使用模运算 (front % capacity) 和 (rear % capacity) 来处理循环。
- 为了区分队列为空和队列为满的情况，使用一个额外的变量 size 来记录当前队列中的元素数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 所有操作的时间复杂度都是常数级。
空间复杂度: O(k) - 需要一个固定大小的数组来存储队列元素。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [0] * k
        self.front = 0
        self.rear = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear % self.capacity] = value
        self.rear += 1
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front += 1
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front % self.capacity]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.rear - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


Solution = create_solution(MyCircularQueue)