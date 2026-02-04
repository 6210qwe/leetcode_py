# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2370
标题: Users With Two Purchases Within Seven Days
难度: medium
链接: https://leetcode.cn/problems/users-with-two-purchases-within-seven-days/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2228. 7 天内两次购买的用户 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用自连接和窗口函数来查找在7天内有两次购买记录的用户。

算法步骤:
1. 使用自连接将同一个用户的购买记录进行连接，并筛选出时间差在7天内的记录。
2. 使用窗口函数 `ROW_NUMBER()` 来为每个用户的购买记录编号。
3. 筛选出每个用户在7天内有两次购买记录的情况。

关键点:
- 自连接用于找到同一用户在不同时间的购买记录。
- 窗口函数 `ROW_NUMBER()` 用于为每个用户的购买记录编号，以便后续筛选。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是购买记录的数量。主要的时间开销在于排序操作。
空间复杂度: O(n)，自连接和窗口函数的使用需要额外的空间来存储中间结果。
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
    # SQL 查询实现最优解法
    query = """
    WITH PurchaseWindow AS (
        SELECT
            p1.user_id,
            p1.purchase_date,
            COUNT(*) OVER (PARTITION BY p1.user_id) as purchase_count
        FROM
            Purchases p1
        JOIN
            Purchases p2 ON p1.user_id = p2.user_id AND p1.purchase_date < p2.purchase_date
        WHERE
            p2.purchase_date - p1.purchase_date <= 7
    )
    SELECT DISTINCT user_id
    FROM PurchaseWindow
    WHERE purchase_count >= 2;
    """
    return query

Solution = create_solution(solution_function_name)