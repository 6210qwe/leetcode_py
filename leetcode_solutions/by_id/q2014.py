# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2014
标题: Orders With Maximum Quantity Above Average
难度: medium
链接: https://leetcode.cn/problems/orders-with-maximum-quantity-above-average/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1867. 最大数量高于平均水平的订单 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个产品的平均数量，并找出数量高于平均值的订单。

算法步骤:
1. 计算每个产品的平均数量。
2. 找出数量高于平均值的订单。
3. 返回这些订单的信息。

关键点:
- 使用子查询来计算平均数量。
- 使用 JOIN 来连接表并筛选出符合条件的订单。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是订单的数量，m 是产品的数量。我们需要遍历订单表和产品表来计算平均数量和筛选订单。
空间复杂度: O(1)，SQL 查询的空间复杂度通常是常数级别的。
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
    SELECT o.product_id, o.order_id, o.quantity
    FROM Orders o
    JOIN (
        SELECT product_id, AVG(quantity) AS avg_quantity
        FROM Orders
        GROUP BY product_id
    ) AS avg_orders ON o.product_id = avg_orders.product_id
    WHERE o.quantity > avg_orders.avg_quantity;
    """
    # 执行查询并返回结果
    return query


Solution = create_solution(solution_function_name)