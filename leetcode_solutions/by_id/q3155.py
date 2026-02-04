# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3155
标题: Highest Salaries Difference
难度: easy
链接: https://leetcode.cn/problems/highest-salaries-difference/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2853. 最高薪水差异 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到最高和第二高的薪水，然后计算它们的差值。

算法步骤:
1. 使用子查询找到最高薪水。
2. 使用子查询找到第二高的薪水。
3. 计算最高薪水和第二高薪水的差值。

关键点:
- 使用 `LIMIT` 和 `OFFSET` 来获取最高和第二高的薪水。
- 使用 `IFNULL` 来处理可能的空值情况。
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
    函数式接口 - 使用 SQL 查询来找到最高和第二高的薪水，并计算它们的差值
    """
    # SQL 查询
    query = """
    SELECT
        (MAX(salary) - IFNULL((SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1, 1), 0)) AS salary_difference
    FROM
        Employee
    """
    return query


Solution = create_solution(solution_function_name)