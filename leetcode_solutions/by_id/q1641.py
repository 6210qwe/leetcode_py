# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1641
标题: Countries You Can Safely Invest In
难度: medium
链接: https://leetcode.cn/problems/countries-you-can-safely-invest-in/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1501. 可以放心投资的国家 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找出可以放心投资的国家。

算法步骤:
1. 从表 `countries` 中选择所有国家。
2. 通过子查询检查每个国家是否在 `investments` 表中有任何高风险的投资。
3. 返回那些没有任何高风险投资的国家。

关键点:
- 使用 NOT EXISTS 子查询来过滤掉有高风险投资的国家。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 countries 表的行数，m 是 investments 表的行数。
空间复杂度: O(1)，因为只使用了常数级的额外空间。
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
    SELECT country_name
    FROM countries
    WHERE NOT EXISTS (
        SELECT 1
        FROM investments
        WHERE risk_level = 'high' AND countries.country_id = investments.country_id
    );
    """
    return query


Solution = create_solution(solution_function_name)