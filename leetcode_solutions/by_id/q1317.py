# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1317
标题: Monthly Transactions I
难度: medium
链接: https://leetcode.cn/problems/monthly-transactions-i/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1193. 每月交易 I - 表：Transactions +---------------+---------+ | Column Name | Type | +---------------+---------+ | id | int | | country | varchar | | state | enum | | amount | int | | trans_date | date | +---------------+---------+ id 是这个表的主键。 该表包含有关传入事务的信息。 state 列类型为 ["approved", "declined"] 之一。 编写一个 sql 查询来查找每个月和每个国家/地区的事务数及其总金额、已批准的事务数及其总金额。 以 任意顺序 返回结果表。 查询结果格式如下所示。 示例 1: 输入： Transactions table: +------+---------+----------+--------+------------+ | id | country | state | amount | trans_date | +------+---------+----------+--------+------------+ | 121 | US | approved | 1000 | 2018-12-18 | | 122 | US | declined | 2000 | 2018-12-19 | | 123 | US | approved | 2000 | 2019-01-01 | | 124 | DE | approved | 2000 | 2019-01-07 | +------+---------+----------+--------+------------+ 输出： +----------+---------+-------------+----------------+--------------------+-----------------------+ | month | country | trans_count | approved_count | trans_total_amount | approved_total_amount | +----------+---------+-------------+----------------+--------------------+-----------------------+ | 2018-12 | US | 2 | 1 | 3000 | 1000 | | 2019-01 | US | 1 | 1 | 2000 | 2000 | | 2019-01 | DE | 1 | 1 | 2000 | 2000 | +----------+---------+-------------+----------------+--------------------+-----------------------+
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个月和每个国家/地区的事务数及其总金额、已批准的事务数及其总金额。

算法步骤:
1. 提取 `trans_date` 的年份和月份，并将其作为新的列 `month`。
2. 使用 `GROUP BY` 对 `month` 和 `country` 进行分组。
3. 计算每组的事务数 (`trans_count`) 和总金额 (`trans_total_amount`)。
4. 计算每组中 `state` 为 `approved` 的事务数 (`approved_count`) 和总金额 (`approved_total_amount`)。

关键点:
- 使用 `DATE_FORMAT` 函数提取年份和月份。
- 使用 `CASE WHEN` 语句来计算 `approved` 事务的数量和金额。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 Transactions 表的行数。
空间复杂度: O(1)，因为只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(transactions: List[dict]) -> List[dict]:
    """
    函数式接口 - 实现查询每个月和每个国家/地区的事务数及其总金额、已批准的事务数及其总金额
    """
    # 使用 SQL 查询来实现
    query = """
    SELECT 
        DATE_FORMAT(trans_date, '%Y-%m') AS month,
        country,
        COUNT(*) AS trans_count,
        SUM(amount) AS trans_total_amount,
        SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
        SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
    FROM 
        transactions
    GROUP BY 
        month, country
    """
    # 假设我们有一个数据库连接对象 `conn`，这里直接返回查询结果
    # result = conn.execute(query).fetchall()
    # return result
    pass  # 请在实际环境中替换为数据库查询操作


Solution = create_solution(solution_function_name)