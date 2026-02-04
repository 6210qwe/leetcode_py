# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1390
标题: Average Selling Price
难度: easy
链接: https://leetcode.cn/problems/average-selling-price/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1251. 平均售价 - 表：Prices +---------------+---------+ | Column Name | Type | +---------------+---------+ | product_id | int | | start_date | date | | end_date | date | | price | int | +---------------+---------+ (product_id，start_date，end_date) 是 prices 表的主键（具有唯一值的列的组合）。 prices 表的每一行表示的是某个产品在一段时期内的价格。 每个产品的对应时间段是不会重叠的，这也意味着同一个产品的价格时段不会出现交叉。 表：UnitsSold +---------------+---------+ | Column Name | Type | +---------------+---------+ | product_id | int | | purchase_date | date | | units | int | +---------------+---------+ 该表可能包含重复数据。 该表的每一行表示的是每种产品的出售日期，单位和产品 id。 编写解决方案以查找每种产品的平均售价。average_price 应该 四舍五入到小数点后两位。如果产品没有任何售出，则假设其平均售价为 0。 返回结果表 无顺序要求 。 结果格式如下例所示。 示例 1： 输入： Prices table: +------------+------------+------------+--------+ | product_id | start_date | end_date | price | +------------+------------+------------+--------+ | 1 | 2019-02-17 | 2019-02-28 | 5 | | 1 | 2019-03-01 | 2019-03-22 | 20 | | 2 | 2019-02-01 | 2019-02-20 | 15 | | 2 | 2019-02-21 | 2019-03-31 | 30 | +------------+------------+------------+--------+ UnitsSold table: +------------+---------------+-------+ | product_id | purchase_date | units | +------------+---------------+-------+ | 1 | 2019-02-25 | 100 | | 1 | 2019-03-01 | 15 | | 2 | 2019-02-10 | 200 | | 2 | 2019-03-22 | 30 | +------------+---------------+-------+ 输出： +------------+---------------+ | product_id | average_price | +------------+---------------+ | 1 | 6.96 | | 2 | 16.96 | +------------+---------------+ 解释： 平均售价 = 产品总价 / 销售的产品数量。 产品 1 的平均售价 = ((100 * 5)+(15 * 20) )/ 115 = 6.96 产品 2 的平均售价 = ((200 * 15)+(30 * 30) )/ 230 = 16.96
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个产品的平均售价。

算法步骤:
1. 将 `Prices` 和 `UnitsSold` 表进行连接，条件是 `product_id` 相同且 `purchase_date` 在 `start_date` 和 `end_date` 之间。
2. 计算每个产品的总销售额和总销售数量。
3. 计算每个产品的平均售价，并四舍五入到小数点后两位。
4. 如果产品没有任何售出，则假设其平均售价为 0。

关键点:
- 使用 `LEFT JOIN` 确保所有产品都被考虑，即使没有售出记录。
- 使用 `COALESCE` 函数处理没有售出记录的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 `Prices` 表的行数，m 是 `UnitsSold` 表的行数。
空间复杂度: O(1)，查询过程中使用的额外空间是常数级别的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(prices: List[List[int]], units_sold: List[List[int]]) -> List[List[float]]:
    """
    函数式接口 - 计算每个产品的平均售价
    """
    # 构建 SQL 查询
    query = """
    SELECT 
        p.product_id,
        COALESCE(ROUND(SUM(p.price * u.units) / SUM(u.units), 2), 0) AS average_price
    FROM 
        (VALUES %s) AS p(product_id, start_date, end_date, price)
    LEFT JOIN 
        (VALUES %s) AS u(product_id, purchase_date, units)
    ON 
        p.product_id = u.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
    GROUP BY 
        p.product_id
    """ % (
        ", ".join(["(%d, '%s', '%s', %d)" % tuple(row) for row in prices]),
        ", ".join(["(%d, '%s', %d)" % tuple(row) for row in units_sold])
    )
    
    # 执行 SQL 查询
    result = []
    for row in execute_sql(query):
        result.append([row[0], row[1]])
    
    return result


def execute_sql(query: str) -> List[tuple]:
    """
    执行 SQL 查询并返回结果
    """
    # 假设这里有一个数据库连接对象 `conn`
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


Solution = create_solution(solution_function_name)