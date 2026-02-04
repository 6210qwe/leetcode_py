# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1852
标题: Biggest Window Between Visits
难度: medium
链接: https://leetcode.cn/problems/biggest-window-between-visits/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1709. 访问日期之间最大的空档期 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个用户访问日期之间的最大空档期。

算法步骤:
1. 使用窗口函数 `LAG` 获取每个用户的前一个访问日期。
2. 计算当前访问日期与前一个访问日期之间的差值。
3. 使用 `MAX` 函数找到每个用户的最大空档期。
4. 返回结果。

关键点:
- 使用 `LAG` 窗口函数来获取前一个访问日期。
- 使用 `DATEDIFF` 函数来计算日期差值。
- 使用 `MAX` 函数来找到最大空档期。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是用户访问记录的数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，查询中使用的额外空间是常数级别的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(user_visits: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 计算每个用户访问日期之间的最大空档期
    """
    # 构建 SQL 查询
    query = """
    WITH visit_dates AS (
        SELECT
            user_id,
            visit_date,
            LAG(visit_date, 1) OVER (PARTITION BY user_id ORDER BY visit_date) AS prev_visit_date
        FROM
            (SELECT user_id, visit_date FROM user_visits) t
    )
    SELECT
        user_id,
        MAX(DATEDIFF(visit_date, prev_visit_date)) AS max_gap
    FROM
        visit_dates
    GROUP BY
        user_id
    """

    # 执行查询并返回结果
    # 这里假设有一个数据库连接对象 `db_connection` 和执行查询的方法 `execute_query`
    result = db_connection.execute_query(query)
    return result


Solution = create_solution(solution_function_name)