# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3256
标题: Find Candidates for Data Scientist Position
难度: easy
链接: https://leetcode.cn/problems/find-candidates-for-data-scientist-position/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3051. 寻找数据科学家职位的候选人 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来筛选符合条件的数据科学家候选人。

算法步骤:
1. 选择所有具有 "Data Scientist" 职位的候选人。
2. 筛选出满足特定条件（如工作经验、教育背景等）的候选人。

关键点:
- 使用 SQL 查询来高效地筛选和过滤数据。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数据库中候选人的数量。查询操作的时间复杂度取决于数据库的索引和表的大小。
空间复杂度: O(1)，查询操作的空间复杂度主要取决于数据库引擎的实现，通常为常数级别。
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
    函数式接口 - 使用 SQL 查询来筛选数据科学家候选人
    """
    # 假设 params 包含数据库连接和其他必要的参数
    db_connection = params['db_connection']
    query = """
    SELECT *
    FROM candidates
    WHERE position = 'Data Scientist'
      AND years_of_experience >= 5
      AND education_level = 'Master';
    """
    cursor = db_connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results


Solution = create_solution(solution_function_name)