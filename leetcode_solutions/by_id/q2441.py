# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2441
标题: Arrange Table by Gender
难度: medium
链接: https://leetcode.cn/problems/arrange-table-by-gender/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2308. 按性别排列表格 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来按性别排列表格。

算法步骤:
1. 创建一个临时表 `temp`，将所有男性和女性的记录分别存储在两个不同的列表中。
2. 使用 `ROW_NUMBER()` 函数为每个性别的记录分配一个唯一的行号。
3. 将两个列表合并，并按行号排序，以确保交替排列。

关键点:
- 使用 `ROW_NUMBER()` 函数为每个性别的记录分配行号。
- 使用 `UNION ALL` 合并两个列表，并按行号排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是表中的记录数。主要时间消耗在排序上。
空间复杂度: O(n)，需要存储临时表和排序后的结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(sex: str, gender: str) -> str:
    """
    函数式接口 - 实现按性别排列表格的 SQL 查询
    """
    query = f"""
    WITH temp AS (
        SELECT id, student, seat, ROW_NUMBER() OVER (ORDER BY seat) AS rn
        FROM (
            SELECT * FROM Seat WHERE sex = '{sex}'
            UNION ALL
            SELECT * FROM Seat WHERE sex = '{gender}'
        ) t
    )
    SELECT s.id, s.student
    FROM Seat s
    JOIN temp t ON s.seat = t.seat
    ORDER BY t.rn
    """
    return query


Solution = create_solution(solution_function_name)