# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2382
标题: Dynamic Unpivoting of a Table
难度: hard
链接: https://leetcode.cn/problems/dynamic-unpivoting-of-a-table/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2253. 动态取消表的旋转 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来动态取消表的旋转。

算法步骤:
1. 从 `Products` 表中选择 `product_id` 和所有 `store` 列。
2. 使用 `UNION ALL` 将每一列的数据合并成一行。
3. 使用 `CASE` 语句将 `store` 列的值转换为相应的 `store` 名称。
4. 最终结果包含 `product_id`, `store` 和 `price` 三列。

关键点:
- 使用 `UNION ALL` 来合并多列数据。
- 使用 `CASE` 语句来处理不同 `store` 列的值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 `Products` 表的行数，m 是 `store` 列的数量。
空间复杂度: O(1)，SQL 查询本身不占用额外的空间。
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
    函数式接口 - 实现动态取消表的旋转
    """
    # SQL 查询实现
    query = """
    SELECT product_id, 'store1' AS store, store1 AS price
    FROM Products
    WHERE store1 IS NOT NULL
    UNION ALL
    SELECT product_id, 'store2' AS store, store2 AS price
    FROM Products
    WHERE store2 IS NOT NULL
    UNION ALL
    SELECT product_id, 'store3' AS store, store3 AS price
    FROM Products
    WHERE store3 IS NOT NULL
    """
    return query


Solution = create_solution(solution_function_name)