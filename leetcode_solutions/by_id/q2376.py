# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2376
标题: Number of Times a Driver Was a Passenger
难度: medium
链接: https://leetcode.cn/problems/number-of-times-a-driver-was-a-passenger/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2376. 司机成为乘客的次数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个司机作为乘客的次数。

算法步骤:
1. 创建一个临时表 `rides`，包含所有行程记录。
2. 使用子查询和 GROUP BY 来统计每个司机作为乘客的次数。
3. 返回结果集。

关键点:
- 使用 JOIN 和 GROUP BY 来统计每个司机作为乘客的次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是行程记录的数量。GROUP BY 操作的时间复杂度通常为 O(n log n)。
空间复杂度: O(1)，除了输入和输出外，不使用额外的空间。
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
    函数式接口 - 使用 SQL 查询来统计每个司机作为乘客的次数
    """
    # 实现最优解法
    query = """
    SELECT 
        driver_id, 
        COUNT(*) AS passenger_count
    FROM (
        SELECT 
            ride_id, 
            driver_id, 
            passenger_id
        FROM Rides
        UNION ALL
        SELECT 
            ride_id, 
            passenger_id AS driver_id, 
            driver_id AS passenger_id
        FROM Rides
    ) AS rides
    WHERE driver_id IN (SELECT DISTINCT driver_id FROM Rides)
    GROUP BY driver_id
    ORDER BY driver_id
    """
    return query

Solution = create_solution(solution_function_name)