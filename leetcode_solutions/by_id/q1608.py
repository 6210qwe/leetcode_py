# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1608
标题: Calculate Salaries
难度: medium
链接: https://leetcode.cn/problems/calculate-salaries/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1468. 计算税后工资 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个员工的税后工资。

算法步骤:
1. 创建一个临时表 `tax_brackets` 来存储税率和对应的收入区间。
2. 使用 `JOIN` 操作将员工表与税率表连接起来，根据员工的收入找到对应的税率。
3. 计算每个员工的税后工资，并返回结果。

关键点:
- 使用 `CASE` 语句来处理不同的税率区间。
- 确保税率表的正确性和完整性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是员工表的行数，m 是税率表的行数。
空间复杂度: O(m)，用于存储税率表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(employees: List[dict], tax_brackets: List[dict]) -> List[dict]:
    """
    函数式接口 - 计算每个员工的税后工资
    :param employees: 员工表，包含员工ID和收入
    :param tax_brackets: 税率表，包含收入区间和税率
    :return: 包含员工ID和税后工资的结果表
    """
    # 创建税率表
    tax_brackets_dict = {}
    for bracket in tax_brackets:
        tax_brackets_dict[(bracket['income_from'], bracket['income_to'])] = bracket['tax_rate']

    # 计算每个员工的税后工资
    result = []
    for employee in employees:
        income = employee['income']
        tax_rate = 0
        for (income_from, income_to), rate in tax_brackets_dict.items():
            if income_from <= income <= income_to:
                tax_rate = rate
                break
        after_tax_income = income * (1 - tax_rate)
        result.append({'employee_id': employee['employee_id'], 'after_tax_income': after_tax_income})

    return result


Solution = create_solution(solution_function_name)