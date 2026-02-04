# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3205
标题: Market Analysis III
难度: medium
链接: https://leetcode.cn/problems/market-analysis-iii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2922. 市场分析 III - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数和子查询来计算每个用户的平均消费金额，并找出消费金额大于平均值的用户。

算法步骤:
1. 计算每个用户的总消费金额。
2. 计算所有用户的平均消费金额。
3. 找出消费金额大于平均值的用户。

关键点:
- 使用窗口函数 `SUM` 和 `AVG` 来计算总消费金额和平均消费金额。
- 使用子查询来过滤出消费金额大于平均值的用户。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
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
    函数式接口 - 实现
    """
    # SQL 查询实现
    query = """
    WITH UserSpending AS (
        SELECT user_id, SUM(amount) AS total_spent
        FROM Transactions
        GROUP BY user_id
    ),
    AverageSpending AS (
        SELECT AVG(total_spent) AS avg_spent
        FROM UserSpending
    )
    SELECT user_id
    FROM UserSpending, AverageSpending
    WHERE UserSpending.total_spent > AverageSpending.avg_spent;
    """
    return query

Solution = create_solution(solution_function_name)