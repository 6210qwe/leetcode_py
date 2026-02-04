# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1932
标题: Grand Slam Titles
难度: medium
链接: https://leetcode.cn/problems/grand-slam-titles/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1783. 大满贯数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个选手的大满贯数量。

算法步骤:
1. 创建一个临时表来存储每个选手在每个大满贯赛事中的成绩。
2. 使用 GROUP BY 和 COUNT 来统计每个选手在每个大满贯赛事中的获胜次数。
3. 最后，将结果汇总并返回。

关键点:
- 使用 UNION ALL 将多个查询结果合并。
- 使用 GROUP BY 和 COUNT 来统计每个选手的获胜次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数据表中的行数。
空间复杂度: O(1)，因为只使用了常数级的额外空间。
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
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)

# SQL 查询实现
def get_grand_slam_titles():
    query = """
    SELECT player_id, player_name, SUM(wins) AS total_wins
    FROM (
        SELECT player_id, player_name, COUNT(*) AS wins
        FROM wimbledon
        WHERE result = 'W'
        GROUP BY player_id, player_name
        UNION ALL
        SELECT player_id, player_name, COUNT(*) AS wins
        FROM us_open
        WHERE result = 'W'
        GROUP BY player_id, player_name
        UNION ALL
        SELECT player_id, player_name, COUNT(*) AS wins
        FROM french_open
        WHERE result = 'W'
        GROUP BY player_id, player_name
        UNION ALL
        SELECT player_id, player_name, COUNT(*) AS wins
        FROM australian_open
        WHERE result = 'W'
        GROUP BY player_id, player_name
    ) AS combined_results
    GROUP BY player_id, player_name
    ORDER BY total_wins DESC, player_name ASC;
    """
    return query

# 示例调用
print(get_grand_slam_titles())