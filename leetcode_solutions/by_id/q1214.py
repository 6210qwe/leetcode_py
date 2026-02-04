# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1214
标题: Highest Grade For Each Student
难度: medium
链接: https://leetcode.cn/problems/highest-grade-for-each-student/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1112. 每位学生的最高成绩 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来获取每位学生的最高成绩。

算法步骤:
1. 使用子查询找到每个学生每门课程的最高成绩。
2. 将结果与原始表进行连接，以获取对应的课程名称和学生成绩。
3. 返回最终结果。

关键点:
- 使用 GROUP BY 和 MAX 函数来找到每个学生每门课程的最高成绩。
- 使用 INNER JOIN 来连接子查询结果和原始表。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log n)，其中 n 是数据表中的行数。GROUP BY 和 JOIN 操作的时间复杂度通常为 O(n * log n)。
空间复杂度: O(n)，存储中间结果和最终结果所需的空间。
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
    函数式接口 - 使用 SQL 查询来获取每位学生的最高成绩
    """
    # SQL 查询实现最优解法
    query = """
    SELECT s1.student_id, s1.course_id, s1.grade
    FROM Enrollments s1
    INNER JOIN (
        SELECT student_id, course_id, MAX(grade) AS max_grade
        FROM Enrollments
        GROUP BY student_id, course_id
    ) s2
    ON s1.student_id = s2.student_id AND s1.course_id = s2.course_id AND s1.grade = s2.max_grade
    """
    return query


Solution = create_solution(solution_function_name)