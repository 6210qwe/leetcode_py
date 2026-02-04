# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1357
标题: Report Contiguous Dates
难度: hard
链接: https://leetcode.cn/problems/report-contiguous-dates/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1225. 报告系统状态的连续日期 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数和自连接来找到连续日期

算法步骤:
1. 使用窗口函数 `ROW_NUMBER()` 为每个日期分配一个行号。
2. 计算每个日期与行号之间的差值，以标识连续日期块。
3. 使用自连接和条件过滤来找到连续日期块。

关键点:
- 使用窗口函数 `ROW_NUMBER()` 来标识连续日期。
- 通过自连接和条件过滤来找到连续日期块。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是表中的行数。排序操作的时间复杂度是 O(n log n)。
空间复杂度: O(n)，需要额外的空间来存储中间结果。
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
    WITH DateRow AS (
        SELECT 
            fail_date,
            ROW_NUMBER() OVER (ORDER BY fail_date) - 
            ROW_NUMBER() OVER (PARTITION BY status ORDER BY fail_date) AS grp
        FROM 
            (SELECT fail_date, 'failed' AS status FROM Failed
             UNION ALL
             SELECT success_date, 'succeeded' AS status FROM Succeeded) AS Combined
    ),
    GroupedDates AS (
        SELECT 
            MIN(fail_date) AS start_date,
            MAX(fail_date) AS end_date,
            status
        FROM 
            DateRow
        GROUP BY 
            grp, status
    )
    SELECT 
        start_date, 
        end_date, 
        status
    FROM 
        GroupedDates
    ORDER BY 
        start_date;
    """
    return query

Solution = create_solution(solution_function_name)