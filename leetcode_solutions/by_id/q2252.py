# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2252
标题: The Airport With the Most Traffic
难度: medium
链接: https://leetcode.cn/problems/the-airport-with-the-most-traffic/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2112. 最繁忙的机场 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个机场的进出航班数量，并找出最繁忙的机场。

算法步骤:
1. 创建一个临时表来存储每个机场的进出航班数量。
2. 使用 UNION ALL 将出发和到达的航班数据合并到一个表中。
3. 对合并后的表进行分组并计算每个机场的航班总数。
4. 找出航班总数最多的机场。

关键点:
- 使用 UNION ALL 合并出发和到达的数据。
- 使用 GROUP BY 和 COUNT 进行分组计数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是出发航班的数量，m 是到达航班的数量。
空间复杂度: O(n + m)，用于存储合并后的数据。
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
    # 实现最优解法
    query = """
    WITH combined_flights AS (
        SELECT departure_airport AS airport FROM flights
        UNION ALL
        SELECT arrival_airport AS airport FROM flights
    )
    SELECT airport, COUNT(*) AS total_flights
    FROM combined_flights
    GROUP BY airport
    ORDER BY total_flights DESC
    LIMIT 1;
    """
    return query


Solution = create_solution(solution_function_name)