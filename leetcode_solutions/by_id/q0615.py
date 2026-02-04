# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 615
标题: Average Salary: Departments VS Company
难度: hard
链接: https://leetcode.cn/problems/average-salary-departments-vs-company/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
615. 平均工资：部门与公司比较 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个部门的平均工资，并与公司的平均工资进行比较。

算法步骤:
1. 计算每个部门的平均工资。
2. 计算整个公司的平均工资。
3. 将每个部门的平均工资与公司的平均工资进行比较，并返回结果。

关键点:
- 使用子查询和窗口函数来计算平均工资。
- 使用 CASE WHEN 语句来进行比较。
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

import pandas as pd

def solution_function_name(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    """
    函数式接口 - 计算每个部门的平均工资，并与公司的平均工资进行比较
    """
    # 计算每个部门的平均工资
    dept_avg_salary = employee.groupby('departmentId')['salary'].mean().reset_index()
    dept_avg_salary.rename(columns={'salary': 'avgDeptSalary'}, inplace=True)

    # 计算整个公司的平均工资
    company_avg_salary = employee['salary'].mean()

    # 合并部门信息
    result = dept_avg_salary.merge(department, left_on='departmentId', right_on='id', how='left')

    # 比较每个部门的平均工资与公司的平均工资
    result['comparison'] = result.apply(lambda row: 'higher' if row['avgDeptSalary'] > company_avg_salary else ('lower' if row['avgDeptSalary'] < company_avg_salary else 'same'), axis=1)

    # 选择需要的列
    result = result[['name_y', 'avgDeptSalary', 'comparison']]
    result.columns = ['Department', 'AverageSalary', 'Comparison']

    return result

Solution = create_solution(solution_function_name)