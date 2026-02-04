# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1399
标题: 页面推荐
难度: medium
链接: https://leetcode.cn/problems/page-recommendations/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1264. 页面推荐 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来实现页面推荐

算法步骤:
1. 从 `friendship` 表中获取每个用户的朋友列表。
2. 从 `likes` 表中获取每个用户喜欢的页面。
3. 对于每个用户，找到其朋友喜欢的页面，但该用户自己不喜欢的页面。
4. 将结果按用户 ID 和页面 ID 排序。

关键点:
- 使用子查询和连接操作来过滤和获取所需数据。
- 确保结果中不包含用户已经喜欢的页面。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是用户的数量，m 是每个用户的朋友数量。
空间复杂度: O(1)，除了输入和输出外，不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

def solution_function_name(user_id: int) -> List[List[int]]:
    """
    函数式接口 - 实现页面推荐
    """
    # SQL 查询实现
    query = """
    SELECT 
        f.user1_id AS user_id, 
        l.page_id AS page_id
    FROM 
        friendship f
    JOIN 
        likes l ON f.user2_id = l.user_id
    WHERE 
        f.user1_id = %s AND 
        l.page_id NOT IN (SELECT page_id FROM likes WHERE user_id = %s)
    UNION
    SELECT 
        f.user2_id AS user_id, 
        l.page_id AS page_id
    FROM 
        friendship f
    JOIN 
        likes l ON f.user1_id = l.user_id
    WHERE 
        f.user2_id = %s AND 
        l.page_id NOT IN (SELECT page_id FROM likes WHERE user_id = %s)
    ORDER BY 
        user_id, page_id;
    """
    # 执行查询并返回结果
    # 这里假设有一个数据库连接对象 `db_connection` 可以执行查询
    with db_connection.cursor() as cursor:
        cursor.execute(query, (user_id, user_id, user_id, user_id))
        result = cursor.fetchall()
    return result

Solution = create_solution(solution_function_name)