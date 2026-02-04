# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1439
标题: Running Total for Different Genders
难度: medium
链接: https://leetcode.cn/problems/running-total-for-different-genders/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1308. 不同性别每日分数总计 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数 OVER() 来计算每个性别的累计分数。

算法步骤:
1. 使用子查询来获取每个用户的性别和分数。
2. 使用窗口函数 SUM() OVER(PARTITION BY gender ORDER BY day) 来计算每个性别的累计分数。
3. 返回结果集。

关键点:
- 使用窗口函数可以有效地计算累计分数，避免了自连接或循环计算的复杂性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是表中的行数。排序操作的时间复杂度为 O(n log n)，窗口函数的计算时间为 O(n)。
空间复杂度: O(1)，除了输入和输出外，不使用额外的空间。
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
    函数式接口 - 使用 SQL 查询实现不同性别的每日分数总计
    """
    # 实现最优解法
    query = """
    SELECT 
        gender, 
        day, 
        SUM(score) OVER (PARTITION BY gender ORDER BY day) AS total
    FROM 
        Scores
    ORDER BY 
        gender, 
        day;
    """
    return query


Solution = create_solution(solution_function_name)