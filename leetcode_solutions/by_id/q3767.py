# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3767
标题: Find Students Who Improved
难度: medium
链接: https://leetcode.cn/problems/find-students-who-improved/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3421. 查找进步的学生 - 表：Scores +-------------+---------+ | Column Name | Type | +-------------+---------+ | student_id | int | | subject | varchar | | score | int | | exam_date | varchar | +-------------+---------+ (student_id, subject, exam_date) 是这张表的主键。 每一行包含有关学生在特定考试日期特定科目成绩的信息。分数范围从 0 到 100（包括边界）。 编写一个解决方案来查找 进步的学生。如果 同时 满足以下两个条件，则该学生被认为是进步的： * 在 同一科目 至少参加过两个不同日期的考试。 * 他们在该学科 最近的分数 比他们 第一次该学科考试的分数更高。 返回结果表以 student_id，subject 升序 排序。 结果格式如下所示。 示例： 输入： Scores 表： +------------+----------+-------+------------+ | student_id | subject | score | exam_date | +------------+----------+-------+------------+ | 101 | Math | 70 | 2023-01-15 | | 101 | Math | 85 | 2023-02-15 | | 101 | Physics | 65 | 2023-01-15 | | 101 | Physics | 60 | 2023-02-15 | | 102 | Math | 80 | 2023-01-15 | | 102 | Math | 85 | 2023-02-15 | | 103 | Math | 90 | 2023-01-15 | | 104 | Physics | 75 | 2023-01-15 | | 104 | Physics | 85 | 2023-02-15 | +------------+----------+-------+------------+ 出： +------------+----------+-------------+--------------+ | student_id | subject | first_score | latest_score | +------------+----------+-------------+--------------+ | 101 | Math | 70 | 85 | | 102 | Math | 80 | 85 | | 104 | Physics | 75 | 85 | +------------+----------+-------------+--------------+ 解释： * 学生 101 的数学：从 70 分进步到 85 分。 * 学生 101 的物理：没有进步（从 65 分退步到 60分） * 学生 102 的数学：从 80 进步到 85 分。 * 学生 103 的数学：只有一次考试，不符合资格。 * 学生 104 的物理：从 75 分进步到 85 分。 结果表以 student_id，subject 升序排序。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用Pandas库进行数据处理和分析。

算法步骤:
1. 将输入的DataFrame按 `student_id` 和 `subject` 分组，并按 `exam_date` 升序排序。
2. 计算每个学生的每门科目的第一次和最近一次考试的成绩。
3. 筛选出满足条件的学生：在同一科目至少参加过两次考试，并且最近一次考试的成绩高于第一次考试的成绩。
4. 返回结果表并按 `student_id` 和 `subject` 升序排序。

关键点:
- 使用Pandas的groupby和sort_values方法进行数据分组和排序。
- 使用first和last方法获取每个学生的每门科目的第一次和最近一次考试的成绩。
- 使用布尔索引筛选出符合条件的学生。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中n是输入DataFrame的行数。主要的时间开销在于排序操作。
空间复杂度: O(n)，用于存储中间结果和最终结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    # 按 student_id 和 subject 分组，并按 exam_date 升序排序
    scores = scores.sort_values(by=['student_id', 'subject', 'exam_date'])
    
    # 获取每个学生的每门科目的第一次和最近一次考试的成绩
    first_scores = scores.groupby(['student_id', 'subject']).first().reset_index()
    latest_scores = scores.groupby(['student_id', 'subject']).last().reset_index()
    
    # 合并第一次和最近一次考试的成绩
    merged_scores = pd.merge(first_scores, latest_scores, on=['student_id', 'subject'], suffixes=('_first', '_latest'))
    
    # 筛选出满足条件的学生
    improved_students = merged_scores[merged_scores['score_latest'] > merged_scores['score_first']]
    
    # 选择需要的列并重命名
    result = improved_students[['student_id', 'subject', 'score_first', 'score_latest']].rename(columns={'score_first': 'first_score', 'score_latest': 'latest_score'})
    
    # 按 student_id 和 subject 升序排序
    result = result.sort_values(by=['student_id', 'subject'])
    
    return result

Solution = create_solution(find_students_who_improved)