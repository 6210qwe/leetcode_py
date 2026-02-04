# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2613
标题: Customers With Strictly Increasing Purchases
难度: hard
链接: https://leetcode.cn/problems/customers-with-strictly-increasing-purchases/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2474. 购买量严格增加的客户 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数和自连接来查找购买量严格增加的客户。

算法步骤:
1. 使用窗口函数 `ROW_NUMBER()` 为每个客户的购买记录按购买日期排序并分配一个行号。
2. 自连接购买记录表，确保同一客户的后续购买记录的金额大于前一条记录的金额。
3. 通过递归查询或子查询过滤出满足条件的客户。

关键点:
- 使用窗口函数和自连接来处理时间序列数据。
- 确保每条记录的金额都严格大于前一条记录的金额。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是购买记录的数量。主要开销在于排序操作。
空间复杂度: O(n)，用于存储中间结果和递归查询。
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
    函数式接口 - 查询购买量严格增加的客户
    """
    # SQL 查询实现
    query = """
    WITH RankedPurchases AS (
        SELECT
            customer_id,
            purchase_date,
            amount,
            ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY purchase_date) as rn
        FROM
            purchases
    ),
    RecursivePurchases AS (
        SELECT
            r1.customer_id,
            r1.purchase_date AS date1,
            r1.amount AS amount1,
            r1.rn AS rn1,
            r2.purchase_date AS date2,
            r2.amount AS amount2,
            r2.rn AS rn2
        FROM
            RankedPurchases r1
        JOIN
            RankedPurchases r2
        ON
            r1.customer_id = r2.customer_id AND r1.rn + 1 = r2.rn
        WHERE
            r1.amount < r2.amount
    )
    SELECT DISTINCT
        customer_id
    FROM
        RecursivePurchases
    WHERE NOT EXISTS (
        SELECT 1
        FROM
            RankedPurchases r1
        JOIN
            RankedPurchases r2
        ON
            r1.customer_id = r2.customer_id AND r1.rn + 1 = r2.rn
        WHERE
            r1.amount >= r2.amount
    );
    """
    return query

Solution = create_solution(solution_function_name)