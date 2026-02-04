# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3589
标题: Find Candidates for Data Scientist Position II
难度: medium
链接: https://leetcode.cn/problems/find-candidates-for-data-scientist-position-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3278. 寻找数据科学家职位的候选人 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来筛选符合条件的数据科学家候选人。

算法步骤:
1. 筛选出具有数据科学相关经验的候选人。
2. 确保候选人具有至少 3 年的相关工作经验。
3. 按照候选人的总评分进行排序，返回评分最高的前 5 名候选人。

关键点:
- 使用 INNER JOIN 来连接多个表，确保数据的一致性。
- 使用 WHERE 子句来过滤符合条件的候选人。
- 使用 ORDER BY 和 LIMIT 来获取评分最高的前 5 名候选人。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是候选人的数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，查询过程中不使用额外的空间。
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
    函数式接口 - 实现最优解法
    """
    # SQL 查询实现
    query = """
    SELECT c.id, c.name, SUM(e.experience_years) AS total_experience, AVG(c.score) AS average_score
    FROM candidates c
    INNER JOIN experiences e ON c.id = e.candidate_id
    WHERE e.role LIKE '%Data Scientist%' AND e.experience_years >= 3
    GROUP BY c.id, c.name
    ORDER BY average_score DESC
    LIMIT 5;
    """
    # 返回查询结果
    return query


Solution = create_solution(solution_function_name)