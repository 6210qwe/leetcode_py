# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2092
标题: Users That Actively Request Confirmation Messages
难度: easy
链接: https://leetcode.cn/problems/users-that-actively-request-confirmation-messages/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1939. 主动请求确认消息的用户 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来筛选出在指定时间范围内主动请求确认消息的用户。

算法步骤:
1. 筛选出 `action = 'confirmed'` 的记录。
2. 确保这些记录的时间在 `start_date` 和 `end_date` 之间。
3. 按 `user_id` 分组并计算每个用户的确认次数。
4. 筛选出确认次数大于等于 2 的用户。

关键点:
- 使用 `BETWEEN` 关键字来筛选时间范围。
- 使用 `GROUP BY` 和 `HAVING` 来筛选出符合条件的用户。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(start_date: str, end_date: str) -> List[int]:
    """
    函数式接口 - 查询在指定时间范围内主动请求确认消息的用户
    """
    query = f"""
    SELECT user_id
    FROM Confirmations
    WHERE action = 'confirmed'
      AND action_date BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY user_id
    HAVING COUNT(*) >= 2;
    """
    # 假设这里有一个数据库连接对象 db_connection
    # result = db_connection.execute(query).fetchall()
    # return [row[0] for row in result]
    pass  # 请在实际环境中替换为数据库查询执行代码


Solution = create_solution(solution_function_name)