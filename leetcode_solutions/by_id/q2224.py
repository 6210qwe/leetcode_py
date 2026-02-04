# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2224
标题: Drop Type 1 Orders for Customers With Type 0 Orders
难度: medium
链接: https://leetcode.cn/problems/drop-type-1-orders-for-customers-with-type-0-orders/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2084. 为订单类型为 0 的客户删除类型为 1 的订单 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用子查询和左连接来过滤掉类型为 1 的订单。

算法步骤:
1. 找出所有有类型为 0 的订单的客户。
2. 使用左连接将这些客户与他们的订单连接起来。
3. 过滤掉类型为 1 的订单。

关键点:
- 使用子查询来找出有类型为 0 的订单的客户。
- 使用左连接来保留所有类型为 0 的订单，并过滤掉类型为 1 的订单。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log n)，其中 n 是订单表的大小。子查询和连接操作的时间复杂度取决于数据库的实现。
空间复杂度: O(1)，不使用额外的空间，只使用 SQL 查询。
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
    # SQL 查询实现最优解法
    query = """
    SELECT o.customer_id, o.order_type, o.product_name, o.product_id, o.order_date
    FROM Orders o
    LEFT JOIN (
        SELECT customer_id
        FROM Orders
        WHERE order_type = 0
    ) t ON o.customer_id = t.customer_id
    WHERE o.order_type = 0 OR t.customer_id IS NULL
    ORDER BY o.customer_id, o.order_date
    """
    return query


Solution = create_solution(solution_function_name)