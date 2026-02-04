# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1862
标题: Count Apples and Oranges
难度: medium
链接: https://leetcode.cn/problems/count-apples-and-oranges/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1715. 苹果和橘子的个数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计苹果和橘子的数量。

算法步骤:
1. 创建一个 SQL 查询来统计苹果的数量。
2. 创建一个 SQL 查询来统计橘子的数量。
3. 将两个查询的结果合并并返回。

关键点:
- 使用 COUNT 函数来统计数量。
- 使用 WHERE 子句来过滤苹果和橘子。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是表中的行数。每个查询都需要遍历整个表。
空间复杂度: O(1)，查询结果只包含常数级的额外空间。
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
    函数式接口 - 使用 SQL 查询来统计苹果和橘子的数量
    """
    # 实现最优解法
    query_apples = "SELECT COUNT(*) FROM fruits WHERE type = 'apple';"
    query_oranges = "SELECT COUNT(*) FROM fruits WHERE type = 'orange';"

    # 假设我们有一个数据库连接对象 `conn` 和一个游标对象 `cursor`
    cursor = conn.cursor()

    # 执行查询
    cursor.execute(query_apples)
    apples_count = cursor.fetchone()[0]

    cursor.execute(query_oranges)
    oranges_count = cursor.fetchone()[0]

    return apples_count, oranges_count


Solution = create_solution(solution_function_name)