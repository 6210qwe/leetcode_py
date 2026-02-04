# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2452
标题: Product Sales Analysis V
难度: easy
链接: https://leetcode.cn/problems/product-sales-analysis-v/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2329. 产品销售分析Ⅴ - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来获取每个产品的总销售额，并按销售额降序排列。

算法步骤:
1. 使用 `GROUP BY` 子句按产品 ID 分组。
2. 使用 `SUM` 函数计算每个产品的总销售额。
3. 使用 `ORDER BY` 子句按总销售额降序排列。

关键点:
- 使用 `GROUP BY` 和 `SUM` 函数来聚合数据。
- 使用 `ORDER BY` 来排序结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是销售记录的数量。`GROUP BY` 操作的时间复杂度是 O(n)，而 `ORDER BY` 操作的时间复杂度是 O(n log n)。
空间复杂度: O(1)，不考虑输出结果的空间占用。
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
    函数式接口 - 使用 SQL 查询来获取每个产品的总销售额，并按销售额降序排列。
    """
    # 实现最优解法
    query = """
    SELECT product_id, SUM(quantity * price) AS total_sales
    FROM Sales
    GROUP BY product_id
    ORDER BY total_sales DESC;
    """
    return query


Solution = create_solution(solution_function_name)