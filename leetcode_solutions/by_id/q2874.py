# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2874
标题: Popularity Percentage
难度: hard
链接: https://leetcode.cn/problems/popularity-percentage/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2720. 受欢迎度百分比 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数计算每个用户的受欢迎度百分比。

算法步骤:
1. 使用窗口函数 `RANK()` 和 `COUNT()` 计算每个用户的排名和总用户数。
2. 计算每个用户的受欢迎度百分比。
3. 返回结果。

关键点:
- 使用窗口函数 `RANK()` 和 `COUNT()` 来计算排名和总用户数。
- 计算百分比时需要将排名转换为浮点数以避免整数除法。
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
    函数式接口 - 实现
    """
    # SQL 查询实现最优解法
    query = """
    SELECT 
        user_id,
        ROUND((RANK() OVER (ORDER BY follower_count DESC) - 1) * 100 / (COUNT(*) OVER () - 1), 2) AS popularity_percentage
    FROM 
        Users
    ORDER BY 
        popularity_percentage DESC, user_id ASC;
    """
    return query

Solution = create_solution(solution_function_name)