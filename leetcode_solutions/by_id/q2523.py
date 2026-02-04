# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2523
标题: Change Null Values in a Table to the Previous Value
难度: medium
链接: https://leetcode.cn/problems/change-null-values-in-a-table-to-the-previous-value/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2388. 将表中的空值更改为前一个值 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数 LAG 和 COALESCE 来替换空值

算法步骤:
1. 使用 LAG 函数获取每一行的前一行的值
2. 使用 COALESCE 函数将当前行的空值替换为前一行的值

关键点:
- LAG 函数用于获取前一行的值
- COALESCE 函数用于在第一个非空值中选择
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
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
    函数式接口 - 使用 SQL 查询来实现
    """
    # 实现最优解法
    query = """
    SELECT 
        id,
        COALESCE(value, prev_value) AS value
    FROM (
        SELECT 
            id, 
            value, 
            LAG(value) OVER (ORDER BY id) AS prev_value
        FROM table_name
    ) subquery
    """
    return query


Solution = create_solution(solution_function_name)