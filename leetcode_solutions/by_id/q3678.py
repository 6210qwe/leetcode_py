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
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
