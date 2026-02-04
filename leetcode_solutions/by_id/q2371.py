# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2371
标题: The Users That Are Eligible for Discount
难度: easy
链接: https://leetcode.cn/problems/the-users-that-are-eligible-for-discount/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2371. 查找可享受优惠的用户 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来筛选符合条件的用户。

算法步骤:
1. 筛选出在连续三天内至少有三次交易的用户。
2. 返回这些用户的 id 和 name。

关键点:
- 使用窗口函数和子查询来实现连续三天的条件。
- 使用 GROUP BY 和 HAVING 子句来筛选出符合条件的用户。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是交易记录的数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，存储中间结果的空间复杂度为 O(n)。
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
    # 定义 SQL 查询
    query = """
    WITH ConsecutiveTransactions AS (
        SELECT
            user_id,
            transaction_date,
            COUNT(*) OVER (PARTITION BY user_id, DATE_SUB(transaction_date, INTERVAL RANK() OVER (PARTITION BY user_id ORDER BY transaction_date) DAY)) AS consecutive_count
        FROM
            Purchases
    ),
    EligibleUsers AS (
        SELECT
            DISTINCT user_id
        FROM
            ConsecutiveTransactions
        WHERE
            consecutive_count >= 3
    )
    SELECT
        u.user_id,
        u.name
    FROM
        Users u
    JOIN
        EligibleUsers eu ON u.user_id = eu.user_id;
    """
    # 执行查询并返回结果
    # 这里假设有一个数据库连接对象 `conn` 和一个执行查询的方法 `execute_query`
    result = execute_query(query)
    return result

Solution = create_solution(solution_function_name)