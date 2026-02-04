# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1914
标题: Find the Subtasks That Did Not Execute
难度: hard
链接: https://leetcode.cn/problems/find-the-subtasks-that-did-not-execute/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1767. 寻找没有被执行的任务对 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用集合来记录所有执行过的子任务，并通过遍历所有任务来找出未执行的子任务。

算法步骤:
1. 从 `Tasks` 表中获取所有任务的主任务名和子任务名。
2. 从 `Executed` 表中获取所有已执行的子任务名。
3. 使用集合存储所有已执行的子任务名。
4. 遍历所有任务，检查每个子任务是否在已执行的子任务集合中，如果不在，则将其添加到结果列表中。

关键点:
- 使用集合来快速查找已执行的子任务。
- 确保结果列表中的子任务按任务名排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 `Tasks` 表的行数，m 是 `Executed` 表的行数。
空间复杂度: O(m)，用于存储已执行的子任务集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(tasks: List[List[str]], executed: List[str]) -> List[str]:
    """
    函数式接口 - 实现
    """
    # 获取所有已执行的子任务名
    executed_set = set(executed)
    
    # 存储未执行的子任务
    unexecuted_tasks = []
    
    # 遍历所有任务
    for task in tasks:
        subtask = task[1]
        if subtask not in executed_set:
            unexecuted_tasks.append(subtask)
    
    # 返回未执行的子任务列表
    return sorted(unexecuted_tasks)


Solution = create_solution(solution_function_name)