# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1226
标题: User Purchase Platform
难度: hard
链接: https://leetcode.cn/problems/user-purchase-platform/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1127. 用户购买平台 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个用户的购买平台，并按用户 ID 排序。

算法步骤:
1. 使用 GROUP BY 和 COUNT 来统计每个用户在不同平台上的购买次数。
2. 使用 CASE WHEN 语句来标记每个用户是否在多个平台上购买。
3. 按用户 ID 排序结果。

关键点:
- 使用 GROUP BY 和 COUNT 来统计每个用户在不同平台上的购买次数。
- 使用 CASE WHEN 语句来标记每个用户是否在多个平台上购买。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log n)，其中 n 是用户购买记录的数量。排序操作的时间复杂度为 O(n * log n)。
空间复杂度: O(1)，不考虑输出结果所需的空间。
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
    函数式接口 - 实现 SQL 查询
    """
    query = """
    SELECT 
        user_id, 
        COUNT(DISTINCT platform) AS platforms, 
        CASE 
            WHEN COUNT(DISTINCT platform) > 1 THEN 'multiple' 
            ELSE 'single' 
        END AS purchase_platform
    FROM 
        Purchases
    GROUP BY 
        user_id
    ORDER BY 
        user_id
    """
    return query


Solution = create_solution(solution_function_name)