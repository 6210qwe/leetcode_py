# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2185
标题: Accepted Candidates From the Interviews
难度: medium
链接: https://leetcode.cn/problems/accepted-candidates-from-the-interviews/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2041. 面试中被录取的候选人 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来获取被录取的候选人。

算法步骤:
1. 使用 INNER JOIN 将两个表连接起来，确保只保留两个表中都存在的记录。
2. 使用 WHERE 子句过滤出状态为 'accepted' 的记录。
3. 选择需要的列并返回结果。

关键点:
- 使用 INNER JOIN 和 WHERE 子句来过滤和连接数据。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是两个表的大小。JOIN 操作的时间复杂度通常与表的大小成线性关系。
空间复杂度: O(1)，查询本身不使用额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(candidates: List[str], rounds: List[str]) -> List[str]:
    """
    函数式接口 - 使用 SQL 查询来获取被录取的候选人。
    """
    # 使用 SQL 查询来获取被录取的候选人
    query = """
    SELECT c.name
    FROM candidates c
    INNER JOIN rounds r ON c.round_id = r.round_id
    WHERE r.status = 'accepted';
    """
    # 执行查询并返回结果
    # 这里假设有一个数据库连接对象 `conn` 和一个执行查询的方法 `execute_query`
    # result = execute_query(conn, query)
    # return result
    pass  # 请在实际环境中替换为具体的数据库查询执行代码


Solution = create_solution(solution_function_name)