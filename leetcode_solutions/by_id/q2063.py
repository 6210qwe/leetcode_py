# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2063
标题: Leetcodify Friends Recommendations
难度: hard
链接: https://leetcode.cn/problems/leetcodify-friends-recommendations/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1917. Leetcodify 好友推荐 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到每个用户的好友推荐。首先，找到每个用户的所有朋友，然后排除那些已经是好友的用户。

算法步骤:
1. 找到每个用户的所有朋友。
2. 排除那些已经是好友的用户。
3. 返回每个用户的好友推荐列表。

关键点:
- 使用子查询和连接操作来实现高效的查询。
- 确保查询结果中不包含重复的推荐。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是用户数量，m 是好友关系的数量。
空间复杂度: O(1)，查询过程中使用的额外空间是常数级别的。
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
    函数式接口 - 实现好友推荐的 SQL 查询
    """
    # 最优解法
    query = """
    SELECT 
        user1_id AS user_id,
        user2_id AS recommended_id
    FROM (
        SELECT 
            f1.user1_id, 
            f2.user2_id
        FROM 
            Friendship f1
        JOIN 
            Friendship f2 ON f1.user2_id = f2.user1_id
        WHERE 
            f1.user1_id != f2.user2_id AND
            NOT EXISTS (
                SELECT 1 
                FROM Friendship f3
                WHERE (f3.user1_id = f1.user1_id AND f3.user2_id = f2.user2_id) OR
                      (f3.user1_id = f2.user2_id AND f3.user2_id = f1.user1_id)
            )
    ) AS subquery
    UNION
    SELECT 
        user2_id AS user_id,
        user1_id AS recommended_id
    FROM (
        SELECT 
            f1.user2_id, 
            f2.user1_id
        FROM 
            Friendship f1
        JOIN 
            Friendship f2 ON f1.user1_id = f2.user2_id
        WHERE 
            f1.user2_id != f2.user1_id AND
            NOT EXISTS (
                SELECT 1 
                FROM Friendship f3
                WHERE (f3.user1_id = f1.user2_id AND f3.user2_id = f2.user1_id) OR
                      (f3.user1_id = f2.user1_id AND f3.user2_id = f1.user2_id)
            )
    ) AS subquery
    ORDER BY user_id, recommended_id;
    """
    return query

Solution = create_solution(solution_function_name)