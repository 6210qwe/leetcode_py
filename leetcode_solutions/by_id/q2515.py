# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2515
标题: Calculate the Influence of Each Salesperson
难度: medium
链接: https://leetcode.cn/problems/calculate-the-influence-of-each-salesperson/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2372. 计算每个销售人员的影响力 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个销售人员的影响力。

算法步骤:
1. 创建一个临时表 `sales_with_influence`，其中包含每个销售人员的销售额和影响力。
2. 在 `sales_with_influence` 表中，计算每个销售人员的总销售额和总影响力。
3. 返回最终结果。

关键点:
- 使用窗口函数 `SUM` 来计算累计销售额和累计影响力。
- 使用 `GROUP BY` 和 `ORDER BY` 来确保结果按销售人员分组并排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是销售记录的数量。因为我们需要遍历所有记录来计算累计值。
空间复杂度: O(1)，因为我们只使用了常数级的额外空间。
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
    函数式接口 - 使用 SQL 查询来计算每个销售人员的影响力
    """
    # 实现最优解法
    query = """
    WITH sales_with_influence AS (
        SELECT
            salesperson_id,
            SUM(sales_amount) OVER (PARTITION BY salesperson_id ORDER BY sale_date) AS cumulative_sales,
            SUM(influence) OVER (PARTITION BY salesperson_id ORDER BY sale_date) AS cumulative_influence
        FROM
            sales
    )
    SELECT
        salesperson_id,
        MAX(cumulative_sales) AS total_sales,
        MAX(cumulative_influence) AS total_influence
    FROM
        sales_with_influence
    GROUP BY
        salesperson_id
    ORDER BY
        salesperson_id;
    """
    return query


Solution = create_solution(solution_function_name)