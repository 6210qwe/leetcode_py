# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1688
标题: The Most Recent Orders for Each Product
难度: medium
链接: https://leetcode.cn/problems/the-most-recent-orders-for-each-product/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1549. 每件商品的最新订单 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数 `ROW_NUMBER` 来为每个产品的订单按时间排序，并选择最新的订单。

算法步骤:
1. 使用 `ROW_NUMBER` 窗口函数为每个产品的订单按时间排序。
2. 选择每个产品中最新的订单（即 `ROW_NUMBER` 为 1 的订单）。

关键点:
- 使用 `PARTITION BY product_id` 和 `ORDER BY order_date DESC` 来确保每个产品的订单按时间降序排列。
- 通过 `ROW_NUMBER` 函数为每个分区内的行编号，选择编号为 1 的行作为最新订单。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是订单的数量。因为我们需要对每个产品的订单进行排序。
空间复杂度: O(1)，因为我们只使用了常数级的额外空间。
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
    函数式接口 - 查询每件商品的最新订单
    """
    # SQL 查询实现最优解法
    query = """
    SELECT product_id, order_id, order_date
    FROM (
        SELECT 
            product_id, 
            order_id, 
            order_date,
            ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY order_date DESC) AS rn
        FROM orders
    ) t
    WHERE rn = 1
    ORDER BY product_id, order_date DESC;
    """
    return query

Solution = create_solution(solution_function_name)