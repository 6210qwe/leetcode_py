# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1785
标题: Hopper Company Queries II
难度: hard
链接: https://leetcode.cn/problems/hopper-company-queries-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1645. Hopper 公司查询 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来解决这个问题。我们需要计算每个用户的平均行程时间，并找到每个月份的最小、最大和平均行程时间。

算法步骤:
1. 计算每个用户的每次行程时间。
2. 按月份分组，计算每个月份的最小、最大和平均行程时间。
3. 返回结果。

关键点:
- 使用 `DATEDIFF` 函数计算行程时间。
- 使用 `GROUP BY` 和聚合函数 `MIN`, `MAX`, `AVG` 来计算每个月份的统计数据。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是行程记录的数量。需要遍历所有记录进行计算。
空间复杂度: O(1)，除了返回的结果外，不需要额外的空间。
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
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)

# SQL 查询实现
def hopper_company_queries_ii() -> str:
    query = """
    SELECT 
        DATE_FORMAT(begin_date, '%Y-%m') AS month,
        MIN(duration) AS min_duration,
        MAX(duration) AS max_duration,
        AVG(duration) AS avg_duration
    FROM (
        SELECT 
            begin_date,
            DATEDIFF(end_date, begin_date) + 1 AS duration
        FROM 
            Rides
    ) AS durations
    GROUP BY 
        month
    ORDER BY 
        month;
    """
    return query

Solution = create_solution(hopper_company_queries_ii)