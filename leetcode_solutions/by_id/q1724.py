# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1724
标题: Customer Who Visited but Did Not Make Any Transactions
难度: easy
链接: https://leetcode.cn/problems/customer-who-visited-but-did-not-make-any-transactions/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1581. 进店却未进行过交易的顾客 - 表：Visits +-------------+---------+ | Column Name | Type | +-------------+---------+ | visit_id | int | | customer_id | int | +-------------+---------+ visit_id 是该表中具有唯一值的列。 该表包含有关光临过购物中心的顾客的信息。 表：Transactions +----------------+---------+ | Column Name | Type | +----------------+---------+ | transaction_id | int | | visit_id | int | | amount | int | +----------------+---------+ transaction_id 是该表中具有唯一值的列。 此表包含 visit_id 期间进行的交易的信息。 有一些顾客可能光顾了购物中心但没有进行交易。请你编写一个解决方案，来查找这些顾客的 ID ，以及他们只光顾不交易的次数。 返回以 任何顺序 排序的结果表。 返回结果格式如下例所示。 示例 1： 输入: Visits +----------+-------------+ | visit_id | customer_id | +----------+-------------+ | 1 | 23 | | 2 | 9 | | 4 | 30 | | 5 | 54 | | 6 | 96 | | 7 | 54 | | 8 | 54 | +----------+-------------+ Transactions +----------------+----------+--------+ | transaction_id | visit_id | amount | +----------------+----------+--------+ | 2 | 5 | 310 | | 3 | 5 | 300 | | 9 | 5 | 200 | | 12 | 1 | 910 | | 13 | 2 | 970 | +----------------+----------+--------+ 输出: +-------------+----------------+ | customer_id | count_no_trans | +-------------+----------------+ | 54 | 2 | | 30 | 1 | | 96 | 1 | +-------------+----------------+ 解释: ID = 23 的顾客曾经逛过一次购物中心，并在 ID = 12 的访问期间进行了一笔交易。 ID = 9 的顾客曾经逛过一次购物中心，并在 ID = 13 的访问期间进行了一笔交易。 ID = 30 的顾客曾经去过购物中心，并且没有进行任何交易。 ID = 54 的顾客三度造访了购物中心。在 2 次访问中，他们没有进行任何交易，在 1 次访问中，他们进行了 3 次交易。 ID = 96 的顾客曾经去过购物中心，并且没有进行任何交易。 如我们所见，ID 为 30 和 96 的顾客一次没有进行任何交易就去了购物中心。顾客 54 也两次访问了购物中心并且没有进行任何交易。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找出没有进行交易的顾客及其访问次数。

算法步骤:
1. 找出所有有交易记录的 visit_id。
2. 从 Visits 表中筛选出不在上述 visit_id 列表中的记录。
3. 按 customer_id 分组并计算每个 customer_id 的访问次数。

关键点:
- 使用子查询和 NOT IN 来过滤没有交易的访问记录。
- 使用 GROUP BY 和 COUNT 来统计每个顾客的访问次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 Visits 表的行数，m 是 Transactions 表的行数。
空间复杂度: O(1)，除了输入和输出外，不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(visits: List[List[int]], transactions: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 实现最优解法
    """
    from collections import defaultdict

    # 1. 找出所有有交易记录的 visit_id
    trans_visit_ids = set([t[1] for t in transactions])

    # 2. 从 Visits 表中筛选出不在上述 visit_id 列表中的记录
    no_trans_visits = [v for v in visits if v[0] not in trans_visit_ids]

    # 3. 按 customer_id 分组并计算每个 customer_id 的访问次数
    customer_count = defaultdict(int)
    for visit in no_trans_visits:
        customer_count[visit[1]] += 1

    # 返回结果
    result = [[customer_id, count] for customer_id, count in customer_count.items()]
    return result


Solution = create_solution(solution_function_name)