# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1712
标题: Unique Orders and Customers Per Month
难度: easy
链接: https://leetcode.cn/problems/unique-orders-and-customers-per-month/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1565. 按月统计订单数与顾客数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来按月统计唯一订单数和唯一顾客数。

算法步骤:
1. 从 `Orders` 表中选择 `order_id`, `customer_id` 和 `order_date` 列。
2. 使用 `DATE_FORMAT` 函数提取 `order_date` 的年份和月份。
3. 使用 `GROUP BY` 子句按年份和月份分组。
4. 使用 `COUNT(DISTINCT ...)` 函数计算每组的唯一订单数和唯一顾客数。

关键点:
- 使用 `DATE_FORMAT` 提取日期格式。
- 使用 `COUNT(DISTINCT ...)` 计算唯一值的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 `Orders` 表中的行数。因为我们需要遍历整个表来进行分组和计数。
空间复杂度: O(1)，SQL 查询的空间复杂度通常是常数级别的，因为我们只返回了聚合结果。
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
    # 实现最优解法
    query = """
    SELECT 
        DATE_FORMAT(order_date, '%Y-%m') AS month,
        COUNT(DISTINCT order_id) AS order_count,
        COUNT(DISTINCT customer_id) AS customer_count
    FROM 
        Orders
    GROUP BY 
        DATE_FORMAT(order_date, '%Y-%m')
    ORDER BY 
        month;
    """
    return query


Solution = create_solution(solution_function_name)