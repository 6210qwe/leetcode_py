# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2853
标题: Consecutive Transactions with Increasing Amounts
难度: hard
链接: https://leetcode.cn/problems/consecutive-transactions-with-increasing-amounts/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2701. 连续递增交易 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到连续递增的交易记录。

算法步骤:
1. 通过自连接表来比较相邻的交易金额。
2. 使用窗口函数 `ROW_NUMBER()` 来为每条记录分配一个唯一的行号。
3. 通过条件过滤找到连续递增的交易记录。

关键点:
- 使用自连接和窗口函数来处理连续递增的交易记录。
- 确保查询结果满足题目要求。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是交易记录的数量。主要由排序操作决定。
空间复杂度: O(1)，不考虑输出结果的空间占用。
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
    WITH RankedTransactions AS (
        SELECT 
            t1.transaction_id,
            t1.amount,
            ROW_NUMBER() OVER (PARTITION BY t1.customer_id ORDER BY t1.day) AS rn
        FROM 
            Transactions t1
    )
    SELECT 
        t1.transaction_id
    FROM 
        RankedTransactions t1
        JOIN RankedTransactions t2 ON t1.customer_id = t2.customer_id AND t1.rn = t2.rn + 1
    WHERE 
        t1.amount > t2.amount
    ORDER BY 
        t1.transaction_id
    """
    return query


Solution = create_solution(solution_function_name)