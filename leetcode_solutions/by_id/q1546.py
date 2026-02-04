# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1546
标题: Find the Quiet Students in All Exams
难度: hard
链接: https://leetcode.cn/problems/find-the-quiet-students-in-all-exams/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一个学生表 `student` 和一个考试成绩表 `exam`，找出在所有考试中都是安静的学生。安静的学生是指在每个考试中的排名都低于某个阈值。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来筛选出在所有考试中排名都低于某个阈值的学生。

算法步骤:
1. 计算每个学生在每场考试中的排名。
2. 筛选出在所有考试中排名都低于某个阈值的学生。

关键点:
- 使用窗口函数 `RANK()` 来计算每个学生在每场考试中的排名。
- 使用 `GROUP BY` 和 `HAVING` 子句来筛选出符合条件的学生。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m log m)，其中 n 是学生的数量，m 是考试的数量。排序操作的时间复杂度为 O(m log m)。
空间复杂度: O(n * m)，存储每个学生在每场考试中的排名。
"""

# ============================================================================
# 代码实现
# ============================================================================

def solution_function_name(student: List[List[str]], exam: List[List[str]]) -> List[str]:
    """
    函数式接口 - 找出在所有考试中都是安静的学生
    """
    import pandas as pd
    from io import StringIO
    
    # 将输入数据转换为 DataFrame
    student_df = pd.DataFrame(student, columns=['student_id', 'student_name'])
    exam_df = pd.DataFrame(exam, columns=['exam_id', 'student_id', 'score'])
    
    # 计算每个学生在每场考试中的排名
    exam_df['rank'] = exam_df.groupby('exam_id')['score'].rank(method='dense', ascending=False)
    
    # 筛选出在所有考试中排名都低于某个阈值的学生
    quiet_students = (
        exam_df
        .groupby('student_id')
        .filter(lambda x: (x['rank'] > 2).all())
        ['student_id']
        .unique()
    )
    
    # 获取这些学生的姓名
    result = student_df[student_df['student_id'].isin(quiet_students)]['student_name'].tolist()
    
    return result


Solution = create_solution(solution_function_name)