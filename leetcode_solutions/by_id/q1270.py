# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1270
标题: Dinner Plate Stacks
难度: hard
链接: https://leetcode.cn/problems/dinner-plate-stacks/
题目类型: 栈、设计、哈希表、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1172. 餐盘栈 - 我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。 实现一个叫「餐盘」的类 DinnerPlates： * DinnerPlates(int capacity) - 给出栈的最大容量 capacity。 * void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。 * int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。 * int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回 -1。 示例： 输入： ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"] [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]] 输出： [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1] 解释： DinnerPlates D = DinnerPlates(2); // 初始化，栈最大容量 capacity = 2 D.push(1); D.push(2); D.push(3); D.push(4); D.push(5); // 栈的现状为： 2 4 1 3 5 ﹈ ﹈ ﹈ D.popAtStack(0); // 返回 2。栈的现状为： 4 1 3 5 ﹈ ﹈ ﹈ D.push(20); // 栈的现状为： 20 4 1 3 5 ﹈ ﹈ ﹈ D.push(21); // 栈的现状为： 20 4 21 1 3 5 ﹈ ﹈ ﹈ D.popAtStack(0); // 返回 20。栈的现状为： 4 21 1 3 5 ﹈ ﹈ ﹈ D.popAtStack(2); // 返回 21。栈的现状为： 4 1 3 5 ﹈ ﹈ ﹈ D.pop() // 返回 5。栈的现状为： 4 1 3 ﹈ ﹈ D.pop() // 返回 4。栈的现状为： 1 3 ﹈ ﹈ D.pop() // 返回 3。栈的现状为： 1 ﹈ D.pop() // 返回 1。现在没有栈。 D.pop() // 返回 -1。仍然没有栈。 提示： * 1 <= capacity <= 20000 * 1 <= val <= 20000 * 0 <= index <= 100000 * 最多会对 push，pop，和 popAtStack 进行 200000 次调用。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个堆来管理未满的栈和非空的栈。一个最小堆用于快速找到第一个未满的栈，另一个最小堆用于快速找到第一个非空的栈。

算法步骤:
1. 初始化时，创建两个最小堆：一个用于存储未满的栈索引，另一个用于存储非空的栈索引。
2. push 操作时，从未满的栈堆中取出最小的索引，将值推入该栈。如果该栈已满，则从未满的栈堆中移除该索引。
3. pop 操作时，从非空的栈堆中取出最大的索引，弹出该栈的顶部值。如果该栈为空，则从非空的栈堆中移除该索引。
4. popAtStack 操作时，直接从指定索引的栈中弹出顶部值。如果该栈为空，则从非空的栈堆中移除该索引。

关键点:
- 使用两个最小堆来高效地管理未满的栈和非空的栈。
- 动态调整堆中的索引，以保持堆的有效性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n)，其中 n 是当前栈的数量。堆操作的时间复杂度为 O(log n)。
空间复杂度: O(n)，其中 n 是当前栈的数量。需要额外的空间来存储堆。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.non_full_stacks = []  # 最小堆，存储未满的栈索引
        self.non_empty_stacks = []  # 最小堆，存储非空的栈索引

    def push(self, val: int) -> None:
        if not self.non_full_stacks:
            self.stacks.append([val])
            if len(self.stacks[-1]) < self.capacity:
                heapq.heappush(self.non_full_stacks, len(self.stacks) - 1)
            if len(self.stacks[-1]) == 1:
                heapq.heappush(self.non_empty_stacks, -(len(self.stacks) - 1))
        else:
            index = heapq.heappop(self.non_full_stacks)
            self.stacks[index].append(val)
            if len(self.stacks[index]) < self.capacity:
                heapq.heappush(self.non_full_stacks, index)
            if len(self.stacks[index]) == 1:
                heapq.heappush(self.non_empty_stacks, -index)

    def pop(self) -> int:
        while self.non_empty_stacks and -self.non_empty_stacks[0] >= len(self.stacks):
            heapq.heappop(self.non_empty_stacks)
        if not self.non_empty_stacks:
            return -1
        index = -heapq.heappop(self.non_empty_stacks)
        value = self.stacks[index].pop()
        if self.stacks[index]:
            heapq.heappush(self.non_empty_stacks, -index)
        if len(self.stacks[index]) < self.capacity:
            heapq.heappush(self.non_full_stacks, index)
        return value

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        value = self.stacks[index].pop()
        if self.stacks[index]:
            heapq.heappush(self.non_empty_stacks, -index)
        if len(self.stacks[index]) < self.capacity:
            heapq.heappush(self.non_full_stacks, index)
        return value

# 示例测试
if __name__ == "__main__":
    dinner_plates = DinnerPlates(2)
    dinner_plates.push(1)
    dinner_plates.push(2)
    dinner_plates.push(3)
    dinner_plates.push(4)
    dinner_plates.push(5)
    print(dinner_plates.popAtStack(0))  # 输出 2
    dinner_plates.push(20)
    dinner_plates.push(21)
    print(dinner_plates.popAtStack(0))  # 输出 20
    print(dinner_plates.popAtStack(2))  # 输出 21
    print(dinner_plates.pop())  # 输出 5
    print(dinner_plates.pop())  # 输出 4
    print(dinner_plates.pop())  # 输出 3
    print(dinner_plates.pop())  # 输出 1
    print(dinner_plates.pop())  # 输出 -1