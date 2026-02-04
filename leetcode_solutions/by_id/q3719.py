# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3719
标题: Team Dominance by Pass Success
难度: hard
链接: https://leetcode.cn/problems/team-dominance-by-pass-success/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3384. 球队传球成功的优势得分 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个球队的传球成功率，并找出优势球队。

算法步骤:
1. 计算每个球队的总传球次数和成功的传球次数。
2. 计算每个球队的传球成功率。
3. 找出传球成功率最高的球队。

关键点:
- 使用子查询来计算每个球队的总传球次数和成功的传球次数。
- 使用窗口函数来计算传球成功率。
- 使用 `ORDER BY` 和 `LIMIT` 来找出传球成功率最高的球队。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是传球记录的数量。主要的时间开销在于排序操作。
空间复杂度: O(n)，需要存储每个球队的传球记录。
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
    函数式接口 - 实现最优解法
    """
    # SQL 查询实现
    query = """
    WITH team_passes AS (
        SELECT
            team_id,
            COUNT(*) AS total_passes,
            SUM(CASE WHEN pass_success = 'Y' THEN 1 ELSE 0 END) AS successful_passes
        FROM
            passes
        GROUP BY
            team_id
    ),
    team_pass_success_rate AS (
        SELECT
            team_id,
            (successful_passes * 1.0 / total_passes) AS pass_success_rate
        FROM
            team_passes
    )
    SELECT
        team_id
    FROM
        team_pass_success_rate
    ORDER BY
        pass_success_rate DESC
    LIMIT 1;
    """
    # 假设 params 是一个数据库连接对象
    cursor = params.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0] if result else None


Solution = create_solution(solution_function_name)