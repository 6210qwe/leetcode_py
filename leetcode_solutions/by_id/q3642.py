# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3642
标题: Premier League Table Ranking III
难度: medium
链接: https://leetcode.cn/problems/premier-league-table-ranking-iii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3322. 英超积分榜排名 III - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个球队的积分、胜场、平局和负场，并按积分降序排列。

算法步骤:
1. 计算每个球队的胜场、平局和负场。
2. 计算每个球队的积分（胜场 * 3 + 平局 * 1）。
3. 按积分降序排列球队。
4. 如果积分相同，按净胜球数降序排列。
5. 如果净胜球数相同，按进球数降序排列。
6. 如果进球数相同，按球队名称升序排列。

关键点:
- 使用 SQL 的 GROUP BY 和 JOIN 来聚合数据。
- 使用 CASE WHEN 语句来计算胜场、平局和负场。
- 使用 ORDER BY 子句来排序结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是比赛记录的数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，不使用额外的空间，只使用常数级的额外空间。
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
    函数式接口 - 实现英超积分榜排名
    """
    # 实现最优解法
    query = """
    SELECT 
        team_name,
        SUM(CASE WHEN team_goals > opponent_goals THEN 1 ELSE 0 END) AS wins,
        SUM(CASE WHEN team_goals = opponent_goals THEN 1 ELSE 0 END) AS draws,
        SUM(CASE WHEN team_goals < opponent_goals THEN 1 ELSE 0 END) AS losses,
        (SUM(CASE WHEN team_goals > opponent_goals THEN 1 ELSE 0 END) * 3 + SUM(CASE WHEN team_goals = opponent_goals THEN 1 ELSE 0 END)) AS points,
        SUM(team_goals) AS goals_for,
        SUM(opponent_goals) AS goals_against,
        (SUM(team_goals) - SUM(opponent_goals)) AS goal_difference
    FROM 
        Matches
    JOIN 
        Teams ON Matches.team_id = Teams.team_id
    GROUP BY 
        team_name
    ORDER BY 
        points DESC, 
        goal_difference DESC, 
        goals_for DESC, 
        team_name ASC
    """
    return query

Solution = create_solution(solution_function_name)