# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3366
标题: User Activities within Time Bounds
难度: hard
链接: https://leetcode.cn/problems/user-activities-within-time-bounds/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3060. 时间范围内的用户活动 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来筛选出在指定时间范围内的用户活动。

算法步骤:
1. 使用 `BETWEEN` 关键字来筛选出在指定时间范围内的记录。
2. 使用 `GROUP BY` 和 `COUNT` 来统计每个用户的活动次数。
3. 使用 `HAVING` 子句来过滤出活动次数大于等于指定阈值的用户。

关键点:
- 使用 `BETWEEN` 关键字来筛选时间范围。
- 使用 `GROUP BY` 和 `HAVING` 来过滤和统计用户活动。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是表中的记录数。需要遍历所有记录来进行筛选和统计。
空间复杂度: O(1)，查询本身不需要额外的空间。
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
    # 最优解法
    query = """
    SELECT user_id, COUNT(*) AS activity_count
    FROM user_activities
    WHERE activity_date BETWEEN :start_date AND :end_date
    GROUP BY user_id
    HAVING COUNT(*) >= :min_activity_count
    """
    return query


Solution = create_solution(solution_function_name)