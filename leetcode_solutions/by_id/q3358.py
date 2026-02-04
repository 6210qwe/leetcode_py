# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3358
标题: Friends With No Mutual Friends
难度: medium
链接: https://leetcode.cn/problems/friends-with-no-mutual-friends/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3058. 没有共同朋友的朋友 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找出没有共同朋友的朋友对。

算法步骤:
1. 创建一个临时表 `friend_pairs`，包含所有朋友关系。
2. 使用自连接和子查询来找出没有共同朋友的朋友对。

关键点:
- 使用自连接和子查询来过滤掉有共同朋友的朋友对。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是朋友关系的数量。因为我们需要进行自连接和子查询操作。
空间复杂度: O(1)，不考虑查询结果的存储空间。
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
    函数式接口 - 实现 SQL 查询来找出没有共同朋友的朋友对
    """
    query = """
    WITH friend_pairs AS (
        SELECT user1_id AS user_id, user2_id AS friend_id FROM Friendship
        UNION
        SELECT user2_id AS user_id, user1_id AS friend_id FROM Friendship
    )
    SELECT DISTINCT f1.user_id, f1.friend_id
    FROM friend_pairs f1
    JOIN friend_pairs f2 ON f1.user_id = f2.user_id AND f1.friend_id < f2.friend_id
    LEFT JOIN friend_pairs f3 ON f1.friend_id = f3.user_id AND f2.friend_id = f3.friend_id
    WHERE f3.user_id IS NULL
    ORDER BY f1.user_id, f1.friend_id
    """
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


Solution = create_solution(solution_function_name)