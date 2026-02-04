# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100170
标题: Implement Queue using Stacks LCCI
难度: easy
链接: https://leetcode.cn/problems/implement-queue-using-stacks-lcci/
题目类型: 栈、设计、队列
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 03.04. 化栈为队 - 实现一个MyQueue类，该类用两个栈来实现一个队列。 示例： MyQueue queue = new MyQueue(); queue.push(1); queue.push(2); queue.peek(); // 返回 1 queue.pop(); // 返回 1 queue.empty(); // 返回 false 说明： * 你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size 和 is empty 操作是合法的。 * 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。 * 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个栈来实现队列的功能。一个栈用于输入 (in_stack)，另一个栈用于输出 (out_stack)。

算法步骤:
1. push 操作：直接将元素压入 in_stack。
2. pop/peek 操作：如果 out_stack 为空，则将 in_stack 中的所有元素依次弹出并压入 out_stack，然后对 out_stack 进行 pop/peek 操作。
3. empty 操作：检查 in_stack 和 out_stack 是否都为空。

关键点:
- 使用两个栈来实现队列的 FIFO 特性。
- 在需要从队列前端获取元素时，先将 in_stack 的元素转移到 out_stack，以保证顺序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) 平均摊销时间复杂度
空间复杂度: O(n) 其中 n 是队列中的元素数量
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.in_stack and not self.out_stack

Solution = create_solution(MyQueue)