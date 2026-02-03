# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 232
标题: Implement Queue using Stacks
难度: easy
链接: https://leetcode.cn/problems/implement-queue-using-stacks/
题目类型: 栈、设计、队列
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
232. 用栈实现队列 - 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）： 实现 MyQueue 类： * void push(int x) 将元素 x 推到队列的末尾 * int pop() 从队列的开头移除并返回元素 * int peek() 返回队列开头的元素 * boolean empty() 如果队列为空，返回 true ；否则，返回 false 说明： * 你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。 * 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。 示例 1： 输入： ["MyQueue", "push", "push", "peek", "pop", "empty"] [[], [1], [2], [], [], []] 输出： [null, null, null, 1, 1, false] 解释： MyQueue myQueue = new MyQueue(); myQueue.push(1); // queue is: [1] myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue) myQueue.peek(); // return 1 myQueue.pop(); // return 1, queue is [2] myQueue.empty(); // return false 提示： * 1 <= x <= 9 * 最多调用 100 次 push、pop、peek 和 empty * 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作） 进阶： * 你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个栈，一个用于入队，一个用于出队

算法步骤:
1. push操作：直接压入stack_in
2. pop/peek操作：如果stack_out为空，将stack_in的所有元素弹出并压入stack_out
3. 从stack_out弹出或查看栈顶元素

关键点:
- 使用两个栈实现队列的FIFO特性
- 均摊时间复杂度O(1)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 均摊O(1) - 每个元素最多入栈和出栈各一次
空间复杂度: O(n) - 两个栈的空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from leetcode_solutions.utils.solution import create_solution


class MyQueue:
    """
    用栈实现队列
    """
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def push(self, x: int) -> None:
        """将元素x推到队列的末尾"""
        self.stack_in.append(x)
    
    def pop(self) -> int:
        """从队列的开头移除并返回元素"""
        self._move()
        return self.stack_out.pop()
    
    def peek(self) -> int:
        """返回队列开头的元素"""
        self._move()
        return self.stack_out[-1]
    
    def empty(self) -> bool:
        """如果队列为空，返回true；否则，返回false"""
        return len(self.stack_in) == 0 and len(self.stack_out) == 0
    
    def _move(self):
        """将stack_in的元素移动到stack_out"""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


def implement_queue_using_stacks() -> MyQueue:
    """
    函数式接口 - 创建用栈实现的队列
    
    实现思路:
    使用两个栈，一个用于入队，一个用于出队。
    
    Returns:
        MyQueue实例
        
    Example:
        >>> queue = implement_queue_using_stacks()
        >>> queue.push(1)
        >>> queue.push(2)
        >>> queue.peek()
        1
    """
    return MyQueue()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(implement_queue_using_stacks)
