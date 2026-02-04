# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3160
标题: Calculate Orders Within Each Interval
难度: medium
链接: https://leetcode.cn/problems/calculate-orders-within-each-interval/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2893. 计算每个区间内的订单 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个区间内的订单数量。

算法步骤:
1. 创建一个临时表 `intervals` 来存储所有的时间区间。
2. 使用 `UNION ALL` 将 `Orders` 表中的订单时间与 `intervals` 表中的区间进行连接。
3. 使用 `BETWEEN` 关键字来判断订单时间是否在区间内。
4. 对每个区间进行分组，并计算每个区间的订单数量。

关键点:
- 使用 `UNION ALL` 来生成所有可能的区间组合。
- 使用 `BETWEEN` 来判断订单时间是否在区间内。
- 使用 `GROUP BY` 和 `COUNT` 来统计每个区间的订单数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 `Orders` 表的行数，m 是 `intervals` 表的行数。
空间复杂度: O(1)，因为只使用了常数级的额外空间。
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
    函数式接口 - 实现 SQL 查询来计算每个区间内的订单数量
    """
    # 定义 SQL 查询
    query = """
    WITH intervals AS (
        SELECT start, end FROM Intervals
    )
    SELECT 
        i.start, 
        i.end, 
        COUNT(o.order_id) AS order_count
    FROM 
        intervals i
    LEFT JOIN 
        Orders o ON o.order_date BETWEEN i.start AND i.end
    GROUP BY 
        i.start, i.end
    ORDER BY 
        i.start, i.end;
    """
    # 执行查询并返回结果
    return query

Solution = create_solution(solution_function_name)