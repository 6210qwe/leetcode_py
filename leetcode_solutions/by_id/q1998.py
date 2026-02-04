# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1998
标题: Suspicious Bank Accounts
难度: medium
链接: https://leetcode.cn/problems/suspicious-bank-accounts/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1843. 可疑银行账户 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找出可疑的银行账户。

算法步骤:
1. 创建一个临时表 `transactions` 来存储所有交易记录。
2. 使用子查询和聚合函数来计算每个账户的总存款和总取款。
3. 筛选出总存款大于总取款的账户，并且总存款超过某个阈值（例如 10000）。
4. 返回这些可疑账户的列表。

关键点:
- 使用 SQL 的 GROUP BY 和 HAVING 子句来过滤出符合条件的账户。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 其中 n 是交易记录的数量。我们需要遍历所有交易记录来进行聚合操作。
空间复杂度: O(1) - 除了输入和输出外，我们只使用了常数级的额外空间。
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
    函数式接口 - 使用 SQL 查询来找出可疑的银行账户
    """
    # SQL 查询语句
    query = """
    WITH transactions AS (
        SELECT account_id, SUM(amount) AS total_deposit
        FROM Transactions
        WHERE type = 'Deposit'
        GROUP BY account_id
    ),
    withdrawals AS (
        SELECT account_id, SUM(amount) AS total_withdrawal
        FROM Transactions
        WHERE type = 'Withdraw'
        GROUP BY account_id
    )
    SELECT t.account_id
    FROM transactions t
    JOIN withdrawals w ON t.account_id = w.account_id
    WHERE t.total_deposit > w.total_withdrawal
    AND t.total_deposit > 10000;
    """
    # 执行查询并返回结果
    return query


Solution = create_solution(solution_function_name)