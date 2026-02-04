# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3961
标题: Find Students with Study Spiral Pattern
难度: hard
链接: https://leetcode.cn/problems/find-students-with-study-spiral-pattern/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3617. 查找具有螺旋学习模式的学生 - 表：students +--------------+---------+ | Column Name | Type | +--------------+---------+ | student_id | int | | student_name | varchar | | major | varchar | +--------------+---------+ student_id 是这张表的唯一主键。 每一行包含有关学生及其学术专业的信息。 表：study_sessions +---------------+---------+ | Column Name | Type | +---------------+---------+ | session_id | int | | student_id | int | | subject | varchar | | session_date | date | | hours_studied | decimal | +---------------+---------+ session_id 是这张表的唯一主键。 每一行代表一个学生针对特定学科的学习时段。 编写一个解决方案来找出遵循 螺旋学习模式 的学生——即那些持续学习多个学科并按循环周期进行学习的学生。 * 螺旋学习模式意味着学生以重复的顺序学习至少 3 个 不同的学科。 * 模式必须重复 至少 2 个完整周期（最少 6 次学习记录）。 * 两次学习记录必须是间隔不超过 2 天的 连续日期。 * 计算 循环长度（模式中不同的学科数量）。 * 计算模式中所有学习记录的 总学习时长。 * 仅包含循环长度 至少为 3 门学科 的学生。 返回结果表按循环长度 降序 排序，然后按总学习时间 降序 排序。 结果格式如下所示。 示例： 输入： students 表： +------------+--------------+------------------+ | student_id | student_name | major | +------------+--------------+------------------+ | 1 | Alice Chen | Computer Science | | 2 | Bob Johnson | Mathematics | | 3 | Carol Davis | Physics | | 4 | David Wilson | Chemistry | | 5 | Emma Brown | Biology | +------------+--------------+------------------+ study_sessions 表： +------------+------------+------------+--------------+---------------+ | session_id | student_id | subject | session_date | hours_studied | +------------+------------+------------+--------------+---------------+ | 1 | 1 | Math | 2023-10-01 | 2.5 | | 2 | 1 | Physics | 2023-10-02 | 3.0 | | 3 | 1 | Chemistry | 2023-10-03 | 2.0 | | 4 | 1 | Math | 2023-10-04 | 2.5 | | 5 | 1 | Physics | 2023-10-05 | 3.0 | | 6 | 1 | Chemistry | 2023-10-06 | 2.0 | | 7 | 2 | Algebra | 2023-10-01 | 4.0 | | 8 | 2 | Calculus | 2023-10-02 | 3.5 | | 9 | 2 | Statistics | 2023-10-03 | 2.5 | | 10 | 2 | Geometry | 2023-10-04 | 3.0 | | 11 | 2 | Algebra | 2023-10-05 | 4.0 | | 12 | 2 | Calculus | 2023-10-06 | 3.5 | | 13 | 2 | Statistics | 2023-10-07 | 2.5 | | 14 | 2 | Geometry | 2023-10-08 | 3.0 | | 15 | 3 | Biology | 2023-10-01 | 2.0 | | 16 | 3 | Chemistry | 2023-10-02 | 2.5 | | 17 | 3 | Biology | 2023-10-03 | 2.0 | | 18 | 3 | Chemistry | 2023-10-04 | 2.5 | | 19 | 4 | Organic | 2023-10-01 | 3.0 | | 20 | 4 | Physical | 2023-10-05 | 2.5 | +------------+------------+------------+--------------+---------------+ 输出： +------------+--------------+------------------+--------------+-------------------+ | student_id | student_name | major | cycle_length | total_study_hours | +------------+--------------+------------------+--------------+-------------------+ | 2 | Bob Johnson | Mathematics | 4 | 26.0 | | 1 | Alice Chen | Computer Science | 3 | 15.0 | +------------+--------------+------------------+--------------+-------------------+ 解释： * Alice Chen (student_id = 1): * 学习序列：Math → Physics → Chemistry → Math → Physics → Chemistry * 模式：3 门学科（Math，Physics，Chemistry）重复 2 个完整周期 * 连续日期：十月 1-6，没有超过 2 天的间隔 * 循环长度：3 门学科 * 总时间：2.5 + 3.0 + 2.0 + 2.5 + 3.0 + 2.0 = 15.0 小时 * Bob Johnson (student_id = 2): * 学习序列：Algebra → Calculus → Statistics → Geometry → Algebra → Calculus → Statistics → Geometry * 模式：4 门学科（Algebra，Calculus，Statistics，Geometry）重复 2 个完整周期 * 连续日期：十月 1-8，没有超过 2 天的间隔 * 循环长度：4 门学科 * 总时间：4.0 + 3.5 + 2.5 + 3.0 + 4.0 + 3.5 + 2.5 + 3.0 = 26.0 小时 * 未包含学生： * Carol Davis (student_id = 3)：仅 2 门学科（生物，化学）- 未满足至少 3 门学科的要求 * David Wilson (student_id = 4)：仅 2 次学习课程，间隔 4 天 - 不符合连续日期要求 * Emma Brown (student_id = 5)：没有记录学习课程 结果表以 cycle_length 降序排序，然后以 total_study_hours 降序排序。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 对每个学生的学习记录按日期排序。
2. 检查每个学生的记录是否满足螺旋学习模式。
3. 如果满足，计算循环长度和总学习时长，并将结果存储在列表中。
4. 最后对结果进行排序。

