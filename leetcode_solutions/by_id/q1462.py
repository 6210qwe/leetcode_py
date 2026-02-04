# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1462
标题: List the Products Ordered in a Period
难度: easy
链接: https://leetcode.cn/problems/list-the-products-ordered-in-a-period/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1327. 列出指定时间段内所有的下单产品 - 表: Products +------------------+---------+ | Column Name | Type | +------------------+---------+ | product_id | int | | product_name | varchar | | product_category | varchar | +------------------+---------+ product_id 是该表主键(具有唯一值的列)。 该表包含该公司产品的数据。 表: Orders +---------------+---------+ | Column Name | Type | +---------------+---------+ | product_id | int | | order_date | date | | unit | int | +---------------+---------+ 该表可能包含重复行。 product_id 是表单 Products 的外键（reference 列）。 unit 是在日期 order_date 内下单产品的数目。 写一个解决方案，要求获取在 2020 年 2 月份下单的数量不少于 100 的产品的名字和数目。 返回结果表单的 顺序无要求 。 查询结果的格式如下。 示例 1: 输入： Products 表: +-------------+-----------------------+------------------+ | product_id | product_name | product_category | +-------------+-----------------------+------------------+ | 1 | Leetcode Solutions | Book | | 2 | Jewels of Stringology | Book | | 3 | HP | Laptop | | 4 | Lenovo | Laptop | | 5 | Leetcode Kit | T-shirt | +-------------+-----------------------+------------------+ Orders 表: +--------------+--------------+----------+ | product_id | order_date | unit | +--------------+--------------+----------+ | 1 | 2020-02-05 | 60 | | 1 | 2020-02-10 | 70 | | 2 | 2020-01-18 | 30 | | 2 | 2020-02-11 | 80 | | 3 | 2020-02-17 | 2 | | 3 | 2020-02-24 | 3 | | 4 | 2020-03-01 | 20 | | 4 | 2020-03-04 | 30 | | 4 | 2020-03-04 | 60 | | 5 | 2020-02-25 | 50 | | 5 | 2020-02-27 | 50 | | 5 | 2020-03-01 | 50 | +--------------+--------------+----------+ 输出： +--------------------+---------+ | product_name | unit | +--------------------+---------+ | Leetcode Solutions | 130 | | Leetcode Kit | 100 | +--------------------+---------+ 解释： 2020 年 2 月份下单 product_id = 1 的产品的数目总和为 (60 + 70) = 130 。 2020 年 2 月份下单 product_id = 2 的产品的数目总和为 80 。 2020 年 2 月份下单 product_id = 3 的产品的数目总和为 (2 + 3) = 5 。 2020 年 2 月份 product_id = 4 的产品并没有下单。 2020 年 2 月份下单 product_id = 5 的产品的数目总和为 (50 + 50) = 100 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来筛选 2020 年 2 月份下单数量不少于 100 的产品，并返回其名称和数量。

算法步骤:
1. 过滤 Orders 表，只保留 2020 年 2 月份的数据。
2. 按 product_id 分组并计算每个产品的总下单数量。
3. 筛选出总下单数量不少于 100 的产品。
4. 将这些产品与 Products 表进行连接，获取产品名称。
5. 返回结果表，包含产品名称和总下单数量。

关键点:
- 使用 WHERE 子句过滤 2020 年 2 月份的数据。
- 使用 GROUP BY 和 SUM 函数计算每个产品的总下单数量。
- 使用 INNER JOIN 连接 Orders 和 Products 表。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 Orders 表的行数。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，需要存储中间结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(products: List[List[str]], orders: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 实现
    """
    # 将输入转换为 Pandas DataFrame
    import pandas as pd
    products_df = pd.DataFrame(products[1:], columns=products[0])
    orders_df = pd.DataFrame(orders[1:], columns=orders[0])

    # 过滤 2020 年 2 月份的数据
    orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])
    orders_df = orders_df[(orders_df['order_date'].dt.year == 2020) & (orders_df['order_date'].dt.month == 2)]

    # 按 product_id 分组并计算每个产品的总下单数量
    orders_grouped = orders_df.groupby('product_id')['unit'].sum().reset_index()

    # 筛选出总下单数量不少于 100 的产品
    filtered_orders = orders_grouped[orders_grouped['unit'] >= 100]

    # 将这些产品与 Products 表进行连接，获取产品名称
    result = pd.merge(filtered_orders, products_df, on='product_id', how='inner')[['product_name', 'unit']]

    # 返回结果表
    return result.values.tolist()


Solution = create_solution(solution_function_name)