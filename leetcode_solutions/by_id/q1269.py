# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1269
标题: Market Analysis II
难度: hard
链接: https://leetcode.cn/problems/market-analysis-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1159. 市场分析 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来解决这个问题。我们需要找到每个产品在每个商店的销售情况，并计算出产品的平均价格。

算法步骤:
1. 创建一个临时表 `ProductPrices` 来存储每个产品在每个商店的销售情况。
2. 在 `ProductPrices` 表中计算每个产品的平均价格。
3. 返回结果。

关键点:
- 使用子查询和聚合函数来计算每个产品的平均价格。
- 确保结果按要求排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 `Products` 表的行数，m 是 `Purchases` 表的行数。
空间复杂度: O(1)，因为只使用了常数级的额外空间。
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
    函数式接口 - 实现
    """
    # SQL 查询实现
    query = """
    WITH ProductPrices AS (
        SELECT
            p.product_id,
            p.store_id,
            AVG(p.price) AS average_price
        FROM
            Products p
        JOIN
            Purchases pu ON p.product_id = pu.product_id AND p.store_id = pu.store_id
        GROUP BY
            p.product_id, p.store_id
    )
    SELECT
        product_id,
        store_id,
        average_price
    FROM
        ProductPrices
    ORDER BY
        product_id, store_id;
    """
    return query

Solution = create_solution(solution_function_name)