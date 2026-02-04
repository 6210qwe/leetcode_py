# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 577
标题: Employee Bonus
难度: easy
链接: https://leetcode.cn/problems/employee-bonus/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
577. 员工奖金 - 表：Employee +-------------+---------+ | Column Name | Type | +-------------+---------+ | empId | int | | name | varchar | | supervisor | int | | salary | int | +-------------+---------+ empId 是该表中具有唯一值的列。 该表的每一行都表示员工的 id 和姓名，以及他们经理的 id 和他们的工资。 表：Bonus +-------------+------+ | Column Name | Type | +-------------+------+ | empId | int | | bonus | int | +-------------+------+ empId 是该表具有唯一值的列。 empId 是 Employee 表中 empId 的外键(reference 列)。 该表的每一行都包含一个员工的 id 和他们各自的奖金。 编写一个解决方案来报告满足以下任一条件的每个员工的姓名和奖金金额： * 奖金 少于 1000 的员工。 * 没有任何奖金的员工。 以 任意顺序 返回结果表。 结果格式如下所示。 示例 1： 输入： Employee table: +-------+--------+------------+--------+ | empId | name | supervisor | salary | +-------+--------+------------+--------+ | 3 | Brad | null | 4000 | | 1 | John | 3 | 1000 | | 2 | Dan | 3 | 2000 | | 4 | Thomas | 3 | 4000 | +-------+--------+------------+--------+ Bonus table: +-------+-------+ | empId | bonus | +-------+-------+ | 2 | 500 | | 4 | 2000 | +-------+-------+ 输出： +------+-------+ | name | bonus | +------+-------+ | Brad | null | | John | null | | Dan | 500 | +------+-------+
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来实现，通过左连接将 Employee 表和 Bonus 表连接起来，并筛选出奖金少于 1000 或没有奖金的员工。

算法步骤:
1. 使用 LEFT JOIN 将 Employee 表和 Bonus 表连接起来。
2. 筛选出奖金少于 1000 或没有奖金的员工。
3. 返回结果表，包含员工的姓名和奖金金额。

关键点:
- 使用 LEFT JOIN 来确保所有员工都被包含在结果中，即使他们没有奖金。
- 使用 WHERE 子句来筛选符合条件的员工。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 Employee 表的行数，m 是 Bonus 表的行数。
空间复杂度: O(1)，因为查询结果只包含必要的列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(employee: List[List[str]], bonus: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 实现
    """
    # 构建 SQL 查询
    query = """
    SELECT e.name, b.bonus
    FROM employee e
    LEFT JOIN bonus b ON e.empId = b.empId
    WHERE b.bonus < 1000 OR b.bonus IS NULL;
    """

    # 执行查询
    result = []
    for row in employee:
        emp_id, name, _, _ = row
        bonus_row = next((b for b in bonus if b[0] == emp_id), [None, None])
        if not bonus_row[1] or (bonus_row[1] and int(bonus_row[1]) < 1000):
            result.append([name, bonus_row[1]])

    return result


Solution = create_solution(solution_function_name)