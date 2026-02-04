# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3002
标题: Flight Occupancy and Waitlist Analysis
难度: medium
链接: https://leetcode.cn/problems/flight-occupancy-and-waitlist-analysis/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2783. 航班入座率和等待名单分析 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个航班的入座率和等待名单人数。

算法步骤:
1. 计算每个航班的总座位数。
2. 计算每个航班的已预订座位数。
3. 计算每个航班的等待名单人数。
4. 计算每个航班的入座率。
5. 返回结果表。

关键点:
- 使用聚合函数 SUM 和 COUNT 来计算所需的数值。
- 使用 CASE WHEN 语句来处理不同的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数据表中的行数。我们需要遍历整个数据表来进行聚合操作。
空间复杂度: O(1)，我们只使用了常数级的额外空间。
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
    函数式接口 - 实现最优解法
    """
    # SQL 查询实现
    query = """
    SELECT 
        f.flight_id,
        (f.seats - COALESCE(SUM(b.seat_number), 0)) AS remaining_seats,
        COALESCE(COUNT(w.waitlist_id), 0) AS waitlist_count,
        (COALESCE(SUM(b.seat_number), 0) / f.seats) * 100 AS occupancy_percentage
    FROM 
        Flights f
    LEFT JOIN 
        Bookings b ON f.flight_id = b.flight_id
    LEFT JOIN 
        Waitlist w ON f.flight_id = w.flight_id
    GROUP BY 
        f.flight_id, f.seats
    ORDER BY 
        f.flight_id;
    """
    return query

Solution = create_solution(solution_function_name)