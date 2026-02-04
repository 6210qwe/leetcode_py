# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3465
标题: Employee Task Duration and Concurrent Tasks
难度: hard
链接: https://leetcode.cn/problems/employee-task-duration-and-concurrent-tasks/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3156. 员工任务持续时间和并发任务 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个员工的任务持续时间和并发任务数。

算法步骤:
1. 计算每个任务的开始时间和结束时间。
2. 计算每个任务的持续时间。
3. 计算每个员工在同一时间点上的并发任务数。

关键点:
- 使用窗口函数和自连接来计算并发任务数。
- 确保查询结果的正确性和性能。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是任务的数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，存储中间结果所需的空间。
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
    函数式接口 - 实现 SQL 查询来计算每个员工的任务持续时间和并发任务数
    """
    # SQL 查询实现
    query = """
    WITH task_durations AS (
        SELECT
            employee_id,
            task_id,
            start_time,
            end_time,
            (end_time - start_time) AS duration
        FROM
            tasks
    ),
    concurrent_tasks AS (
        SELECT
            t1.employee_id,
            t1.task_id,
            t1.start_time,
            t1.end_time,
            COUNT(t2.task_id) AS concurrent_count
        FROM
            task_durations t1
        LEFT JOIN
            task_durations t2 ON t1.employee_id = t2.employee_id AND t1.start_time < t2.end_time AND t1.end_time > t2.start_time
        GROUP BY
            t1.employee_id, t1.task_id, t1.start_time, t1.end_time
    )
    SELECT
        employee_id,
        task_id,
        start_time,
        end_time,
        duration,
        concurrent_count
    FROM
        concurrent_tasks
    ORDER BY
        employee_id, start_time;
    """
    return query


Solution = create_solution(solution_function_name)