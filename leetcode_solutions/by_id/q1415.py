# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1415
标题: Students and Examinations
难度: easy
链接: https://leetcode.cn/problems/students-and-examinations/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1280. 学生们参加各科测试的次数 - 学生表: Students +---------------+---------+ | Column Name | Type | +---------------+---------+ | student_id | int | | student_name | varchar | +---------------+---------+ 在 SQL 中，主键为 student_id（学生ID）。 该表内的每一行都记录有学校一名学生的信息。 科目表: Subjects +--------------+---------+ | Column Name | Type | +--------------+---------+ | subject_name | varchar | +--------------+---------+ 在 SQL 中，主键为 subject_name（科目名称）。 每一行记录学校的一门科目名称。 考试表: Examinations +--------------+---------+ | Column Name | Type | +--------------+---------+ | student_id | int | | subject_name | varchar | +--------------+---------+ 这个表可能包含重复数据（换句话说，在 SQL 中，这个表没有主键）。 学生表里的一个学生修读科目表里的每一门科目。 这张考试表的每一行记录就表示学生表里的某个学生参加了一次科目表里某门科目的测试。 查询出每个学生参加每一门科目测试的次数，结果按 student_id 和 subject_name 排序。 查询结构格式如下所示。 示例 1： 输入： Students table: +------------+--------------+ | student_id | student_name | +------------+--------------+ | 1 | Alice | | 2 | Bob | | 13 | John | | 6 | Alex | +------------+--------------+ Subjects table: +--------------+ | subject_name | +--------------+ | Math | | Physics | | Programming | +--------------+ Examinations table: +------------+--------------+ | student_id | subject_name | +------------+--------------+ | 1 | Math | | 1 | Physics | | 1 | Programming | | 2 | Programming | | 1 | Physics | | 1 | Math | | 13 | Math | | 13 | Programming | | 13 | Physics | | 2 | Math | | 1 | Math | +------------+--------------+ 输出： +------------+--------------+--------------+----------------+ | student_id | student_name | subject_name | attended_exams | +------------+--------------+--------------+----------------+ | 1 | Alice | Math | 3 | | 1 | Alice | Physics | 2 | | 1 | Alice | Programming | 1 | | 2 | Bob | Math | 1 | | 2 | Bob | Physics | 0 | | 2 | Bob | Programming | 1 | | 6 | Alex | Math | 0 | | 6 | Alex | Physics | 0 | | 6 | Alex | Programming | 0 | | 13 | John | Math | 1 | | 13 | John | Physics | 1 | | 13 | John | Programming | 1 | +------------+--------------+--------------+----------------+ 解释： 结果表需包含所有学生和所有科目（即便测试次数为0）： Alice 参加了 3 次数学测试, 2 次物理测试，以及 1 次编程测试； Bob 参加了 1 次数学测试, 1 次编程测试，没有参加物理测试； Alex 啥测试都没参加； John 参加了数学、物理、编程测试各 1 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 使用笛卡尔积生成所有学生和所有科目的组合。
2. 对于每个组合，计算该学生参加该科目的考试次数。
3. 将结果按照 student_id 和 subject_name 排序。

算法步骤:
1. 生成所有学生和所有科目的笛卡尔积。
2. 计算每个学生在每个科目上的考试次数。
3. 将结果合并并排序。

关键点:
- 使用笛卡尔积确保所有学生和所有科目的组合都被考虑到。
- 使用聚合函数 COUNT 来计算每个学生在每个科目上的考试次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是学生数量，m 是科目数量。
空间复杂度: O(n * m)，存储所有学生和所有科目的组合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(students: List[List[str]], subjects: List[str], examinations: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 查询每个学生参加每一门科目测试的次数
    """
    from collections import defaultdict
    from itertools import product

    # 生成所有学生和所有科目的笛卡尔积
    all_combinations = list(product(students, subjects))

    # 计算每个学生在每个科目上的考试次数
    exam_count = defaultdict(int)
    for student_id, subject in examinations:
        exam_count[(student_id, subject)] += 1

    # 生成结果
    result = []
    for (student_id, student_name), subject in all_combinations:
        count = exam_count.get((student_id, subject), 0)
        result.append([student_id, student_name, subject, count])

    # 按 student_id 和 subject_name 排序
    result.sort(key=lambda x: (x[0], x[2]))

    return result


Solution = create_solution(solution_function_name)