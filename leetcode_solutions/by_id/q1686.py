# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1686
标题: Fix Product Name Format
难度: easy
链接: https://leetcode.cn/problems/fix-product-name-format/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1543. 产品名称格式修复 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来修复产品名称的格式。

算法步骤:
1. 使用 `REPLACE` 函数去除产品名称中的多余空格。
2. 使用 `TRIM` 函数去除产品名称中的前导和尾随空格。
3. 将修复后的产品名称返回。

关键点:
- 使用 `REPLACE` 和 `TRIM` 函数来处理字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n 是表中产品的数量，每个产品的名称处理时间是常数。
空间复杂度: O(1) - 不需要额外的空间，只对每个产品名称进行原地修改。
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
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)

# SQL 查询实现
def fix_product_name_format():
    """
    修复产品名称格式的 SQL 查询
    """
    query = """
    SELECT 
        TRIM(REPLACE(product_name, '  ', ' ')) AS product_name, 
        price 
    FROM 
        products;
    """
    return query

Solution = create_solution(fix_product_name_format)