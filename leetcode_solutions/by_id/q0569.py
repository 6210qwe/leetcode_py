# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 569
标题: Median Employee Salary
难度: hard
链接: https://leetcode.cn/problems/median-employee-salary/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
569. 员工薪水中位数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数和子查询来计算中位数

算法步骤:
1. 使用窗口函数 `ROW_NUMBER()` 来为每个员工的薪水分配一个行号。
2. 计算总行数并确定中位数的位置。
3. 通过子查询选择中位数位置的薪水。

关键点:
- 使用窗口函数 `ROW_NUMBER()` 来排序并编号。
- 确定中位数的位置，并通过子查询选择相应的薪水。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是员工数量。主要是由于排序操作。
空间复杂度: O(1)，不需要额外的空间，除了常数级的变量。
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
    函数式接口 - 查询员工薪水中位数
    """
    # 实现最优解法
    query = """
    SELECT AVG(salary) AS median_salary
    FROM (
        SELECT salary, ROW_NUMBER() OVER (ORDER BY salary) AS row_num, COUNT(*) OVER () AS total_count
        FROM Employee
    ) AS subquery
    WHERE row_num IN ((total_count + 1) / 2, (total_count + 2) / 2)
    """
    return query


Solution = create_solution(solution_function_name)