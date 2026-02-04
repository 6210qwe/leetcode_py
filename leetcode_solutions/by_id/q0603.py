# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 603
标题: Consecutive Available Seats
难度: easy
链接: https://leetcode.cn/problems/consecutive-available-seats/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
603. 连续空余座位 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找出连续的空余座位。

算法步骤:
1. 从 `cinema` 表中选择所有行，并按座位编号排序。
2. 使用窗口函数 `LAG` 和 `LEAD` 来获取当前行的前一行和后一行的座位状态。
3. 筛选出当前座位为空且前一个座位或后一个座位也为空的行。
4. 返回这些行的座位编号。

关键点:
- 使用窗口函数 `LAG` 和 `LEAD` 来处理相邻行的数据。
- 确保筛选出的座位是连续的空座位。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 `cinema` 表中的行数。主要的时间开销在于排序操作。
空间复杂度: O(1)，查询过程中只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(cinema):
    """
    函数式接口 - 实现 SQL 查询来找出连续的空余座位
    """
    query = """
    SELECT seat_id
    FROM (
        SELECT 
            seat_id,
            seat_status,
            LAG(seat_status, 1) OVER (ORDER BY seat_id) AS prev_seat_status,
            LEAD(seat_status, 1) OVER (ORDER BY seat_id) AS next_seat_status
        FROM cinema
    ) AS subquery
    WHERE seat_status = 'empty' AND (prev_seat_status = 'empty' OR next_seat_status = 'empty')
    ORDER BY seat_id
    """
    return query


Solution = create_solution(solution_function_name)