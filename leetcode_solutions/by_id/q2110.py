# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2110
标题: Employees With Missing Information
难度: easy
链接: https://leetcode.cn/problems/employees-with-missing-information/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1965. 丢失信息的雇员 - 表: Employees +-------------+---------+ | Column Name | Type | +-------------+---------+ | employee_id | int | | name | varchar | +-------------+---------+ employee_id 是该表中具有唯一值的列。 每一行表示雇员的 id 和他的姓名。 表: Salaries +-------------+---------+ | Column Name | Type | +-------------+---------+ | employee_id | int | | salary | int | +-------------+---------+ employee_id 是该表中具有唯一值的列。 每一行表示雇员的 id 和他的薪水。 编写解决方案，找到所有 丢失信息 的雇员 id。当满足下面一个条件时，就被认为是雇员的信息丢失： * 雇员的 姓名 丢失了，或者 * 雇员的 薪水信息 丢失了 返回这些雇员的 id employee_id ， 从小到大排序 。 查询结果格式如下面的例子所示。 示例 1： 输入： Employees table: +-------------+----------+ | employee_id | name | +-------------+----------+ | 2 | Crew | | 4 | Haven | | 5 | Kristian | +-------------+----------+ Salaries table: +-------------+--------+ | employee_id | salary | +-------------+--------+ | 5 | 76071 | | 1 | 22517 | | 4 | 63539 | +-------------+--------+ 输出： +-------------+ | employee_id | +-------------+ | 1 | | 2 | +-------------+ 解释： 雇员 1，2，4，5 都在这个公司工作。 1 号雇员的姓名丢失了。 2 号雇员的薪水信息丢失了。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用集合操作来找出在 Employees 表和 Salaries 表中缺失的 employee_id。

算法步骤:
1. 将 Employees 表中的 employee_id 放入一个集合。
2. 将 Salaries 表中的 employee_id 放入另一个集合。
3. 找出两个集合的对称差集，即为缺失信息的 employee_id。
4. 对结果进行排序并返回。

关键点:
- 使用集合操作可以高效地找出缺失的 employee_id。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是员工的数量。集合操作的时间复杂度为 O(n)，排序的时间复杂度为 O(n log n)。
空间复杂度: O(n)，用于存储两个集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(employees: List[List[str]], salaries: List[List[str]]) -> List[int]:
    """
    函数式接口 - 实现最优解法
    """
    # 将 Employees 表中的 employee_id 放入一个集合
    employees_set = {int(row[0]) for row in employees}
    
    # 将 Salaries 表中的 employee_id 放入另一个集合
    salaries_set = {int(row[0]) for row in salaries}
    
    # 找出两个集合的对称差集
    missing_ids = sorted(employees_set ^ salaries_set)
    
    return missing_ids


Solution = create_solution(solution_function_name)