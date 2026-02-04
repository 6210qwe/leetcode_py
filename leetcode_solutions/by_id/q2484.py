# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2484
标题: Compute the Rank as a Percentage
难度: medium
链接: https://leetcode.cn/problems/compute-the-rank-as-a-percentage/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2346. 以百分比计算排名 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数 `RANK()` 和 `COUNT()` 来计算每个用户的排名和总用户数，然后计算排名百分比。

算法步骤:
1. 使用窗口函数 `RANK()` 计算每个用户的排名。
2. 使用窗口函数 `COUNT()` 计算总用户数。
3. 计算每个用户的排名百分比。
4. 返回结果。

关键点:
- 使用窗口函数可以高效地计算排名和总用户数。
- 排名百分比的计算公式为 `(rank - 1) / (total_users - 1) * 100`。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是用户数量。窗口函数的计算是线性的。
空间复杂度: O(1)，不考虑输出结果的空间消耗。
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
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass

Solution = create_solution(solution_function_name)

# SQL 查询实现
sql_query = """
WITH UserRank AS (
    SELECT
        user_id,
        score,
        RANK() OVER (ORDER BY score DESC) AS rank,
        COUNT(*) OVER () AS total_users
    FROM
        Scores
)
SELECT
    user_id,
    score,
    ROUND((rank - 1) / (total_users - 1) * 100, 2) AS percentage
FROM
    UserRank
ORDER BY
    percentage DESC, user_id ASC;
"""

# 将 SQL 查询结果作为解决方案
def solution_sql():
    return sql_query

Solution = create_solution(solution_sql)