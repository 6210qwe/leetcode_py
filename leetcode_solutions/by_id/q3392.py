# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3392
标题: Find Trending Hashtags
难度: medium
链接: https://leetcode.cn/problems/find-trending-hashtags/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3087. 查找热门话题标签 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个话题标签的出现次数，并按降序排序。

算法步骤:
1. 使用 `GROUP BY` 和 `COUNT` 来统计每个话题标签的出现次数。
2. 使用 `ORDER BY` 按出现次数降序排序。
3. 选择前 N 个热门话题标签。

关键点:
- 使用 `GROUP BY` 和 `COUNT` 来统计每个话题标签的出现次数。
- 使用 `ORDER BY` 进行排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是数据表中的记录数。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，存储中间结果和最终结果所需的空间。
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
    函数式接口 - 实现查找热门话题标签
    """
    # SQL 查询语句
    query = """
    SELECT hashtag, COUNT(*) as count
    FROM posts
    GROUP BY hashtag
    ORDER BY count DESC
    LIMIT %s;
    """
    # 执行查询并返回结果
    # 假设 params 包含一个数据库连接对象 conn 和一个整数 N
    conn, N = params
    cursor = conn.cursor()
    cursor.execute(query, (N,))
    results = cursor.fetchall()
    return [row[0] for row in results]


Solution = create_solution(solution_function_name)