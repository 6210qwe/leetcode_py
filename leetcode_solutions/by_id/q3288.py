# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3288
标题: Top Three Wineries
难度: hard
链接: https://leetcode.cn/problems/top-three-wineries/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2991. 最好的三家酒庄 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数和排序来找到评分最高的三家酒庄。

算法步骤:
1. 使用窗口函数计算每个酒庄的平均评分。
2. 按照平均评分降序排序。
3. 取前三名酒庄。

关键点:
- 使用窗口函数 `AVG` 计算每个酒庄的平均评分。
- 使用 `ROW_NUMBER` 窗口函数为每个酒庄分配一个排名。
- 选择排名前三位的酒庄。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是数据表中的行数。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，不考虑结果集的空间占用，查询本身不需要额外的空间。
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
    函数式接口 - 查询评分最高的三家酒庄
    """
    # SQL 查询实现最优解法
    query = """
    WITH WineryRatings AS (
        SELECT 
            winery_id,
            AVG(rating) AS avg_rating,
            ROW_NUMBER() OVER (ORDER BY AVG(rating) DESC) AS rank
        FROM 
            wine_ratings
        GROUP BY 
            winery_id
    )
    SELECT 
        winery_id, 
        avg_rating
    FROM 
        WineryRatings
    WHERE 
        rank <= 3
    ORDER BY 
        avg_rating DESC;
    """
    return query


Solution = create_solution(solution_function_name)