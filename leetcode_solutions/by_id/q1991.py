# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1991
标题: League Statistics
难度: medium
链接: https://leetcode.cn/problems/league-statistics/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1841. 联赛信息统计 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计联赛信息

算法步骤:
1. 计算每个队伍的总得分
2. 计算每个队伍的总进球数和失球数
3. 将结果按要求格式化输出

关键点:
- 使用聚合函数 SUM 和 GROUP BY 来计算每个队伍的统计数据
- 使用 CASE WHEN 语句来处理不同的情况
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是比赛记录的数量
空间复杂度: O(1)，因为只使用了常数级的额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(matches: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 统计联赛信息
    """
    from collections import defaultdict

    # 初始化统计字典
    team_stats = defaultdict(lambda: {"points": 0, "goal_diff": 0, "goals_for": 0, "goals_against": 0})

    # 遍历每场比赛记录
    for match in matches:
        home_team, away_team, home_score, away_score = match[0], match[1], int(match[2]), int(match[3])

        if home_score > away_score:
            team_stats[home_team]["points"] += 3
        elif home_score < away_score:
            team_stats[away_team]["points"] += 3
        else:
            team_stats[home_team]["points"] += 1
            team_stats[away_team]["points"] += 1

        team_stats[home_team]["goals_for"] += home_score
        team_stats[home_team]["goals_against"] += away_score
        team_stats[away_team]["goals_for"] += away_score
        team_stats[away_team]["goals_against"] += home_score

        team_stats[home_team]["goal_diff"] = team_stats[home_team]["goals_for"] - team_stats[home_team]["goals_against"]
        team_stats[away_team]["goal_diff"] = team_stats[away_team]["goals_for"] - team_stats[away_team]["goals_against"]

    # 按照积分、净胜球、进球数排序
    sorted_teams = sorted(team_stats.items(), key=lambda x: (-x[1]["points"], -x[1]["goal_diff"], -x[1]["goals_for"]))

    # 构建结果列表
    result = []
    for team, stats in sorted_teams:
        result.append([team, str(stats["points"]), str(stats["goal_diff"]), str(stats["goals_for"]), str(stats["goals_against"])])

    return result


Solution = create_solution(solution_function_name)