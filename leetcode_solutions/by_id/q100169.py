# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100169
标题: Min Stack LCCI
难度: easy
链接: https://leetcode.cn/problems/min-stack-lcci/
题目类型: 栈、设计
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 03.02. 栈的最小值 - 请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。 示例： MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0); minStack.push(-3); minStack.getMin(); --> 返回 -3. minStack.pop(); minStack.top(); --> 返回 0. minStack.getMin(); --> 返回 -2.
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个栈，一个用于存储所有元素，另一个用于存储当前的最小值。

算法步骤:
1. 初始化两个栈，一个用于存储所有元素，另一个用于存储当前的最小值。
2. 在 push 操作时，将元素压入主栈，并根据情况更新最小值栈。
3. 在 pop 操作时，同时从主栈和最小值栈中弹出元素。
4. 在 getMin 操作时，直接返回最小值栈的栈顶元素。

关键点:
- 最小值栈始终维护当前栈中的最小值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 所有操作（push, pop, getMin）的时间复杂度均为 O(1)。
空间复杂度: O(n) - 最坏情况下，最小值栈的空间复杂度为 O(n)，其中 n 是栈中元素的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# 示例用法
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # 返回 -3
    minStack.pop()
    print(minStack.top())     # 返回 0
    print(minStack.getMin())  # 返回 -2