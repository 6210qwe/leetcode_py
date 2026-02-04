# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2315
标题: The Change in Global Rankings
难度: medium
链接: https://leetcode.cn/problems/the-change-in-global-rankings/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2175. 世界排名的变化 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数和自连接来计算排名变化

算法步骤:
1. 使用窗口函数 `RANK()` 计算每个国家在两个不同年份的排名。
2. 通过自连接将两个年份的排名表连接起来，计算排名变化。
3. 过滤出排名变化大于或等于上升位数的国家。

关键点:
- 使用窗口函数 `RANK()` 来计算排名。
- 使用自连接来比较不同年份的排名。
- 过滤出符合条件的国家。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是数据表中的行数。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，存储中间结果所需的空间。
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
    # SQL 查询实现
    query = """
    WITH Rank2019 AS (
        SELECT country, RANK() OVER (ORDER BY score DESC) as rank
        FROM World
        WHERE year = 2019
    ),
    Rank2020 AS (
        SELECT country, RANK() OVER (ORDER BY score DESC) as rank
        FROM World
        WHERE year = 2020
    )
    SELECT r2020.country, r2020.rank - r2019.rank as rank_change
    FROM Rank2019 r2019
    JOIN Rank2020 r2020 ON r2019.country = r2020.country
    WHERE r2020.rank - r2019.rank >= :rank_change
    ORDER BY rank_change DESC, r2020.country
    """
    return query

Solution = create_solution(solution_function_name)