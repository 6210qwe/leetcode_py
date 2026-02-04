# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2214
标题: The Winner University
难度: easy
链接: https://leetcode.cn/problems/the-winner-university/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2072. 赢得比赛的大学 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个大学的获胜次数，并返回获胜次数最多的大学。

算法步骤:
1. 使用子查询计算每个大学的获胜次数。
2. 在外层查询中，选择获胜次数最多的大学。
3. 如果有多个大学获胜次数相同，则返回所有这些大学。

关键点:
- 使用 GROUP BY 和 COUNT 函数来统计每个大学的获胜次数。
- 使用 ORDER BY 和 LIMIT 来获取获胜次数最多的大学。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是记录的数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，查询不使用额外的空间。
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
def get_winner_university():
    query = """
    SELECT university
    FROM (
        SELECT university, COUNT(*) AS win_count
        FROM results
        WHERE result = 'W'
        GROUP BY university
    ) AS subquery
    ORDER BY win_count DESC
    LIMIT 1;
    """
    return query

# 示例调用
# print(get_winner_university())

# 修改后的 SQL 查询实现
def get_winner_universities():
    query = """
    WITH university_wins AS (
        SELECT university, COUNT(*) AS win_count
        FROM results
        WHERE result = 'W'
        GROUP BY university
    ),
    max_wins AS (
        SELECT MAX(win_count) AS max_win_count
        FROM university_wins
    )
    SELECT university
    FROM university_wins, max_wins
    WHERE university_wins.win_count = max_wins.max_win_count;
    """
    return query

# 示例调用
# print(get_winner_universities())