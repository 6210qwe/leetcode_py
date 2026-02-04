# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4012
标题: Earliest Time to Finish One Task
难度: easy
链接: https://leetcode.cn/problems/earliest-time-to-finish-one-task/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3683. 完成一个任务的最早时间 - 给你一个二维整数数组 tasks，其中 tasks[i] = [si, ti]。 数组中的每个 [si, ti] 表示一个任务，该任务的开始时间为 si，完成该任务需要 ti 个时间单位。 返回至少完成一个任务的最早时间。 示例 1： 输入： tasks = [[1,6],[2,3]] 输出： 5 解释： 第一个任务从时间 t = 1 开始，并在 1 + 6 = 7 时完成。第二个任务在时间 t = 2 开始，并在 2 + 3 = 5 时完成。因此，最早完成的任务在时间 5。 示例 2： 输入： tasks = [[100,100],[100,100],[100,100]] 输出： 200 解释： 三个任务都在时间 100 + 100 = 200 时完成。 提示： * 1 <= tasks.length <= 100 * tasks[i] = [si, ti] * 1 <= si, ti <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算每个任务的完成时间，并找到最早完成的任务的时间。

算法步骤:
1. 初始化一个变量 `min_completion_time` 为正无穷大。
2. 遍历每个任务，计算其完成时间 `completion_time = start_time + duration`。
3. 更新 `min_completion_time` 为当前任务的完成时间和 `min_completion_time` 的最小值。
4. 返回 `min_completion_time`。

关键点:
- 直接遍历任务列表，计算每个任务的完成时间，并找到最小值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是任务的数量。我们需要遍历每个任务一次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def earliest_time_to_finish_one_task(tasks: List[List[int]]) -> int:
    """
    函数式接口 - 计算完成一个任务的最早时间
    """
    min_completion_time = float('inf')
    for start_time, duration in tasks:
        completion_time = start_time + duration
        min_completion_time = min(min_completion_time, completion_time)
    return min_completion_time


Solution = create_solution(earliest_time_to_finish_one_task)