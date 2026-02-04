# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1074
标题: High Five
难度: easy
链接: https://leetcode.cn/problems/high-five/
题目类型: 数组、哈希表、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1086. 前五科的均分 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储每个学生的成绩，然后对每个学生的成绩进行排序，取前五名计算平均分。

算法步骤:
1. 使用一个字典来存储每个学生的成绩列表。
2. 遍历输入的成绩列表，将每个学生的成绩添加到对应的列表中。
3. 对每个学生的成绩列表进行排序，取前五名的成绩并计算平均分。
4. 返回结果列表。

关键点:
- 使用字典来存储每个学生的成绩列表。
- 对每个学生的成绩列表进行排序并取前五名。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log n)，其中 n 是成绩的数量。因为我们需要对每个学生的成绩列表进行排序。
空间复杂度: O(n)，存储所有学生的成绩列表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def highFive(items: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 计算每个学生的前五科成绩的平均分
    """
    # 使用字典存储每个学生的成绩列表
    student_scores = {}
    
    # 遍历输入的成绩列表，将每个学生的成绩添加到对应的列表中
    for student_id, score in items:
        if student_id not in student_scores:
            student_scores[student_id] = []
        student_scores[student_id].append(score)
    
    # 对每个学生的成绩列表进行排序，取前五名的成绩并计算平均分
    result = []
    for student_id, scores in student_scores.items():
        top_five_scores = sorted(scores, reverse=True)[:5]
        average_score = sum(top_five_scores) // 5
        result.append([student_id, average_score])
    
    # 按学生ID排序
    result.sort(key=lambda x: x[0])
    
    return result


Solution = create_solution(highFive)