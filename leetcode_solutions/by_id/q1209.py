# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1209
标题: Design Bounded Blocking Queue
难度: medium
链接: https://leetcode.cn/problems/design-bounded-blocking-queue/
题目类型: 多线程
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1209. 设计有限阻塞队列 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 threading.Condition 来实现线程同步和阻塞

算法步骤:
1. 初始化队列，设置容量上限
2. 实现 enqueue 方法，当队列未满时添加元素，否则阻塞
3. 实现 dequeue 方法，当队列不为空时移除元素，否则阻塞
4. 实现 size 方法，返回当前队列中的元素数量

关键点:
- 使用 Condition 对象来控制线程的等待和通知
- 在 enqueue 和 dequeue 方法中使用锁来保护共享资源
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每个操作（enqueue, dequeue, size）的时间复杂度都是常数级
空间复杂度: O(n) - 队列存储 n 个元素
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import threading

class BoundedBlockingQueue:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def enqueue(self, element: int) -> None:
        with self.not_full:
            while len(self.queue) == self.capacity:
                self.not_full.wait()
            self.queue.append(element)
            self.not_empty.notify()

    def dequeue(self) -> int:
        with self.not_empty:
            while not self.queue:
                self.not_empty.wait()
            element = self.queue.pop(0)
            self.not_full.notify()
            return element

    def size(self) -> int:
        with self.lock:
            return len(self.queue)


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(BoundedBlockingQueue)