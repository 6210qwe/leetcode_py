# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1181
标题: Game Play Analysis III
难度: medium
链接: https://leetcode.cn/problems/game-play-analysis-iii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
534. 游戏玩法分析 III - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到每个玩家首次登录后的第二天再次登录的玩家数量。

算法步骤:
1. 找到每个玩家的首次登录日期。
2. 计算每个玩家首次登录后的第二天。
3. 统计在第二天再次登录的玩家数量。

关键点:
- 使用窗口函数 `ROW_NUMBER()` 来找到每个玩家的首次登录日期。
- 使用 `DATE_ADD()` 函数来计算第二天的日期。
- 使用 `INNER JOIN` 来匹配首次登录和第二天登录的记录。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是活动记录的数量。主要的时间开销在于排序和连接操作。
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
    函数式接口 - 使用 SQL 查询来找到每个玩家首次登录后的第二天再次登录的玩家数量。
    """
    # SQL 查询实现最优解法
    query = """
    WITH FirstLogin AS (
        SELECT
            player_id,
            MIN(event_date) AS first_login
        FROM
            Activity
        GROUP BY
            player_id
    ),
    SecondDayLogin AS (
        SELECT
            a.player_id,
            DATE_ADD(f.first_login, INTERVAL 1 DAY) AS second_day
        FROM
            Activity a
        INNER JOIN
            FirstLogin f ON a.player_id = f.player_id
        WHERE
            a.event_date = DATE_ADD(f.first_login, INTERVAL 1 DAY)
    )
    SELECT
        COUNT(DISTINCT player_id) AS second_day_players
    FROM
        SecondDayLogin;
    """
    return query


Solution = create_solution(solution_function_name)