# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1481
标题: Students With Invalid Departments
难度: easy
链接: https://leetcode.cn/problems/students-with-invalid-departments/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1350. 院系无效的学生 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找出不在部门表中的学生。

算法步骤:
1. 从 `students` 表中选择所有学生的 `id` 和 `name`。
2. 通过 `LEFT JOIN` 将 `students` 表和 `departments` 表连接起来。
3. 筛选出 `department_id` 在 `departments` 表中不存在的记录。

关键点:
- 使用 `LEFT JOIN` 和 `IS NULL` 来筛选出无效的部门。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 `students` 表的行数，m 是 `departments` 表的行数。
空间复杂度: O(1)，查询的空间复杂度是常数级别的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(students: List[tuple], departments: List[tuple]) -> List[tuple]:
    """
    函数式接口 - 找出不在部门表中的学生

    :param students: 学生列表，每个元素为 (student_id, name, department_id)
    :param departments: 部门列表，每个元素为 (department_id, department_name)
    :return: 无效部门的学生列表，每个元素为 (student_id, name)
    """
    # 创建一个集合来存储有效的部门 ID
    valid_departments = {dept[0] for dept in departments}
    
    # 筛选出不在有效部门 ID 列表中的学生
    invalid_students = [(student[0], student[1]) for student in students if student[2] not in valid_departments]
    
    return invalid_students


Solution = create_solution(solution_function_name)