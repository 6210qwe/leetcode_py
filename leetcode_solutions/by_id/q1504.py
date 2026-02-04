# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1504
标题: Get the Second Most Recent Activity
难度: hard
链接: https://leetcode.cn/problems/get-the-second-most-recent-activity/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1369. 获取最近第二次的活动 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数和子查询来获取每个用户的第二最近活动。

算法步骤:
1. 使用窗口函数 `ROW_NUMBER()` 按用户分组并按时间降序排列，为每条记录分配一个行号。
2. 子查询筛选出行号为2的记录，即每个用户的第二最近活动。
3. 返回结果集。

关键点:
- 使用窗口函数 `ROW_NUMBER()` 来为每条记录分配行号。
- 通过子查询筛选出特定行号的记录。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是记录的数量。主要开销在于排序操作。
空间复杂度: O(n)，用于存储中间结果。
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
    函数式接口 - 实现获取每个用户的第二最近活动
    """
    # SQL 查询语句
    query = """
    WITH RankedActivities AS (
        SELECT
            user_id,
            activity,
            timestamp,
            ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY timestamp DESC) as rnk
        FROM
            UserActivity
    )
    SELECT
        user_id,
        activity,
        timestamp
    FROM
        RankedActivities
    WHERE
        rnk = 2;
    """
    return query

Solution = create_solution(solution_function_name)