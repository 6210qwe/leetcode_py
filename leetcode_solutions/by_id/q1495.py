# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1495
标题: Number of Trusted Contacts of a Customer
难度: medium
链接: https://leetcode.cn/problems/number-of-trusted-contacts-of-a-customer/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1364. 顾客的可信联系人数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个顾客的可信联系人数量。

算法步骤:
1. 创建一个临时表来存储每个顾客的可信联系人。
2. 使用 GROUP BY 和 COUNT 来统计每个顾客的可信联系人数量。

关键点:
- 使用 JOIN 操作来连接顾客和他们的联系人。
- 使用子查询来过滤出可信联系人。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是顾客的数量，m 是联系人的数量。
空间复杂度: O(n + m)，用于存储中间结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(customers: str, contacts: str) -> str:
    """
    函数式接口 - 返回每个顾客的可信联系人数量
    """
    # 实现最优解法
    query = f"""
    WITH trusted_contacts AS (
        SELECT c.customer_id, c.contact_name, c.email
        FROM {customers} c
        JOIN {contacts} co ON c.customer_id = co.customer_id
        WHERE co.trusted = 1
    )
    SELECT c.customer_id, COUNT(tc.contact_name) AS num_trusted_contacts
    FROM {customers} c
    LEFT JOIN trusted_contacts tc ON c.customer_id = tc.customer_id
    GROUP BY c.customer_id
    ORDER BY c.customer_id;
    """
    return query


Solution = create_solution(solution_function_name)