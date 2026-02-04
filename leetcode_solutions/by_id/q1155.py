# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1155
标题: Product Sales Analysis III
难度: medium
链接: https://leetcode.cn/problems/product-sales-analysis-iii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1070. 产品销售分析 III - 销售表 Sales： +-------------+-------+ | Column Name | Type | +-------------+-------+ | sale_id | int | | product_id | int | | year | int | | quantity | int | | price | int | +-------------+-------+ (sale_id, year) 是这张表的主键（具有唯一值的列的组合）。 这张表的每一行都表示：编号 product_id 的产品在某一年的销售额。 一个产品可能在同一年内有多个销售条目。 请注意，价格是按每单位计的。 编写解决方案，选出每个售出过的产品 第一年 销售的 产品 id、年份、数量 和 价格。 * 对每个 product_id，找到其在Sales表中首次出现的最早年份。 * 返回该产品在该年度的 所有 销售条目。 返回一张有这些列的表：product_id，first_year，quantity 和 price。 结果表中的条目可以按 任意顺序 排列。 示例 1： 输入： Sales 表： +---------+------------+------+----------+-------+ | sale_id | product_id | year | quantity | price | +---------+------------+------+----------+-------+ | 1 | 100 | 2008 | 10 | 5000 | | 2 | 100 | 2009 | 12 | 5000 | | 7 | 200 | 2011 | 15 | 9000 | +---------+------------+------+----------+-------+ 输出： +------------+------------+----------+-------+ | product_id | first_year | quantity | price | +------------+------------+----------+-------+ | 100 | 2008 | 10 | 5000 | | 200 | 2011 | 15 | 9000 | +------------+------------+----------+-------+
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用子查询来找到每个产品的最早销售年份，然后筛选出该年份的所有销售记录。

算法步骤:
1. 使用子查询找到每个产品的最早销售年份。
2. 筛选出这些最早年份的所有销售记录。

关键点:
- 使用 `MIN` 函数和 `GROUP BY` 来找到每个产品的最早销售年份。
- 使用 `IN` 子查询来筛选出这些最早年份的所有销售记录。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是销售记录的数量。子查询和连接操作的时间复杂度通常为 O(n log n)。
空间复杂度: O(1)，不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(sales: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 实现产品销售分析 III
    """
    # 将输入转换为字典，方便后续处理
    sales_dict = {}
    for sale in sales:
        sale_id, product_id, year, quantity, price = sale
        if product_id not in sales_dict:
            sales_dict[product_id] = []
        sales_dict[product_id].append((year, quantity, price))

    # 找到每个产品的最早销售年份
    earliest_years = {product_id: min(years) for product_id, years in ((product_id, [year for year, _, _ in sales]) for product_id, sales in sales_dict.items())}

    # 筛选出这些最早年份的所有销售记录
    result = []
    for product_id, sales in sales_dict.items():
        for year, quantity, price in sales:
            if year == earliest_years[product_id]:
                result.append([product_id, year, quantity, price])

    return result


Solution = create_solution(solution_function_name)