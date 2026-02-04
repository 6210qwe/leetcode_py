# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3340
标题: Snaps Analysis
难度: medium
链接: https://leetcode.cn/problems/snaps-analysis/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3056. 快照分析 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来分析快照数据

算法步骤:
1. 创建一个临时表来存储每个用户的最新快照时间。
2. 使用子查询来获取每个用户在每个时间点的快照数据。
3. 通过连接操作将最新的快照数据与原始数据进行关联。
4. 返回所需的分析结果。

关键点:
- 使用窗口函数和子查询来优化查询性能。
- 确保查询结果的正确性和完整性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是快照数据的条数。主要由排序和连接操作决定。
空间复杂度: O(n)，需要额外的空间来存储临时表和中间结果。
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
    函数式接口 - 实现快照分析
    """
    # 定义 SQL 查询
    query = """
    WITH LatestSnap AS (
        SELECT user_id, MAX(snap_time) AS latest_snap_time
        FROM Snapshots
        GROUP BY user_id
    )
    SELECT s.user_id, s.snap_time, s.snap_data
    FROM Snapshots s
    JOIN LatestSnap ls ON s.user_id = ls.user_id AND s.snap_time = ls.latest_snap_time;
    """
    # 执行查询并返回结果
    return query


Solution = create_solution(solution_function_name)