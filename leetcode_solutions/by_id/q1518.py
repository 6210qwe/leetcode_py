# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1518
标题: Total Sales Amount by Year
难度: hard
链接: https://leetcode.cn/problems/total-sales-amount-by-year/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1384. 按年度列出销售总额 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来按年度汇总销售总额

算法步骤:
1. 从 `Sales` 表中选择 `sale_date` 和 `amount` 列。
2. 使用 `DATE_FORMAT` 函数将 `sale_date` 转换为年份格式。
3. 按年份分组并计算每一年的销售总额。

关键点:
- 使用 `DATE_FORMAT` 函数提取年份
- 使用 `GROUP BY` 子句按年份分组
- 使用 `SUM` 函数计算每一年的销售总额
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 `Sales` 表中的行数
空间复杂度: O(1)，不考虑结果集占用的空间
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
    # 实现最优解法
    query = """
    SELECT 
        DATE_FORMAT(sale_date, '%Y') AS sale_year,
        SUM(amount) AS total_amount
    FROM 
        Sales
    GROUP BY 
        sale_year
    ORDER BY 
        sale_year;
    """
    return query


Solution = create_solution(solution_function_name)