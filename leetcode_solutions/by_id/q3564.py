# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3564
标题: Premier League Table Ranking II
难度: medium
链接: https://leetcode.cn/problems/premier-league-table-ranking-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3252. 英超积分榜排名 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个队伍的积分，并根据积分进行排序。

算法步骤:
1. 计算每个队伍的胜场、平局和负场。
2. 根据胜场、平局和负场计算每个队伍的积分。
3. 按照积分从高到低对队伍进行排序。

关键点:
- 使用 SQL 的 GROUP BY 和 SUM 函数来统计每个队伍的胜场、平局和负场。
- 使用 CASE WHEN 语句来计算积分。
- 使用 ORDER BY 对积分进行排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是比赛记录的数量。主要的时间开销在于排序操作。
空间复杂度: O(1)，除了存储查询结果外，不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(matches: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 实现英超积分榜排名
    """
    # 创建一个字典来存储每个队伍的胜场、平局和负场
    team_stats = {}
    
    for match in matches:
        home_team, away_team, home_score, away_score = match
        
        if home_team not in team_stats:
            team_stats[home_team] = [0, 0, 0]  # 胜, 平, 负
        if away_team not in team_stats:
            team_stats[away_team] = [0, 0, 0]  # 胜, 平, 负
        
        if home_score > away_score:
            team_stats[home_team][0] += 1  # 主队胜
            team_stats[away_team][2] += 1  # 客队负
        elif home_score < away_score:
            team_stats[away_team][0] += 1  # 客队胜
            team_stats[home_team][2] += 1  # 主队负
        else:
            team_stats[home_team][1] += 1  # 主队平
            team_stats[away_team][1] += 1  # 客队平
    
    # 计算每个队伍的积分
    team_points = []
    for team, stats in team_stats.items():
        points = stats[0] * 3 + stats[1] * 1
        team_points.append([team, points])
    
    # 按积分从高到低排序
    team_points.sort(key=lambda x: (-x[1], x[0]))
    
    # 返回排序后的队伍列表
    return [team for team, _ in team_points]


Solution = create_solution(solution_function_name)