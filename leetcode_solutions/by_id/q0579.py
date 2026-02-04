# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 579
标题: Find Cumulative Salary of an Employee
难度: hard
链接: https://leetcode.cn/problems/find-cumulative-salary-of-an-employee/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
579. 查询员工的累计薪水 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数 `SUM` 来计算每个员工的累计薪水，并使用 `GROUP BY` 和 `ORDER BY` 来确保结果按要求排序。

算法步骤:
1. 使用 SQL 窗口函数 `SUM` 计算每个员工的累计薪水。
2. 使用 `GROUP BY` 和 `ORDER BY` 对结果进行分组和排序。

关键点:
- 使用窗口函数 `SUM` 进行累计求和。
- 使用 `GROUP BY` 和 `ORDER BY` 确保结果按要求排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是数据表中的行数。主要的时间开销在于排序操作。
空间复杂度: O(1)，SQL 查询的空间复杂度通常为常数级别，不考虑数据库内部实现的额外空间。
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
    函数式接口 - 查询员工的累计薪水
    """
    # 实现最优解法
    query = """
    SELECT 
        id, 
        month, 
        SUM(salary) OVER (PARTITION BY id ORDER BY month) AS cumulative_salary
    FROM 
        Employee
    ORDER BY 
        id, 
        month;
    """
    return query


Solution = create_solution(solution_function_name)