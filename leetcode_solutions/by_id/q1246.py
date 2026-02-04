# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1246
标题: User Activity for the Past 30 Days II
难度: easy
链接: https://leetcode.cn/problems/user-activity-for-the-past-30-days-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1142. 过去30天的用户活动 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个用户的活跃天数，并按要求进行分组和排序。

算法步骤:
1. 创建一个临时表 `active_days` 来存储每个用户的活跃天数。
2. 使用 `GROUP BY` 和 `COUNT` 函数计算每个用户的活跃天数。
3. 使用 `CASE` 语句将活跃天数分为不同的区间。
4. 按要求进行分组和排序。

关键点:
- 使用 `DATE_SUB` 和 `CURDATE` 函数来获取过去30天的数据。
- 使用 `CASE` 语句来分组活跃天数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是用户活动记录的数量。
空间复杂度: O(1)，不考虑结果集的空间占用。
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
    函数式接口 - 使用 SQL 查询来统计每个用户的活跃天数，并按要求进行分组和排序。
    """
    # SQL 查询实现
    query = """
    SELECT 
        activity_date AS day,
        COUNT(DISTINCT user_id) AS active_users
    FROM 
        Activity
    WHERE 
        activity_date > DATE_SUB(CURDATE(), INTERVAL 30 DAY)
    GROUP BY 
        activity_date
    ORDER BY 
        activity_date;
    """
    return query


Solution = create_solution(solution_function_name)