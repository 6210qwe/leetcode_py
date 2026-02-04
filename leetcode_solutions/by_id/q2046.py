# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2046
标题: Page Recommendations II
难度: hard
链接: https://leetcode.cn/problems/page-recommendations-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1892. 页面推荐Ⅱ - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到用户喜欢的页面，并根据这些页面推荐新的页面。

算法步骤:
1. 创建一个临时表 `user_likes` 来存储每个用户喜欢的页面。
2. 使用 `user_likes` 表来查找与用户喜欢的页面相关的其他页面。
3. 过滤掉用户已经喜欢的页面，只推荐新的页面。

关键点:
- 使用 JOIN 和 GROUP BY 来处理相关页面的推荐。
- 确保推荐的页面是用户尚未喜欢的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是用户数量，m 是页面数量。最坏情况下需要遍历所有用户的喜欢页面和所有页面。
空间复杂度: O(n * m)，临时表 `user_likes` 可能会存储所有用户的喜欢页面。
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
    函数式接口 - 实现 SQL 查询来推荐新的页面
    """
    # SQL 查询实现最优解法
    query = """
    WITH user_likes AS (
        SELECT user_id, page_id
        FROM likes
    ),
    related_pages AS (
        SELECT l1.user_id, l2.page_id
        FROM user_likes l1
        JOIN similar_pages s ON l1.page_id = s.page1_id
        JOIN user_likes l2 ON s.page2_id = l2.page_id
        UNION
        SELECT l1.user_id, l2.page_id
        FROM user_likes l1
        JOIN similar_pages s ON l1.page_id = s.page2_id
        JOIN user_likes l2 ON s.page1_id = l2.page_id
    )
    SELECT DISTINCT r.user_id, r.page_id
    FROM related_pages r
    LEFT JOIN user_likes u ON r.user_id = u.user_id AND r.page_id = u.page_id
    WHERE u.page_id IS NULL
    ORDER BY r.user_id, r.page_id
    """
    return query


Solution = create_solution(solution_function_name)