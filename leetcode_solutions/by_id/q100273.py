# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100273
标题: 图书整理 II
难度: easy
链接: https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
题目类型: 栈、设计、队列
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 125. 图书整理 II - 读者来到图书馆排队借还书，图书管理员使用两个书车来完成整理借还书的任务。书车中的书从下往上叠加存放，图书管理员每次只能拿取书车顶部的书。排队的读者会有两种操作： * push(bookID)：把借阅的书籍还到图书馆。 * pop()：从图书馆中借出书籍。 为了保持图书的顺序，图书管理员每次取出供读者借阅的书籍是 最早 归还到图书馆的书籍。你需要返回 每次读者借出书的值 。 如果没有归还的书可以取出，返回 -1 。 示例 1： 输入： ["BookQueue", "push", "push", "pop"] [[], [1], [2], []] 输出：[null,null,null,1] 解释： MyQueue myQueue = new MyQueue(); myQueue.push(1); // queue is: [1] myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue) myQueue.pop(); // return 1, queue is [2] 提示： * 1 <= bookID <= 10000 * 最多会对 push、pop 进行 10000 次调用
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个栈来模拟队列的操作。一个栈用于存储入队的元素，另一个栈用于辅助出队操作。

算法步骤:
1. 初始化两个栈 `stack1` 和 `stack2`。
2. 对于 `push` 操作，直接将元素压入 `stack1`。
3. 对于 `pop` 操作，如果 `stack2` 为空，则将 `stack1` 中的所有元素依次弹出并压入 `stack2`，然后弹出 `stack2` 的栈顶元素。如果 `stack2` 不为空，则直接弹出 `stack2` 的栈顶元素。

关键点:
- 使用两个栈来实现队列的先进先出特性。
- 只有当 `stack2` 为空时，才将 `stack1` 中的元素转移到 `stack2`。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)（均摊时间复杂度）
空间复杂度: O(n)，其中 n 是队列中的元素数量
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class BookQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, book_id: int) -> None:
        self.stack1.append(book_id)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return -1


Solution = create_solution(BookQueue)