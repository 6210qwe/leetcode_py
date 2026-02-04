# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1974
标题: Find Customers With Positive Revenue this Year
难度: easy
链接: https://leetcode.cn/problems/find-customers-with-positive-revenue-this-year/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1821. 寻找今年具有正收入的客户 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来筛选出今年有正收入的客户。

算法步骤:
1. 从 `Customers` 表中选择所有客户的 `customer_id` 和 `name`。
2. 使用子查询从 `Orders` 表中筛选出今年有正收入的订单。
3. 将 `Customers` 表和子查询结果进行连接，筛选出符合条件的客户。

关键点:
- 使用子查询来筛选出今年有正收入的订单。
- 使用 INNER JOIN 来连接 `Customers` 表和子查询结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 `Customers` 表的行数，m 是 `Orders` 表的行数。
空间复杂度: O(1)，不考虑查询结果所占用的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(customers: List[dict], orders: List[dict]) -> List[dict]:
    """
    函数式接口 - 筛选出今年有正收入的客户
    """
    # 从 Orders 表中筛选出今年有正收入的订单
    positive_revenue_orders = [order for order in orders if order['revenue'] > 0 and order['year'] == 2023]

    # 获取有正收入订单的客户 ID
    positive_revenue_customer_ids = {order['customer_id'] for order in positive_revenue_orders}

    # 从 Customers 表中筛选出符合条件的客户
    result = [customer for customer in customers if customer['id'] in positive_revenue_customer_ids]

    return result


Solution = create_solution(solution_function_name)