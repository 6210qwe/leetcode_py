# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1173
标题: Sales Analysis II
难度: easy
链接: https://leetcode.cn/problems/sales-analysis-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1083. 销售分析 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到每个产品在每个商店的销售日期和数量。

算法步骤:
1. 从 `Product` 表中选择所有列。
2. 从 `Sales` 表中选择 `store`, `sale_date`, 和 `total` 列。
3. 使用 `INNER JOIN` 将 `Product` 表和 `Sales` 表连接起来，条件是 `product_id` 相同。
4. 按照 `product_name`, `store`, `sale_date` 排序结果。

关键点:
- 使用 `INNER JOIN` 来连接两个表。
- 确保查询结果按要求排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 `Sales` 表的行数。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，不考虑输出结果的空间消耗。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name():
    """
    函数式接口 - 实现 SQL 查询
    """
    query = """
    SELECT p.product_name, s.store, s.sale_date, s.total
    FROM Product p
    INNER JOIN Sales s ON p.product_id = s.product_id
    ORDER BY p.product_name, s.store, s.sale_date;
    """
    return query


Solution = create_solution(solution_function_name)