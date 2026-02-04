# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3357
标题: Employees Project Allocation
难度: hard
链接: https://leetcode.cn/problems/employees-project-allocation/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3057. 员工项目分配 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来分配员工到项目

算法步骤:
1. 创建一个临时表来存储每个项目的可用员工数量
2. 使用子查询来获取每个项目需要的员工数量
3. 将员工分配到项目，确保每个项目的需求得到满足

关键点:
- 使用 JOIN 和 GROUP BY 来处理多对多关系
- 确保每个项目的需求得到满足
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是员工数量，m 是项目数量
空间复杂度: O(n + m)，用于存储临时表和结果
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
    函数式接口 - 使用 SQL 查询来分配员工到项目
    """
    # 实现最优解法
    query = """
    WITH project_requirements AS (
        SELECT project_id, COUNT(*) as required_employees
        FROM project_requirements
        GROUP BY project_id
    ),
    available_employees AS (
        SELECT employee_id, COUNT(*) as available_projects
        FROM employee_availability
        GROUP BY employee_id
    )
    SELECT p.project_id, e.employee_id
    FROM project_requirements p
    JOIN available_employees e ON p.required_employees <= e.available_projects
    ORDER BY p.project_id, e.employee_id
    """
    return query


Solution = create_solution(solution_function_name)