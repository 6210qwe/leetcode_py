# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100195
标题: Stack of Plates LCCI
难度: medium
链接: https://leetcode.cn/problems/stack-of-plates-lcci/
题目类型: 栈、设计、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 03.03. 堆盘子 - 堆盘子。设想有一堆盘子，堆太高可能会倒下来。因此，在现实生活中，盘子堆到一定高度时，我们就会另外堆一堆盘子。请实现数据结构SetOfStacks，模拟这种行为。SetOfStacks应该由多个栈组成，并且在前一个栈填满时新建一个栈。此外，SetOfStacks.push()和SetOfStacks.pop()应该与普通栈的操作方法相同（也就是说，pop()返回的值，应该跟只有一个栈时的情况一样）。 进阶：实现一个popAt(int index)方法，根据指定的子栈，执行pop操作。 当某个栈为空时，应当删除该栈。当栈中没有元素或不存在该栈时，pop，popAt 应返回 -1. 示例 1： 输入： ["StackOfPlates", "push", "push", "popAt", "pop", "pop"] [[1], [1], [2], [1], [], []] 输出： [null, null, null, 2, 1, -1] 示例 2： 输入： ["StackOfPlates", "push", "push", "push", "popAt", "popAt", "popAt"] [[2], [1], [2], [3], [0], [0], [0]] 输出： [null, null, null, null, 2, 1, 3]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个列表来存储多个栈，每个栈是一个列表。当一个栈达到最大容量时，创建一个新的栈。

算法步骤:
1. 初始化一个空的栈列表。
2. push 操作时，如果当前栈已满或没有栈，则创建一个新的栈。
3. pop 操作时，从最后一个栈中弹出元素，如果该栈为空则删除该栈。
4. popAt 操作时，从指定索引的栈中弹出元素，如果该栈为空则删除该栈。

关键点:
- 使用列表来存储多个栈，每个栈是一个列表。
- 在 push 和 popAt 操作时，确保栈的管理和删除是正确的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) 对于 push 和 pop 操作，O(n) 对于 popAt 操作（n 是栈的数量）。
空间复杂度: O(n) 其中 n 是所有元素的总数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional


class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.stacks = []

    def push(self, val: int) -> None:
        if self.cap == 0:
            return
        if not self.stacks or len(self.stacks[-1]) == self.cap:
            self.stacks.append([])
        self.stacks[-1].append(val)

    def pop(self) -> int:
        if not self.stacks:
            return -1
        val = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return val

    def popAt(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks.pop(index)
        return val


# 示例测试
if __name__ == "__main__":
    stack = StackOfPlates(2)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())  # 输出 3
    print(stack.popAt(0))  # 输出 2
    print(stack.pop())  # 输出 1
    print(stack.pop())  # 输出 -1