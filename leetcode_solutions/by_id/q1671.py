# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1671
标题: The Most Recent Three Orders
难度: medium
链接: https://leetcode.cn/problems/the-most-recent-three-orders/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1532. 最近的三笔订单 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数 `ROW_NUMBER()` 来获取每个用户的最近三笔订单。

算法步骤:
1. 使用 `ROW_NUMBER()` 窗口函数为每个用户的订单按时间降序排序。
2. 过滤出每个用户最近的三笔订单。
3. 返回结果集。

关键点:
- 使用 `ROW_NUMBER()` 窗口函数可以方便地对每个用户的订单进行排序和筛选。
- 通过 `PARTITION BY` 和 `ORDER BY` 子句来实现分组和排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是订单的数量。主要的时间开销在于排序操作。
空间复杂度: O(n)，窗口函数的中间结果需要存储。
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
    函数式接口 - 实现
    """
    # SQL 查询语句
    query = """
    SELECT 
        user_id, 
        order_id, 
        order_date
    FROM (
        SELECT 
            user_id, 
            order_id, 
            order_date,
            ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY order_date DESC) AS rn
        FROM 
            Orders
    ) AS subquery
    WHERE 
        rn <= 3
    ORDER BY 
        user_id, 
        order_date DESC;
    """
    return query


Solution = create_solution(solution_function_name)