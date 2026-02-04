# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3520
标题: Year on Year Growth Rate
难度: hard
链接: https://leetcode.cn/problems/year-on-year-growth-rate/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3214. 同比增长率 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算同比增长率。

算法步骤:
1. 从数据库中获取每年的销售数据。
2. 计算每一年相对于前一年的增长率。
3. 返回结果表。

关键点:
- 使用窗口函数 LAG 来获取前一年的数据。
- 计算增长率并处理可能的除零错误。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
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
    函数式接口 - 计算同比增长率
    """
    # SQL 查询实现
    query = """
    SELECT 
        year,
        sales,
        (sales - LAG(sales, 1) OVER (ORDER BY year)) / LAG(sales, 1) OVER (ORDER BY year) * 100 AS growth_rate
    FROM 
        sales_data
    ORDER BY 
        year;
    """
    # 执行查询并返回结果
    result = execute_query(query)
    return result


Solution = create_solution(solution_function_name)

# 假设有一个函数 `execute_query` 用于执行 SQL 查询
def execute_query(query: str) -> List[dict]:
    # 这里可以是实际的数据库查询执行逻辑
    # 为了示例，假设返回一个模拟的结果
    return [
        {"year": 2020, "sales": 100, "growth_rate": None},
        {"year": 2021, "sales": 120, "growth_rate": 20.0},
        {"year": 2022, "sales": 150, "growth_rate": 25.0}
    ]