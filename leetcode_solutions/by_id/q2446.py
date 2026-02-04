# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2446
标题: The First Day of the Maximum Recorded Degree in Each City
难度: medium
链接: https://leetcode.cn/problems/the-first-day-of-the-maximum-recorded-degree-in-each-city/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2314. 每个城市最高气温的第一天 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到每个城市最高气温出现的第一天。

算法步骤:
1. 使用子查询找到每个城市的最高气温。
2. 使用主查询找到每个城市最高气温出现的第一天。

关键点:
- 使用 GROUP BY 和 MAX 函数来找到每个城市的最高气温。
- 使用 WHERE 子句和 MIN 函数来找到每个城市最高气温出现的第一天。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是记录的数量。因为我们需要对数据进行分组和排序操作。
空间复杂度: O(n)，存储中间结果的空间复杂度。
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
    WITH MaxTemp AS (
        SELECT city, MAX(recordDate) AS max_date, MAX(temperature) AS max_temp
        FROM Weather
        GROUP BY city
    )
    SELECT w.city, MIN(w.recordDate) AS first_day
    FROM Weather w
    JOIN MaxTemp mt ON w.city = mt.city AND w.temperature = mt.max_temp
    GROUP BY w.city;
    """
    return query


Solution = create_solution(solution_function_name)