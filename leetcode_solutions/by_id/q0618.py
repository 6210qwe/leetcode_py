# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 618
标题: Students Report By Geography
难度: hard
链接: https://leetcode.cn/problems/students-report-by-geography/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
618. 学生地理信息报告 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数和分组排序来生成学生报告。

算法步骤:
1. 使用窗口函数 `ROW_NUMBER()` 来为每个国家的学生按名字排序。
2. 选择需要的列并生成最终报告。

关键点:
- 使用窗口函数 `ROW_NUMBER()` 来为每个国家的学生按名字排序。
- 通过 `PARTITION BY` 和 `ORDER BY` 来确保每个国家的学生按名字排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是学生的数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，除了输入和输出外，不需要额外的空间。
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
    函数式接口 - 生成学生地理信息报告
    """
    # SQL 查询实现
    query = """
    SELECT 
        student_id, 
        student_name, 
        gender, 
        country, 
        ROW_NUMBER() OVER (PARTITION BY country ORDER BY student_name) AS row_num
    FROM 
        students
    """
    return query

Solution = create_solution(solution_function_name)