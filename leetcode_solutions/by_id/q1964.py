# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1964
标题: Find Interview Candidates
难度: medium
链接: https://leetcode.cn/problems/find-interview-candidates/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1811. 寻找面试候选人 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到符合条件的候选人。

算法步骤:
1. 从 `Candidates` 表中选择所有满足条件的记录。
2. 使用 `GROUP BY` 和 `HAVING` 子句来过滤出符合条件的候选人。

关键点:
- 使用 `GROUP BY` 和 `HAVING` 子句来过滤数据。
- 确保查询语句的性能优化。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 `Candidates` 表中的记录数。
空间复杂度: O(1)，因为只使用了常数级的额外空间。
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
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass

# 由于这是一道数据库题目，我们直接提供 SQL 查询语句
sql_query = """
SELECT candidate_id
FROM Candidates
WHERE years_of_exp >= 2
  AND interview_id IN (
    SELECT interview_id
    FROM Rounds
    GROUP BY interview_id
    HAVING SUM(score) > 15
  )
"""

Solution = create_solution(sql_query)