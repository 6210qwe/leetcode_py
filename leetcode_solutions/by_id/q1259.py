# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1259
标题: Article Views II
难度: medium
链接: https://leetcode.cn/problems/article-views-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1149. 文章浏览 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个作者的文章浏览量。

算法步骤:
1. 使用 GROUP BY 子句按 author_id 分组。
2. 使用 COUNT 函数计算每个作者的文章浏览量。
3. 返回结果集。

关键点:
- 使用 GROUP BY 和 COUNT 函数进行分组和计数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 views 表的行数。需要遍历整个表来进行分组和计数。
空间复杂度: O(1)，除了返回的结果集外，不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(views: List[List[str]]) -> List[List[int]]:
    """
    函数式接口 - 统计每个作者的文章浏览量
    """
    from collections import defaultdict

    # 使用字典来存储每个作者的文章浏览量
    author_views = defaultdict(int)

    # 遍历 views 表，统计每个作者的文章浏览量
    for view in views:
        author_id, article_id = int(view[0]), int(view[1])
        author_views[author_id] += 1

    # 将结果转换为列表
    result = [[author_id, count] for author_id, count in author_views.items()]

    return result


Solution = create_solution(solution_function_name)