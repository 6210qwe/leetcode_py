# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2302
标题: Order Two Columns Independently
难度: medium
链接: https://leetcode.cn/problems/order-two-columns-independently/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2159. 分别排序两列 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询分别对两列进行排序，然后将结果合并。

算法步骤:
1. 对第一列进行排序。
2. 对第二列进行排序。
3. 将两个排序后的结果合并。

关键点:
- 使用 `ROW_NUMBER()` 函数为每一列生成一个行号，以便在合并时保持顺序。
- 使用 `UNION ALL` 合并两个排序后的结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是表的行数。排序操作的时间复杂度是 O(n log n)。
空间复杂度: O(n)，需要存储排序后的结果。
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
    函数式接口 - 实现最优解法
    """
    # SQL 查询实现
    query = """
    WITH ranked AS (
        SELECT score, @rank1 := @rank1 + 1 AS rank1
        FROM Scores, (SELECT @rank1 := 0) r
        ORDER BY score DESC
    ),
    ranked2 AS (
        SELECT score, @rank2 := @rank2 + 1 AS rank2
        FROM Scores, (SELECT @rank2 := 0) r
        ORDER BY score
    )
    SELECT s1.score, s1.rank1, s2.rank2
    FROM ranked s1
    JOIN ranked2 s2 ON s1.score = s2.score
    ORDER BY s1.rank1;
    """
    return query


Solution = create_solution(solution_function_name)