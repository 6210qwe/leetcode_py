# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2097
标题: Strong Friendship
难度: medium
链接: https://leetcode.cn/problems/strong-friendship/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1949. 坚定的友谊 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找出满足条件的强友谊关系。

算法步骤:
1. 创建一个临时表 `friendships` 来存储所有朋友关系。
2. 使用自连接查询来找到满足条件的强友谊关系。
3. 返回结果集。

关键点:
- 使用自连接查询来比较两个用户的朋友列表。
- 确保两个用户的朋友列表完全相同。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - 其中 n 是用户的数量。自连接查询的时间复杂度为 O(n^2)。
空间复杂度: O(1) - 除了输入和输出外，不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(connection):
    """
    函数式接口 - 实现强友谊关系的查询
    """
    # 创建一个临时表 friendships 来存储所有朋友关系
    connection.execute("""
        CREATE TEMPORARY TABLE IF NOT EXISTS friendships AS
        SELECT user1_id, user2_id
        FROM friendship
    """)

    # 使用自连接查询来找到满足条件的强友谊关系
    query = """
        SELECT f1.user1_id, f1.user2_id
        FROM friendships f1
        JOIN friendships f2 ON f1.user1_id = f2.user1_id AND f1.user2_id != f2.user2_id
        WHERE NOT EXISTS (
            SELECT 1 FROM friendships f3
            WHERE (f3.user1_id = f1.user1_id AND f3.user2_id = f1.user2_id)
            EXCEPT
            SELECT 1 FROM friendships f4
            WHERE (f4.user1_id = f2.user1_id AND f4.user2_id = f2.user2_id)
        )
        AND NOT EXISTS (
            SELECT 1 FROM friendships f3
            WHERE (f3.user1_id = f2.user1_id AND f3.user2_id = f2.user2_id)
            EXCEPT
            SELECT 1 FROM friendships f4
            WHERE (f4.user1_id = f1.user1_id AND f4.user2_id = f1.user2_id)
        )
    """

    # 执行查询并返回结果
    result = connection.execute(query).fetchall()
    return result

Solution = create_solution(solution_function_name)