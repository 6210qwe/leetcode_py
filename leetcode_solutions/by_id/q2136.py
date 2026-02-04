# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2136
标题: Find Cutoff Score for Each School
难度: medium
链接: https://leetcode.cn/problems/find-cutoff-score-for-each-school/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1988. 找出每所学校的最低分数要求 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找出每所学校的最低分数要求。

算法步骤:
1. 从 `Schools` 表中获取所有学校的信息。
2. 从 `Exam` 表中获取所有考试成绩。
3. 将 `Schools` 表和 `Exam` 表进行连接，基于 `school_id` 进行匹配。
4. 对每个学校，找到其对应的最低分数要求。
5. 返回结果。

关键点:
- 使用 `LEFT JOIN` 来确保即使某个学校没有学生参加考试也能返回结果。
- 使用 `MIN` 函数来找到每个学校的最低分数要求。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 `Schools` 表的大小，m 是 `Exam` 表的大小。
空间复杂度: O(1)，查询过程中使用的额外空间是常数级别的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(schools: List[List[int]], exams: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 实现
    """
    from collections import defaultdict
    import pandas as pd

    # 将输入数据转换为 DataFrame
    schools_df = pd.DataFrame(schools, columns=['school_id', 'capacity'])
    exams_df = pd.DataFrame(exams, columns=['exam_id', 'student_id', 'score'])

    # 使用 LEFT JOIN 连接两个表
    merged_df = pd.merge(schools_df, exams_df, left_on='school_id', right_on='exam_id', how='left')

    # 按学校分组，找到每个学校的最低分数要求
    result = merged_df.groupby('school_id').agg({'score': 'min'}).reset_index()
    result.columns = ['school_id', 'cutoff_score']

    # 填充缺失值为 0（表示没有学生参加考试）
    result['cutoff_score'] = result['cutoff_score'].fillna(0)

    # 转换为列表
    result_list = result.values.tolist()

    return result_list


Solution = create_solution(solution_function_name)