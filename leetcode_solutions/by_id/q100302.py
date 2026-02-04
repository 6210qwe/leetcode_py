# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100302
标题: 最小栈
难度: easy
链接: https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof/
题目类型: 栈、设计
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 147. 最小栈 - 请你设计一个 最小栈 。它提供 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。 实现 MinStack 类: * MinStack() 初始化堆栈对象。 * void push(int val) 将元素val推入堆栈。 * void pop() 删除堆栈顶部的元素。 * int top() 获取堆栈顶部的元素。 * int getMin() 获取堆栈中的最小元素。 示例 1： 输入： ["MinStack","push","push","push","getMin","pop","top","getMin"] [[],[-2],[0],[-3],[],[],[],[]] 输出： [null,null,null,null,-3,null,0,-2] 解释： MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0); minStack.push(-3); minStack.getMin(); --> 返回 -3. minStack.pop(); minStack.top(); --> 返回 0. minStack.getMin(); --> 返回 -2. 提示： * -231 <= val <= 231 - 1 * pop、top 和 getMin 操作总是在 非空栈 上调用 * push、pop、top 和 getMin 最多被调用 3 * 104 次 注意：本题与主站 155 题相同：https://leetcode.cn/problems/min-stack/ [https://leetcode.cn/problems/min-stack/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个栈，一个用于存储所有元素，另一个用于存储当前最小值。

算法步骤:
1. 初始化两个栈，一个用于存储所有元素（stack），另一个用于存储当前最小值（min_stack）。
2. 在 push 操作时，将元素压入 stack，如果该元素小于等于 min_stack 的栈顶元素，则也将其压入 min_stack。
3. 在 pop 操作时，从 stack 弹出元素，如果该元素等于 min_stack 的栈顶元素，则也从 min_stack 弹出。
4. top 操作直接返回 stack 的栈顶元素。
5. getMin 操作直接返回 min_stack 的栈顶元素。

关键点:
- 通过维护一个辅助栈来存储当前最小值，确保 getMin 操作的时间复杂度为 O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 所有操作（push, pop, top, getMin）的时间复杂度均为 O(1)。
空间复杂度: O(n) - 其中 n 是栈中元素的数量，因为我们需要额外的空间来存储最小值。
"""

# ============================================================================
# 代码实现
# ============================================================================

class MinStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        """
        Removes the element on top of the stack.
        """
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        """
        if self.min_stack:
            return self.min_stack[-1]


# 示例测试
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # 返回 -3
    minStack.pop()
    print(minStack.top())     # 返回 0
    print(minStack.getMin())  # 返回 -2