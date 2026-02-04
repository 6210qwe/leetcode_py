# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3549
标题: CEO Subordinate Hierarchy
难度: hard
链接: https://leetcode.cn/problems/ceo-subordinate-hierarchy/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3236. 首席执行官下属层级 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归查询每个员工的直接下属，并构建层次结构。

算法步骤:
1. 创建一个递归函数 `get_subordinates`，用于获取某个员工的所有下属。
2. 在主函数中调用 `get_subordinates` 函数，传入 CEO 的 ID，获取所有下属的层次结构。
3. 将结果格式化为所需的输出格式。

关键点:
- 使用递归查询每个员工的直接下属，并构建层次结构。
- 使用字典存储员工及其下属的关系，以便快速查找。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是员工的数量。每个员工最多被访问一次。
空间复杂度: O(n)，递归调用栈和存储员工及其下属关系的字典。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def get_subordinates(employee_id: int, manager_to_employees: dict) -> List[dict]:
    """
    递归获取某个员工的所有下属。
    """
    if employee_id not in manager_to_employees:
        return []
    
    subordinates = []
    for subordinate in manager_to_employees[employee_id]:
        subordinates.append({
            "id": subordinate,
            "subordinates": get_subordinates(subordinate, manager_to_employees)
        })
    
    return subordinates

def solution_function_name(employees: List[List[int]]) -> List[dict]:
    """
    函数式接口 - 获取 CEO 及其下属的层次结构。
    """
    # 构建员工及其下属的关系字典
    manager_to_employees = {}
    for employee in employees:
        if employee[1] not in manager_to_employees:
            manager_to_employees[employee[1]] = []
        manager_to_employees[employee[1]].append(employee[0])
    
    # 获取 CEO 的 ID
    ceo_id = next((e[0] for e in employees if e[1] is None), None)
    
    # 获取 CEO 及其下属的层次结构
    result = {
        "id": ceo_id,
        "subordinates": get_subordinates(ceo_id, manager_to_employees)
    }
    
    return [result]

Solution = create_solution(solution_function_name)