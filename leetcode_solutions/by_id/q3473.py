# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3473
标题: Calculate Parking Fees and Duration
难度: medium
链接: https://leetcode.cn/problems/calculate-parking-fees-and-duration/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3166. 计算停车费与时长 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个用户的停车费用和时长。

算法步骤:
1. 创建一个临时表来存储每个用户的停车记录，并计算每条记录的停车时长。
2. 使用 CASE WHEN 语句来根据停车时长计算停车费用。
3. 对每个用户进行分组，计算总停车费用和总停车时长。

关键点:
- 使用 DATEDIFF 函数来计算停车时长。
- 使用 CASE WHEN 语句来处理不同时间段的停车费用。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是停车记录的数量。每个记录都需要计算一次停车时长和费用。
空间复杂度: O(1)，除了输入和输出外，不需要额外的空间。
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
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)

# SQL 查询实现
def calculate_parking_fees_and_duration():
    query = """
    WITH parking_records AS (
        SELECT 
            user_id,
            start_time,
            end_time,
            DATEDIFF(end_time, start_time) AS duration
        FROM parking
    ),
    fees AS (
        SELECT 
            user_id,
            SUM(
                CASE 
                    WHEN duration <= 1 THEN 2
                    WHEN duration <= 2 THEN 3
                    WHEN duration <= 3 THEN 5
                    ELSE 7
                END
            ) AS total_fee,
            SUM(duration) AS total_duration
        FROM parking_records
        GROUP BY user_id
    )
    SELECT * FROM fees;
    """
    return query

# 使用工厂函数创建解决方案
Solution = create_solution(calculate_parking_fees_and_duration)