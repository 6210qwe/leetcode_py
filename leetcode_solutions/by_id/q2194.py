# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2194
标题: The Category of Each Member in the Store
难度: medium
链接: https://leetcode.cn/problems/the-category-of-each-member-in-the-store/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2051. 商店中每个成员的级别 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个成员的消费金额，并根据消费金额将其分类。

算法步骤:
1. 计算每个成员的总消费金额。
2. 根据总消费金额将成员分类为 "Diamond", "Gold", "Silver" 或 "Bronze"。

关键点:
- 使用 CASE WHEN 语句进行分类。
- 使用 GROUP BY 和 SUM 函数计算每个成员的总消费金额。
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
    # 实现最优解法
    query = """
    SELECT 
        member_id,
        CASE
            WHEN total_spent >= 20000 THEN 'Diamond'
            WHEN total_spent >= 5000 THEN 'Gold'
            WHEN total_spent >= 0 THEN 'Silver'
            ELSE 'Bronze'
        END AS category
    FROM (
        SELECT 
            member_id,
            SUM(amount) AS total_spent
        FROM 
            sales
        GROUP BY 
            member_id
    ) AS subquery
    ORDER BY 
        member_id;
    """
    return query


Solution = create_solution(solution_function_name)