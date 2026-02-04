# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2281
标题: The Number of Passengers in Each Bus I
难度: medium
链接: https://leetcode.cn/problems/the-number-of-passengers-in-each-bus-i/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2142. 每辆车的乘客人数 I - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每辆公交车上的乘客人数。

算法步骤:
1. 创建一个临时表 `passenger_count` 来统计每个车站的上下车人数。
2. 使用窗口函数 `SUM` 来累加每个车站的上下车人数，得到每个车站的总乘客数。
3. 将结果按车站顺序排列，返回每辆公交车的乘客人数。

关键点:
- 使用窗口函数 `SUM` 来累加乘客人数。
- 确保结果按车站顺序排列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是记录的数量。SQL 查询的时间复杂度主要取决于数据量和索引情况。
空间复杂度: O(1)，查询过程中使用的额外空间是常数级别的。
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
    WITH passenger_count AS (
        SELECT
            bus_id,
            station,
            SUM(CASE WHEN status = 'in' THEN 1 ELSE 0 END) AS in_count,
            SUM(CASE WHEN status = 'out' THEN 1 ELSE 0 END) AS out_count
        FROM
            (SELECT bus_id, station, status, COUNT(*) AS count
             FROM Buses
             GROUP BY bus_id, station, status) AS subquery
        GROUP BY bus_id, station
    )
    SELECT
        bus_id,
        station,
        SUM(in_count - out_count) OVER (PARTITION BY bus_id ORDER BY station) AS passengers
    FROM
        passenger_count
    ORDER BY
        bus_id,
        station;
    """
    return query


Solution = create_solution(solution_function_name)