算法步骤:
1. 对每个学生的学习记录按日期排序。
2. 检查每个学生的记录是否满足螺旋学习模式：
   - 检查记录是否至少有 6 次学习记录。
   - 检查记录是否至少有 3 个不同学科。
   - 检查记录是否按循环模式重复至少 2 个完整周期。
   - 检查记录是否连续日期间隔不超过 2 天。
3. 如果满足，计算循环长度和总学习时长，并将结果存储在列表中。
4. 对结果进行排序，按循环长度降序排序，然后按总学习时间降序排序。

关键点:
- 使用滑动窗口检查记录是否满足螺旋学习模式。
- 使用集合检查学科是否至少有 3 个不同学科。
- 使用日期差检查记录是否连续日期间隔不超过 2 天。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是学习记录的数量。排序操作的时间复杂度为 O(n log n)，后续的遍历操作为 O(n)。
空间复杂度: O(n)，需要存储中间结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import pandas as pd
from datetime import timedelta

def find_students_with_study_spiral_pattern(students: pd.DataFrame, study_sessions: pd.DataFrame) -> pd.DataFrame:
    # 按学生 ID 和日期排序
    study_sessions = study_sessions.sort_values(by=['student_id', 'session_date']).reset_index(drop=True)
    
    result = []
    
    for student_id in study_sessions['student_id'].unique():
        student_sessions = study_sessions[study_sessions['student_id'] == student_id]
        
        if len(student_sessions) < 6:
            continue
        
        subjects = student_sessions['subject'].tolist()
        dates = student_sessions['session_date'].tolist()
        hours = student_sessions['hours_studied'].tolist()
        
        # 检查是否有至少 3 个不同学科
        if len(set(subjects)) < 3:
            continue
        
        # 检查是否按循环模式重复至少 2 个完整周期
        pattern = subjects[:3]
        if subjects != pattern * (len(subjects) // len(pattern)):
            continue
        
        # 检查是否连续日期间隔不超过 2 天
        for i in range(1, len(dates)):
            if (dates[i] - dates[i - 1]).days > 2:
                break
        else:
            # 计算循环长度和总学习时长
            cycle_length = len(pattern)
            total_study_hours = sum(hours)
            
            # 获取学生信息
            student_info = students[students['student_id'] == student_id].iloc[0]
            student_name = student_info['student_name']
            major = student_info['major']
            
            result.append({
                'student_id': student_id,
                'student_name': student_name,
                'major': major,
                'cycle_length': cycle_length,
                'total_study_hours': total_study_hours
            })
    
    # 对结果进行排序
    result_df = pd.DataFrame(result)
    result_df = result_df.sort_values(by=['cycle_length', 'total_study_hours'], ascending=[False, False])
    
    return result_df

Solution = create_solution(find_students_with_study_spiral_pattern)