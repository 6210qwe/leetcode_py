# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2158
标题: The Number of Seniors and Juniors to Join the Company II
难度: hard
链接: https://leetcode.cn/problems/the-number-of-seniors-and-juniors-to-join-the-company-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2010. 职员招聘人数 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计符合条件的职员数量。

算法步骤:
1. 使用子查询来计算每个部门的高级职员和初级职员的数量。
2. 根据给定的条件过滤出符合要求的部门。
3. 计算总人数并返回结果。

关键点:
- 使用子查询和聚合函数进行统计。
- 确保查询条件正确且高效。
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
    函数式接口 - 实现最优解法
    """
    # SQL 查询实现
    query = """
    SELECT 
        SUM(CASE WHEN experience = 'Senior' THEN 1 ELSE 0 END) AS senior_count,
        SUM(CASE WHEN experience = 'Junior' THEN 1 ELSE 0 END) AS junior_count
    FROM Candidates
    WHERE (experience = 'Senior' AND salary <= :max_salary_senior) OR 
          (experience = 'Junior' AND salary <= :max_salary_junior)
    """
    # 执行查询并返回结果
    result = execute_query(query, params)
    return result

Solution = create_solution(solution_function_name)