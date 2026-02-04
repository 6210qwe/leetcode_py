# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1377
标题: Number of Comments per Post
难度: easy
链接: https://leetcode.cn/problems/number-of-comments-per-post/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1241. 每个帖子的评论数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个帖子的评论数。

算法步骤:
1. 创建一个子查询来获取所有评论的帖子 ID。
2. 使用 COUNT 函数和 GROUP BY 子句来统计每个帖子的评论数。
3. 将结果与帖子表进行左连接，以确保即使没有评论的帖子也能显示。

关键点:
- 使用 LEFT JOIN 确保所有帖子都包含在结果中。
- 使用 COUNT 和 GROUP BY 来统计评论数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是评论表的行数，m 是帖子表的行数。
空间复杂度: O(m)，用于存储结果集。
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
    函数式接口 - 使用 SQL 查询来统计每个帖子的评论数
    """
    # 实现最优解法
    query = """
    SELECT p.post_id, COALESCE(c.comment_count, 0) AS number_of_comments
    FROM Posts p
    LEFT JOIN (
        SELECT post_id, COUNT(*) AS comment_count
        FROM Comments
        GROUP BY post_id
    ) c ON p.post_id = c.post_id;
    """
    return query


Solution = create_solution(solution_function_name)