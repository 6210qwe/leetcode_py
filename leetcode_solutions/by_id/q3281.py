# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3281
标题: Find Peak Calling Hours for Each City
难度: medium
链接: https://leetcode.cn/problems/find-peak-calling-hours-for-each-city/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2984. 找到每座城市的高峰通话小时 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到每座城市的高峰通话小时。

算法步骤:
1. 使用 GROUP BY 和 COUNT 函数按城市和小时分组统计通话次数。
2. 使用子查询找到每个城市的最大通话次数。
3. 再次使用 GROUP BY 和 JOIN 来找到每个城市的高峰通话小时。

关键点:
- 使用子查询来找到每个城市的最大通话次数。
- 使用 JOIN 来匹配每个城市的高峰通话小时。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log n)，其中 n 是数据表的行数。主要开销在于排序和聚合操作。
空间复杂度: O(n)，需要存储中间结果。
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
    函数式接口 - 实现 SQL 查询来找到每座城市的高峰通话小时
    """
    # SQL 查询实现
    query = """
    WITH CallCounts AS (
        SELECT city, hour, COUNT(*) as call_count
        FROM Calls
        GROUP BY city, hour
    ),
    MaxCallCounts AS (
        SELECT city, MAX(call_count) as max_call_count
        FROM CallCounts
        GROUP BY city
    )
    SELECT c.city, c.hour
    FROM CallCounts c
    JOIN MaxCallCounts m ON c.city = m.city AND c.call_count = m.max_call_count
    ORDER BY c.city, c.hour;
    """
    return query

Solution = create_solution(solution_function_name)