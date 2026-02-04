# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1154
标题: Product Sales Analysis II
难度: easy
链接: https://leetcode.cn/problems/product-sales-analysis-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1069. 产品销售分析 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来获取每个产品的销售总量。

算法步骤:
1. 使用 GROUP BY 子句按产品 ID 分组。
2. 使用 SUM 函数计算每个产品的销售总量。
3. 使用 ORDER BY 子句按产品 ID 排序。

关键点:
- 使用 SQL 的聚合函数和分组功能来高效地计算每个产品的销售总量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是销售记录的数量。GROUP BY 和 ORDER BY 操作的时间复杂度通常为 O(n log n)。
空间复杂度: O(1)，SQL 查询的额外空间复杂度通常是常数级别的。
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
    函数式接口 - 实现 SQL 查询来获取每个产品的销售总量
    """
    # 实现最优解法
    query = """
    SELECT product_id, SUM(quantity) AS total_quantity
    FROM Sales
    GROUP BY product_id
    ORDER BY product_id
    """
    return query


Solution = create_solution(solution_function_name)