# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1328
标题: Monthly Transactions II
难度: medium
链接: https://leetcode.cn/problems/monthly-transactions-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1205. 每月交易 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个月的交易情况。

算法步骤:
1. 创建一个包含所有月份的临时表。
2. 将用户表和交易表进行连接，并按月份分组。
3. 计算每个月的交易金额总和，并处理缺失值。

关键点:
- 使用 `LEFT JOIN` 来确保每个月都有记录，即使没有交易。
- 使用 `COALESCE` 函数来处理缺失值，确保结果中没有 NULL。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是用户表的行数，m 是交易表的行数。
空间复杂度: O(1)，查询过程中使用的额外空间是常数级别的。
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
    WITH RECURSIVE Months AS (
        SELECT 1 AS month
        UNION ALL
        SELECT month + 1
        FROM Months
        WHERE month < 12
    )
    SELECT 
        M.month,
        COALESCE(SUM(T.amount), 0) AS total_amount
    FROM 
        Months M
    LEFT JOIN 
        (SELECT * FROM User U JOIN Transactions T ON U.account = T.account) UT
    ON 
        M.month = EXTRACT(MONTH FROM UT.trans_date)
    GROUP BY 
        M.month
    ORDER BY 
        M.month;
    """
    return query


Solution = create_solution(solution_function_name)