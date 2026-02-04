# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2431
标题: Products With Three or More Orders in Two Consecutive Years
难度: medium
链接: https://leetcode.cn/problems/products-with-three-or-more-orders-in-two-consecutive-years/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2292. 连续两年有 3 个及以上订单的产品 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找出连续两年有 3 个及以上订单的产品。

算法步骤:
1. 使用子查询找到每一年每个产品的订单数。
2. 使用自连接找到连续两年的订单数，并筛选出订单数大于等于 3 的产品。

关键点:
- 使用窗口函数 `LAG` 或 `LEAD` 来获取前一年或后一年的数据。
- 确保在自连接时正确处理年份和产品 ID。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是订单表的行数。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，用于存储中间结果。
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
    # 实现最优解法
    query = """
    WITH OrderCounts AS (
        SELECT 
            product_id, 
            YEAR(order_date) AS order_year, 
            COUNT(*) AS order_count
        FROM 
            Orders
        GROUP BY 
            product_id, 
            YEAR(order_date)
    ),
    ConsecutiveYears AS (
        SELECT 
            o1.product_id,
            o1.order_year AS year1,
            o2.order_year AS year2,
            o1.order_count AS count1,
            o2.order_count AS count2
        FROM 
            OrderCounts o1
        JOIN 
            OrderCounts o2
        ON 
            o1.product_id = o2.product_id AND o1.order_year + 1 = o2.order_year
    )
    SELECT DISTINCT 
        product_id
    FROM 
        ConsecutiveYears
    WHERE 
        count1 >= 3 AND count2 >= 3
    """
    return query

Solution = create_solution(solution_function_name)