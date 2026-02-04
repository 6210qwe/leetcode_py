# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3574
标题: Find Overlapping Shifts
难度: medium
链接: https://leetcode.cn/problems/find-overlapping-shifts/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3262. 查找重叠的班次 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来查找重叠的班次。通过比较班次的开始时间和结束时间来判断是否重叠。

算法步骤:
1. 创建一个临时表，包含所有班次的开始时间和结束时间。
2. 使用自连接查询，找到所有重叠的班次对。
3. 返回结果集。

关键点:
- 使用自连接来比较不同班次的时间范围。
- 确保查询条件正确地识别重叠的班次。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是班次的数量。自连接查询的时间复杂度为 O(n^2)。
空间复杂度: O(1)，查询本身不使用额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name():
    """
    函数式接口 - 使用 SQL 查询来查找重叠的班次
    """
    # SQL 查询实现最优解法
    query = """
    SELECT a.start_time AS start_time_a, a.end_time AS end_time_a, b.start_time AS start_time_b, b.end_time AS end_time_b
    FROM shifts a
    JOIN shifts b ON a.shift_id != b.shift_id
    WHERE (a.start_time < b.end_time AND a.end_time > b.start_time)
    OR (b.start_time < a.end_time AND b.end_time > a.start_time)
    """
    return query


Solution = create_solution(solution_function_name)