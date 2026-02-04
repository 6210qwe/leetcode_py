# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3440
标题: Server Utilization Time
难度: medium
链接: https://leetcode.cn/problems/server-utilization-time/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3126. 服务器利用时间 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个服务器的利用时间。

算法步骤:
1. 计算每个服务器的开始时间和结束时间。
2. 使用窗口函数计算每个服务器的利用时间。
3. 返回结果。

关键点:
- 使用窗口函数来计算每个服务器的利用时间。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是记录的数量。
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
    函数式接口 - 实现最优解法
    """
    # SQL 查询实现
    query = """
    SELECT 
        server_id, 
        ROUND(SUM(end_time - start_time) / COUNT(DISTINCT request_id), 3) AS utilization_time
    FROM 
        (
            SELECT 
                server_id, 
                request_id, 
                MIN(event_time) AS start_time, 
                MAX(event_time) AS end_time
            FROM 
                Activity
            GROUP BY 
                server_id, 
                request_id
        ) AS subquery
    GROUP BY 
        server_id;
    """
    return query


Solution = create_solution(solution_function_name)