# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2296
标题: The Number of Passengers in Each Bus II
难度: hard
链接: https://leetcode.cn/problems/the-number-of-passengers-in-each-bus-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2153. 每辆车的乘客人数 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每辆车上的乘客人数。

算法步骤:
1. 创建一个临时表 `buses` 来存储每辆车的出发时间和到达时间。
2. 使用窗口函数 `SUM` 和 `OVER` 来计算每个时刻的累计上车和下车人数。
3. 计算每辆车的乘客人数。

关键点:
- 使用窗口函数来处理累计上车和下车人数。
- 确保时间复杂度和空间复杂度尽可能最优。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是行程记录的数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，不考虑输出结果所需的空间。
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
    WITH buses AS (
        SELECT bus_id, arrival_time, departure_time
        FROM Buses
    ),
    events AS (
        SELECT time, SUM(delta) AS delta
        FROM (
            SELECT arrival_time AS time, capacity AS delta
            FROM Buses
            UNION ALL
            SELECT departure_time AS time, -capacity AS delta
            FROM Buses
        ) AS all_events
        GROUP BY time
    ),
    cumulative_passengers AS (
        SELECT time, SUM(delta) OVER (ORDER BY time) AS passengers
        FROM events
    )
    SELECT b.bus_id, COALESCE(c.passengers, 0) AS passengers
    FROM buses b
    LEFT JOIN cumulative_passengers c ON b.departure_time = c.time
    ORDER BY b.bus_id
    """
    return query


Solution = create_solution(solution_function_name)