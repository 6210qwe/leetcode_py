# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3678
标题: Design Task Manager
难度: medium
链接: https://leetcode.cn/problems/design-task-manager/
题目类型: 设计、哈希表、有序集合、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3408. 设计任务管理器 - 一个任务管理器系统可以让用户管理他们的任务，每个任务有一个优先级。这个系统需要高效地处理添加、修改、执行和删除任务的操作。 请你设计一个 TaskManager 类： * TaskManager(vector<vector<int>>& tasks) 初始化任务管理器，初始化的数组格式为 [userId, taskId, priority] ，表示给 userId 添加一个优先级为 priority 的任务 taskId 。 * void add(int userId, int taskId, int priority) 表示给用户 userId 添加一个优先级为 priority 的任务 taskId ，输入 保证 taskId 不在系统中。 * void edit(int taskId, int newPriority) 更新已经存在的任务 taskId 的优先级为 newPriority 。输入 保证 taskId 存在于系统中。 * void rmv(int taskId) 从系统中删除任务 taskId 。输入 保证 taskId 存在于系统中。 * int execTop() 执行所有用户的任务中优先级 最高 的任务，如果有多个任务优先级相同且都为 最高 ，执行 taskId 最大的一个任务。执行完任务后，taskId 从系统中 删除 。同时请你返回这个任务所属的用户 userId 。如果不存在任何任务，返回 -1 。 注意 ，一个用户可能被安排多个任务。 示例 1： 输入： ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"] [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []] 输出： [null, null, null, 3, null, null, 5] 解释： TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]); // 分别给用户 1 ，2 和 3 初始化一个任务。 taskManager.add(4, 104, 5); // 给用户 4 添加优先级为 5 的任务 104 。 taskManager.edit(102, 8); // 更新任务 102 的优先级为 8 。 taskManager.execTop(); // 返回 3 。执行用户 3 的任务 103 。 taskManager.rmv(101); // 将系统中的任务 101 删除。 taskManager.add(5, 105, 15); // 给用户 5 添加优先级为 15 的任务 105 。 taskManager.execTop(); // 返回 5 。执行用户 5 的任务 105 。 提示： * 1 <= tasks.length <= 105 * 0 <= userId <= 105 * 0 <= taskId <= 105 * 0 <= priority <= 109 * 0 <= newPriority <= 109 * add ，edit ，rmv 和 execTop 的总操作次数 加起来 不超过 2 * 105 次。 * 输入保证 taskId 是合法的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个最大堆来维护任务的优先级，并使用一个字典来快速查找任务。

算法步骤:
1. 初始化时，将所有任务加入最大堆，并用字典记录每个任务的详细信息。
2. 添加任务时，将任务加入最大堆，并更新字典。
3. 修改任务时，先从最大堆中移除旧任务，再将新任务加入最大堆，并更新字典。
4. 删除任务时，从最大堆中移除任务，并更新字典。
5. 执行最高优先级任务时，从最大堆中取出任务并返回其用户ID，然后从字典中移除该任务。

关键点:
- 使用最大堆来高效地获取最高优先级的任务。
- 使用字典来快速查找和更新任务。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 对于添加、修改、删除和执行最高优先级任务的操作，最大堆的操作时间复杂度为 O(log n)。
空间复杂度: O(n) - 使用了最大堆和字典来存储任务信息。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task_dict = {}
        self.max_heap = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int):
        # Add task to the max heap and task dictionary
        heapq.heappush(self.max_heap, (-priority, -taskId, userId))
        self.task_dict[taskId] = (userId, priority)

    def edit(self, taskId: int, newPriority: int):
        # Remove the old task from the max heap and task dictionary
        userId, oldPriority = self.task_dict[taskId]
        self.task_dict.pop(taskId)
        self.max_heap.remove((-oldPriority, -taskId, userId))
        heapq.heapify(self.max_heap)
        
        # Add the new task to the max heap and task dictionary
        heapq.heappush(self.max_heap, (-newPriority, -taskId, userId))
        self.task_dict[taskId] = (userId, newPriority)

    def rmv(self, taskId: int):
        # Remove the task from the max heap and task dictionary
        userId, priority = self.task_dict[taskId]
        self.task_dict.pop(taskId)
        self.max_heap.remove((-priority, -taskId, userId))
        heapq.heapify(self.max_heap)

    def execTop(self) -> int:
        if not self.max_heap:
            return -1
        
        # Get the highest priority task
        _, taskId, userId = heapq.heappop(self.max_heap)
        taskId = -taskId
        self.task_dict.pop(taskId)
        
        # Re-heapify to maintain the heap property
        heapq.heapify(self.max_heap)
        
        return userId


# Example usage
if __name__ == "__main__":
    tasks = [[1, 101, 10], [2, 102, 20], [3, 103, 15]]
    task_manager = TaskManager(tasks)
    task_manager.add(4, 104, 5)
    task_manager.edit(102, 8)
    print(task_manager.execTop())  # Output: 3
    task_manager.rmv(101)
    task_manager.add(5, 105, 15)
    print(task_manager.execTop())  # Output: 5