# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3283
标题: Find Third Transaction
难度: medium
链接: https://leetcode.cn/problems/find-third-transaction/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2986. 找到第三笔交易 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数 `ROW_NUMBER()` 来为每条交易记录分配一个行号，然后筛选出行号为3的记录。

算法步骤:
1. 使用 `ROW_NUMBER()` 窗口函数为每个用户的交易记录分配行号。
2. 筛选出每个用户第三笔交易的记录。

关键点:
- 使用 `PARTITION BY` 对每个用户进行分区。
- 使用 `ORDER BY` 对每个用户的交易记录按时间排序。
- 选择行号为3的记录。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 主要由排序操作决定。
空间复杂度: O(n) - 需要存储中间结果。
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
    函数式接口 - 实现找到第三笔交易
    """
    # SQL 查询实现
    query = """
    SELECT *
    FROM (
        SELECT *, ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY transaction_time) as row_num
        FROM transactions
    ) t
    WHERE t.row_num = 3
    """
    return query


Solution = create_solution(solution_function_name)