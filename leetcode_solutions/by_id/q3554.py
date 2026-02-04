# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3554
标题: Premier League Table Ranking
难度: easy
链接: https://leetcode.cn/problems/premier-league-table-ranking/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3246. 英超积分榜排名 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个球队的积分，并按积分进行排序。

算法步骤:
1. 计算每个球队的胜场数、平局数和负场数。
2. 根据胜场数、平局数和负场数计算每个球队的积分。
3. 按积分从高到低对球队进行排序。
4. 如果积分相同，则按净胜球数进行排序。
5. 如果净胜球数也相同，则按球队名称进行排序。

关键点:
- 使用 SQL 的 GROUP BY 和 SUM 函数来计算每个球队的胜场数、平局数和负场数。
- 使用 CASE WHEN 语句来计算积分。
- 使用 ORDER BY 语句来进行多条件排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是比赛记录的数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，除了输入和输出外，不需要额外的空间。
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
    # SQL 查询实现最优解法
    query = """
    SELECT 
        team_name,
        SUM(CASE WHEN result = 'win' THEN 1 ELSE 0 END) AS wins,
        SUM(CASE WHEN result = 'draw' THEN 1 ELSE 0 END) AS draws,
        SUM(CASE WHEN result = 'lose' THEN 1 ELSE 0 END) AS loses,
        SUM(CASE WHEN result = 'win' THEN 3 ELSE 0 END) + SUM(CASE WHEN result = 'draw' THEN 1 ELSE 0 END) AS points
    FROM 
        Matches
    GROUP BY 
        team_name
    ORDER BY 
        points DESC, (wins - loses) DESC, team_name ASC;
    """
    return query


Solution = create_solution(solution_function_name)