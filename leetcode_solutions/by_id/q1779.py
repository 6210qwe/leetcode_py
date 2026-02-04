# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1779
标题: Hopper Company Queries I
难度: hard
链接: https://leetcode.cn/problems/hopper-company-queries-i/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1635. Hopper 公司查询 I - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来解决这个问题。我们需要从表中提取出满足条件的数据，并进行适当的聚合和排序。

算法步骤:
1. 从 `Drivers` 表中选择所有在 `2020-01-01` 到 `2020-12-31` 之间注册的司机。
2. 计算每个月注册的司机数量。
3. 生成一个包含所有月份的结果集，即使某些月份没有新注册的司机。
4. 将结果按月份排序。

关键点:
- 使用 `LEFT JOIN` 和 `UNION ALL` 来确保每个月份都在结果集中。
- 使用 `GROUP BY` 和 `COUNT` 来计算每个月的新注册司机数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 `Drivers` 表中的行数，m 是生成的月份行数（最多 12 行）。
空间复杂度: O(1)，因为只使用了常数级的额外空间。
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
    函数式接口 - 实现
    """
    query = """
    WITH RECURSIVE Months AS (
        SELECT 1 AS month
        UNION ALL
        SELECT month + 1 FROM Months WHERE month < 12
    ),
    RegisteredDrivers AS (
        SELECT 
            EXTRACT(MONTH FROM join_date) AS month,
            COUNT(*) AS driver_count
        FROM Drivers
        WHERE join_date BETWEEN '2020-01-01' AND '2020-12-31'
        GROUP BY month
    )
    SELECT 
        M.month,
        IFNULL(RD.driver_count, 0) AS active_drivers
    FROM Months M
    LEFT JOIN RegisteredDrivers RD ON M.month = RD.month
    ORDER BY M.month
    """
    return query

Solution = create_solution(solution_function_name)