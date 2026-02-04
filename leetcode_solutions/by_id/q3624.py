# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3624
标题: Find Top Performing Driver
难度: medium
链接: https://leetcode.cn/problems/find-top-performing-driver/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3308. 寻找表现最佳的司机 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个司机的总行程数和总金额，然后根据这些数据找出表现最佳的司机。

算法步骤:
1. 计算每个司机的总行程数和总金额。
2. 找出总行程数最多的司机。
3. 如果有多个司机总行程数相同，则选择总金额最高的司机。
4. 如果仍然有多个司机总金额相同，则选择 driver_id 最小的司机。

关键点:
- 使用 GROUP BY 和 SUM 函数来计算每个司机的总行程数和总金额。
- 使用 ORDER BY 和 LIMIT 来找到表现最佳的司机。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 trips 表中的行数。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，查询过程中只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(trips: List[List[int]], users: List[List[int]]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    # 构建 SQL 查询
    query = """
    WITH driver_stats AS (
        SELECT 
            T.driver_id, 
            COUNT(*) AS total_trips, 
            SUM(T.amount) AS total_amount
        FROM 
            (SELECT * FROM trips WHERE client_id IN (SELECT users_id FROM users WHERE banned = 'No')) T
        JOIN 
            (SELECT * FROM users WHERE banned = 'No') U
        ON 
            T.client_id = U.users_id
        GROUP BY 
            T.driver_id
    )
    SELECT 
        driver_id
    FROM 
        driver_stats
    ORDER BY 
        total_trips DESC, 
        total_amount DESC, 
        driver_id ASC
    LIMIT 1;
    """

    # 执行 SQL 查询
    # 这里假设有一个函数 execute_sql_query(query, trips, users) 可以执行 SQL 查询并返回结果
    result = execute_sql_query(query, trips, users)

    return result[0][0] if result else None


Solution = create_solution(solution_function_name)