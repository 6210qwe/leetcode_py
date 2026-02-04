# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 614
标题: Second Degree Follower
难度: medium
链接: https://leetcode.cn/problems/second-degree-follower/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
614. 二级关注者 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到二级关注者。首先找到每个用户的一级关注者，然后找到这些一级关注者的关注者，即为二级关注者。

算法步骤:
1. 创建一个临时表 `first_degree` 来存储每个用户的一级关注者。
2. 使用 `first_degree` 表来查找二级关注者。
3. 计算每个用户的二级关注者数量，并返回结果。

关键点:
- 使用子查询和 JOIN 操作来高效地找到二级关注者。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是用户的数量。在最坏情况下，每个用户都关注了所有其他用户，需要进行两层嵌套的查询。
空间复杂度: O(n)，存储中间结果的空间复杂度。
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
    函数式接口 - 实现 SQL 查询来找到二级关注者
    """
    # SQL 查询实现
    query = """
    WITH first_degree AS (
        SELECT follower, followee
        FROM Follow
    )
    SELECT f1.follower, COUNT(DISTINCT f2.followee) AS num_second_degree_followers
    FROM first_degree f1
    JOIN first_degree f2 ON f1.followee = f2.follower
    WHERE f1.follower != f2.followee
    GROUP BY f1.follower
    """
    return query

Solution = create_solution(solution_function_name)