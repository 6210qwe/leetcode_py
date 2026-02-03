# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 225
标题: Implement Stack using Queues
难度: easy
链接: https://leetcode.cn/problems/implement-stack-using-queues/
题目类型: 栈、设计、队列
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
225. 用队列实现栈 - 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。 实现 MyStack 类： * void push(int x) 将元素 x 压入栈顶。 * int pop() 移除并返回栈顶元素。 * int top() 返回栈顶元素。 * boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。 注意： * 你只能使用队列的标准操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。 * 你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。 示例： 输入： ["MyStack", "push", "push", "top", "pop", "empty"] [[], [1], [2], [], [], []] 输出： [null, null, null, 2, 2, false] 解释： MyStack myStack = new MyStack(); myStack.push(1); myStack.push(2); myStack.top(); // 返回 2 myStack.pop(); // 返回 2 myStack.empty(); // 返回 False 提示： * 1 <= x <= 9 * 最多调用100 次 push、pop、top 和 empty * 每次调用 pop 和 top 都保证栈不为空 进阶：你能否仅用一个队列来实现栈。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个队列实现栈，push时将新元素加入队列，然后将队列中其他元素依次出队再入队

算法步骤:
1. push: 将元素加入队列，然后将队列中除新元素外的所有元素依次出队再入队
2. pop: 直接出队
3. top: 返回队列头部元素
4. empty: 检查队列是否为空

关键点:
- 使用一个队列实现栈
- push时间复杂度O(n)，其他操作O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: push O(n)，pop/top/empty O(1)
空间复杂度: O(n) - 队列存储元素
"""

# ============================================================================
# 代码实现
# ============================================================================

from collections import deque
from leetcode_solutions.utils.solution import create_solution


class MyStack:
    """
    用队列实现栈
    """
    def __init__(self):
        self.queue = deque()
    
    def push(self, x: int) -> None:
        """将元素x压入栈顶"""
        self.queue.append(x)
        # 将新元素之前的所有元素移到新元素后面
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
    
    def pop(self) -> int:
        """移除并返回栈顶元素"""
        return self.queue.popleft()
    
    def top(self) -> int:
        """返回栈顶元素"""
        return self.queue[0]
    
    def empty(self) -> bool:
        """如果栈是空的，返回true"""
        return len(self.queue) == 0


def implement_stack_using_queues() -> MyStack:
    """
    函数式接口 - 创建用队列实现的栈
    
    实现思路:
    使用一个队列实现栈，push时将新元素加入队列，然后将队列中其他元素依次出队再入队。
    
    Returns:
        MyStack实例
        
    Example:
        >>> stack = implement_stack_using_queues()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.top()
        2
    """
    return MyStack()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(implement_stack_using_queues)
