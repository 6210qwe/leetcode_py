# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1623
标题: Sales by Day of the Week
难度: hard
链接: https://leetcode.cn/problems/sales-by-day-of-the-week/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1479. 周内每天的销售情况 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每周每天的销售情况。

算法步骤:
1. 创建一个临时表，包含每一天的日期和对应的星期几。
2. 将销售数据与临时表进行连接，按星期几分组并计算总销售额。
3. 返回结果。

关键点:
- 使用 `WITH` 子句创建临时表。
- 使用 `CASE` 语句将日期转换为星期几。
- 按星期几分组并计算总销售额。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是销售记录的数量。
空间复杂度: O(1)，因为只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

def solution_function_name(params):
    """
    函数式接口 - 实现
    """
    # 实现最优解法
    query = """
    WITH RECURSIVE DateRange AS (
        SELECT MIN(sale_date) AS sale_date FROM sales
        UNION ALL
        SELECT DATE_ADD(sale_date, INTERVAL 1 DAY)
        FROM DateRange
        WHERE DATE_ADD(sale_date, INTERVAL 1 DAY) <= (SELECT MAX(sale_date) FROM sales)
    ),
    Weekdays AS (
        SELECT 
            sale_date,
            CASE 
                WHEN DAYOFWEEK(sale_date) = 1 THEN 'Sunday'
                WHEN DAYOFWEEK(sale_date) = 2 THEN 'Monday'
                WHEN DAYOFWEEK(sale_date) = 3 THEN 'Tuesday'
                WHEN DAYOFWEEK(sale_date) = 4 THEN 'Wednesday'
                WHEN DAYOFWEEK(sale_date) = 5 THEN 'Thursday'
                WHEN DAYOFWEEK(sale_date) = 6 THEN 'Friday'
                WHEN DAYOFWEEK(sale_date) = 7 THEN 'Saturday'
            END AS weekday
        FROM DateRange
    )
    SELECT 
        w.weekday,
        SUM(s.amount) AS total_sales
    FROM Weekdays w
    LEFT JOIN sales s ON w.sale_date = s.sale_date
    GROUP BY w.weekday
    ORDER BY FIELD(w.weekday, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday');
    """
    return query


Solution = create_solution(solution_function_name)