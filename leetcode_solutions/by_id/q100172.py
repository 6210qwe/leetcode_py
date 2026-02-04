```python
# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100172
标题: Three in One LCCI
难度: easy
链接: https://leetcode.cn/problems/three-in-one-lcci/
题目类型: 栈、设计、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 03.01. 三合一 - 三合一。描述如何只用一个数组来实现三个栈。 你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。 构造函数会传入一个stackSize参数，代表每个栈的大小。 示例 1： 输入： ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"] [[1], [0, 1], [0, 2], [0], [0], [0], [0]] 输出： [null, null, null, 1, -1, -1, true] 说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。 示例 2： 输入： ["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"] [[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]] 输出： [null, null, null, null, 2, 1, -1, -1] 提示： * 0 <= stackNum <= 2
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个固定大小的数组来存储三个栈的数据，并使用三个指针分别指向每个栈的栈顶。

算法步骤:
1. 初始化一个固定大小的数组和三个指针，分别指向三个栈的栈顶。
2. 对于push操作，检查当前栈是否已满，如果未满则将数据压入栈中并更新指针。
3. 对于pop操作，检查当前栈是否为空，如果不为空则弹出栈顶元素并更新指针。
4. 对于peek操作，直接返回当前栈顶元素。
5. 对于isEmpty操作，检查当前栈指针是否等于初始位置。

关键点:
- 使用一个数组存储三个栈的数据，通过计算偏移量来确定每个栈的位置。
- 每个栈的指针用于跟踪栈顶位置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(n)，其中n是总的栈大小
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional


class TripleInOne:

    def __init__(self, stack_size: int):
        self.stack_size = stack_size
        self.array = [0] * (3 * stack_size)
        self.pointers = [0, stack_size, 2 * stack_size]

    def push(self, stack_num: int, value: int) -> None:
        if self.pointers[stack_num] < (stack_num + 1) * self.stack_size:
            self.array[self.pointers[stack_num]] = value
            self.pointers[stack_num] += 1

    def pop(self, stack_num: int) -> int:
        if self.pointers[stack_num] > stack_num * self.stack_size:
            self.pointers[stack_num] -= 1
            return self.array[self.pointers[stack_num]]
        return -1

    def peek(self, stack_num: int) -> int:
        if self.pointers[stack_num] > stack_num * self.stack_size:
            return self.array[self.pointers[stack_num] - 1]
        return -1

    def is_empty(self, stack_num: int) -> bool:
        return self.pointers[stack_num] == stack_num * self.stack_size


# 测试用例
if __name__ == "__main__":
    triple_stack = TripleInOne(1)
    triple_stack.push(0, 1)
    triple_stack.push(0, 2)
    print(triple_stack.pop(0))  # 输出: 1
    print(triple_stack.pop(0))  # 输出: 2
    print(triple_stack.pop(0))  # 输出: -1
    print(triple_stack.is_empty(0))  # 输出: True
```

这个实现使用了一个固定大小的数组来存储三个栈的数据，并使用三个指针分别指向每个栈的栈顶。每个操作的时间复杂度都是 O(1)，空间复杂度是 O(n)，其中 n 是总的栈大小。