# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1153
标题: Product Sales Analysis I
难度: easy
链接: https://leetcode.cn/problems/product-sales-analysis-i/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1068. 产品销售分析 I - 销售表 Sales： +-------------+-------+ | Column Name | Type | +-------------+-------+ | sale_id | int | | product_id | int | | year | int | | quantity | int | | price | int | +-------------+-------+ (sale_id, year) 是销售表 Sales 的主键（具有唯一值的列的组合）。 product_id 是关联到产品表 Product 的外键（reference 列）。 该表的每一行显示 product_id 在某一年的销售情况。 注意: price 表示每单位价格。 产品表 Product： +--------------+---------+ | Column Name | Type | +--------------+---------+ | product_id | int | | product_name | varchar | +--------------+---------+ product_id 是表的主键（具有唯一值的列）。 该表的每一行表示每种产品的产品名称。 编写解决方案，以获取 Sales 表中所有 sale_id 对应的 product_name 以及该产品的所有 year 和 price 。 返回结果表 无顺序要求 。 结果格式示例如下。 示例 1： 输入： Sales 表： +---------+------------+------+----------+-------+ | sale_id | product_id | year | quantity | price | +---------+------------+------+----------+-------+ | 1 | 100 | 2008 | 10 | 5000 | | 2 | 100 | 2009 | 12 | 5000 | | 7 | 200 | 2011 | 15 | 9000 | +---------+------------+------+----------+-------+ Product 表： +------------+--------------+ | product_id | product_name | +------------+--------------+ | 100 | Nokia | | 200 | Apple | | 300 | Samsung | +------------+--------------+ 输出： +--------------+-------+-------+ | product_name | year | price | +--------------+-------+-------+ | Nokia | 2008 | 5000 | | Nokia | 2009 | 5000 | | Apple | 2011 | 9000 | +--------------+-------+-------+
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询将 Sales 表和 Product 表进行连接，并选择所需的列。

算法步骤:
1. 使用 INNER JOIN 将 Sales 表和 Product 表连接起来。
2. 选择 product_name, year 和 price 列。

关键点:
- 使用 INNER JOIN 确保只选择在两个表中都存在的 product_id。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 Sales 表的行数，m 是 Product 表的行数。
空间复杂度: O(1)，因为查询结果的大小与输入表的大小无关。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(sales: List[List[int]], products: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 实现 SQL 查询逻辑
    """
    # 创建一个字典来存储 product_id 和 product_name 的映射
    product_map = {product[0]: product[1] for product in products}
    
    # 生成结果列表
    result = []
    for sale in sales:
        product_id, year, _, price = sale
        if product_id in product_map:
            result.append([product_map[product_id], year, price])
    
    return result


Solution = create_solution(solution_function_name)