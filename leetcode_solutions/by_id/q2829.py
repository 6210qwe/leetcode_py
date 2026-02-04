# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2829
标题: Find Latest Salaries
难度: easy
链接: https://leetcode.cn/problems/find-latest-salaries/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2668. 查询员工当前薪水 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来获取每个员工的最新薪水记录。

算法步骤:
1. 使用子查询找到每个员工的最新薪水记录的时间戳。
2. 在主查询中，使用内连接将员工表和最新薪水时间戳表连接起来，获取最新的薪水记录。

关键点:
- 使用 `MAX` 函数和 `GROUP BY` 子句来找到每个员工的最新薪水时间戳。
- 使用内连接 (`INNER JOIN`) 来获取最新的薪水记录。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是员工表的行数，m 是薪水表的行数。
空间复杂度: O(1)，不考虑查询结果所占用的空间。
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
    函数式接口 - 查询员工的最新薪水
    """
    # SQL 查询语句
    query = """
    SELECT e.employee_id, s.salary
    FROM Employees e
    INNER JOIN (
        SELECT employee_id, MAX(salary_date) AS max_salary_date
        FROM Salaries
        GROUP BY employee_id
    ) s1 ON e.employee_id = s1.employee_id
    INNER JOIN Salaries s ON s1.employee_id = s.employee_id AND s1.max_salary_date = s.salary_date
    """
    return query


Solution = create_solution(solution_function_name)