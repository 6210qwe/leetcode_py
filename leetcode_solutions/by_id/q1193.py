# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1193
标题: Game Play Analysis V
难度: hard
链接: https://leetcode.cn/problems/game-play-analysis-v/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1097. 游戏玩法分析 V - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到每个玩家的首次活动日期，并计算每个玩家在首次活动后的第二天仍然活跃的玩家数量。

算法步骤:
1. 找到每个玩家的首次活动日期。
2. 过滤出那些在首次活动后的第二天仍然有活动记录的玩家。
3. 计算这些玩家的数量。

关键点:
- 使用窗口函数 `MIN` 来找到每个玩家的首次活动日期。
- 使用 `DATEDIFF` 函数来计算日期差。
- 使用 `GROUP BY` 和 `COUNT` 来统计满足条件的玩家数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 `Activity` 表的行数。主要的时间开销在于排序和分组操作。
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
    函数式接口 - 实现
    """
    # 实现最优解法
    query = """
    SELECT COUNT(DISTINCT player_id) AS active_players
    FROM (
        SELECT player_id, MIN(event_date) AS first_login
        FROM Activity
        GROUP BY player_id
    ) AS FirstLogin
    JOIN Activity AS A
    ON FirstLogin.player_id = A.player_id AND DATEDIFF(A.event_date, FirstLogin.first_login) = 1
    """
    return query


Solution = create_solution(solution_function_name)