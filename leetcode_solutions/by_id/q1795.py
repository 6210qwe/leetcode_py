# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1795
标题: Hopper Company Queries III
难度: hard
链接: https://leetcode.cn/problems/hopper-company-queries-iii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1651. Hopper 公司查询 III - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: SQL查询，使用窗口函数计算移动平均

算法步骤:
1. 使用窗口函数计算3个月的平均值
2. 过滤2020年的数据
3. 按月份排序

关键点:
- SQL窗口函数
- ROWS BETWEEN
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 数据库查询
空间复杂度: O(n) - 查询结果
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def hopper_company_queries_iii():
    """
    函数式接口 - Hopper 公司查询 III
    
    实现思路:
    SQL查询：使用窗口函数计算移动平均。
    
    Returns:
        SQL查询字符串
        
    Example:
        >>> sql = hopper_company_queries_iii()
    """
    sql = """
    SELECT 
        month,
        ROUND(AVG(ride_distance) OVER (
            ORDER BY month 
            ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING
        ), 2) AS average_ride_distance,
        ROUND(AVG(ride_duration) OVER (
            ORDER BY month 
            ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING
        ), 2) AS average_ride_duration
    FROM (
        SELECT 
            MONTH(requested_at) AS month,
            ride_distance,
            ride_duration
        FROM Rides r
        JOIN AcceptedRides a ON r.ride_id = a.ride_id
        WHERE YEAR(requested_at) = 2020
    ) t
    ORDER BY month
    LIMIT 10
    """
    return sql


Solution = create_solution(hopper_company_queries_iii)
