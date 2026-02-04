# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1135
标题: Customers Who Bought All Products
难度: medium
链接: https://leetcode.cn/problems/customers-who-bought-all-products/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1045. 买下所有产品的客户 - Customer 表： +-------------+---------+ | Column Name | Type | +-------------+---------+ | customer_id | int | | product_key | int | +-------------+---------+ 该表可能包含重复的行。 customer_id 不为 NULL。 product_key 是 Product 表的外键(reference 列)。 Product 表： +-------------+---------+ | Column Name | Type | +-------------+---------+ | product_key | int | +-------------+---------+ product_key 是这张表的主键（具有唯一值的列）。 编写解决方案，报告 Customer 表中购买了 Product 表中所有产品的客户的 id。 返回结果表 无顺序要求 。 返回结果格式如下所示。 示例 1： 输入： Customer 表： +-------------+-------------+ | customer_id | product_key | +-------------+-------------+ | 1 | 5 | | 2 | 6 | | 3 | 5 | | 3 | 6 | | 1 | 6 | +-------------+-------------+ Product 表： +-------------+ | product_key | +-------------+ | 5 | | 6 | +-------------+ 输出： +-------------+ | customer_id | +-------------+ | 1 | | 3 | +-------------+ 解释： 购买了所有产品（5 和 6）的客户的 id 是 1 和 3 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用集合操作来找出购买了所有产品的客户。

算法步骤:
1. 从 Product 表中获取所有产品的产品键。
2. 从 Customer 表中按 customer_id 分组，并统计每个客户购买的产品键。
3. 检查每个客户的购买记录是否包含所有产品键。
4. 返回满足条件的客户 ID。

关键点:
- 使用集合操作来高效地检查每个客户的购买记录是否包含所有产品键。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 Customer 表的行数，m 是 Product 表的行数。
空间复杂度: O(k + p)，其中 k 是不同客户 ID 的数量，p 是不同产品键的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(customer: List[List[int]], product: List[int]) -> List[int]:
    """
    函数式接口 - 实现
    """
    # 获取所有产品的产品键
    all_products = set(product)
    
    # 从 Customer 表中按 customer_id 分组，并统计每个客户购买的产品键
    customer_purchases = {}
    for cust_id, prod_key in customer:
        if cust_id not in customer_purchases:
            customer_purchases[cust_id] = set()
        customer_purchases[cust_id].add(prod_key)
    
    # 检查每个客户的购买记录是否包含所有产品键
    result = []
    for cust_id, purchases in customer_purchases.items():
        if all_products.issubset(purchases):
            result.append(cust_id)
    
    return result


Solution = create_solution(solution_function_name)