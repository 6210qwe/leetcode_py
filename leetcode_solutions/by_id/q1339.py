# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1339
标题: Team Scores in Football Tournament
难度: medium
链接: https://leetcode.cn/problems/team-scores-in-football-tournament/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1212. 查询球队积分 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个球队的积分。通过分析比赛结果，我们可以为每场比赛计算出胜负关系，并据此计算积分。

算法步骤:
1. 创建一个临时表 `match_results`，包含每场比赛的结果。
2. 使用 CASE 语句根据比赛结果计算每个球队的积分。
3. 对每个球队的积分进行汇总。

关键点:
- 使用 CASE 语句来处理不同的比赛结果。
- 使用 GROUP BY 和 SUM 来汇总每个球队的积分。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是比赛的数量。我们需要遍历所有比赛记录来计算积分。
空间复杂度: O(1)，除了输入和输出外，我们不需要额外的空间。
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
        team_id,
        SUM(
            CASE 
                WHEN team_id = host_team AND host_goals > guest_goals THEN 3
                WHEN team_id = host_team AND host_goals < guest_goals THEN 0
                WHEN team_id = guest_team AND host_goals < guest_goals THEN 3
                WHEN team_id = guest_team AND host_goals > guest_goals THEN 0
                ELSE 1
            END
        ) AS num_points
    FROM (
        SELECT host_team, guest_team, host_goals, guest_goals, host_team AS team_id
        FROM Matches
        UNION ALL
        SELECT host_team, guest_team, host_goals, guest_goals, guest_team AS team_id
        FROM Matches
    ) AS match_results
    GROUP BY team_id
    ORDER BY num_points DESC, team_id ASC;
    """
    return query


Solution = create_solution(solution_function_name)