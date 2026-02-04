# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2030
标题: Group Employees of the Same Salary
难度: medium
链接: https://leetcode.cn/problems/group-employees-of-the-same-salary/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1875. 将工资相同的雇员分组 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询将工资相同的雇员分组。

算法步骤:
1. 使用 GROUP BY 子句按工资分组。
2. 使用 COUNT 函数统计每组的雇员数量。
3. 使用 HAVING 子句过滤出雇员数量大于 1 的组。

关键点:
- 使用 GROUP BY 和 HAVING 子句来实现分组和过滤。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是雇员的数量。GROUP BY 操作的时间复杂度通常是 O(n log n)。
空间复杂度: O(n)，存储分组结果所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name():
    """
    函数式接口 - 实现 SQL 查询
    """
    # 实现最优解法
    query = """
    SELECT salary, COUNT(*) AS employee_count
    FROM employees
    GROUP BY salary
    HAVING COUNT(*) > 1
    """
    return query


Solution = create_solution(solution_function_name)