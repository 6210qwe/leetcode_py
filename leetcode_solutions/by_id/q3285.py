# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3285
标题: Manager of the Largest Department
难度: medium
链接: https://leetcode.cn/problems/manager-of-the-largest-department/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2988. 最大部门的经理 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找出最大部门的经理。

算法步骤:
1. 计算每个部门的员工数量。
2. 找出员工数量最多的部门。
3. 找出这些部门的经理。

关键点:
- 使用子查询和聚合函数来计算每个部门的员工数量。
- 使用窗口函数来找出最大部门。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
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
    函数式接口 - 使用 SQL 查询来找出最大部门的经理
    """
    # 实现最优解法
    query = """
    WITH EmployeeCount AS (
        SELECT departmentId, COUNT(*) AS numEmployees
        FROM Employee
        GROUP BY departmentId
    ),
    MaxDepartment AS (
        SELECT departmentId, numEmployees
        FROM EmployeeCount
        WHERE numEmployees = (SELECT MAX(numEmployees) FROM EmployeeCount)
    )
    SELECT E.name, E.departmentId, M.numEmployees
    FROM Employee E
    JOIN MaxDepartment M ON E.departmentId = M.departmentId
    WHERE E.managerId IS NULL;
    """
    return query


Solution = create_solution(solution_function_name)