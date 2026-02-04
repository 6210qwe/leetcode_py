# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1174
标题: Sales Analysis III
难度: easy
链接: https://leetcode.cn/problems/sales-analysis-iii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1084. 销售分析 III - 表： Product +--------------+---------+ | Column Name | Type | +--------------+---------+ | product_id | int | | product_name | varchar | | unit_price | int | +--------------+---------+ product_id 是该表的主键（具有唯一值的列）。 该表的每一行显示每个产品的名称和价格。 表：Sales +-------------+---------+ | Column Name | Type | +-------------+---------+ | seller_id | int | | product_id | int | | buyer_id | int | | sale_date | date | | quantity | int | | price | int | +------ ------+---------+ 这个表可能有重复的行。 product_id 是 Product 表的外键（reference 列）。 该表的每一行包含关于一个销售的一些信息。 编写解决方案，报告 2019年春季 才售出的产品。即 仅 在 2019-01-01 （含）至 2019-03-31 （含）之间出售的商品。 以 任意顺序 返回结果表。 结果格式如下所示。 示例 1: 输入： Product table: +------------+--------------+------------+ | product_id | product_name | unit_price | +------------+--------------+------------+ | 1 | S8 | 1000 | | 2 | G4 | 800 | | 3 | iPhone | 1400 | +------------+--------------+------------+ Sales table: +-----------+------------+----------+------------+----------+-------+ | seller_id | product_id | buyer_id | sale_date | quantity | price | +-----------+------------+----------+------------+----------+-------+ | 1 | 1 | 1 | 2019-01-21 | 2 | 2000 | | 1 | 2 | 2 | 2019-02-17 | 1 | 800 | | 2 | 2 | 3 | 2019-06-02 | 1 | 800 | | 3 | 3 | 4 | 2019-05-13 | 2 | 2800 | +-----------+------------+----------+------------+----------+-------+ 输出： +-------------+--------------+ | product_id | product_name | +-------------+--------------+ | 1 | S8 | +-------------+--------------+ 解释: id 为 1 的产品仅在 2019 年春季销售。 id 为 2 的产品在 2019 年春季销售，但也在 2019 年春季之后销售。 id 为 3 的产品在 2019 年春季之后销售。 我们只返回 id 为 1 的产品，因为它是 2019 年春季才销售的产品。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 筛选出在 2019-01-01 至 2019-03-31 之间的销售记录。
2. 找出这些销售记录中所有出现的产品 ID。
3. 筛选出不在其他时间销售的产品 ID。
4. 返回这些产品 ID 及其名称。

算法步骤:
1. 使用 SQL 查询筛选出 2019-01-01 至 2019-03-31 之间的销售记录。
2. 使用子查询找出这些销售记录中所有出现的产品 ID。
3. 再次使用子查询找出不在其他时间销售的产品 ID。
4. 最后从 Product 表中获取这些产品 ID 对应的产品名称。

关键点:
- 使用子查询和集合操作来筛选出符合条件的产品。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(product: List[List[str]], sales: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 实现
    """
    # 将输入转换为 Pandas DataFrame
    import pandas as pd
    product_df = pd.DataFrame(product[1:], columns=product[0])
    sales_df = pd.DataFrame(sales[1:], columns=sales[0])

    # 转换日期格式
    sales_df['sale_date'] = pd.to_datetime(sales_df['sale_date'])

    # 筛选出 2019-01-01 至 2019-03-31 之间的销售记录
    spring_sales = sales_df[(sales_df['sale_date'] >= '2019-01-01') & (sales_df['sale_date'] <= '2019-03-31')]

    # 找出这些销售记录中所有出现的产品 ID
    spring_product_ids = set(spring_sales['product_id'])

    # 筛选出不在其他时间销售的产品 ID
    other_sales = sales_df[(sales_df['sale_date'] < '2019-01-01') | (sales_df['sale_date'] > '2019-03-31')]
    other_product_ids = set(other_sales['product_id'])
    only_spring_product_ids = spring_product_ids - other_product_ids

    # 从 Product 表中获取这些产品 ID 对应的产品名称
    result = product_df[product_df['product_id'].isin(only_spring_product_ids)][['product_id', 'product_name']].values.tolist()

    return result


Solution = create_solution(solution_function_name)