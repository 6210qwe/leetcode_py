```python
# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2688
标题: Design a Todo List
难度: medium
链接: https://leetcode.cn/problems/design-a-todo-list/
题目类型: 设计、数组、哈希表、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2590. 设计一个待办事项清单 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典来存储任务，并使用优先队列来管理任务的优先级。

算法步骤:
1. 初始化时，创建一个字典来存储任务，键为时间戳，值为任务列表。
2. 添加任务时，将任务添加到对应时间戳的任务列表中。
3. 获取任务时，从优先队列中获取当前时间戳的任务列表，并返回前 k 个任务。
4. 移除任务时，从对应时间戳的任务列表中移除指定任务。

关键点:
- 使用字典来存储任务，便于快速查找和更新。
- 使用优先队列来管理任务的优先级，确保按时间顺序处理任务。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 
- addTask: O(1)
- getTasks: O(log n + k log k)，其中 n 是不同时间戳的数量，k 是要返回的任务数量。
- removeTask: O(m)，其中 m 是对应时间戳的任务数量。

空间复杂度: O(t + m)，其中 t 是不同时间戳的数量，m 是任务总数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq

class TodoList:
    def __init__(self):
        self.tasks = {}
        self.timestamps = []

    def addTask(self, timestamp: int, task: str) -> None:
        if timestamp not in self.tasks:
            heapq.heappush(self.timestamps, timestamp)
        if timestamp in self.tasks:
            self.tasks[timestamp].append(task)
        else:
            self.tasks[timestamp] = [task]

    def getTasks(self, timestamp: int, k: int) -> List[str]:
        result = []
        while self.timestamps and self.timestamps[0] <= timestamp:
            current_timestamp = heapq.heappop(self.timestamps)
            for task in self.tasks[current_timestamp]:
                result.append(task)
                if len(result) == k:
                    return result
        return result[:k]

    def removeTask(self, timestamp: int, task: str) -> None:
        if timestamp in self.tasks and task in self.tasks[timestamp]:
            self.tasks[timestamp].remove(task)
            if not self.tasks[timestamp]:
                del self.tasks[timestamp]
                self.timestamps = [t for t in self.timestamps if t != timestamp]
                heapq.heapify(self.timestamps)

# 示例用法
if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.addTask(1, "Task1")
    todo_list.addTask(1, "Task2")
    todo_list.addTask(2, "Task3")
    print(todo_list.getTasks(2, 2))  # 输出: ["Task1", "Task2"]
    todo_list.removeTask(1, "Task1")
    print(todo_list.getTasks(2, 2))  # 输出: ["Task2", "Task3"]
```

这个实现中，我们使用了一个字典 `tasks` 来存储每个时间戳对应的任务列表，并使用一个最小堆 `timestamps` 来管理时间戳的优先级。这样可以确保我们在获取任务时能够按时间顺序处理。添加任务和移除任务的时间复杂度都比较低，而获取任务的时间复杂度稍微高一些，但仍然在可接受范围内。