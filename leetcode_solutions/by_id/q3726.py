# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3726
标题: Longest Team Pass Streak
难度: hard
链接: https://leetcode.cn/problems/longest-team-pass-streak/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3390. 最长团队传球连击 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到最长的团队传球连击。

算法步骤:
1. 创建一个临时表来存储每个传球的顺序编号。
2. 使用窗口函数来计算每个传球的连击长度。
3. 选择最长的连击长度。

关键点:
- 使用窗口函数和子查询来计算连击长度。
- 确保正确处理边界情况，如空表或单个传球。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

def solution_function_name():
    """
    函数式接口 - 实现最优解法
    """
    # SQL 查询实现
    query = """
    WITH PassesWithRowNum AS (
        SELECT 
            player_id, 
            pass_id, 
            ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY pass_time) AS row_num
        FROM passes
    ),
    ConsecutivePasses AS (
        SELECT 
            player_id, 
            pass_id,
            pass_time,
            pass_id - row_num AS group_id
        FROM PassesWithRowNum
    )
    SELECT 
        player_id, 
        MAX(pass_id) - MIN(pass_id) + 1 AS longest_streak
    FROM ConsecutivePasses
    GROUP BY player_id, group_id
    ORDER BY longest_streak DESC
    LIMIT 1;
    """
    return query

Solution = create_solution(solution_function_name)