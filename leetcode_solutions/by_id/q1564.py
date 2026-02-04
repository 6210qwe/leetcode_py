# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1564
标题: Create a Session Bar Chart
难度: easy
链接: https://leetcode.cn/problems/create-a-session-bar-chart/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1435. 制作会话柱状图 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来生成会话柱状图

算法步骤:
1. 从 sessions 表中选择 session_id 和 duration 字段。
2. 按照 duration 进行分组，并计算每个分组的会话数量。
3. 将结果按照 duration 从小到大排序。

关键点:
- 使用 COUNT 函数统计每个分组的会话数量。
- 使用 GROUP BY 对 duration 进行分组。
- 使用 ORDER BY 对 duration 进行排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 sessions 表中的记录数。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，存储分组和计数结果需要 O(n) 的空间。
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
    SELECT 
        duration,
        COUNT(session_id) AS session_count
    FROM 
        sessions
    GROUP BY 
        duration
    ORDER BY 
        duration ASC
    """
    return query


Solution = create_solution(solution_function_name)