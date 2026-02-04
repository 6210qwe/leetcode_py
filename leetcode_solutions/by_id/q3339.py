# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3339
标题: Top Percentile Fraud
难度: medium
链接: https://leetcode.cn/problems/top-percentile-fraud/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3055. 最高欺诈百分位数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算最高欺诈百分位数。

算法步骤:
1. 计算每个用户的欺诈分数。
2. 对欺诈分数进行排序。
3. 找到指定百分位的欺诈分数。

关键点:
- 使用窗口函数和子查询来计算百分位。
- 确保查询的性能优化。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是用户数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，除了输入输出外，不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

def solution_function_name(params):
    """
    函数式接口 - 实现最优解法
    """
    # SQL 查询实现
    query = """
    WITH FraudScores AS (
        SELECT user_id, SUM(fraud_score) AS total_fraud_score
        FROM transactions
        GROUP BY user_id
    ),
    RankedFraudScores AS (
        SELECT user_id, total_fraud_score,
               PERCENT_RANK() OVER (ORDER BY total_fraud_score DESC) AS fraud_percentile
        FROM FraudScores
    )
    SELECT user_id, total_fraud_score, fraud_percentile
    FROM RankedFraudScores
    WHERE fraud_percentile <= :percentile
    ORDER BY fraud_percentile DESC
    LIMIT 1;
    """
    # 执行查询并返回结果
    result = execute_sql_query(query, params)
    return result


Solution = create_solution(solution_function_name)