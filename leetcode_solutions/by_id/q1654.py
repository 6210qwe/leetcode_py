# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1654
标题: Customer Order Frequency
难度: easy
链接: https://leetcode.cn/problems/customer-order-frequency/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1511. 消费者下单频率 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个消费者的订单频率。

算法步骤:
1. 从 `Orders` 表中选择 `customer_id` 和 `order_date` 字段。
2. 使用 `GROUP BY` 子句按 `customer_id` 分组。
3. 使用 `COUNT` 函数计算每个消费者的订单数量。
4. 将结果按订单数量降序排列，如果订单数量相同，则按 `customer_id` 升序排列。

关键点:
- 使用 `GROUP BY` 和 `COUNT` 函数进行分组和计数。
- 使用 `ORDER BY` 子句对结果进行排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 `Orders` 表的行数。主要的时间开销在于排序操作。
空间复杂度: O(1)，除了存储查询结果外，不需要额外的空间。
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
    函数式接口 - 实现 SQL 查询
    """
    # 实现最优解法
    query = """
    SELECT customer_id, COUNT(order_date) AS order_count
    FROM Orders
    GROUP BY customer_id
    ORDER BY order_count DESC, customer_id ASC;
    """
    return query


Solution = create_solution(solution_function_name)