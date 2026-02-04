# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1702
标题: Bank Account Summary
难度: medium
链接: https://leetcode.cn/problems/bank-account-summary/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1555. 银行账户概要 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个用户的总存款金额，并按用户 ID 排序。

算法步骤:
1. 使用 GROUP BY 子句按用户 ID 分组。
2. 使用 SUM 函数计算每个用户的总存款金额。
3. 使用 ORDER BY 子句按用户 ID 排序。

关键点:
- 使用 GROUP BY 和 SUM 函数进行聚合操作。
- 使用 ORDER BY 进行排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是数据表的行数。GROUP BY 和 SUM 操作的时间复杂度是 O(n)，而 ORDER BY 操作的时间复杂度是 O(n log n)。
空间复杂度: O(1)，除了存储结果外，不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name():
    """
    函数式接口 - 返回 SQL 查询语句
    """
    # 实现最优解法
    query = """
    SELECT user_id, SUM(amount) AS total_amount
    FROM Transactions
    GROUP BY user_id
    ORDER BY user_id;
    """
    return query


Solution = create_solution(solution_function_name)